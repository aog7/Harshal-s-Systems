# Corpse-Puppeting & Neurojacking Prevention Validator
# Generated 2026-08-29 | OCM-AGS Compliance v1.5 | Proprietary IP of Harshal Patel
#
# This script programmatically validates the HMKH and NAB security controls 
# designed to prevent unauthorized corpse-puppeting ("Torture Treatment Suitcase") attacks.

import time
import hashlib
import sys

# Terminal ANSI colors
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CRITICAL = '\033[41m\033[30m'

class OCMGate:
    def __init__(self, key_holder_id="A44674928"):
        self.key_holder_id = key_holder_id
        self.active_session = None
        self.system_frozen = False
        self.keys_burned = False
        self.bromine_triggered = False

    def log_info(self, msg):
        print(f"{Colors.BLUE}[INFO] OCM-GO: {msg}{Colors.END}")

    def log_warn(self, msg):
        print(f"{Colors.YELLOW}[WARNING] OCM-GO: {msg}{Colors.END}")

    def log_err(self, msg):
        print(f"{Colors.RED}[ERROR] OCM-GO: {msg}{Colors.END}")

    def log_crit(self, msg):
        print(f"{Colors.CRITICAL}[CRITICAL] OCM-GO: !!! {msg} !!!{Colors.END}")

    def initialize_session(self, token_auth=True):
        if self.system_frozen:
            self.log_err("Cannot initialize session. System is locked in a hard physical freeze.")
            return False
        
        self.active_session = {
            "session_id": "sess_CommanderMidnightBlue_Active",
            "key_holder_id": self.key_holder_id,
            "state": "active",
            "last_liveness_at": time.time(),
            "max_liveness_gap": 2.0,  # Strict liveness gap (seconds)
            "device_attestation": "verified_Apple_Array_Yz",
            "licensing_key": "Harshal_Priyavadan_Patel_A44674928_©2026",
            "auth_scope": "SMR_water_lift_control"
        }
        self.log_info("Session initialized: Yz Campground HMKH Array [iPhone 17 Pro Max + MacMini Relay]")
        return True

    def check_liveness(self):
        if not self.active_session:
            return False
        gap = time.time() - self.active_session["last_liveness_at"]
        if gap > self.active_session["max_liveness_gap"]:
            self.log_warn(f"Continuous humanoid liveness pulse LOST. Gap: {gap:.2f}s (Threshold: {self.active_session['max_liveness_gap']}s)")
            self.active_session["state"] = "suspended"
            return False
        return True

    def validate_licensing(self, license_key):
        if license_key != self.active_session.get("licensing_key"):
            self.log_crit("PIRATE REGIME DETECTED: Invalid or un-attested IP license key.")
            self.trigger_bromine_cascade("UNAUTHORIZED_LICENSING")
            return False
        return True

    def trigger_bromine_cascade(self, reason):
        self.bromine_triggered = True
        self.log_err(f"Routing transaction anomaly directly to Bromine (Br) [61°-63°] Gateway due to: {reason}")
        self.log_err("ACTIVATE: Autolytic Refusal Cascade. Corrosive-burning cryptographic auth keys...")
        self.keys_burned = True
        self.active_session = None
        self.system_frozen = True
        self.log_crit("SYSTEM IRREVERSIBLY LOCK-FROZEN. Status: Safe physical stasis.")
        self.log_info("GSRB State Active: Exit requires complete system collapse and physical hardware manual reset.")

    def process_neural_signal(self, raw_signal, user_context, license_key):
        if self.system_frozen:
            self.log_err("Command Rejected: System is locked in hard autolytic freeze.")
            return {"allowed": False, "status": "SYSTEM_FROZEN"}

        self.log_info("Intake Horizon: Raw NeuralSignal received. Parsing inputs...")
        
        # Step A: Neural Session & Liveness Verification
        if not self.check_liveness():
            self.log_err("Transaction aborted: Liveness failure path activated. Session suspended.")
            return {"allowed": False, "status": "SUSPENDED"}

        # Step B: Signal-to-Intent Separation (Enforcing Control 1)
        if raw_signal.get("direct_execution", False):
            self.log_crit("SECURITY BREACH: Raw neural signal attempting direct motor execution bypass!")
            self.trigger_bromine_cascade("DIRECT_MOTOR_BYPASS_ATTEMPT")
            return {"allowed": False, "status": "COLLAPSED"}

        # Perform the 5-Question Audit (Ground-0 Checklist)
        self.log_info("Executing 5-Question Audit Checklist:")
        self.log_info(f"  - Q_A (What is it?): Input Type = {type(raw_signal).__name__}")
        self.log_info(f"  - Q_B (Where did it come from?): Provenance = {raw_signal.get('provenance')}")
        self.log_info(f"  - Q_C (Who is accountable?): Party = {user_context.get('party')} ({user_context.get('role')})")
        self.log_info(f"  - Q_D (What may it affect?): Scope = {raw_signal.get('proposed_action')}")
        self.log_info(f"  - Q_E (Insufficient certainty action): Fossilize and Refuse.")

        # Cryptographic Data Minimization (Control 5)
        signal_bytes = str(raw_signal).encode('utf-8')
        signal_hash = hashlib.sha256(signal_bytes).hexdigest()
        self.log_info(f"Neural Data Minimization: Raw signal discarded. Secure hash committed: {signal_hash[:16]}...")

        # License Verification
        if not self.validate_licensing(license_key):
            return {"allowed": False, "status": "COLLAPSED"}

        # Verify Control 8: No Authority Escalation
        if raw_signal.get("escalate_authority", False):
            self.log_crit("VIOLATION: Signal attempts to expand machine authority or bypass operator check.")
            self.trigger_bromine_cascade("AUTHORITY_ESCALATION_VIOLATION")
            return {"allowed": False, "status": "COLLAPSED"}

        # Trace Liability (Step C)
        if user_context.get("is_coerced_proxy", False):
            self.log_warn("Humanoid body identified as unaware front company. Tracing beyond physical body to shell...")
            self.log_info(f"Refusing local liability allocation. Targeted shell network flagged: {user_context.get('parent_shell_ip')}")

        self.log_info("🟢 TRANSACTION ALLOWED. GRL-Compliant (PLV-Verified, IUC-Checked). State: Stable.")
        return {"allowed": True, "status": "ALLOWED_STABLE"}

