# -*- coding: utf-8 -*-
# Generated by scripts/generate_from_specs.py
from __future__ import unicode_literals

# CompletionCriteria

APPROX_TIME = "approx_time"
DETERMINED_BY_RESOURCE = "determined_by_resource"
MASTERY = "mastery"
PAGES = "pages"
REFERENCE = "reference"
TIME = "time"

choices = (
    (APPROX_TIME, "Approx Time"),
    (DETERMINED_BY_RESOURCE, "Determined By Resource"),
    (MASTERY, "Mastery"),
    (PAGES, "Pages"),
    (REFERENCE, "Reference"),
    (TIME, "Time"),
)

COMPLETIONCRITERIALIST = [
    APPROX_TIME,
    DETERMINED_BY_RESOURCE,
    MASTERY,
    PAGES,
    REFERENCE,
    TIME,
]

SCHEMA = {
    "$id": "/schemas/completion_criteria",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "description": "Schema for completion criteria of content nodes",
    "additionalProperties": False,
    "definitions": {
        "model": {
            "type": "string",
            "$exportConstants": "completion_criteria",
            "enum": [
                "time",
                "approx_time",
                "pages",
                "mastery",
                "reference",
                "determined_by_resource",
            ],
        },
        "mastery_criteria": {"$ref": "/schemas/mastery_criteria"},
    },
    "properties": {
        "model": {"$ref": "#/definitions/model"},
        "learner_managed": {"type": "boolean"},
        "threshold": True,
    },
    "required": ["model"],
    "anyOf": [
        {
            "properties": {
                "model": {
                    "anyOf": [
                        {"const": "time"},
                        {"const": "approx_time"},
                        {"const": "pages"},
                    ]
                },
                "threshold": {"type": "number", "exclusiveMinimum": 0},
            },
            "required": ["threshold"],
        },
        {
            "properties": {
                "model": {"const": "pages"},
                "threshold": {
                    "type": "string",
                    "pattern": "^(100|[1-9][0-9]?)%$",
                    "description": "A percentage",
                    "minLength": 2,
                    "maxLength": 4,
                },
            },
            "required": ["threshold"],
        },
        {
            "properties": {
                "model": {"const": "mastery"},
                "threshold": {"$ref": "#/definitions/mastery_criteria"},
            },
            "required": ["threshold"],
        },
        {
            "properties": {
                "model": {
                    "anyOf": [
                        {"const": "reference"},
                        {"const": "determined_by_resource"},
                    ]
                },
                "threshold": {"type": "null"},
            },
            "required": [],
        },
    ],
}
