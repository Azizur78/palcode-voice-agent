"""
Configuration for the NovaCare voice agent.

Sensitive values such as phone numbers are loaded from
environment variables rather than being stored in source code.
"""

import os


def get_contact_numbers():
    """Load predefined routing destinations from environment variables."""

    return {
        "appointment": os.getenv("APPOINTMENT_NUMBER"),
        "billing": os.getenv("BILLING_NUMBER"),
        "support": os.getenv("SUPPORT_NUMBER"),
        "emergency": os.getenv("EMERGENCY_NUMBER"),
    }
