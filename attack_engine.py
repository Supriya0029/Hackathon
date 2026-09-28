"""
attack_engine.py

Cybersecurity Attack Simulation Module
(Safe educational simulation for SIH project)

Author: Member 3
"""

import uuid
import random
from datetime import datetime


class AttackEngine:

    def __init__(self):
        self.used_signature_ids = set()

    # -------------------------------------------------
    # 1. FORGERY ATTACK
    # -------------------------------------------------
    def simulate_forgery(self):

        expected_score = round(random.uniform(0.90, 1.00), 2)

        observed_score = round(
            expected_score - random.uniform(0.20, 0.50),
            2
        )

        return {
            "attack": "Forgery",
            "modified": True,
            "description": "Digital signature was altered after generation.",
            "expected": expected_score,
            "observed": observed_score,
            "verification_result": False,
            "timestamp": str(datetime.now())
        }

    # -------------------------------------------------
    # 2. IMPERSONATION ATTACK
    # -------------------------------------------------
    def simulate_impersonation(self):

        authorized_user = "Alice"
        attacker = "Mallory"

        return {
            "attack": "Impersonation",
            "authorized_identity": authorized_user,
            "claimed_identity": attacker,
            "identity_match": False,
            "verification_result": False,
            "description":
                "Unauthorized entity attempts to sign as another user.",
            "timestamp": str(datetime.now())
        }

    # -------------------------------------------------
    # 3. REPLAY ATTACK
    # -------------------------------------------------
    def simulate_replay(self):

        signature_id = str(uuid.uuid4())

        self.used_signature_ids.add(signature_id)

        replay_detected = signature_id in self.used_signature_ids

        return {
            "attack": "Replay",
            "signature_id": signature_id,
            "reused": replay_detected,
            "verification_result": False,
            "description":
                "Previously accepted signature/session reused.",
            "timestamp": str(datetime.now())
        }

    # -------------------------------------------------
    # 4. QUANTUM CHANNEL MANIPULATION
    # -------------------------------------------------
    def simulate_channel_attack(self):

        expected_qber = round(random.uniform(0.01, 0.05), 3)

        manipulated_qber = round(
            expected_qber + random.uniform(0.10, 0.30),
            3
        )

        return {
            "attack": "Quantum Channel Manipulation",
            "channel_modified": True,
            "expected_qber": expected_qber,
            "observed_qber": manipulated_qber,
            "verification_result": False,
            "description":
                "Quantum communication altered during transmission.",
            "timestamp": str(datetime.now())
        }


# -------------------------------------------------
# Demo Run
# -------------------------------------------------

if __name__ == "__main__":

    engine = AttackEngine()

    print("\nFORGERY\n")
    print(engine.simulate_forgery())

    print("\nIMPERSONATION\n")
    print(engine.simulate_impersonation())

    print("\nREPLAY\n")
    print(engine.simulate_replay())

    print("\nCHANNEL ATTACK\n")
    print(engine.simulate_channel_attack())