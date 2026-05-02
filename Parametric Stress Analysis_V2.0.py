import numpy as np
import matplotlib.pyplot as plt

# --- Configuration & Constants ---
LOAD_N = 800            # Axial Load (N)
SIDE_M = 0.04           # Side length (m) - 40mm
AREA_M2 = SIDE_M**2     # Cross-sectional area
MAX_STRESS_KPA = (LOAD_N / AREA_M2) / 1000 

def calculate_stresses(angles_rad):
    """Computes normal and shear stresses based on the inclined plane angle."""
    sigma = MAX_STRESS_KPA * (np.sin(angles_rad)**2)
    tau = MAX_STRESS_KPA * np.sin(angles_rad) * np.cos(angles_rad)
    return sigma, tau

def setup_plot(title, ylabel):
    """Applies standard formatting to plots."""
    plt.title(title, fontsize=12, fontweight='bold')
    plt.xlabel('Theta Angle (degrees)', fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlim(0, 180)

def generate_plots():
    # Domain definition (0 to 180 degrees)
    theta_deg = np.linspace(0, 180, 500)
    theta_rad = np.radians(theta_deg)
    
    sigma, tau = calculate_stresses(theta_rad)

    # --- Normal Stress Plot ---
    plt.figure(figsize=(8, 5))
    plt.plot(theta_deg, sigma, color='navy', linewidth=2, label=r'$\sigma$ (Normal)')
    setup_plot('Average Normal Stress vs. Theta', 'Stress (kPa)')
    
    # Peak annotation
    plt.annotate(f'Max: {MAX_STRESS_KPA:.0f} kPa (90°)', 
                 xy=(90, MAX_STRESS_KPA), 
                 xytext=(110, MAX_STRESS_KPA - 50),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1))
    
    plt.legend()
    plt.tight_layout()
    plt.savefig('normal_stress.png', dpi=300)
    plt.show()

    # --- Shear Stress Plot ---
    plt.figure(figsize=(8, 5))
    plt.plot(theta_deg, tau, color='firebrick', linewidth=2, label=r'$\tau$ (Shear)')
    setup_plot('Average Shear Stress vs. Theta', 'Stress (kPa)')
    plt.axhline(0, color='black', linewidth=0.8)

    # Critical point annotations
    tau_max = MAX_STRESS_KPA / 2
    plt.annotate(f'Max: {tau_max:.1f} kPa (45°)', 
                 xy=(45, tau_max), 
                 xytext=(10, tau_max + 20),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1))
    
    plt.annotate(f'Min: {-tau_max:.1f} kPa (135°)', 
                 xy=(135, -tau_max), 
                 xytext=(145, -tau_max - 20),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1))

    plt.legend()
    plt.tight_layout()
    plt.savefig('shear_stress.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    generate_plots()
    print("Execution successful. Files 'normal_stress.png' and 'shear_stress.png' generated.")