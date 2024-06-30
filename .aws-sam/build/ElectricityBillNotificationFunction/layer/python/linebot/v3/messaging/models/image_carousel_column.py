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



from pydantic.v1 import BaseModel, Field, StrictStr
from linebot.v3.messaging.models.action import Action

class ImageCarouselColumn(BaseModel):
    """
    ImageCarouselColumn
    """
    image_url: StrictStr = Field(..., alias="imageUrl")
    action: Action = Field(...)

    __properties = ["imageUrl", "action"]

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
    def from_json(cls, json_str: str) -> ImageCarouselColumn:
        """Create an instance of ImageCarouselColumn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImageCarouselColumn:
        """Create an instance of ImageCarouselColumn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ImageCarouselColumn.parse_obj(obj)

        _obj = ImageCarouselColumn.parse_obj({
            "image_url": obj.get("imageUrl"),
            "action": Action.from_dict(obj.get("action")) if obj.get("action") is not None else None
        })
        return _obj

