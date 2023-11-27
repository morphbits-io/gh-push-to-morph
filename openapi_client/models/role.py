# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Role(str, Enum):
    """
    Role
    """

    """
    allowed enum values
    """
    USER = 'USER'
    SYSTEM = 'SYSTEM'
    OTHERS = 'OTHERS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Role from a JSON string"""
        return cls(json.loads(json_str))

