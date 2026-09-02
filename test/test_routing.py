"""
Tests for NovaCare intent-to-destination routing.
"""

import os
import unittest

os.environ["APPOINTMENT_NUMBER"] = "+910000000001"
os.environ["BILLING_NUMBER"] = "+910000000002"
os.environ["SUPPORT_NUMBER"] = "+910000000003"
os.environ["EMERGENCY_NUMBER"] = "+910000000004"

from agent.routing import get_destination


class TestRouting(unittest.TestCase):

    def test_appointment_routing(self):
        self.assertEqual(
            get_destination("appointment"),
            "+910000000001"
        )

    def test_billing_routing(self):
        self.assertEqual(
            get_destination("billing"),
            "+910000000002"
        )

    def test_support_routing(self):
        self.assertEqual(
            get_destination("support"),
            "+910000000003"
        )

    def test_emergency_routing(self):
        self.assertEqual(
            get_destination("emergency"),
            "+910000000004"
        )

    def test_unknown_intent_returns_none(self):
        self.assertIsNone(
            get_destination("unknown")
        )

    def test_case_and_whitespace_are_normalized(self):
        self.assertEqual(
            get_destination("  APPOINTMENT  "),
            "+910000000001"
        )


if __name__ == "__main__":
    unittest.main()
