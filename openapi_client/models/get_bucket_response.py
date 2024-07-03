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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from openapi_client.models.basic_acl import BasicACL
from openapi_client.models.eacl import EACL
from openapi_client.models.placement_policy import PlacementPolicy
from typing import Optional, Set
from typing_extensions import Self

class GetBucketResponse(BaseModel):
    """
    GetBucketResponse
    """ # noqa: E501
    creation_date: datetime = Field(description="Bucket creation date in RFC 3339 format.", alias="creationDate")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Bucket name.")
    basic_acl: BasicACL = Field(alias="basicACL")
    e_acl: EACL = Field(alias="eACL")
    placement_policy: PlacementPolicy = Field(alias="placementPolicy")
    owner: StrictStr = Field(description="User that owns this bucket.")
    used_space: StrictInt = Field(description="Bucket used space in bytes.", alias="usedSpace")
    __properties: ClassVar[List[str]] = ["creationDate", "name", "basicACL", "eACL", "placementPolicy", "owner", "usedSpace"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetBucketResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of basic_acl
        if self.basic_acl:
            _dict['basicACL'] = self.basic_acl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of e_acl
        if self.e_acl:
            _dict['eACL'] = self.e_acl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of placement_policy
        if self.placement_policy:
            _dict['placementPolicy'] = self.placement_policy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetBucketResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "creationDate": obj.get("creationDate"),
            "name": obj.get("name"),
            "basicACL": BasicACL.from_dict(obj["basicACL"]) if obj.get("basicACL") is not None else None,
            "eACL": EACL.from_dict(obj["eACL"]) if obj.get("eACL") is not None else None,
            "placementPolicy": PlacementPolicy.from_dict(obj["placementPolicy"]) if obj.get("placementPolicy") is not None else None,
            "owner": obj.get("owner"),
            "usedSpace": obj.get("usedSpace")
        })
        return _obj


