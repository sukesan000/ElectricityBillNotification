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
import linebot.v3.messaging.models


from typing import Union
from pydantic.v1 import BaseModel, Field, StrictStr
from linebot.v3.messaging.models.imagemap_area import ImagemapArea

class ImagemapAction(BaseModel):
    """
    ImagemapAction
    https://developers.line.biz/en/reference/messaging-api/#imagemap-action-objects
    """
    type: StrictStr = Field(...)
    area: ImagemapArea = Field(...)

    __properties = ["type", "area"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = 'type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'clipboard': 'ClipboardImagemapAction',
        'message': 'MessageImagemapAction',
        'uri': 'URIImagemapAction'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(ClipboardImagemapAction, MessageImagemapAction, URIImagemapAction):
        """Create an instance of ImagemapAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of area
        if self.area:
            _dict['area'] = self.area.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(ClipboardImagemapAction, MessageImagemapAction, URIImagemapAction):
        """Create an instance of ImagemapAction from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(linebot.v3.messaging.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError("ImagemapAction failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

