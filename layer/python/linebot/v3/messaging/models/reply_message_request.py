# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist
from linebot.v3.messaging.models.message import Message

class ReplyMessageRequest(BaseModel):
    """
    ReplyMessageRequest
    https://developers.line.biz/en/reference/messaging-api/#send-reply-message
    """
    reply_token: StrictStr = Field(..., alias="replyToken", description="replyToken received via webhook.")
    messages: conlist(Message, max_items=5, min_items=1) = Field(..., description="List of messages.")
    notification_disabled: Optional[StrictBool] = Field(False, alias="notificationDisabled", description="`true`: The user doesn’t receive a push notification when a message is sent. `false`: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false. ")

    __properties = ["replyToken", "messages", "notificationDisabled"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ReplyMessageRequest:
        """Create an instance of ReplyMessageRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReplyMessageRequest:
        """Create an instance of ReplyMessageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReplyMessageRequest.parse_obj(obj)

        _obj = ReplyMessageRequest.parse_obj({
            "reply_token": obj.get("replyToken"),
            "messages": [Message.from_dict(_item) for _item in obj.get("messages")] if obj.get("messages") is not None else None,
            "notification_disabled": obj.get("notificationDisabled") if obj.get("notificationDisabled") is not None else False
        })
        return _obj

