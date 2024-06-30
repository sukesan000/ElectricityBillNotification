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


from typing import List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator

class SubscribedMembershipPlan(BaseModel):
    """
    Object containing information about the membership plan.
    """
    membership_id: StrictInt = Field(..., alias="membershipId", description="Membership plan ID.")
    title: StrictStr = Field(..., description="Membership plan name.")
    description: StrictStr = Field(..., description="Membership plan description.")
    benefits: conlist(StrictStr, min_items=1) = Field(..., description="List of membership plan perks.")
    price: Union[StrictFloat, StrictInt] = Field(..., description="Monthly fee for membership plan. (e.g. 1500.00)")
    currency: StrictStr = Field(..., description="The currency of membership.price.")

    __properties = ["membershipId", "title", "description", "benefits", "price", "currency"]

    @validator('currency')
    def currency_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('JPY', 'TWD', 'THB'):
            raise ValueError("must be one of enum values ('JPY', 'TWD', 'THB')")
        return value

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
    def from_json(cls, json_str: str) -> SubscribedMembershipPlan:
        """Create an instance of SubscribedMembershipPlan from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscribedMembershipPlan:
        """Create an instance of SubscribedMembershipPlan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscribedMembershipPlan.parse_obj(obj)

        _obj = SubscribedMembershipPlan.parse_obj({
            "membership_id": obj.get("membershipId"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "benefits": obj.get("benefits"),
            "price": obj.get("price"),
            "currency": obj.get("currency")
        })
        return _obj

