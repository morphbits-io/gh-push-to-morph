# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MatchType(str, Enum):
    """
    MatchType
    """

    """
    allowed enum values
    """
    STRING_EQUAL = 'STRING_EQUAL'
    STRING_NOT_EQUAL = 'STRING_NOT_EQUAL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MatchType from a JSON string"""
        return cls(json.loads(json_str))