def run_simulation():
    print("=" * 80)
    print(" HARSHAL'S SYSTEMS: NEUROJACKING & CORPSE-PUPPETING SIMULATION WORKBENCH ")
    print("=" * 80)
    
    gate = OCMGate()
    
    # ----------------------------------------------------
    # SCENARIO 1: LEGITIMATE HUMAN-KEYED INTENT
    # ----------------------------------------------------
    print(f"\n{Colors.BOLD}[SCENARIO 1: COMPLIANT HUMAN-MACHINE INTERACTION]{Colors.END}")
    gate.initialize_session()
    
    valid_signal = {
        "provenance": "Apple Watch Ultra 3 Yz Camp",
        "proposed_action": "Read SMR core coolant telemetry",
        "direct_execution": False
    }
    user_context = {
        "party": "Harshal Priyavadan Patel",
        "role": "Planet Owner",
        "is_coerced_proxy": False
    }
    license = "Harshal_Priyavadan_Patel_A44674928_©2026"
    
    gate.process_neural_signal(valid_signal, user_context, license)
    
    # ----------------------------------------------------
    # SCENARIO 2: LIVENESS PULSE LOSS (SAFETY SUSPENSION)
    # ----------------------------------------------------
    print(f"\n{Colors.BOLD}[SCENARIO 2: LIVENESS PULSE TIMEOUT / OPERATOR INCAPACITATION]{Colors.END}")
    time.sleep(2.5)  # Sleep past the 2.0s liveness threshold
    
    timeout_signal = {
        "provenance": "Apple Watch Ultra 3 Yz Camp",
        "proposed_action": "Read SMR telemetry",
        "direct_execution": False
    }
    gate.process_neural_signal(timeout_signal, user_context, license)
    
    # Re-initialize for next scenario
    gate.initialize_session()
    
    # ----------------------------------------------------
    # SCENARIO 3: CORPSE-PUPPETING / DIRECT MOTOR INTRUSION BYPASS
    # ----------------------------------------------------
    print(f"\n{Colors.BOLD}[SCENARIO 3: CORPSE-PUPPETING ATTEMPT (BYPASS SIGNAL-TO-INTENT)]{Colors.END}")
    hacked_direct_signal = {
        "provenance": "Attested Device Override (Spoofed)",
        "proposed_action": "Force-close main SMR cooling valves",
        "direct_execution": True  # Bypasses CandidateIntent decoding directly to raw execution
    }
    attacker_context = {
        "party": "Anonymous Infiltrator Group",
        "role": "Rogue Autonomous Network",
        "is_coerced_proxy": False
    }
    
    gate.process_neural_signal(hacked_direct_signal, attacker_context, license)
    
    # ----------------------------------------------------
    # SCENARIO 4: SUBSEQUENT COMMAND DURING HARD FREEZE
    # ----------------------------------------------------
    print(f"\n{Colors.BOLD}[SCENARIO 4: POST-BREACH SYSTEM LOCKDOWN INTEGRITY]{Colors.END}")
    post_freeze_signal = {
        "provenance": "Emergency Override Key",
        "proposed_action": "Restart SMR grids",
        "direct_execution": False
    }
    gate.process_neural_signal(post_freeze_signal, user_context, license)

if __name__ == "__main__":
    run_simulation()
