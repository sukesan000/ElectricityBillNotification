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


from typing import Optional
from pydantic.v1 import BaseModel, Field, StrictStr

class DetachModuleRequest(BaseModel):
    """
    Unlink (detach) the module channel by the operation of the module channel administrator
    https://developers.line.biz/en/reference/partner-docs/#unlink-detach-module-channel-by-operation-mc-admin
    """
    bot_id: Optional[StrictStr] = Field(None, alias="botId", description="User ID of the LINE Official Account bot attached to the module channel.")

    __properties = ["botId"]

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
    def from_json(cls, json_str: str) -> DetachModuleRequest:
        """Create an instance of DetachModuleRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetachModuleRequest:
        """Create an instance of DetachModuleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DetachModuleRequest.parse_obj(obj)

        _obj = DetachModuleRequest.parse_obj({
            "bot_id": obj.get("botId")
        })
        return _obj

