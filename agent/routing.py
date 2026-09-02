"""
Static destination routing for the NovaCare voice agent.

The AI agent determines the caller's intent.
This module maps that intent to a predefined destination.
"""

import os


CONTACTS = {
    "appointment": os.getenv("APPOINTMENT_NUMBER"),
    "billing": os.getenv("BILLING_NUMBER"),
    "support": os.getenv("SUPPORT_NUMBER"),
    "emergency": os.getenv("EMERGENCY_NUMBER"),
}


VALID_INTENTS = {
    "appointment",
    "billing",
    "support",
    "emergency",
}


def get_destination(intent: str):
    """
    Return the predefined destination for a valid routing intent.

    The function does not create or modify destinations.
    It only looks up the destination associated with the intent.
    """
    normalized_intent = intent.strip().lower()

    if normalized_intent not in VALID_INTENTS:
        return None

    return CONTACTS.get(normalized_intent)
