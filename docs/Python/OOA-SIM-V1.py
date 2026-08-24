# Lead Architect: Emanuel Schaaf
# Open Origin Architecture
# PCME-RAM Research Modeling and Feasibility Framework V1

import sys
import traceback

try:
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
except ImportError as e:
    print(f"Critical Import Error: {e}")
    input("Press Enter to safely exit the application...")
    sys.exit(1)

def run_simulation():
    # --- Style Configuration (Dark Mode) ---
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(14, 12), facecolor="#0d1117")
    fig.suptitle("PCME-RAM: OOA-SIM-V1 Parameter Visualization", fontsize=16, color="#00ffcc", fontweight="bold")
    
    gs = fig.add_gridspec(3, 1, hspace=0.45)
    ax1 = fig.add_subplot(gs[0, 0], facecolor="#161b22")
    ax2 = fig.add_subplot(gs[1, 0], facecolor="#161b22")
    ax3 = fig.add_subplot(gs[2, 0], facecolor="#161b22")
    
    for ax in [ax1, ax2, ax3]:
        ax.grid(color="#30363d", linestyle="--", linewidth=0.5)
        ax.tick_params(colors="white")
        for spine in ax.spines.values():
            spine.set_color("#30363d")
            
    # --- Data Generation (Framework Models) ---
    frames = 150
    
    # 1. LLG Dynamics Approximation (Sigmoid Reversal)
    t_llg = np.linspace(0, 5, frames)  # Time in ns
    mz = -1 + 2 / (1 + np.exp(-3 * (t_llg - 2.5))) 
    
    # 2. BVD Equivalent Circuit (Impedance over Frequency)
    freq = np.linspace(1e9, 10e9, frames)  # 1 GHz to 10 GHz
    omega = 2 * np.pi * freq
    C0 = 2e-13  
    Cm = 1e-14  
    Lm = 1e-8   
    Rm = 5.0    
    
    Z_m = Rm + 1j * omega * Lm + 1 / (1j * omega * Cm)
    Z_total = 1 / (1j * omega * C0 + 1 / Z_m)
    Z_mag = np.abs(Z_total)
    
    # 3. Acoustic Attenuation Model (A(x) = A_0 * e^(-alpha * x))
    layers = np.linspace(1, 16, frames)  # 1 to 16 Layers (Stack)
    alpha_damping = 0.12  # Assumed attenuation coefficient
    amplitude = 1.0 * np.exp(-alpha_damping * layers)
    
    # --- Plot Setup ---
    line1, = ax1.plot([], [], color="#00ffcc", lw=2, label="Mz (Magnetization Reversal)")
    ax1.set_xlim(0, 5)
    ax1.set_ylim(-1.1, 1.1)
    ax1.set_title("Modeled LLG Switching Dynamics (Magnetoelectric Strain)", color="white")
    ax1.set_ylabel("Normalized Mz", color="white")
    ax1.set_xlabel("Time (ns)", color="white")
    ax1.legend(loc="lower right", facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
    
    line2, = ax2.plot([], [], color="#ff00ff", lw=2, label="|Z| Impedance (Ohm)")
    ax2.set_xlim(1, 10)
    ax2.set_ylim(0, np.max(Z_mag) * 1.1)
    ax2.set_title("BVD Equivalent Circuit (AlN Transducer Resonance)", color="white")
    ax2.set_ylabel("Magnitude |Z|", color="white")
    ax2.set_xlabel("Frequency (GHz)", color="white")
    ax2.legend(loc="upper right", facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
    
    line3, = ax3.plot([], [], color="#ffd700", lw=2, label="Signal Amplitude A(x)")
    ax3.set_xlim(1, 16)
    ax3.set_ylim(0, 1.1)
    ax3.set_title("Acoustic Attenuation across Memory Layers (A(x) = A_0 e^{-\\alpha x})", color="white")
    ax3.set_ylabel("Relative Amplitude", color="white")
    ax3.set_xlabel("Stack Layer (x)", color="white")
    ax3.legend(loc="upper right", facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
    
    # --- Animation Function ---
    def update(frame):
        # Progressive drawing process
        line1.set_data(t_llg[:frame], mz[:frame])
        line2.set_data(freq[:frame] / 1e9, Z_mag[:frame])
        line3.set_data(layers[:frame], amplitude[:frame])
        return line1, line2, line3
        
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    
    # --- Export Logic ---
    print("Initiating progressive animation export (High-Res MP4)...")
    writer = animation.FFMpegWriter(fps=30, bitrate=3000)
    try:
        ani.save("PCME_RAM_Simulation_V1.mp4", writer=writer)
        print("Success: Animation saved as 'PCME_RAM_Simulation_V1.mp4'")
    except Exception as e:
        print(f"FFmpeg failed or is not installed: {e}")
        print("Failing over silently to PillowWriter (GIF)...")
        try:
            writer_gif = animation.PillowWriter(fps=30)
            ani.save("PCME_RAM_Simulation_V1.gif", writer=writer_gif)
            print("Success: Fallback animation saved as 'PCME_RAM_Simulation_V1.gif'")
        except Exception as e2:
            print(f"Pillow export also failed: {e2}")
            
    plt.close(fig)

if __name__ == "__main__":
    print("Initializing Open Origin Architecture Framework...")
    try:
        run_simulation()
    except KeyboardInterrupt:
        print("\nProcess aborted by user (KeyboardInterrupt).")
    except Exception as e:
        print(f"\nCritical Runtime Error encountered:")
        traceback.print_exc()
    finally:
        input("\nExecution completed. Press Enter to close the console window...")