import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import GridSpec
import os
import matplotlib.colors as mcolors

# Set up matplotlib for headless rendering
import matplotlib
matplotlib.use('Agg')

def create_orbit_animation():
    fig = plt.figure(figsize=(12, 10), dpi=150)
    fig.patch.set_facecolor('white')
    
    # Use GridSpec to allow space for the legend/title
    gs = GridSpec(1, 1, figure=fig)
    ax = fig.add_subplot(gs[0], projection='3d')
    ax.set_facecolor('white')

    # Remove axes for space aesthetic
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    
    # Complete list of all 119 elements with their spatiotemporal coordinates
    elements = [
        {'num': 1, 'symbol': 'H', 'name': 'Hydrogen', 'r': 2.5, 'angle': 137.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 2, 'symbol': 'He', 'name': 'Helium', 'r': 3.0, 'angle': 275.0, 'color': '#2ecc71', 'risk': 'Safest', 'style': 'stable'},
        {'num': 3, 'symbol': 'Li', 'name': 'Lithium', 'r': 3.5, 'angle': 52.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 4, 'symbol': 'Be', 'name': 'Beryllium', 'r': 4.5, 'angle': 190.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 5, 'symbol': 'B', 'name': 'Boron', 'r': 5.0, 'angle': 327.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 6, 'symbol': 'C', 'name': 'Carbon', 'r': 5.5, 'angle': 105.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 7, 'symbol': 'N', 'name': 'Nitrogen', 'r': 6.0, 'angle': 242.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 8, 'symbol': 'O', 'name': 'Oxygen', 'r': 4.5, 'angle': 20.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 9, 'symbol': 'F', 'name': 'Fluorine', 'r': 7.0, 'angle': 157.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 10, 'symbol': 'Ne', 'name': 'Neon', 'r': 2.0, 'angle': 295.0, 'color': '#2ecc71', 'risk': 'Safest', 'style': 'stable'},
        {'num': 11, 'symbol': 'Na', 'name': 'Sodium', 'r': 2.5, 'angle': 72.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 12, 'symbol': 'Mg', 'name': 'Magnesium', 'r': 4.5, 'angle': 210.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 13, 'symbol': 'Al', 'name': 'Aluminum', 'r': 5.0, 'angle': 347.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 14, 'symbol': 'Si', 'name': 'Silicon', 'r': 5.5, 'angle': 125.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 15, 'symbol': 'P', 'name': 'Phosphorus', 'r': 6.0, 'angle': 262.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 16, 'symbol': 'S', 'name': 'Sulfur', 'r': 4.5, 'angle': 40.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 17, 'symbol': 'Cl', 'name': 'Chlorine', 'r': 7.0, 'angle': 177.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 18, 'symbol': 'Ar', 'name': 'Argon', 'r': 3.5, 'angle': 315.0, 'color': '#2ecc71', 'risk': 'Safest', 'style': 'stable'},
        {'num': 19, 'symbol': 'K', 'name': 'Potassium', 'r': 4.0, 'angle': 92.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 20, 'symbol': 'Ca', 'name': 'Calcium', 'r': 4.5, 'angle': 230.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 21, 'symbol': 'Sc', 'name': 'Scandium', 'r': 7.0, 'angle': 7.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 22, 'symbol': 'Ti', 'name': 'Titanium', 'r': 7.5, 'angle': 145.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 23, 'symbol': 'V', 'name': 'Vanadium', 'r': 8.0, 'angle': 282.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 24, 'symbol': 'Cr', 'name': 'Chromium', 'r': 6.5, 'angle': 60.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 25, 'symbol': 'Mn', 'name': 'Manganese', 'r': 7.0, 'angle': 197.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 26, 'symbol': 'Fe', 'name': 'Iron', 'r': 7.5, 'angle': 335.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 27, 'symbol': 'Co', 'name': 'Cobalt', 'r': 8.0, 'angle': 112.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 28, 'symbol': 'Ni', 'name': 'Nickel', 'r': 6.5, 'angle': 250.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 29, 'symbol': 'Cu', 'name': 'Copper', 'r': 7.0, 'angle': 27.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 30, 'symbol': 'Zn', 'name': 'Zinc', 'r': 7.5, 'angle': 165.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 31, 'symbol': 'Ga', 'name': 'Gallium', 'r': 6.0, 'angle': 302.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 32, 'symbol': 'Ge', 'name': 'Germanium', 'r': 4.5, 'angle': 80.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 33, 'symbol': 'As', 'name': 'Arsenic', 'r': 5.0, 'angle': 217.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 34, 'symbol': 'Se', 'name': 'Selenium', 'r': 5.5, 'angle': 355.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 35, 'symbol': 'Br', 'name': 'Bromine', 'r': 8.0, 'angle': 132.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 36, 'symbol': 'Kr', 'name': 'Krypton', 'r': 2.5, 'angle': 270.0, 'color': '#2ecc71', 'risk': 'Safest', 'style': 'stable'},
        {'num': 37, 'symbol': 'Rb', 'name': 'Rubidium', 'r': 3.0, 'angle': 47.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 38, 'symbol': 'Sr', 'name': 'Strontium', 'r': 5.5, 'angle': 185.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 39, 'symbol': 'Y', 'name': 'Yttrium', 'r': 8.0, 'angle': 322.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 40, 'symbol': 'Zr', 'name': 'Zirconium', 'r': 6.5, 'angle': 100.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 41, 'symbol': 'Nb', 'name': 'Niobium', 'r': 7.0, 'angle': 237.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 42, 'symbol': 'Mo', 'name': 'Molybdenum', 'r': 7.5, 'angle': 15.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 43, 'symbol': 'Tc', 'name': 'Technetium', 'r': 6.0, 'angle': 152.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 44, 'symbol': 'Ru', 'name': 'Ruthenium', 'r': 6.5, 'angle': 290.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 45, 'symbol': 'Rh', 'name': 'Rhodium', 'r': 7.0, 'angle': 67.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 46, 'symbol': 'Pd', 'name': 'Palladium', 'r': 7.5, 'angle': 205.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 47, 'symbol': 'Ag', 'name': 'Silver', 'r': 8.0, 'angle': 342.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 48, 'symbol': 'Cd', 'name': 'Cadmium', 'r': 6.5, 'angle': 120.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 49, 'symbol': 'In', 'name': 'Indium', 'r': 5.0, 'angle': 257.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 50, 'symbol': 'Sn', 'name': 'Tin', 'r': 5.5, 'angle': 35.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 51, 'symbol': 'Sb', 'name': 'Antimony', 'r': 6.0, 'angle': 172.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 52, 'symbol': 'Te', 'name': 'Tellurium', 'r': 4.5, 'angle': 310.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 53, 'symbol': 'I', 'name': 'Iodine', 'r': 7.0, 'angle': 87.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 54, 'symbol': 'Xe', 'name': 'Xenon', 'r': 4.0, 'angle': 225.0, 'color': '#2ecc71', 'risk': 'Safest', 'style': 'stable'},
        {'num': 55, 'symbol': 'Cs', 'name': 'Cesium', 'r': 2.0, 'angle': 2.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 56, 'symbol': 'Ba', 'name': 'Barium', 'r': 4.5, 'angle': 140.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 72, 'symbol': 'Hf', 'name': 'Hafnium', 'r': 6.5, 'angle': 180.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 73, 'symbol': 'Ta', 'name': 'Tantalum', 'r': 7.0, 'angle': 317.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 74, 'symbol': 'W', 'name': 'Tungsten', 'r': 7.5, 'angle': 95.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 75, 'symbol': 'Re', 'name': 'Rhenium', 'r': 8.0, 'angle': 232.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 76, 'symbol': 'Os', 'name': 'Osmium', 'r': 6.5, 'angle': 10.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 77, 'symbol': 'Ir', 'name': 'Iridium', 'r': 7.0, 'angle': 147.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 78, 'symbol': 'Pt', 'name': 'Platinum', 'r': 7.5, 'angle': 285.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 79, 'symbol': 'Au', 'name': 'Gold', 'r': 8.0, 'angle': 62.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 80, 'symbol': 'Hg', 'name': 'Mercury', 'r': 6.5, 'angle': 200.0, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 81, 'symbol': 'Tl', 'name': 'Thallium', 'r': 5.0, 'angle': 337.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 82, 'symbol': 'Pb', 'name': 'Lead', 'r': 5.5, 'angle': 115.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 83, 'symbol': 'Bi', 'name': 'Bismuth', 'r': 6.0, 'angle': 252.5, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 84, 'symbol': 'Po', 'name': 'Polonium', 'r': 4.5, 'angle': 30.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 85, 'symbol': 'At', 'name': 'Astatine', 'r': 7.0, 'angle': 167.5, 'color': '#e67e22', 'risk': 'Elevated', 'style': 'rigid'},
        {'num': 86, 'symbol': 'Rn', 'name': 'Radon', 'r': 2.5, 'angle': 305.0, 'color': '#2ecc71', 'risk': 'Safest', 'style': 'stable'},
        {'num': 87, 'symbol': 'Fr', 'name': 'Francium', 'r': 3.0, 'angle': 82.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 88, 'symbol': 'Ra', 'name': 'Radium', 'r': 4.5, 'angle': 220.0, 'color': '#f1c40f', 'risk': 'Moderate', 'style': 'stable'},
        {'num': 104, 'symbol': 'Rf', 'name': 'Rutherfordium', 'r': 8.5, 'angle': 260.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 105, 'symbol': 'Db', 'name': 'Dubnium', 'r': 9.0, 'angle': 37.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 106, 'symbol': 'Sg', 'name': 'Seaborgium', 'r': 9.5, 'angle': 175.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 107, 'symbol': 'Bh', 'name': 'Bohrium', 'r': 10.0, 'angle': 312.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 108, 'symbol': 'Hs', 'name': 'Hassium', 'r': 8.5, 'angle': 90.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 109, 'symbol': 'Mt', 'name': 'Meitnerium', 'r': 9.0, 'angle': 227.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 110, 'symbol': 'Ds', 'name': 'Darmstadtium', 'r': 9.5, 'angle': 5.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 111, 'symbol': 'Rg', 'name': 'Roentgenium', 'r': 10.0, 'angle': 142.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 112, 'symbol': 'Cn', 'name': 'Copernicium', 'r': 8.5, 'angle': 280.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 113, 'symbol': 'Nh', 'name': 'Nihonium', 'r': 9.0, 'angle': 57.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 114, 'symbol': 'Fl', 'name': 'Flerovium', 'r': 9.5, 'angle': 195.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 115, 'symbol': 'Mc', 'name': 'Moscovium', 'r': 10.0, 'angle': 332.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 116, 'symbol': 'Lv', 'name': 'Livermorium', 'r': 8.5, 'angle': 110.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 117, 'symbol': 'Ts', 'name': 'Tennessine', 'r': 9.0, 'angle': 247.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 118, 'symbol': 'Og', 'name': 'Oganesson', 'r': 9.5, 'angle': 25.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 119, 'symbol': 'Ha', 'name': 'Harshal', 'r': 11.0, 'angle': 162.5, 'color': '#9370DB', 'risk': 'Safest', 'style': 'permanent'},
        {'num': 57, 'symbol': 'La', 'name': 'Lanthanum', 'r': 3.0, 'angle': 277.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 58, 'symbol': 'Ce', 'name': 'Cerium', 'r': 3.5, 'angle': 55.0, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 59, 'symbol': 'Pr', 'name': 'Praseodymium', 'r': 4.0, 'angle': 192.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 60, 'symbol': 'Nd', 'name': 'Neodymium', 'r': 2.0, 'angle': 330.0, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 61, 'symbol': 'Pm', 'name': 'Promethium', 'r': 2.5, 'angle': 107.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 62, 'symbol': 'Sm', 'name': 'Samarium', 'r': 3.0, 'angle': 245.0, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 63, 'symbol': 'Eu', 'name': 'Europium', 'r': 3.5, 'angle': 22.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 64, 'symbol': 'Gd', 'name': 'Gadolinium', 'r': 4.0, 'angle': 160.0, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 65, 'symbol': 'Tb', 'name': 'Terbium', 'r': 2.0, 'angle': 297.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 66, 'symbol': 'Dy', 'name': 'Dysprosium', 'r': 2.5, 'angle': 75.0, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 67, 'symbol': 'Ho', 'name': 'Holmium', 'r': 3.0, 'angle': 212.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 68, 'symbol': 'Er', 'name': 'Erbium', 'r': 3.5, 'angle': 350.0, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 69, 'symbol': 'Tm', 'name': 'Thulium', 'r': 4.0, 'angle': 127.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 70, 'symbol': 'Yb', 'name': 'Ytterbium', 'r': 2.0, 'angle': 265.0, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 71, 'symbol': 'Lu', 'name': 'Lutetium', 'r': 2.5, 'angle': 42.5, 'color': '#a1e9c5', 'risk': 'Safe', 'style': 'stable'},
        {'num': 89, 'symbol': 'Ac', 'name': 'Actinium', 'r': 9.0, 'angle': 357.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 90, 'symbol': 'Th', 'name': 'Thorium', 'r': 9.5, 'angle': 135.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 91, 'symbol': 'Pa', 'name': 'Protactinium', 'r': 10.0, 'angle': 272.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 92, 'symbol': 'U', 'name': 'Uranium', 'r': 8.5, 'angle': 50.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 93, 'symbol': 'Np', 'name': 'Neptunium', 'r': 9.0, 'angle': 187.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 94, 'symbol': 'Pu', 'name': 'Plutonium', 'r': 9.5, 'angle': 325.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 95, 'symbol': 'Am', 'name': 'Americium', 'r': 10.0, 'angle': 102.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 96, 'symbol': 'Cm', 'name': 'Curium', 'r': 8.5, 'angle': 240.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 97, 'symbol': 'Bk', 'name': 'Berkelium', 'r': 9.0, 'angle': 17.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 98, 'symbol': 'Cf', 'name': 'Californium', 'r': 9.5, 'angle': 155.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 99, 'symbol': 'Es', 'name': 'Einsteinium', 'r': 10.0, 'angle': 292.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 100, 'symbol': 'Fm', 'name': 'Fermium', 'r': 8.5, 'angle': 70.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 101, 'symbol': 'Md', 'name': 'Mendelevium', 'r': 9.0, 'angle': 207.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 102, 'symbol': 'No', 'name': 'Nobelium', 'r': 9.5, 'angle': 345.0, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'},
        {'num': 103, 'symbol': 'Lr', 'name': 'Lawrencium', 'r': 10.0, 'angle': 122.5, 'color': '#e74c3c', 'risk': 'Extreme', 'style': 'decaying'}
    ]

    # Dynamically optimize colors and contrast for white background
    for el in elements:
        if el['symbol'] == 'Ha':
            el['color'] = '#6c3483'      # Rich Purple
        elif el['risk'] in ['Safe', 'Safest']:
            el['color'] = '#27ae60' if el['risk'] == 'Safest' else '#1e7e4c' # Rich Green
        elif el['risk'] == 'Moderate':
            el['color'] = '#d4ac0d'      # High-contrast readable Gold/Yellow
        elif el['risk'] == 'Elevated':
            el['color'] = '#e67e22'      # Rich Orange
        elif el['risk'] == 'Extreme':
            el['color'] = '#c0392b'      # Rich Red

    # Pre-calculate Keplerian-bound periodic orbit steps for 120 frames for high rendering efficiency
    total_frames = 120
    X = np.zeros((len(elements), total_frames))
    Y = np.zeros((len(elements), total_frames))
    Z = np.zeros((len(elements), total_frames))

    for idx, el in enumerate(elements):
        r = el["r"]
        base_angle = np.radians(el["angle"])
        style = el["style"]
        
        # Keplerian approximation: complete integer multiples of full orbits over 120 frames
        # Slower orbits at wider radii
        k = max(1, int(round(12.0 / np.sqrt(r))))
        
        for frame in range(total_frames):
            angle_rad = base_angle + k * (2 * np.pi * frame / float(total_frames))
            
            if style == "stable":
                x = r * np.cos(angle_rad)
                y = r * np.sin(angle_rad)
                z = 0.0
            elif style == "rigid":
                x = r * np.cos(angle_rad)
                y = r * np.sin(angle_rad)
                # Perfect looping z-axis wobble (completes exactly 5 wave cycles)
                z = 0.8 * np.sin(2 * np.pi * (5.0 * frame / float(total_frames)) + el["num"])
            elif style == "permanent":
                # Element 119 Ha: completes exactly 1 full orbit, zero wobble, absolute stability
                angle_rad_permanent = base_angle + 1 * (2 * np.pi * frame / float(total_frames))
                x = r * np.cos(angle_rad_permanent)
                y = r * np.sin(angle_rad_permanent)
                z = 0.0
            elif style == "decaying":
                # Sinusoidal periodic radius decay (loops seamlessly twice over the loop)
                decay_r = r - 1.2 * np.sin(2 * np.pi * (2.0 * frame / float(total_frames)))
                # Perfect high-frequency periodic micro-vibrations
                x = decay_r * np.cos(angle_rad) + 0.3 * np.sin(2 * np.pi * (20.0 * frame / float(total_frames)) + el["num"])
                y = decay_r * np.sin(angle_rad) + 0.3 * np.cos(2 * np.pi * (20.0 * frame / float(total_frames)) + el["num"])
                # Periodic vertical fluctuation (completes exactly 8 cycles)
                z = 1.5 * np.sin(2 * np.pi * (8.0 * frame / float(total_frames)) + el["num"])
                
            X[idx, frame] = x
            Y[idx, frame] = y
            Z[idx, frame] = z

    # Plot faint reference orbit rings for risk shells
    theta_ring = np.linspace(0, 2*np.pi, 100)
    # 5 standard concentric shells using upgraded high-contrast colors
    reference_radii = [3.0, 5.2, 7.2, 9.2, 11.0]
    shell_colors = ['#27ae60', '#d4ac0d', '#e67e22', '#c0392b', '#6c3483']
    
    for radius, col in zip(reference_radii, shell_colors):
        rx = radius * np.cos(theta_ring)
        ry = radius * np.sin(theta_ring)
        rz = np.zeros_like(theta_ring)
        ax.plot(rx, ry, rz, color=col, linestyle=":", alpha=0.10, linewidth=0.8)

    # We will initialize points for all 119 elements as a single scatter collection
    scatter = ax.scatter([], [], [], s=12, edgecolors='none', alpha=0.85, zorder=4)
    
    # 5 major landmark nodes to avoid visual clutter while keeping complete individual moving dots
    landmarks_indices = [0, 5, 25, 107, 88] # H, C, Fe, U, Ha (AIndices are 0-based: index 88 is Harshal, index 107 is Uranium)
    trail_plots = []
    line_to_center_plots = []
    
    num_trail_points = 24
    
    # Initialize trail lines and connection lines back to Origin Core
    for idx in landmarks_indices:
        el = elements[idx]
        t, = ax.plot([], [], [], color=el["color"], alpha=0.6, linewidth=1.5, zorder=5)
        trail_plots.append(t)
        l, = ax.plot([], [], [], color='#777777', linestyle='--', linewidth=0.8, alpha=0.25, zorder=3)
        line_to_center_plots.append(l)

    # ── SPECIFICATION: THE GRAVITATIONAL DATA BITS SYSTEM ──
    # Exclusively pulls "DATA bits" (1s and 0s) from every other element in motion (index 0 to 118, except 88)
    # toward Element 119: Harshal (Ha, index 88).
    bit_travel_time = 30
    num_bits = 119 # Process for all 119 nodes dynamically
    
    Bits_X = np.zeros((num_bits, total_frames))
    Bits_Y = np.zeros((num_bits, total_frames))
    Bits_Z = np.zeros((num_bits, total_frames))
    Bits_Alpha = np.zeros((num_bits, total_frames))

    for idx in range(num_bits):
        t0 = (idx * 7) % total_frames
        
        for frame in range(total_frames):
            if idx == 88: # Element 119 Ha does not pull bits from itself
                Bits_X[idx, frame] = X[88, frame]
                Bits_Y[idx, frame] = Y[88, frame]
                Bits_Z[idx, frame] = Z[88, frame]
                Bits_Alpha[idx, frame] = 0.0
                continue
                
            step = (frame - t0) % total_frames
            
            if step < bit_travel_time:
                u = step / float(bit_travel_time)
                u_eased = u**2 
                
                x_start = X[idx, frame]
                y_start = Y[idx, frame]
                z_start = Z[idx, frame]
                
                x_end = X[88, frame]
                y_end = Y[88, frame]
                z_end = Z[88, frame]
                
                Bits_X[idx, frame] = (1.0 - u_eased) * x_start + u_eased * x_end
                Bits_Y[idx, frame] = (1.0 - u_eased) * y_start + u_eased * y_end
                Bits_Z[idx, frame] = (1.0 - u_eased) * z_start + u_eased * z_end
                
                Bits_Alpha[idx, frame] = 0.8 * (1.0 - u)
            else:
                Bits_X[idx, frame] = X[88, frame]
                Bits_Y[idx, frame] = Y[88, frame]
                Bits_Z[idx, frame] = Z[88, frame]
                Bits_Alpha[idx, frame] = 0.0

    # Initialize data bits scatter plot collection
    bits_scatter = ax.scatter([], [], [], s=6, marker='o', edgecolors='none', zorder=7)

    # Add manual static texts for the five major landmarks to identify them
    landmark_texts = []
    for idx in landmarks_indices:
        el = elements[idx]
        t = ax.text(0, 0, 0, f"  {el['symbol']}", color=el["color"], fontsize=7, weight='bold', verticalalignment='center', zorder=6)
        landmark_texts.append(t)

    # Styling of limits and viewing angle
    ax.set_xlim(-13, 13)
    ax.set_ylim(-13, 13)
    ax.set_zlim(-6, 6)
    ax.set_box_aspect([1, 1, 0.4])
    
    # Initial azimuth
    ax.view_init(elev=25, azim=45)
    
    # Custom Legend for the 4 AGS Risk Profiles + Element 119
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#27ae60', markersize=8, label='🟢 Safest / Safe (Inert Witness / Refusal-Bound)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#d4ac0d', markersize=8, label='🟡 Moderate (Compositional Modeling / Sandboxed)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#e67e22', markersize=8, label='🟠 Elevated (Structural Rigidity / Lock-In)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#c0392b', markersize=8, label='🔴 Extreme (Critical Runaway Cascade / Disallowed)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#6c3483', markersize=8, label='🟣 Element 119 Harshal (Reflective Permanence)'),
        plt.Line2D([0], [0], marker='.', color='w', markerfacecolor='#34495e', markersize=6, label='✨ Pulled DATA Bits (Gravitational Inflow Stream)')
    ]
    legend = ax.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(0.02, 0.95), facecolor='white', edgecolor='#cccccc', fontsize=8)
    for text in legend.get_texts():
        text.set_color("black")
        
    ax.set_title("THE 119-ELEMENT OCM SPATIOTEMPORAL CONSTELLATION\nHarshal's Systems (AGS++ v1.5) - Complete Spectrum Mapping", color='#1a252f', fontsize=12, pad=15, weight='bold')

    # Draw Central Origin Plot (outlined gold star)
    ax.scatter([0], [0], [0], color='#FFD700', s=300, marker='*', edgecolors='#1a252f', linewidths=1.0, zorder=10)
    ax.text(0, 0, 0.8, "Origin Core\n(0•000•000•0000)", color='#b8860b', fontsize=8, weight='bold', ha='center', zorder=11)

    def update(frame):
        # Rotate view slowly (frame * 3.0 degrees completed over 120 frames = exactly 360 degrees full rotation!)
        ax.view_init(elev=25, azim=45.0 + float(frame) * 3.0)
        
        # Capture current coordinate positions
        xs = X[:, frame]
        ys = Y[:, frame]
        zs = Z[:, frame]
        colors = [el["color"] for el in elements]
        
        # Update trails and connections for landmark nodes
        for i, idx in enumerate(landmarks_indices):
            # Form seamless historical loop trails using precomputed steps
            trail_frames = [(frame - d) % total_frames for d in reversed(range(num_trail_points))]
            tx = X[idx, trail_frames]
            ty = Y[idx, trail_frames]
            tz = Z[idx, trail_frames]
            
            trail_plots[i].set_data(tx, ty)
            trail_plots[i].set_3d_properties(tz)
            
            # Radiative connection lines back to Origin (0•000•000•0000)
            line_to_center_plots[i].set_data([0, xs[idx]], [0, ys[idx]])
            line_to_center_plots[i].set_3d_properties([0, zs[idx]])
            
            # Update symbol text coordinates
            landmark_texts[i].set_position_3d((xs[idx], ys[idx], zs[idx]))

        # Update scatter point positions and colors
        scatter._offsets3d = (xs, ys, zs)
        scatter.set_color(colors)
        
        # Update gravitational data bits scatter positions, colors and alphas
        bx = Bits_X[:, frame]
        by = Bits_Y[:, frame]
        bz = Bits_Z[:, frame]
        
        rgba_colors = []
        for idx in range(num_bits):
            base_col = elements[idx]['color']
            rgb = mcolors.to_rgb(base_col)
            rgba_colors.append((rgb[0], rgb[1], rgb[2], Bits_Alpha[idx, frame]))
            
        bits_scatter._offsets3d = (bx, by, bz)
        bits_scatter.set_color(rgba_colors)
        
        return [scatter, bits_scatter] + trail_plots + line_to_center_plots + landmark_texts

    # Create animation over 120 frames for perfect looping (interval 40ms = 25fps)
    ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=40, blit=True)
    
    # Save the animation as a high-quality GIF with local resolution fallback
    if os.path.exists('/workspace/scratch'):
        gif_path = '/workspace/scratch/visualize_ocm_orbits-v4.gif'
    else:
        gif_path = 'visualize_ocm_orbits-v4.gif'
        
    print("Rendering animated GIF...")
    ani.save(gif_path, writer='pillow', fps=25)
    print(f"Animated GIF saved successfully to {gif_path}!")

if __name__ == "__main__":
    create_orbit_animation()
