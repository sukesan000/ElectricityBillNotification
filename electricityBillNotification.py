import os
import calendar
import json
from datetime import datetime, timedelta, date
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.aiohttp import AIOHTTPTransport
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    PushMessageRequest,
    TextMessage,
)

LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_USER_ID = os.environ['LINE_USER_ID']
OCTOPUS_EMAIL = os.environ['OCTOPUS_EMAIL']
OCTOPUS_PASSWORD = os.environ['OCTOPUS_PASSWORD']
OCTOPUS_ACCOUNT_NUMBER = os.environ['OCTOPUS_ACCOUNT_NUMBER']


configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)

class OctopusAuthenticationToken:
    # HTTPトランスポートを設定
    transport = RequestsHTTPTransport(url='https://api.oejp-kraken.energy/v1/graphql/')
    
    # クライアントを作成
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # ログイントークンを作成するmutationを定義
    LOGIN_QUERY = gql("""
        mutation($input: ObtainJSONWebTokenInput!) {
          obtainKrakenToken(input: $input) {
            token
            refreshToken
          }
        }
    """)

    @classmethod
    def generate_token(cls):
        result = cls.client.execute(cls.LOGIN_QUERY, variable_values={
            "input": {
                "email": OCTOPUS_EMAIL,
                "password": OCTOPUS_PASSWORD,
            }
        })
        return result.get("obtainKrakenToken", {}).get("token")
    
class OctopusClient:
    @staticmethod
    def get_headers():
        return {
            "Authorization": f"{OctopusAuthenticationToken.generate_token()}"
        }

    @classmethod
    def create_client(cls):
        headers = cls.get_headers()
        transport = AIOHTTPTransport(
            url='https://api.oejp-kraken.energy/v1/graphql/',
            headers=headers
        )
        return Client(transport=transport, fetch_schema_from_transport=True)
    
class OctopusEnergyBillManager:
    GET_BILL_QUERY = gql('''
    query(
        $accountNumber: String!
        $fromDatetime: DateTime
        $toDatetime: DateTime
    ) {
        account(accountNumber: $accountNumber) {
            properties {
                electricitySupplyPoints {
                    agreements {
                        validFrom
                    }
                    halfHourlyReadings(
                        fromDatetime: $fromDatetime
                        toDatetime: $toDatetime
                    ) {
                        startAt
                        endAt
                        value
                        costEstimate
                        consumptionStep
                        consumptionRateBand
                    }
                }
            }
        }
    }
    ''')

    @classmethod
    def get_bill_data(cls):
        client = OctopusClient.create_client()
        
        today = date.today()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])

        from_datetime = first_day_of_month.strftime('%Y-%m-%dT00:00:00Z')
        to_datetime = last_day_of_month.strftime('%Y-%m-%dT23:59:59Z')

        result = client.execute(cls.GET_BILL_QUERY, variable_values={
            'accountNumber': OCTOPUS_ACCOUNT_NUMBER,
            'fromDatetime': from_datetime,
            'toDatetime': to_datetime
        })
        return result

def lambda_handler(event, context):
    bill_data = OctopusEnergyBillManager.get_bill_data()
    
    properties = bill_data["account"]["properties"]
    electricity_supply_points = properties[0]["electricitySupplyPoints"]
    half_hourly_readings = electricity_supply_points[0]["halfHourlyReadings"]
    
    today = date.today()
    kwh = round(sum(float(reading["value"]) for reading in half_hourly_readings))
    cost = round(sum(float(reading["costEstimate"]) for reading in half_hourly_readings))
    messageText=f"{today.strftime('%Y年%m月')}の電気代は{kwh}kWh消費して{cost}円かかったよ"
    
    # Line出力
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        message=TextMessage(text=messageText)
        line_bot_api.push_message_with_http_info(
            PushMessageRequest(
                to=LINE_USER_ID,
                messages=[message]
            )
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent successfully')
    }



    