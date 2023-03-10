// -*- coding: utf-8 -*-
// Generated by scripts/generate_from_specs.py
// CompletionCriteria

export default {
    APPROX_TIME: "approx_time",
    DETERMINED_BY_RESOURCE: "determined_by_resource",
    MASTERY: "mastery",
    PAGES: "pages",
    REFERENCE: "reference",
    TIME: "time",
};

export const SCHEMA = {
  "$id": "/schemas/completion_criteria",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "description": "Schema for completion criteria of content nodes",
  "additionalProperties": false,
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
        "determined_by_resource"
      ]
    },
    "mastery_criteria": { "$ref": "/schemas/mastery_criteria" }
  },
  "properties": {
    "model": {
      "$ref": "#/definitions/model"
    },
    "learner_managed": {
      "type": "boolean"
    },
    "threshold": true
  },
  "required": ["model"],
  "anyOf": [
    {
      "properties": {
        "model": {
          "anyOf": [
            {"const": "time"},
            {"const": "approx_time"},
            {"const": "pages"}
          ]
        },
        "threshold": {
          "type": "number",
          "exclusiveMinimum": 0
        }
      },
      "required": ["threshold"]
    },
    {
      "properties": {
        "model": {
          "const": "pages"
        },
        "threshold": {
          "type": "string",
          "pattern": "^(100|[1-9][0-9]?)%$",
          "description": "A percentage",
          "minLength": 2,
          "maxLength": 4
        }
      },
      "required": ["threshold"]
    },
    {
      "properties": {
        "model": {
          "const": "mastery"
        },
        "threshold": {
          "$ref": "#/definitions/mastery_criteria"
        }
      },
      "required": ["threshold"]
    },
    {
      "properties": {
        "model": {
          "anyOf": [
            {"const": "reference"},
            {"const": "determined_by_resource"}
          ]
        },
        "threshold": {
          "type": "null"
        }
      },
      "required": []
    }
  ]
};
