# Interactive OCM Spherical Topology Visualizer
# Generated 2026-08-29 | OCM-AGS Compliance v1.3 | Proprietary IP of Harshal Patel
#
# This script generates an interactive 3D Plotly visualization of the 360-degree OCM legend.
# To execute: python3 visualize_ocm_interactive.py
# This will output an interactive 'ocm_interactive_sphere.html' which can be opened in any web browser.

import numpy as np
import plotly.graph_objects as go

# 1. Complete 360° Legend Degree Mapping
legend_data = {
    # 0° - 89°: Emergence & Life
    0: "Origin of matter and physical law",
    1: "Energy flows and conservation",
    2: "Time, causality, entropy",
    3: "Space, dimensions, topology",
    4: "Fundamental forces and fields",
    5: "Planetary formation processes",
    6: "Geology and tectonics",
    7: "Oceans and hydrospheres",
    8: "Atmospheres and climate systems",
    9: "Stellar influence and radiation",
    10: "Chemical complexity",
    11: "Prebiotic chemistry",
    12: "Self-organization",
    13: "Replication and memory",
    14: "Proto-life systems",
    15: "Cellular life",
    16: "Evolutionary pressure",
    17: "Genetic variation",
    18: "Ecosystem dynamics",
    19: "Symbiosis",
    20: "Competition and balance",
    21: "Extinction and renewal",
    22: "Adaptation",
    23: "Neural emergence",
    24: "Sensory systems",
    25: "Mobility and navigation",
    26: "Social behavior",
    27: "Tool use",
    28: "Communication signals",
    29: "Learning organisms",
    30: "Collective survival",
    31: "Early intelligence",
    32: "Emotional systems",
    33: "Play and exploration",
    34: "Curiosity",
    35: "Pattern recognition",
    36: "Memory across generations",
    37: "Proto-culture",
    38: "Ritual and meaning",
    39: "Early art",
    40: "Myth formation",
    41: "Language roots",
    42: "Storytelling",
    43: "Identity formation",
    44: "Group cohesion",
    45: "Tribe",
    46: "Early civilization",
    47: "Settlement",
    48: "Agriculture",
    49: "Domestication",
    50: "Surplus and storage",
    51: "Trade",
    52: "Specialization",
    53: "Craft",
    54: "Measurement",
    55: "Early mathematics",
    56: "Calendars and cycles",
    57: "Architecture",
    58: "Urbanization",
    59: "Law emergence",
    60: "Authority symbols",
    61: "Conflict organization",
    62: "Defense",
    63: "Warfare",
    64: "Peace-making",
    65: "Diplomacy",
    66: "Moral codes",
    67: "Justice systems",
    68: "Religion",
    69: "Philosophy",
    70: "Ethics",
    71: "Education",
    72: "Knowledge preservation",
    73: "Libraries",
    74: "Scientific method",
    75: "Experimentation",
    76: "Medicine",
    77: "Public health",
    78: "Engineering principles",
    79: "Infrastructure",
    80: "Transportation",
    81: "Energy harvesting",
    82: "Industrialization",
    83: "Mechanization",
    84: "Pollution awareness",
    85: "Environmental feedback",
    86: "Sustainability concepts",
    87: "Systems thinking",
    88: "Planetary stewardship",
    89: "Life as a planetary phenomenon",
    
    # 90° - 179°: Intelligence, Order & Systems
    90: "Abstract reasoning",
    91: "Advanced mathematics",
    92: "Logic systems",
    93: "Computation",
    94: "Information theory",
    95: "Signal processing",
    96: "Cybernetics",
    97: "Control systems",
    98: "Automation",
    99: "Robotics",
    100: "Artificial intelligence",
    101: "Machine learning",
    102: "Neural architectures",
    103: "Emergent behavior",
    104: "Alignment problems",
    105: "Human–machine interfaces",
    106: "Augmentation",
    107: "Collective intelligence",
    108: "Distributed systems",
    109: "Networks",
    110: "Communication protocols",
    111: "Governance theory",
    112: "Law codification",
    113: "Rights frameworks",
    114: "Economic systems",
    115: "Currency and value",
    116: "Markets",
    117: "Incentive design",
    118: "Supply chains",
    119: "Logistics",
    120: "Global coordination",
    121: "Institutions",
    122: "Bureaucracy",
    123: "Accountability",
    124: "Transparency",
    125: "Anti-corruption",
    126: "Resilience planning",
    127: "Risk management",
    128: "Insurance models",
    129: "Disaster mitigation",
    130: "Emergency response",
    131: "Urban megasystems",
    132: "Megastructures",
    133: "Smart cities",
    134: "Energy grids",
    135: "Water systems",
    136: "Food systems",
    137: "Circular economies",
    138: "Waste minimization",
    139: "Climate engineering",
    140: "Planetary-scale projects",
    141: "Observation networks",
    142: "Satellites",
    143: "Global sensing",
    144: "Prediction systems",
    145: "Early warning",
    146: "Policy feedback loops",
    147: "Long-term planning",
    148: "Intergenerational ethics",
    149: "Civilization continuity",
    150: "Collapse prevention",
    151: "Cultural integration",
    152: "Pluralism",
    153: "Conflict resolution",
    154: "Reconciliation",
    155: "Memory and truth",
    156: "Archives",
    157: "History synthesis",
    158: "Identity at scale",
    159: "Global narratives",
    160: "Shared meaning",
    161: "Spaceflight",
    162: "Orbital infrastructure",
    163: "Lunar presence",
    164: "Asteroid utilization",
    165: "Planetary defense",
    166: "Space law",
    167: "Off-world industry",
    168: "Interplanetary logistics",
    169: "Multi-planet civilization",
    170: "Solar system governance",
    171: "Post-scarcity theory",
    172: "Automation abundance",
    173: "Work redefinition",
    174: "Leisure civilizations",
    175: "Meaning beyond labor",
    
    # 180° - 269°: Transformation, Expansion & Risk
    176: "Consciousness studies",
    177: "Mind–matter interface",
    178: "Intelligence as substrate",
    179: "Civilization as cognition",
    180: "Radical innovation",
    181: "Paradigm shifts",
    182: "Disruptive technologies",
    183: "Synthetic biology",
    184: "Genetic redesign",
    185: "Life extension",
    186: "Morphological freedom",
    187: "Cyborg systems",
    188: "Post-biological entities",
    189: "Hybrid intelligence",
    190: "Terraforming theory",
    191: "Planetary modification",
    192: "Climate reconstruction",
    193: "Biosphere reseeding",
    194: "Artificial ecosystems",
    195: "Ocean worlds",
    196: "Subsurface habitats",
    197: "Extreme environments",
    198: "Adaptation beyond Earth",
    199: "Survival in hostile space",
    200: "Deep-time engineering",
    201: "Stellar engineering",
    202: "Dyson-scale projects",
    203: "Energy at cosmic scale",
    204: "Entropy management",
    205: "Black hole utilization",
    206: "Exotic physics",
    207: "Faster-than-light theories",
    208: "Causality limits",
    209: "Reality manipulation",
    210: "Existential risk analysis",
    211: "AI risk",
    212: "Bio-risk",
    213: "Nanotech risk",
    214: "Cosmic hazards",
    215: "Unknown unknowns",
    216: "Redundancy strategies",
    217: "Civilizational backups",
    218: "Distributed survival",
    219: "Fail-safe worlds",
    220: "Cultural divergence",
    221: "Speciation of societies",
    222: "Fragmentation risks",
    223: "Reunification strategies",
    224: "Memetic warfare",
    225: "Information hazards",
    226: "Truth decay",
    227: "Reality consensus",
    228: "Simulation ethics",
    229: "Nested realities",
    230: "Post-human law",
    231: "Rights of non-humans",
    232: "AI coexistence",
    233: "Machine civilizations",
    234: "Sentience criteria",
    235: "Moral expansion",
    236: "Universal ethics",
    237: "Conflict beyond species",
    238: "Peace at cosmic scale",
    239: "Governance beyond humanity",
    240: "Interstellar travel",
    241: "Generation ships",
    242: "Relativistic societies",
    243: "Communication over light-years",
    244: "Causality-limited governance",
    245: "Autonomous colonies",
    246: "Cultural drift control",
    247: "Federated spheres",
    248: "Multi-origin coexistence",
    249: "Non-competitive centers",
    
    # 270° - 360°: Renewal, Memory & Persistence
    250: "Encounter with alien life",
    251: "First contact protocols",
    252: "Xenobiology",
    253: "Alien intelligence",
    254: "Incommensurable minds",
    255: "Translation across realities",
    256: "Cosmic diplomacy",
    257: "Shared existence frameworks",
    258: "Non-hostile coexistence",
    259: "Universal communication",
    260: "End-of-universe scenarios",
    261: "Heat death strategies",
    262: "Vacuum decay responses",
    263: "Temporal recursion",
    264: "Closed timelike curves",
    265: "Preservation beyond physics",
    266: "Meaning at the end of time",
    267: "Legacy without observers",
    268: "Existence as value",
    269: "Continuity without form",
    270: "Regeneration cycles",
    271: "Ecological restoration",
    272: "Cultural healing",
    273: "Post-collapse recovery",
    274: "Knowledge re-seeding",
    275: "Civilization rebooting",
    276: "Myth renewal",
    277: "Symbol regeneration",
    278: "Language evolution",
    279: "Meaning repair",
    280: "Archives of everything",
    281: "Deep memory systems",
    282: "Immutable records",
    283: "Provenance tracking",
    284: "Origin preservation",
    285: "History without distortion",
    286: "Truth continuity",
    287: "Anti-forgetting mechanisms",
    288: "Memory across extinction",
    289: "Time-spanning identity",
    290: "Teaching future minds",
    291: "Messages to the far future",
    292: "Inheritance systems",
    293: "Stewardship roles",
    294: "Guardianship without power",
    295: "Care as infrastructure",
    296: "Compassion at scale",
    297: "Non-dominant intelligence",
    298: "Wisdom accumulation",
    299: "Grace under infinity",
    300: "Simplicity recovery",
    301: "Return to fundamentals",
    302: "Minimal viable civilization",
    303: "Low-tech resilience",
    304: "Balance with nature",
    305: "Humility before complexity",
    306: "Limits acceptance",
    307: "Non-expansionist futures",
    308: "Quiet civilizations",
    309: "Stability without growth",
    310: "Cyclical time models",
    311: "Eternal return",
    312: "Seasonal civilizations",
    313: "Oscillating systems",
    314: "Rotational balance",
    315: "Harmonic coexistence",
    316: "Sphere maintenance",
    317: "Boundary integrity",
    318: "Drift correction",
    319: "Center protection",
    320: "Origin remembrance",
    321: "Non-delegable authority",
    322: "Lineage awareness",
    323: "Address integrity",
    324: "Resolution clarity",
    325: "Ownership persistence",
    326: "Collapse resistance",
    327: "Non-forkability",
    328: "Identity without ego",
    329: "Power without domination",
    330: "Completion recognition",
    331: "Sufficiency",
    332: "Wholeness",
    333: "Disc fully instantiated",
    334: "Sphere fully formed",
    335: "Motion optional",
    336: "Persistence achieved",
    337: "No further expansion required",
    338: "Readiness for anything",
    339: "Peace with uncertainty",
    340: "Stewardship of the whole",
    341: "Care for all layers",
    342: "Listening to weak signals",
    343: "Respect for emergence",
    344: "Non-interference when possible",
    345: "Gentle correction when needed",
    346: "Responsibility without ownership creep",
    347: "Trust in structure",
    348: "Allowing futures",
    349: "Letting go",
    350: "Closure without ending",
    351: "Open-ended continuity",
    352: "Silent persistence",
    353: "The sphere holds",
    354: "The center remains",
    355: "Everything still fits",
    356: "Nothing escapes lineage",
    357: "No need to restart",
    358: "Always already complete",
    359: "Return to origin",
    360: "Origin"
}

