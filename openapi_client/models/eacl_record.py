# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from openapi_client.models.action_type import ActionType
from openapi_client.models.operation_type import OperationType
from openapi_client.models.record_filter import RecordFilter
from openapi_client.models.record_target import RecordTarget
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EACLRecord(BaseModel):
    """
    EACLRecord
    """ # noqa: E501
    operation: List[OperationType] = Field(description="Request's operation type to match if the rule is applicable to a particular request")
    action: List[ActionType] = Field(description="Rule execution result action.")
    filters: List[RecordFilter] = Field(description="Filters for records.")
    targets: List[RecordTarget] = Field(description="Target to apply ACL rule. Can be a subject's role class or a list of public keys to match.")
    __properties: ClassVar[List[str]] = ["operation", "action", "filters", "targets"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
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
        """Create an instance of EACLRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item in self.targets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['targets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EACLRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operation": obj.get("operation"),
            "action": obj.get("action"),
            "filters": [RecordFilter.from_dict(_item) for _item in obj.get("filters")] if obj.get("filters") is not None else None,
            "targets": [RecordTarget.from_dict(_item) for _item in obj.get("targets")] if obj.get("targets") is not None else None
        })
        return _obj


