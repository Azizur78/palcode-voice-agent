An AI-powered voice receptionist prototype for NovaCare Dental Clinic.

The agent is designed to:

- Handle natural voice conversations
- Answer predefined clinic FAQs
- Understand caller intent
- Route callers to predefined teams
- Handle different phrasings of the same intent
- Avoid IVR / "press 1" menus
- Ask for clarification when intent is unclear
- Avoid inventing destinations or phone numbers

## Architecture

```text
Caller
  |
  v
Vapi Voice Agent
  |
  v
Conversation + Intent Classification
  |
  +-----------------------+
  |                       |
  v                       v
General FAQ           Routing Intent
  |                       |
  v                       v
Direct Answer       Predefined Destination
                          |
              +-----------+-----------+
              |           |           |
              v           v           v
         Appointment   Billing     Support
                                     
                          +
                      Emergency
