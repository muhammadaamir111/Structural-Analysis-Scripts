import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Catenary Profile Generator
# 3DCP Formwork-Free Slab — NUST Final Year Design Project
# Author: Muhammad Aamir
# ============================================================

def catenary_profile(a, x_range, num_points=500):
    """
    Generate catenary curve coordinates.
    
    Parameters:
        a         : catenary parameter (controls curve depth)
        x_range   : half-span of the slab (meters)
        num_points: resolution of the curve
    
    Returns:
        x, y : coordinate arrays
    """
    x = np.linspace(-x_range, x_range, num_points)
    y = a * np.cosh(x / a) - a
    return x, y


def horizontal_thrust(w, L, f):
    """
    Calculate horizontal thrust at supports.
    
    Parameters:
        w : distributed load (kN/m)
        L : span length (m)
        f : sag/rise of catenary (m)
    
    Returns:
        H : horizontal thrust (kN)
    """
    H = (w * L**2) / (8 * f)
    return H


def kevlar_tension(H, angle_deg):
    """
    Calculate required Kevlar string tension to counteract thrust.
    
    Parameters:
        H         : horizontal thrust (kN)
        angle_deg : string angle from horizontal (degrees)
    
    Returns:
        T : required tension in Kevlar string (kN)
    """
    angle_rad = np.radians(angle_deg)
    T = H / np.cos(angle_rad)
    return T


def plot_catenary(x, y, span, rise):
    """Plot and save the catenary slab profile."""
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'b-', linewidth=2.5, label='Catenary Profile')
    plt.fill_between(x, y, min(y), alpha=0.15, color='blue')
    plt.axhline(y=0, color='gray', linestyle='--', linewidth=1)
    plt.title('Catenary Slab Profile — 3DCP Formwork-Free Design', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Horizontal Span (m)')
    plt.ylabel('Depth (m)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('catenary_profile.png', dpi=150)
    plt.show()
    print("✅ Profile saved as catenary_profile.png")


# ============================================================
# Main — Edit these parameters for your slab dimensions
# ============================================================
if __name__ == "__main__":

    # Slab parameters
    a         = 2.5    # catenary parameter (m)
    x_range   = 3.0    # half-span (m) → total span = 6m
    w         = 5.0    # distributed load (kN/m)
    L         = 6.0    # full span (m)
    f         = 0.8    # sag/rise (m)
    angle_deg = 30     # Kevlar string angle (degrees)

    # Generate profile
    x, y = catenary_profile(a, x_range)

    # Calculate thrust and tension
    H = horizontal_thrust(w, L, f)
    T = kevlar_tension(H, angle_deg)

    # Print results
    print("=" * 45)
    print("   CATENARY SLAB — STRUCTURAL SUMMARY")
    print("=" * 45)
    print(f"  Span             : {L} m")
    print(f"  Catenary param a : {a} m")
    print(f"  Distributed load : {w} kN/m")
    print(f"  Horizontal Thrust: {H:.2f} kN")
    print(f"  Kevlar Tension   : {T:.2f} kN @ {angle_deg}°")
    print("=" * 45)

    # Plot
    plot_catenary(x, y, L, f)
