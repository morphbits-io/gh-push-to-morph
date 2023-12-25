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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from openapi_client.models.metrics_drive import MetricsDrive
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MetricsNode(BaseModel):
    """
    Node metrics.
    """ # noqa: E501
    endpoint: StrictStr = Field(description="Network endpoint of the node server.")
    uptime: Annotated[int, Field(strict=True, ge=0)] = Field(description="Time elapsed since node startup in seconds.")
    drives: List[MetricsDrive] = Field(description="Listing of drives' metrics.")
    __properties: ClassVar[List[str]] = ["endpoint", "uptime", "drives"]

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
        """Create an instance of MetricsNode from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in drives (list)
        _items = []
        if self.drives:
            for _item in self.drives:
                if _item:
                    _items.append(_item.to_dict())
            _dict['drives'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MetricsNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endpoint": obj.get("endpoint"),
            "uptime": obj.get("uptime"),
            "drives": [MetricsDrive.from_dict(_item) for _item in obj.get("drives")] if obj.get("drives") is not None else None
        })
        return _obj


