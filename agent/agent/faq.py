"""
Predefined FAQ knowledge base for the NovaCare voice agent.

The voice agent should answer only from this information
and should not invent clinic details.
"""

FAQS = {
    "clinic_name": "NovaCare Dental Clinic",

    "hours": (
        "Monday through Saturday: 9 AM to 7 PM. "
        "Sunday: Closed."
    ),

    "location": "123 Health Avenue.",

    "consultations": (
        "Initial dental consultations are available."
    ),

    "payment_methods": (
        "Cash, cards, and UPI are accepted."
    ),

    "insurance": (
        "Major insurance providers are accepted. "
        "For specific insurance coverage questions, "
        "the caller can be connected with the support team."
    ),

    "cancellation": (
        "Please provide at least 24 hours' notice "
        "whenever possible."
    ),

    "emergency": (
        "Urgent dental cases should be connected "
        "to the configured urgent care destination."
    ),
}


def get_faq(topic: str):
    """
    Return the predefined answer for a known FAQ topic.

    Returns None when the requested topic is not available.
    """
    normalized_topic = topic.strip().lower()

    return FAQS.get(normalized_topic)