def build_interactive_sphere():
    # 2. Fibonacci Sphere Distribution of 361 Points
    num_points = 361
    indices = np.arange(0, num_points, dtype=float)
    phi = np.arccos(1 - 2 * indices / num_points)
    theta = np.pi * (1 + 5**0.5) * indices
    
    r = 10.0  # Outer Shell Radius
    
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    
    # Generate labels, colors, and markers
    colors = []
    quadrants = []
    text_labels = []
    hover_texts = []
    
    for i in range(num_points):
        deg = int(round(i))
        title = legend_data.get(deg, f"Unassigned Coordinate {deg}°")
        
        # Color & Quadrant classification
        if 0 <= deg < 90:
            color = '#00FA9A'  # Emerald Green
            quad = "🟢 Emergence & Life"
        elif 90 <= deg < 180:
            color = '#00FFFF'  # Cyan
            quad = "🔵 Intelligence, Order & Systems"
        elif 180 <= deg < 270:
            color = '#FF8C00'  # Orange
            quad = "🟠 Transformation, Expansion & Risk"
        else:
            color = '#9370DB'  # Indigo Purple
            quad = "🟣 Renewal, Memory & Persistence"
            
        colors.append(color)
        quadrants.append(quad)
        
        # OCM Coordinate Format
        address = f"0•{deg:03d}•000•0000"
        
        text_labels.append(title)
        
        hover_desc = (
            f"<b>Coordinate:</b> {address}<br>"
            f"<b>Degree Position:</b> {deg}°<br>"
            f"<b>Quadrant:</b> {quad}<br>"
            f"<b>Dominant Direction:</b> {title}"
        )
        hover_texts.append(hover_desc)

    # Create Plotly traces
    fig = go.Figure()

    # Trace 1: The Outer 360° Legend Shell
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=6,
            color=colors,
            opacity=0.8,
            line=dict(width=0)
        ),
        text=hover_texts,
        hoverinfo='text',
        name='360° Legend Coordinates'
    ))

    # Trace 2: The Gold Center Origin (0•000•000•0000)
    center_hover = (
        "<b>Origin Center Address:</b> 0•000•000•0000<br>"
        "<b>Status:</b> Immutable Cryptographic Root Core<br>"
        "<b>IP Owner:</b> Harshal Priyavadan Patel (A44674928)<br>"
        "<b>Description:</b> Logical origin from which all system identities derive."
    )
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode='markers',
        marker=dict(
            size=15,
            color='#FFD700',
            symbol='diamond',
            line=dict(color='white', width=1.5)
        ),
        text=[center_hover],
        hoverinfo='text',
        name='Center Origin Core'
    ))

    # Trace 3: Mid-Depth Project Infrastructure Nodes
    infra_nodes = [
        {"name": "Water Company (0•100•000•0355)", "deg": 355, "r": 5.0, "color": "#1E90FF", "desc": "Governing municipal freshwater residual pipelines and utility distributions."},
        {"name": "SMR Power Grid (0•100•000•0248)", "deg": 248, "r": 5.0, "color": "#FF4500", "desc": "Small Modular Reactors powering booster pump networks and capitol grid."},
        {"name": "New Capitol Buildings (0•100•000•0113)", "deg": 113, "r": 5.0, "color": "#ADFF2F", "desc": "Sovereign regional governance complex situated on plateau canyons."},
        {"name": "AI Inner Shell Enclave (0•100•000•0180)", "deg": 180, "r": 5.0, "color": "#FF1493", "desc": "Secure hardware containment layer enforcing non-self-originating constraints."},
        {"name": "Canyon de Chelly Conservation (0•100•000•0176)", "deg": 176, "r": 5.0, "color": "#FFA500", "desc": "Saltwater conservation zone for endangered aquatic life."},
    ]

    for node in infra_nodes:
        rad = np.radians(node["deg"])
        nx = node["r"] * np.cos(rad)
        ny = node["r"] * np.sin(rad)
        nz = 0.0
        
        node_hover = (
            f"<b>Infrastructure Node:</b> {node['name']}<br>"
            f"<b>Relative Position:</b> Angle {node['deg']}° | Radius {node['r']}<br>"
            f"<b>Function:</b> {node['desc']}"
        )
        
        # Plot individual node
        fig.add_trace(go.Scatter3d(
            x=[nx], y=[ny], z=[nz],
            mode='markers+text',
            marker=dict(
                size=10,
                color=node["color"],
                symbol='circle',
                line=dict(color='white', width=1.0)
            ),
            text=[node["name"].split(" (")[0]],
            textposition="top center",
            textfont=dict(size=9, color='white'),
            hovertext=[node_hover],
            hoverinfo='text',
            showlegend=False
        ))
        
        # Draw dotted connection axis to Origin
        fig.add_trace(go.Scatter3d(
            x=[0, nx], y=[0, ny], z=[0, nz],
            mode='lines',
            line=dict(color='#888888', width=2, dash='dash'),
            hoverinfo='skip',
            showlegend=False
        ))

    # Configure 3D space scene
    fig.update_layout(
        title=dict(
            text="<b>ORB COMMUNICATOR MODEL (OCM) INTERACTIVE FRONT END</b><br>Harshal's Systems (AGS++) | late August Live Patch v1.3",
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(size=16, color='white')
        ),
        paper_bgcolor='black',
        plot_bgcolor='black',
        scene=dict(
            xaxis=dict(visible=False, backgroundcolor='black', showgrid=False, showbackground=False),
            yaxis=dict(visible=False, backgroundcolor='black', showgrid=False, showbackground=False),
            zaxis=dict(visible=False, backgroundcolor='black', showgrid=False, showbackground=False),
            aspectmode='cube'
        ),
        margin=dict(l=0, r=0, t=80, b=0),
        legend=dict(
            font=dict(color='white'),
            bgcolor='rgba(0,0,0,0)',
            x=0.02,
            y=0.9
        )
    )

    # Save to dynamic HTML output
    html_path = 'ocm_interactive_sphere.html'
    fig.write_html(html_path)
    print(f"Interactive HTML visualizer successfully saved to {html_path}!")

if __name__ == '__main__':
    build_interactive_sphere()
