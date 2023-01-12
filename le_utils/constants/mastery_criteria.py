# -*- coding: utf-8 -*-
# Generated by scripts/generate_from_specs.py
from __future__ import unicode_literals

# MasteryCriteria

DO_ALL = "do_all"
M_OF_N = "m_of_n"
NUM_CORRECT_IN_A_ROW_10 = "num_correct_in_a_row_10"
NUM_CORRECT_IN_A_ROW_2 = "num_correct_in_a_row_2"
NUM_CORRECT_IN_A_ROW_3 = "num_correct_in_a_row_3"
NUM_CORRECT_IN_A_ROW_5 = "num_correct_in_a_row_5"

choices = (
    (DO_ALL, "Do All"),
    (M_OF_N, "M Of N"),
    (NUM_CORRECT_IN_A_ROW_10, "Num Correct In A Row 10"),
    (NUM_CORRECT_IN_A_ROW_2, "Num Correct In A Row 2"),
    (NUM_CORRECT_IN_A_ROW_3, "Num Correct In A Row 3"),
    (NUM_CORRECT_IN_A_ROW_5, "Num Correct In A Row 5"),
)

MASTERYCRITERIALIST = [
    DO_ALL,
    M_OF_N,
    NUM_CORRECT_IN_A_ROW_10,
    NUM_CORRECT_IN_A_ROW_2,
    NUM_CORRECT_IN_A_ROW_3,
    NUM_CORRECT_IN_A_ROW_5,
]

SCHEMA = {
    "$id": "/schemas/mastery_criteria",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "description": "Schema for mastery criteria of exercise content types",
    "additionalProperties": False,
    "required": ["mastery_model"],
    "definitions": {
        "mastery_model": {
            "type": "string",
            "$exportConstants": "mastery_criteria",
            "enum": [
                "do_all",
                "m_of_n",
                "num_correct_in_a_row_2",
                "num_correct_in_a_row_3",
                "num_correct_in_a_row_5",
                "num_correct_in_a_row_10",
            ],
        }
    },
    "properties": {
        "m": True,
        "n": True,
        "mastery_model": {"$ref": "#/definitions/mastery_model"},
    },
    "anyOf": [
        {"properties": {"mastery_model": {"const": "m_of_n"}}, "required": ["m", "n"]},
        {
            "properties": {
                "mastery_model": {
                    "enum": [
                        "do_all",
                        "num_correct_in_a_row_2",
                        "num_correct_in_a_row_3",
                        "num_correct_in_a_row_5",
                        "num_correct_in_a_row_10",
                    ]
                },
                "m": {"type": "null"},
                "n": {"type": "null"},
            }
        },
    ],
}
