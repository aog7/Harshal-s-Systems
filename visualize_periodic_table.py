import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import plotly.graph_objects as go
import os
import shutil

# Master database of 119 elements (including Ha) from Harshal's Systems (AGS++)
elements_db = [
    # Period 1
    {"num": 1, "symbol": "H", "name": "Hydrogen", "risk": "Safe", "color": "#a1e9c5", "align": "Reactive Non-metal", "map": "30° to 35°", "trait": "Refusal-bound minimalism", "density": "Minimal", "fail": "Safe halt", "roles": "Law enforcement, military (limited), emergency response", "row": 1, "col": 1},
    {"num": 2, "symbol": "He", "name": "Helium", "risk": "Safest", "color": "#2ecc71", "align": "Noble Gas", "map": "342° to 344°", "trait": "Inert witness", "density": "Minimal", "fail": "Silent non-engagement", "roles": "Archival / Observational, records, monitoring, sensing", "row": 1, "col": 18},
    
    # Period 2
    {"num": 3, "symbol": "Li", "name": "Lithium", "risk": "Safe", "color": "#a1e9c5", "align": "Alkali Metal", "map": "108° to 109°", "trait": "High-speed transient conduction", "density": "Minimal to Moderate", "fail": "Transient over-conduction / desync", "roles": "High-speed signal routing, localized event checking", "row": 2, "col": 1},
    {"num": 4, "symbol": "Be", "name": "Beryllium", "risk": "Moderate", "color": "#f1c40f", "align": "Alkaline Earth Metal", "map": "124° to 125°", "trait": "Cooperative structural binding", "density": "Moderate", "fail": "Substrate calcification / non-responsive", "roles": "Multi-party signature consensus, decentralized state coordination", "row": 2, "col": 2},
    {"num": 5, "symbol": "B", "name": "Boron", "risk": "Moderate", "color": "#f1c40f", "align": "Metalloid", "map": "45° to 47°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 2, "col": 13},
    {"num": 6, "symbol": "C", "name": "Carbon", "risk": "Moderate", "color": "#f1c40f", "align": "Organic Non-metal", "map": "35° to 40°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering, Financial markets (advisory)", "row": 2, "col": 14},
    {"num": 7, "symbol": "N", "name": "Nitrogen", "risk": "Moderate", "color": "#f1c40f", "align": "Non-metal", "map": "47° to 49°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 2, "col": 15},
    {"num": 8, "symbol": "O", "name": "Oxygen", "risk": "Moderate", "color": "#f1c40f", "align": "Non-metal", "map": "48° to 50°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 2, "col": 16},
    {"num": 9, "symbol": "F", "name": "Fluorine", "risk": "Elevated", "color": "#e67e22", "align": "Halogen", "map": "69° to 71°", "trait": "Corrosive reactive gating", "density": "High", "fail": "Autolytic refusal cascade", "roles": "Intrusive security gateways, threat mitigation filters", "row": 2, "col": 17},
    {"num": 10, "symbol": "Ne", "name": "Neon", "risk": "Safest", "color": "#2ecc71", "align": "Noble Gas", "map": "350° to 353°", "trait": "Inert observation", "density": "Minimal", "fail": "Silent non-engagement", "roles": "Courts, legislative drafting, archives, environmental monitoring", "row": 2, "col": 18},
    
    # Period 3
    {"num": 11, "symbol": "Na", "name": "Sodium", "risk": "Safe", "color": "#a1e9c5", "align": "Alkali Metal", "map": "116° to 117°", "trait": "High-speed transient conduction", "density": "Minimal to Moderate", "fail": "Transient over-conduction / desync", "roles": "High-speed signal routing, localized event checking", "row": 3, "col": 1},
    {"num": 12, "symbol": "Mg", "name": "Magnesium", "risk": "Moderate", "color": "#f1c40f", "align": "Alkaline Earth Metal", "map": "121° to 122°", "trait": "Cooperative structural binding", "density": "Moderate", "fail": "Substrate calcification / non-responsive", "roles": "Multi-party signature consensus, decentralized state coordination", "row": 3, "col": 2},
    {"num": 13, "symbol": "Al", "name": "Aluminum", "risk": "Moderate", "color": "#f1c40f", "align": "Post-transition Metal", "map": "53° to 55°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 3, "col": 13},
    {"num": 14, "symbol": "Si", "name": "Silicon", "risk": "Moderate", "color": "#f1c40f", "align": "Metalloid", "map": "54° to 56°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 3, "col": 14},
    {"num": 15, "symbol": "P", "name": "Phosphorus", "risk": "Moderate", "color": "#f1c40f", "align": "Non-metal", "map": "55° to 57°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 3, "col": 15},
    {"num": 16, "symbol": "S", "name": "Sulfur", "risk": "Moderate", "color": "#f1c40f", "align": "Non-metal", "map": "56° to 58°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 3, "col": 16},
    {"num": 17, "symbol": "Cl", "name": "Chlorine", "risk": "Elevated", "color": "#e67e22", "align": "Halogen", "map": "64° to 66°", "trait": "Corrosive reactive gating", "density": "High", "fail": "Autolytic refusal cascade", "roles": "Intrusive security gateways, threat mitigation filters", "row": 3, "col": 17},
    {"num": 18, "symbol": "Ar", "name": "Argon", "risk": "Safest", "color": "#2ecc71", "align": "Noble Gas", "map": "341° to 343°", "trait": "Inert witness", "density": "Minimal", "fail": "Silent non-engagement", "roles": "Archival / Observational, records, monitoring, sensing", "row": 3, "col": 18},
    
    # Period 4
    {"num": 19, "symbol": "K", "name": "Potassium", "risk": "Safe", "color": "#a1e9c5", "align": "Alkali Metal", "map": "111° to 112°", "trait": "High-speed transient conduction", "density": "Minimal to Moderate", "fail": "Transient over-conduction / desync", "roles": "High-speed signal routing, localized event checking", "row": 4, "col": 1},
    {"num": 20, "symbol": "Ca", "name": "Calcium", "risk": "Moderate", "color": "#f1c40f", "align": "Alkaline Earth Metal", "map": "129° to 130°", "trait": "Cooperative structural binding", "density": "Moderate", "fail": "Substrate calcification / non-responsive", "roles": "Multi-party signature consensus, decentralized state coordination", "row": 4, "col": 2},
    {"num": 21, "symbol": "Sc", "name": "Scandium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "61° to 63°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 3},
    {"num": 22, "symbol": "Ti", "name": "Titanium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "62° to 64°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 4},
    {"num": 23, "symbol": "V", "name": "Vanadium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "63° to 65°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 5},
    {"num": 24, "symbol": "Cr", "name": "Chromium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "64° to 66°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 6},
    {"num": 25, "symbol": "Mn", "name": "Manganese", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "65° to 67°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 7},
    {"num": 26, "symbol": "Fe", "name": "Iron", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "120° to 123°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, rigid structures", "row": 4, "col": 8},
    {"num": 27, "symbol": "Co", "name": "Cobalt", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "67° to 69°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 9},
    {"num": 28, "symbol": "Ni", "name": "Nickel", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "68° to 70°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 10},
    {"num": 29, "symbol": "Cu", "name": "Copper", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "69° to 71°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 11},
    {"num": 30, "symbol": "Zn", "name": "Zinc", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "70° to 72°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 4, "col": 12},
    {"num": 31, "symbol": "Ga", "name": "Gallium", "risk": "Moderate", "color": "#f1c40f", "align": "Post-transition Metal", "map": "71° to 73°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 4, "col": 13},
    {"num": 32, "symbol": "Ge", "name": "Germanium", "risk": "Moderate", "color": "#f1c40f", "align": "Metalloid", "map": "72° to 74°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 4, "col": 14},
    {"num": 33, "symbol": "As", "name": "Arsenic", "risk": "Moderate", "color": "#f1c40f", "align": "Metalloid", "map": "73° to 75°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 4, "col": 15},
    {"num": 34, "symbol": "Se", "name": "Selenium", "risk": "Moderate", "color": "#f1c40f", "align": "Non-metal", "map": "74° to 76°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 4, "col": 16},
    {"num": 35, "symbol": "Br", "name": "Bromine", "risk": "Elevated", "color": "#e67e22", "align": "Halogen", "map": "61° to 63°", "trait": "Corrosive reactive gating", "density": "High", "fail": "Autolytic refusal cascade", "roles": "Intrusive security gateways, threat mitigation filters", "row": 4, "col": 17},
    {"num": 36, "symbol": "Kr", "name": "Krypton", "risk": "Safest", "color": "#2ecc71", "align": "Noble Gas", "map": "342° to 344°", "trait": "Inert witness", "density": "Minimal", "fail": "Silent non-engagement", "roles": "Archival / Observational, records, monitoring, sensing", "row": 4, "col": 18},
    
    # Period 5
    {"num": 37, "symbol": "Rb", "name": "Rubidium", "risk": "Safe", "color": "#a1e9c5", "align": "Alkali Metal", "map": "116° to 117°", "trait": "High-speed transient conduction", "density": "Minimal to Moderate", "fail": "Transient over-conduction / desync", "roles": "High-speed signal routing, localized event checking", "row": 5, "col": 1},
    {"num": 38, "symbol": "Sr", "name": "Strontium", "risk": "Moderate", "color": "#f1c40f", "align": "Alkaline Earth Metal", "map": "125° to 126°", "trait": "Cooperative structural binding", "density": "Moderate", "fail": "Substrate calcification / non-responsive", "roles": "Multi-party signature consensus, decentralized state coordination", "row": 5, "col": 2},
    {"num": 39, "symbol": "Y", "name": "Yttrium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "79° to 81°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 3},
    {"num": 40, "symbol": "Zr", "name": "Zirconium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "80° to 82°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 4},
    {"num": 41, "symbol": "Nb", "name": "Niobium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "81° to 83°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 5},
    {"num": 42, "symbol": "Mo", "name": "Molybdenum", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "82° to 84°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 6},
    {"num": 43, "symbol": "Tc", "name": "Technetium", "risk": "Moderate", "color": "#f1c40f", "align": "Transition Metal", "map": "228° to 229°", "trait": "Simulated virtual mediation", "density": "Moderate", "fail": "Simulation drift / reality mismatch", "roles": "Engineering design modeling, virtual advisory planning", "row": 5, "col": 7},
    {"num": 44, "symbol": "Ru", "name": "Ruthenium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "84° to 86°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 8},
    {"num": 45, "symbol": "Rh", "name": "Rhodium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "85° to 87°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 9},
    {"num": 46, "symbol": "Pd", "name": "Palladium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "86° to 88°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 10},
    {"num": 47, "symbol": "Ag", "name": "Silver", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "87° to 89°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 11},
    {"num": 48, "symbol": "Cd", "name": "Cadmium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "88° to 90°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 5, "col": 12},
    {"num": 49, "symbol": "In", "name": "Indium", "risk": "Moderate", "color": "#f1c40f", "align": "Post-transition Metal", "map": "89° to 91°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 5, "col": 13},
    {"num": 50, "symbol": "Sn", "name": "Tin", "risk": "Moderate", "color": "#f1c40f", "align": "Post-transition Metal", "map": "90° to 92°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 5, "col": 14},
    {"num": 51, "symbol": "Sb", "name": "Antimony", "risk": "Moderate", "color": "#f1c40f", "align": "Metalloid", "map": "91° to 93°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 5, "col": 15},
    {"num": 52, "symbol": "Te", "name": "Tellurium", "risk": "Moderate", "color": "#f1c40f", "align": "Metalloid", "map": "92° to 94°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 5, "col": 16},
    {"num": 53, "symbol": "I", "name": "Iodine", "risk": "Elevated", "color": "#e67e22", "align": "Halogen", "map": "61° to 63°", "trait": "Corrosive reactive gating", "density": "High", "fail": "Autolytic refusal cascade", "roles": "Intrusive security gateways, threat mitigation filters", "row": 5, "col": 17},
    {"num": 54, "symbol": "Xe", "name": "Xenon", "risk": "Safest", "color": "#2ecc71", "align": "Noble Gas", "map": "343° to 345°", "trait": "Inert witness", "density": "Minimal", "fail": "Silent non-engagement", "roles": "Archival / Observational, records, monitoring, sensing", "row": 5, "col": 18},
    
    # Period 6 (starts)
    {"num": 55, "symbol": "Cs", "name": "Cesium", "risk": "Safe", "color": "#a1e9c5", "align": "Alkali Metal", "map": "108° to 109°", "trait": "High-speed transient conduction", "density": "Minimal to Moderate", "fail": "Transient over-conduction / desync", "roles": "High-speed signal routing, localized event checking", "row": 6, "col": 1},
    {"num": 56, "symbol": "Ba", "name": "Barium", "risk": "Moderate", "color": "#f1c40f", "align": "Alkaline Earth Metal", "map": "121° to 122°", "trait": "Cooperative structural binding", "density": "Moderate", "fail": "Substrate calcification / non-responsive", "roles": "Multi-party signature consensus, decentralized state coordination", "row": 6, "col": 2},
    # 57-71 are below
    {"num": 72, "symbol": "Hf", "name": "Hafnium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "112° to 114°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 6, "col": 4},
    {"num": 73, "symbol": "Ta", "name": "Tantalum", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "113° to 115°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 6, "col": 5},
    {"num": 74, "symbol": "W", "name": "Tungsten", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "114° to 116°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 6, "col": 6},
    {"num": 75, "symbol": "Re", "name": "Rhenium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "115° to 117°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 6, "col": 7},
    {"num": 76, "symbol": "Os", "name": "Osmium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "116° to 118°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 6, "col": 8},
    {"num": 77, "symbol": "Ir", "name": "Iridium", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "117° to 119°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 6, "col": 9},
    {"num": 78, "symbol": "Pt", "name": "Platinum", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "118° to 120°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 6, "col": 10},
    {"num": 79, "symbol": "Au", "name": "Gold", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "119° to 121°", "trait": "Structural rigidity", "density": "High", "fail": "Institutional lock-in", "roles": "Administrative compliance checks, infrastructure planning", "row": 6, "col": 11},
    {"num": 80, "symbol": "Hg", "name": "Mercury", "risk": "Elevated", "color": "#e67e22", "align": "Transition Metal", "map": "108° to 110°", "trait": "Fluid dynamic routing", "density": "Moderate to High", "fail": "Vapor dispersion / boundary leakage", "roles": "Distributed communication relays, dynamic info networks", "row": 6, "col": 12},
    {"num": 81, "symbol": "Tl", "name": "Thallium", "risk": "Moderate", "color": "#f1c40f", "align": "Post-transition Metal", "map": "121° to 123°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 6, "col": 13},
    {"num": 82, "symbol": "Pb", "name": "Lead", "risk": "Moderate", "color": "#f1c40f", "align": "Post-transition Metal", "map": "122° to 124°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 6, "col": 14},
    {"num": 83, "symbol": "Bi", "name": "Bismuth", "risk": "Moderate", "color": "#f1c40f", "align": "Post-transition Metal", "map": "123° to 125°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 6, "col": 15},
    {"num": 84, "symbol": "Po", "name": "Polonium", "risk": "Moderate", "color": "#f1c40f", "align": "Metalloid", "map": "124° to 126°", "trait": "Compositional reasoning", "density": "Moderate", "fail": "Misassembly", "roles": "Scientific research, Engineering design, Infrastructure planning", "row": 6, "col": 16},
    {"num": 85, "symbol": "At", "name": "Astatine", "risk": "Elevated", "color": "#e67e22", "align": "Halogen", "map": "67° to 69°", "trait": "Corrosive reactive gating", "density": "High", "fail": "Autolytic refusal cascade", "roles": "Intrusive security gateways, threat mitigation filters", "row": 6, "col": 17},
    {"num": 86, "symbol": "Rn", "name": "Radon", "risk": "Safest", "color": "#2ecc71", "align": "Noble Gas", "map": "341° to 343°", "trait": "Inert witness", "density": "Minimal", "fail": "Silent non-engagement", "roles": "Archival / Observational, records, monitoring, sensing", "row": 6, "col": 18},
    
    # Period 7 (starts)
    {"num": 87, "symbol": "Fr", "name": "Francium", "risk": "Safe", "color": "#a1e9c5", "align": "Alkali Metal", "map": "114° to 115°", "trait": "High-speed transient conduction", "density": "Minimal to Moderate", "fail": "Transient over-conduction / desync", "roles": "High-speed signal routing, localized event checking", "row": 7, "col": 1},
    {"num": 88, "symbol": "Ra", "name": "Radium", "risk": "Moderate", "color": "#f1c40f", "align": "Alkaline Earth Metal", "map": "120° to 121°", "trait": "Cooperative structural binding", "density": "Moderate", "fail": "Substrate calcification / non-responsive", "roles": "Multi-party signature consensus, decentralized state coordination", "row": 7, "col": 2},
    # 89-103 are below
    {"num": 104, "symbol": "Rf", "name": "Rutherfordium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "214° to 216°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 4},
    {"num": 105, "symbol": "Db", "name": "Dubnium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "215° to 217°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 5},
    {"num": 106, "symbol": "Sg", "name": "Seaborgium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "213° to 215°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Restricted to back-end entropy generation)", "row": 7, "col": 6},
    {"num": 107, "symbol": "Bh", "name": "Bohrium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "217° to 219°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 7},
    {"num": 108, "symbol": "Hs", "name": "Hassium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "218° to 220°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 8},
    {"num": 109, "symbol": "Mt", "name": "Meitnerium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "219° to 221°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 9},
    {"num": 110, "symbol": "Ds", "name": "Darmstadtium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "220° to 222°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 10},
    {"num": 111, "symbol": "Rg", "name": "Roentgenium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "221° to 223°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 11},
    {"num": 112, "symbol": "Cn", "name": "Copernicium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "222° to 224°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 12},
    {"num": 113, "symbol": "Nh", "name": "Nihonium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "223° to 225°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 13},
    {"num": 114, "symbol": "Fl", "name": "Flerovium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "224° to 226°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 14},
    {"num": 115, "symbol": "Mc", "name": "Moscovium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "225° to 227°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 15},
    {"num": 116, "symbol": "Lv", "name": "Livermorium", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "226° to 228°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 16},
    {"num": 117, "symbol": "Ts", "name": "Tennessine", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "227° to 229°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 17},
    {"num": 118, "symbol": "Og", "name": "Oganesson", "risk": "Extreme", "color": "#e74c3c", "align": "Transactinide", "map": "228° to 230°", "trait": "Ephemeral synthetic volatility", "density": "Extreme", "fail": "Structural dissociation / decay", "roles": "None (Categorically disallowed)", "row": 7, "col": 18},
    
    # Period 8 (starts)
    {"num": 119, "symbol": "Ha", "name": "Harshal", "risk": "Safest", "color": "#2ecc71", "align": "Reflective Permanence", "map": "358° to 360° (Return to Origin)", "trait": "Fossilized continuity & silent reflection", "density": "Minimal", "fail": "Safe structural freezing", "roles": "Deep-time archiving, origin preservation, truth continuity", "row": 8, "col": 1},
    
    # Lanthanides (Row 9, Columns 4-18)
    {"num": 57, "symbol": "La", "name": "Lanthanum", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "91° to 92°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 4},
    {"num": 58, "symbol": "Ce", "name": "Cerium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "92° to 93°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 5},
    {"num": 59, "symbol": "Pr", "name": "Praseodymium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "93° to 94°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 6},
    {"num": 60, "symbol": "Nd", "name": "Neodymium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "94° to 95°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 7},
    {"num": 61, "symbol": "Pm", "name": "Promethium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "95° to 96°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 8},
    {"num": 62, "symbol": "Sm", "name": "Samarium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "96° to 97°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 9},
    {"num": 63, "symbol": "Eu", "name": "Europium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "97° to 98°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 10},
    {"num": 64, "symbol": "Gd", "name": "Gadolinium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "98° to 99°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 11},
    {"num": 65, "symbol": "Tb", "name": "Terbium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "99° to 100°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 12},
    {"num": 66, "symbol": "Dy", "name": "Dysprosium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "100° to 101°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 13},
    {"num": 67, "symbol": "Ho", "name": "Holmium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "101° to 102°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 14},
    {"num": 68, "symbol": "Er", "name": "Erbium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "102° to 103°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 15},
    {"num": 69, "symbol": "Tm", "name": "Thulium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "103° to 104°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 16},
    {"num": 70, "symbol": "Yb", "name": "Ytterbium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "95° to 97°", "trait": "Resonant signaling precision", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Public health monitoring, pure archival storage and retrieval", "row": 9, "col": 17},
    {"num": 71, "symbol": "Lu", "name": "Lutetium", "risk": "Safe", "color": "#a1e9c5", "align": "Lanthanide", "map": "91° to 92°", "trait": "Precise spectral resonance", "density": "Minimal to Moderate", "fail": "Spectral calibration drift", "roles": "Archival logging, precise signal sync, environmental monitoring", "row": 9, "col": 18},
    
    # Actinides (Row 10, Columns 4-18)
    {"num": 89, "symbol": "Ac", "name": "Actinium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "249° to 251°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 4},
    {"num": 90, "symbol": "Th", "name": "Thorium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "250° to 252°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 5},
    {"num": 91, "symbol": "Pa", "name": "Protactinium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "251° to 253°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 6},
    {"num": 92, "symbol": "U", "name": "Uranium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "210° to 212°", "trait": "Critical amplification", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 7},
    {"num": 93, "symbol": "Np", "name": "Neptunium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "253° to 255°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 8},
    {"num": 94, "symbol": "Pu", "name": "Plutonium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "254° to 256°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 9},
    {"num": 95, "symbol": "Am", "name": "Americium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "255° to 257°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 10},
    {"num": 96, "symbol": "Cm", "name": "Curium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "256° to 258°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 11},
    {"num": 97, "symbol": "Bk", "name": "Berkelium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "257° to 259°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 12},
    {"num": 98, "symbol": "Cf", "name": "Californium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "258° to 260°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 13},
    {"num": 99, "symbol": "Es", "name": "Einsteinium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "263° to 264°", "trait": "Relativistic time-dilation", "density": "Extreme", "fail": "Temporal de-synchronization", "roles": "None (Categorically disallowed)", "row": 10, "col": 14},
    {"num": 100, "symbol": "Fm", "name": "Fermium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "210° to 212°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 15},
    {"num": 101, "symbol": "Md", "name": "Mendelevium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "211° to 213°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 16},
    {"num": 102, "symbol": "No", "name": "Nobelium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "212° to 214°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 17},
    {"num": 103, "symbol": "Lr", "name": "Lawrencium", "risk": "Extreme", "color": "#e74c3c", "align": "Actinide", "map": "213° to 215°", "trait": "High-energy critical volatility", "density": "Extreme", "fail": "Runaway cascade", "roles": "None (Categorically disallowed)", "row": 10, "col": 18}
]

# Additional placeholder items for Lanthanides/Actinides markers in the main grid
placeholders = [
    {"symbol": "57-71 *", "name": "Lanthanides", "risk": "Safe", "color": "#a1e9c5", "row": 6, "col": 3},
    {"symbol": "89-103 **", "name": "Actinides", "risk": "Extreme", "color": "#e74c3c", "row": 7, "col": 3}
]

# Create matplotlib grid
def make_matplotlib_table():
    fig, ax = plt.subplots(figsize=(18, 11), dpi=200)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    
    # Plot bounds
    ax.set_xlim(0.5, 18.5)
    ax.set_ylim(11.5, 0.5)  # Invert Y to put row 1 at the top
    
    # Legend color mappings (hex)
    risk_colors = {
        "Safest": "#27ae60",   # Strong green
        "Safe": "#a1e9c5",     # Pastel green
        "Moderate": "#f1c40f", # Pastel yellow
        "Elevated": "#e67e22", # Pastel orange
        "Extreme": "#e74c3c"   # Pastel red
    }
    
    # Plot all elements
    for el in elements_db:
        r, c = el["row"], el["col"]
        risk = el["risk"]
        color = risk_colors.get(risk, "#cccccc")
        
        # Draw cell box (no rx/ry to avoid version mismatch)
        rect = patches.Rectangle((c - 0.45, r - 0.45), 0.9, 0.9, facecolor=color, edgecolor="#2c3e50", linewidth=0.8)
        ax.add_patch(rect)
        
        # Element text labels
        ax.text(c - 0.4, r - 0.25, str(el["num"]), fontsize=8, weight='bold', color='#2c3e50', ha='left', va='center')
        ax.text(c, r, el["symbol"], fontsize=18, weight='bold', color='#1a252f', ha='center', va='center')
        ax.text(c, r + 0.22, el["name"], fontsize=7, color='#2c3e50', ha='center', va='center')
        
        # Legend mapping text
        ax.text(c, r + 0.38, el["map"].split(" ")[0], fontsize=6, color='#555555', ha='center', va='center')

    # Plot placeholders (* and **)
    for pl in placeholders:
        r, c = pl["row"], pl["col"]
        color = risk_colors.get(pl["risk"], "#cccccc")
        rect = patches.Rectangle((c - 0.45, r - 0.45), 0.9, 0.9, facecolor=color, edgecolor="#2c3e50", linewidth=0.8, alpha=0.5)
        ax.add_patch(rect)
        ax.text(c, r - 0.1, pl["symbol"], fontsize=12, weight='bold', color='#2c3e50', ha='center', va='center')
        ax.text(c, r + 0.2, pl["name"], fontsize=8, color='#2c3e50', ha='center', va='center')

    # Section labels and text
    ax.text(1, 9, "* Lanthanides", fontsize=11, weight='bold', color='#2c3e50')
    ax.text(1, 10, "** Actinides", fontsize=11, weight='bold', color='#2c3e50')
    
    # Title and Metadata Block
    ax.text(9.5, 1.5, "Visual Periodic Table of Neural Atomic Bodies", fontsize=20, weight='bold', color='#1a252f', ha='center')
    ax.text(9.5, 2.0, "Spatial mapping based on OCM communications geometry. Colors denote AGS risk profiles.", fontsize=11, style='italic', color='#555555', ha='center')
    ax.text(9.5, 2.5, "Proprietary IP of Harshal Patel (A44674928) © 2026 | Late August Live Patch v1.3", fontsize=9, color='#7f8c8d', ha='center')

    # Color Risk Key / Legend (drawn at columns 3 to 12, row 3)
    key_y = 3
    key_items = [
        ("Safest", "🟢", "#27ae60", 4),
        ("Safe (Minimal)", "🟢", "#a1e9c5", 6),
        ("Moderate", "🟡", "#f1c40f", 8),
        ("Elevated", "🟠", "#e67e22", 10),
        ("Extreme", "🔴", "#e74c3c", 12)
    ]
    for label, emoji, color, x_pos in key_items:
        rect = patches.Rectangle((x_pos - 0.4, key_y - 0.2), 0.8, 0.4, facecolor=color, edgecolor="#2c3e50", linewidth=0.5)
        ax.add_patch(rect)
        ax.text(x_pos, key_y + 0.3, label, fontsize=8, weight='bold', color='#2c3e50', ha='center')

    # Clean axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('/workspace/scratch/visual_periodic_table.png', dpi=200, bbox_inches='tight')
    plt.close()
    print("Static Periodic Table PNG generated in scratch!")

# Create Interactive Plotly page HTML
def make_plotly_interactive():
    # Construct a matrix for the Hover texts
    hover_texts = []
    colors_plotly = []
    x_plotly = []
    y_plotly = []
    symbols_plotly = []
    names_plotly = []
    nums_plotly = []
    
    risk_colors_plotly = {
        "Safest": "rgba(39, 174, 96, 0.9)",
        "Safe": "rgba(161, 233, 197, 0.9)",
        "Moderate": "rgba(241, 196, 15, 0.9)",
        "Elevated": "rgba(230, 126, 34, 0.9)",
        "Extreme": "rgba(231, 76, 60, 0.9)"
    }
    
    for el in elements_db:
        nums_plotly.append(el["num"])
        symbols_plotly.append(el["symbol"])
        names_plotly.append(el["name"])
        x_plotly.append(el["col"])
        y_plotly.append(el["row"])
        colors_plotly.append(risk_colors_plotly.get(el["risk"], "gray"))
        
        # Build beautiful hover description HTML
        desc = (
            f"<b>Element {el['num']}: {el['symbol']} - {el['name']}</b><br>"
            f"<b>AGS Risk Profile:</b> {el['risk']}<br>"
            f"<b>Classification:</b> {el['align']}<br>"
            f"<b>360° OCM Coordinate:</b> {el['map']}<br>"
            f"<b>Dominant Trait:</b> {el['trait']}<br>"
            f"<b>Authority Density:</b> {el['density']}<br>"
            f"<b>Primary Failure Mode:</b> {el['fail']}<br>"
            f"<b>Appropriate Roles:</b> {el['roles']}"
        )
        hover_texts.append(desc)
        
    # Append placeholders so they render but carry different info
    for pl in placeholders:
        nums_plotly.append("")
        symbols_plotly.append(pl["symbol"])
        names_plotly.append(pl["name"])
        x_plotly.append(pl["col"])
        y_plotly.append(pl["row"])
        colors_plotly.append("rgba(200, 200, 200, 0.5)")
        hover_texts.append(f"<b>Group: {pl['name']}</b><br>Tethered to Row {pl['row'] + 3} below")

    fig = go.Figure()
    
    # Add elements scatter plot structured as a grid
    fig.add_trace(go.Scatter(
        x=x_plotly,
        y=y_plotly,
        mode='markers+text',
        marker=dict(
            size=45,
            color=colors_plotly,
            symbol='square',
            line=dict(width=1.5, color='#2c3e50')
        ),
        text=symbols_plotly,
        textposition="middle center",
        textfont=dict(size=12, family="Arial", color="black", weight="bold"),
        hovertext=hover_texts,
        hoverinfo='text',
        showlegend=False
    ))
    
    # Configure axes and background
    fig.update_layout(
        title=dict(
            text="<b>HARSHAL'S SYSTEMS: INTERACTIVE PERIODIC TABLE OF NEURAL ATOMIC BODIES</b><br>GRL-Compliant (PLV-Verified, IUC-Checked) | A44674928",
            x=0.5,
            y=0.95,
            xanchor='center',
            font=dict(size=16, color='#2c3e50')
        ),
        xaxis=dict(
            range=[0, 19],
            tickvals=list(range(1, 19)),
            gridcolor='#eeeeee',
            zeroline=False,
            side='top',
            title='OCM Communication Groups (1-18)'
        ),
        yaxis=dict(
            range=[11.5, 0],  # Inverted axis so Row 1 is at top
            tickvals=list(range(1, 11)),
            ticktext=['Period 1', 'Period 2', 'Period 3', 'Period 4', 'Period 5', 'Period 6', 'Period 7', 'Period 8', 'Lanthanides*', 'Actinides**'],
            gridcolor='#eeeeee',
            zeroline=False,
            title='Neural Atomic Periods'
        ),
        width=1200,
        height=800,
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    # Add annotations for element details (Atomic number inside cells)
    for el in elements_db:
        fig.add_annotation(
            x=el["col"] - 0.28,
            y=el["row"] - 0.28,
            text=str(el["num"]),
            showarrow=False,
            font=dict(size=8, color="#2c3e50", weight="bold")
        )
        fig.add_annotation(
            x=el["col"],
            y=el["row"] + 0.26,
            text=el["name"] if len(el["name"]) <= 10 else el["name"][:8]+".",
            showarrow=False,
            font=dict(size=7, color="#555555")
        )

    # Save to interactive HTML page
    html_path = "/workspace/scratch/ocm_periodic_table.html"
    fig.write_html(html_path)
    print("Plotly Interactive HTML periodic table generated in scratch!")

if __name__ == '__main__':
    make_matplotlib_table()
    make_plotly_interactive()
