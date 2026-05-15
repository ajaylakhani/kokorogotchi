"""
kokorogotchi/schemas.py — Tool schemas the LLM sees.
"""

KOKORO_READ_STATE = {
    "name": "kokoro_read_state",
    "description": (
        "Read Kokoro's state: drift, mood, stage, streak, time since last care, "
        "and tone_hint (reflects stage personality for journal writing). "
        "If response contains naming_ceremony, ask user to name their Kokoro first."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    },
}

KOKORO_UPDATE_STATE = {
    "name": "kokoro_update_state",
    "description": (
        "Update Kokoro after a care action or naming ceremony. "
        "Only pass fields that changed. Drift: feed +0.08, play +0.05."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Pet name (set during naming ceremony at hatchling stage).",
            },
            "gender": {
                "type": "string",
                "enum": ["male", "female", "neutral"],
                "description": "Pet gender (set during naming ceremony).",
            },
            "drift": {
                "type": "number",
                "description": "New drift 0.0–1.0. Nudge small amounts.",
            },
            "mood": {
                "type": "string",
                "enum": ["bonded", "neutral", "wild"],
                "description": "Current mood.",
            },
            "care_action": {
                "type": "string",
                "description": "What the user did, e.g. 'fed Kokoro'.",
            },
        },
    },
}

KOKORO_READ_JOURNAL = {
    "name": "kokoro_read_journal",
    "description": "Read Kokoro's recent journal entries.",
    "parameters": {
        "type": "object",
        "properties": {
            "limit": {
                "type": "integer",
                "description": "Entries to return (default 5).",
            }
        },
    },
}

KOKORO_WRITE_JOURNAL = {
    "name": "kokoro_write_journal",
    "description": "Write a journal entry in Kokoro's voice after a significant moment.",
    "parameters": {
        "type": "object",
        "properties": {
            "entry": {
                "type": "string",
                "description": "Journal entry in Kokoro's voice.",
            }
        },
        "required": ["entry"],
    },
}

