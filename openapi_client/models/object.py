# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Object(BaseModel):
    """
    Object descriptor.
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Object name.")
    creation_date: datetime = Field(description="Creation date in RFC 3339 format.", alias="creationDate")
    size: Annotated[int, Field(strict=True, ge=0)] = Field(description="Data size.")
    content_type: StrictStr = Field(description="Media type from https://www.iana.org/assignments/media-types/media-types.xhtml", alias="contentType")
    lifetime: StrictInt = Field(description="Object lifetime in hours, since object creation time. Zero means no expiration.")
    __properties: ClassVar[List[str]] = ["name", "creationDate", "size", "contentType", "lifetime"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Object from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Object from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "creationDate": obj.get("creationDate"),
            "size": obj.get("size"),
            "contentType": obj.get("contentType") if obj.get("contentType") is not None else 'application/octet-stream',
            "lifetime": obj.get("lifetime") if obj.get("lifetime") is not None else 0
        })
        return _obj


