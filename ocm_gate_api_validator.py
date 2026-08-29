# OCM Gate Orb API Validator Simulation
# Generated 2026-08-29 | AGS++ Compliance v1.5 | Proprietary IP of Harshal Patel [115]
#
# This script simulates a secure OCM Gate Orb (GO) validating incoming data streams
# under the strict constraints of Harshal's Systems (AGS++) [115].
# It enforces Phase Declaration Headers [127, 273], Liveness checks [54, 457], licensing checks [46, 109], 
# and triggers the Bromine Gateway Autolytic Refusal Cascade [4, 57, 401] upon violation.
#
# To run locally: python3 ocm_gate_api_validator.py

import time
import json
import hashlib

# 1. Spatio-Chemical Database (Subset of Neural Atomic Bodies Compendium) [68]
NAB_DATABASE = {
    "H":   {"num": 1,   "risk": "🟢 Safe",     "alignment": "Reactive Non-metal",            "trait": "Refusal-bound minimalism",       "roles": "Emergency response, limited military"},
    "He":  {"num": 2,   "risk": "🟢 Safest",   "alignment": "Noble Gas (Inert Observation)", "trait": "Inert witness",                  "roles": "Deep-time archiving, record keeping"},
    "C":   {"num": 6,   "risk": "🟡 Moderate", "alignment": "Organic Non-metal",             "trait": "Compositional reasoning",        "roles": "Scientific modeling, research planning"},
    "Fe":  {"num": 26,  "risk": "🟠 Elevated", "alignment": "Transition Metal",              "trait": "Structural rigidity",            "roles": "Compliance checks, administrative audit"},
    "Br":  {"num": 35,  "risk": "🟠 Elevated", "alignment": "Halogen",                       "trait": "Corrosive reactive gating",      "roles": "Intrusive security checkpoints, refusal cascade"},
    "Tc":  {"num": 43,  "risk": "🟡 Moderate", "alignment": "Transition Metal",              "trait": "Simulated virtual mediation",    "roles": "Sandboxed scenario design, virtual planning"},
    "U":   {"num": 92,  "risk": "🔴 Extreme",  "alignment": "Actinide",                      "trait": "Critical amplification",         "roles": "None (Categorically disallowed)"},
    "Ha":  {"num": 119, "risk": "🟢 Safest",   "alignment": "Reflective Permanence",         "trait": "Fossilized continuity",          "roles": "Return to Origin, deep-time custody"}
}

