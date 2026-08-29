import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import GridSpec

# Set up matplotlib for headless rendering
import matplotlib
matplotlib.use('Agg')

def create_orbit_animation():
    fig = plt.figure(figsize=(10, 8), dpi=120)
    fig.patch.set_facecolor('black')
    
    # Use GridSpec to allow space for the legend/title
    gs = GridSpec(1, 1, figure=fig)
    ax = fig.add_subplot(gs[0], projection='3d')
    ax.set_facecolor('black')

    # Remove axes for space aesthetic
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    
    # Constants
    center = np.array([0, 0, 0])
    
    # Elemental profiles mapping
    # Name, Angle(deg), Radius, Color, Risk, Trait, OrbitStyle
    elements = [
        {"name": "Hydrogen (H)", "angle": 32.5, "r": 3.0, "color": "#00FA9A", "risk": "[Safe]", "trait": "Refusal-bound minimalism", "style": "stable"},
        {"name": "Carbon (C)", "angle": 37.5, "r": 5.0, "color": "#FFFF00", "risk": "[Moderate]", "trait": "Compositional reasoning", "style": "stable"},
        {"name": "Iron (Fe)", "angle": 121.5, "r": 7.0, "color": "#FF8C00", "risk": "[Elevated]", "trait": "Structural rigidity / Lock-in", "style": "rigid"},
        {"name": "Uranium (U)", "angle": 211.0, "r": 9.0, "color": "#FF1493", "risk": "[Extreme]", "trait": "Critical runaway cascade", "style": "decaying"},
        {"name": "Harshal (Ha)", "angle": 359.0, "r": 10.0, "color": "#9370DB", "risk": "[Safest]", "trait": "Reflective permanence", "style": "permanent"}
    ]
    
    # Create static background rings for stable orbits
    theta_ring = np.linspace(0, 2*np.pi, 100)
    for el in elements:
        if el["style"] != "decaying":
            rx = el["r"] * np.cos(theta_ring)
            ry = el["r"] * np.sin(theta_ring)
            rz = np.zeros_like(theta_ring)
            ax.plot(rx, ry, rz, color=el["color"], linestyle=":", alpha=0.15, linewidth=0.8)
            
    # Central Origin Plot
    ax.scatter([0], [0], [0], color='#FFD700', s=150, marker='*', edgecolors='white', label="Origin Core (0•000•000•0000)")
    
    # Initialize point markers and trails
    point_plots = []
    trail_plots = []
    line_to_center_plots = []
    
    num_trail_points = 25
    trails_x = [[] for _ in elements]
    trails_y = [[] for _ in elements]
    trails_z = [[] for _ in elements]
    
    for el in elements:
        p, = ax.plot([], [], [], marker='o', markersize=8, color=el["color"], markeredgecolor='white', label=f"{el['name']} - {el['risk']}")
        point_plots.append(p)
        t, = ax.plot([], [], [], color=el["color"], alpha=0.5, linewidth=1.5)
        trail_plots.append(t)
        l, = ax.plot([], [], [], color='#555555', linestyle='--', linewidth=0.8, alpha=0.4)
        line_to_center_plots.append(l)

    # Styling of limits and viewing angle
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_zlim(-6, 6)
    
    ax.view_init(elev=25, azim=45)
    
    # Custom Legend
    legend = ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.95), facecolor='black', edgecolor='#333333', fontsize=7)
    for text in legend.get_texts():
        text.set_color("white")
        
    ax.set_title("OCM SPATIOTEMPORAL ORBIT SIMULATION\nElemental Risk Profiles & Alignment", color='white', fontsize=12, pad=10, weight='bold')

    def update(frame):
        # Rotate view slowly
        ax.view_init(elev=25, azim=45 + frame * 0.5)
        
        for i, el in enumerate(elements):
            r = el["r"]
            base_angle = np.radians(el["angle"])
            
            # Different orbit physics based on style
            if el["style"] == "stable":
                # Standard orbital angular velocity (Keplerian-like: slower for wider radii)
                speed = 2.0 / np.sqrt(r)
                omega = speed * frame * 0.05
                x = r * np.cos(base_angle + omega)
                y = r * np.sin(base_angle + omega)
                z = 0.0
            elif el["style"] == "rigid":
                # High rigidity, lock-in, slow precession
                omega = 0.3 * frame * 0.05
                x = r * np.cos(base_angle + omega)
                y = r * np.sin(base_angle + omega)
                # Rigid wobble
                z = 1.0 * np.sin(frame * 0.08)
            elif el["style"] == "permanent":
                # Deep time, slow and massive, perfectly circular, near-zero drift
                omega = 0.1 * frame * 0.05
                x = r * np.cos(base_angle + omega)
                y = r * np.sin(base_angle + omega)
                z = 0.0
            elif el["style"] == "decaying":
                # Uranium: Runaway cascade, unstable, decaying orbit
                # Spatially fluctuating, collapsing toward center, then expanding erratically
                decay_r = r - 0.05 * (frame % 150)
                omega = 3.5 * frame * 0.05
                # High-frequency fluctuations in all 3 axes
                x = decay_r * np.cos(base_angle + omega) + 0.5 * np.sin(frame * 0.5)
                y = decay_r * np.sin(base_angle + omega) + 0.5 * np.cos(frame * 0.5)
                z = 2.0 * np.sin(frame * 0.3)
                
            # Update trails
            trails_x[i].append(x)
            trails_y[i].append(y)
            trails_z[i].append(z)
            
            if len(trails_x[i]) > num_trail_points:
                trails_x[i].pop(0)
                trails_y[i].pop(0)
                trails_z[i].pop(0)
                
            # Set data
            point_plots[i].set_data([x], [y])
            point_plots[i].set_3d_properties([z])
            
            trail_plots[i].set_data(trails_x[i], trails_y[i])
            trail_plots[i].set_3d_properties(trails_z[i])
            
            # Radiative alignment lines back to Origin (0•000•000•0000)
            line_to_center_plots[i].set_data([0, x], [0, y])
            line_to_center_plots[i].set_3d_properties([0, z])
            
        return point_plots + trail_plots + line_to_center_plots

    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=200, interval=40, blit=True)
    
    # Save the animation as a high-quality GIF
    gif_path = '/workspace/scratch/visualize_ocm_orbits.gif'
    print("Rendering animated GIF...")
    ani.save(gif_path, writer='pillow', fps=25)
    print(f"Animated GIF saved successfully to {gif_path}!")

if __name__ == "__main__":
    create_orbit_animation()