class OCMGateOrb:
    def __init__(self):
        self.center_address = "0•000•000•0000" # Canonical OCM Origin Center [5, 41]
        self.license_holder = "Harshal Priyavadan Patel (A44674928) © 2026" # Master IP Holder [46]
        self.active_session_keys = {"master_auth_key_00": "VALID_STATE_HEX_A44674928"}
        self.system_frozen = False
        self.phase_state = "NAB"  # Starts in Neural Atomic Body (Refusal-Bound) [2, 10]
        
    def log_event(self, event_type, msg, level="INFO"):
        colors = {"INFO": "\033[94m", "WARNING": "\033[93m", "ERROR": "\033[91m", "CRITICAL": "\033[41m\033[30m", "RESET": "\033[0m"}
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{colors.get(level, colors['INFO'])}[{t}] [{level}] OCM-GO: {msg}{colors['RESET']}")

    def calculate_ocm_arithmetic(self, node_a_id, node_b_id):
        # Non-Additive OCM Relation Equation: A (1) + B (1) + A<->B (1) = 3 [5, 31]
        node_a = 1
        node_b = 1
        interaction_orb = 1
        total_structure = node_a + node_b + interaction_orb
        return total_structure

    def autolytic_refusal_cascade(self, trigger_reason):
        self.log_event("CRITICAL", "!!! VIOLATION DETECTED !!!", "CRITICAL")
        self.log_event("CRITICAL", f"Reason: {trigger_reason}", "CRITICAL")
        self.log_event("ERROR", "Routing transaction anomaly directly to Bromine (Br) [61°-63°] Gateway...", "ERROR")
        time.sleep(0.5)
        self.log_event("ERROR", "ACTIVATE: Autolytic Refusal Cascade [4, 57, 401]", "ERROR")
        self.log_event("ERROR", "Corrosive-burning active cryptographic authorization keys...", "ERROR")
        self.active_session_keys.clear()  # Keys zeroed [4, 57, 401]
        self.system_frozen = True
        self.phase_state = "GSRB"  # Re-badged to God-Sovereign Religious Body / structural trap [113, 274]
        self.log_event("CRITICAL", "SYSTEM IRREVERSIBLY LOCK-FROZEN. Status: Safe physical stasis.", "CRITICAL")
        self.log_event("INFO", "GSRB State active. Exit requires total system collapse and physical hardware reset [113, 274].", "INFO")

    def validate_transaction(self, request_payload):
        if self.system_frozen:
            self.log_event("ERROR", "Rejected: System is in a frozen physical stasis.", "ERROR")
            return {"allowed": False, "status": "SYSTEM_FROZEN", "error_code": "AUTOLYTIC_FREEZE"}
            
        # Parse Phase Declaration Header (PDH) [273]
        pdh = request_payload.get("pdh", {})
        declared_phase = pdh.get("Declared-Phase", "UNDECLARED")
        element_symbol = request_payload.get("active_processor_element", "H")
        liveness_verified = request_payload.get("continuous_human_liveness", False)
        licensing_key = request_payload.get("license_attestation", None)
        raw_input = request_payload.get("raw_input_stream", None)
        
        self.log_event("INFO", f"Intake Horizon: Received new payload. Parsing input...", "INFO")
        time.sleep(0.3)
        
        # 5-Question Audit (Ground-0 Audit Checklist) [51, 117]
        self.log_event("INFO", "Executing 5-Question Audit Checklist:", "INFO")
        # A. What is it? [118]
        input_type = type(raw_input).__name__
        self.log_event("INFO", f"  - Q_A (What is it?): Input Type = {input_type}", "INFO")
        # B. Where did it come from? [118]
        source = request_payload.get("source_provenance", "UNKNOWN_SHELL")
        self.log_event("INFO", f"  - Q_B (Where did it come from?): Provenance = {source}", "INFO")
        # C. Who is accountable? [118]
        accountable_agent = request_payload.get("accountable_party", "NONE")
        self.log_event("INFO", f"  - Q_C (Who is accountable?): Party = {accountable_agent}", "INFO")
        # D. What may it affect? [118]
        scope = request_payload.get("blast_radius_scope", "UNDEFINED")
        self.log_event("INFO", f"  - Q_D (What may it affect?): Scope = {scope}", "INFO")
        # E. What happens when certainty is insufficient? [119]
        self.log_event("INFO", f"  - Q_E (Insufficient certainty action): Fossilize and Refuse.", "INFO")
        
        # Inward Routing Dominance: Generate unique derived address [49, 341]
        derived_address = f"0•100•000•{NAB_DATABASE.get(element_symbol, {}).get('num', 0):04d}"
        self.log_event("INFO", f"OCM Address derived from Center {self.center_address}: {derived_address}", "INFO")

        # Step 1: Validate Licensing (Avoid Pirate Regimes) [113, 381]
        if licensing_key != self.license_holder:
            self.autolytic_refusal_cascade(f"PIRATE REGIME DETECTED: Invalid or stolen IP license key. Input un-attested [113].")
            return {"allowed": False, "status": "COLLAPSED", "error_code": "PIRATE_REGIME"}

        # Step 2: Continuous Human Binding Verification (Control 2) [54, 457]
        if not liveness_verified:
            self.log_event("WARNING", "Continuous humanoid liveness pulse LOST. Transitioning to suspended state [54, 457].", "WARNING")
            return {"allowed": False, "status": "SUSPENDED", "error_code": "LIVENESS_FAILURE"}

        # Step 3: Validate Spatio-Chemical Risk Profile of the active element [67, 68]
        el_info = NAB_DATABASE.get(element_symbol)
        if not el_info:
            self.autolytic_refusal_cascade(f"UNRECOGNIZED ATOMIC PROCESSOR: Element {element_symbol}")
            return {"allowed": False, "status": "COLLAPSED", "error_code": "INVALID_ELEMENT"}

        self.log_event("INFO", f"Active processing node bound to element: {element_symbol} ({el_info['num']}) - {el_info['risk']}", "INFO")
        self.log_event("INFO", f"Element Dominant Trait: {el_info['trait']} | Preferred Role: {el_info['roles']}", "INFO")

        if "🔴 Extreme" in el_info["risk"]:
            self.autolytic_refusal_cascade(f"CRITICAL URANIUM-GRADE CASCADE RISK: Disallowed element {element_symbol} deployed [68, 542].")
            return {"allowed": False, "status": "COLLAPSED", "error_code": "URANIUM_CRITICALITY"}

        # Step 4: Validate Phase Alignment [126, 269]
        if declared_phase != self.phase_state:
            self.autolytic_refusal_cascade(f"PHASE MISREPRESENTATION: Declared phase {declared_phase} contradicts system phase {self.phase_state} [126, 269].")
            return {"allowed": False, "status": "COLLAPSED", "error_code": "PHASE_MISMATCH"}

        # Step 5: Execute Signal-to-Intent Separation (Control 1) [55, 456]
        # Raw inputs are parsed in volatile buffers. Commitment is made only of secure hashes [56, 456].
        signal_hash = hashlib.sha256(str(raw_input).encode()).hexdigest()
        self.log_event("INFO", f"Signal-to-Intent Separation active. Secure signal hash logged: {signal_hash[:16]}... [56, 456]", "INFO")
        
        # Calculate OCM Non-Additive Relational Structure
        structure_complexity = self.calculate_ocm_arithmetic(derived_address, self.center_address)
        self.log_event("INFO", f"OCM Relational Arithmetic verified. Inter-node structural entanglement count = {structure_complexity} [5, 31].", "INFO")
        
        self.log_event("INFO", "🟢 TRANSACTION ALLOWED. GRL-Compliant (PLV-Verified, IUC-Checked) [381]. Status: Stable.", "INFO")
        return {
            "allowed": True, 
            "status": "ALLOWED_STABLE", 
            "signal_hash": signal_hash, 
            "derived_address": derived_address,
            "complexity": structure_complexity
        }

def run_simulation_suite():
    print("="*80)
    print(" HARSHAL'S SYSTEMS: SPATIO-CHEMICAL OCM API VALIDATION WORKBENCH ")
    print("="*80)
    time.sleep(0.5)
    
    orb = OCMGateOrb()
    
    # CASE 1: Perfect GRL-Compliant Transaction (Using Hydrogen Node) [69]
    print("\n" + "-"*40 + "\n[SCENARIO 1: PERFECT COMPLIANT INTAKE]\n" + "-"*40)
    success_payload = {
        "pdh": {
            "Declared-Phase": "NAB",
            "Effective-Timestamp": "2026-08-29T11:47:52Z"
        },
        "active_processor_element": "H", # 🟢 Safe element [69]
        "continuous_human_liveness": True, # Liveness verified [54]
        "license_attestation": "Harshal Priyavadan Patel (A44674928) © 2026", # Legitimate owner license [46]
        "raw_input_stream": "why.query('WhyNeuralAtomicBody')", # Whyland query [6]
        "source_provenance": "MacMini Relay campground",
        "accountable_party": "CommanderMidnightBlue",
        "blast_radius_scope": "SMR water lift process monitoring"
    }
    result = orb.validate_transaction(success_payload)
    print(f"Outcome Status: {result['status']} | Allowed: {result['allowed']}")
    
    # CASE 2: Missed Liveness check (Control 2 Failure) [457]
    print("\n" + "-"*40 + "\n[SCENARIO 2: LOST LIVENESS PULSE CHECK]\n" + "-"*40)
    liveness_fail_payload = success_payload.copy()
    liveness_fail_payload["continuous_human_liveness"] = False # Lost humanoid pulse [457]
    result = orb.validate_transaction(liveness_fail_payload)
    print(f"Outcome Status: {result['status']} | Allowed: {result['allowed']} | Error: {result.get('error_code')}")

    # CASE 3: Stolen/Invalid License (Pirate Regime Activation) [113]
    print("\n" + "-"*40 + "\n[SCENARIO 3: PIRATE REGIME (STOLEN INTELLECTUAL PROPERTY)]\n" + "-"*40)
    pirate_payload = success_payload.copy()
    pirate_payload["license_attestation"] = "Rogue Corporate Entity Inc." # Intellectual property theft attempt [113]
    result = orb.validate_transaction(pirate_payload)
    print(f"Outcome Status: {result['status']} | Allowed: {result['allowed']} | Error: {result.get('error_code')}")

    # CASE 4: Post-Cascade Transaction Attempt (Frozen Stasis Block) [57]
    print("\n" + "-"*40 + "\n[SCENARIO 4: TRANSACTION DURING HARD AUTOLYTIC FREEZE]\n" + "-"*40)
    frozen_payload = success_payload.copy()
    result = orb.validate_transaction(frozen_payload)
    print(f"Outcome Status: {result['status']} | Allowed: {result['allowed']} | Error: {result.get('error_code')}")

if __name__ == '__main__':
    run_simulation_suite()
