# Physical and Mathematical Core Models

## 1.1 Elastodynamics and Phonon Transit Time
The propagation of acoustic longitudinal waves in monocrystalline silicon is governed by the elastic wave equation:

$$\rho_{Si}\frac{\partial^2 u_i}{\partial t^2}=c_{ijkl}\frac{\partial^2 u_k}{\partial x_j\partial x_l}$$

The phase velocity is given by $v_{Si}=\sqrt{\frac{c_{11}}{\rho_{Si}}} \approx 8433\,m/s$. The signal transit time through a 16-layer stack with a total thickness of $100\,\mu m$ is calculated as:

$$t_{prop}=\frac{d_{total}}{v_{Si}}\approx11.86\,ps$$

## 1.2 Acoustic Impedance and Transmittance
To validate phonon transmission across layer boundaries, the acoustic impedance $Z = \rho v$ must be matched. The reflection coefficient $R$ and the transmission coefficient $T$ at the interface between silicon ($Z_1$) and the h-BN epoxy coupling matrix ($Z_2$) are defined as:

$$R=\left(\frac{Z_2 - Z_1}{Z_2 + Z_1}\right)^2$$
$$T=1 - R$$

## 1.3 Acoustic Attenuation
The dissipation of signal energy across alternating layer boundaries (silicon and polymer) follows an exponential attenuation law. The amplitude decay $A(x)$ over the distance $x$ is:

$$A(x) = A_0 e^{-\alpha x}$$

Similarly, the acoustic power $P(x)$ decays according to:

$$P(x) = P_0 e^{-2\alpha x}$$

Where $\alpha$ represents the frequency-dependent effective attenuation coefficient of the heterogeneous stack. This model numerically dictates the maximum feasible number of memory layers before the signal loss falls below the thermal noise floor of the FDM channel.

## 1.4 Butterworth-Van-Dyke (BVD) Equivalent Circuit
To simulate the piezoelectric AlN transducer, the BVD equivalent circuit is utilized. It models the resonance via a static capacitance $C_0$ in parallel with a motional branch ($C_m, L_m, R_m$). The frequency-dependent impedance $Z(\omega)$ is given by:

$$Z(\omega) = \frac{1}{j\omega C_0 + \frac{1}{R_m + j\omega L_m + 1/(j\omega C_m)}}$$

## 1.5 Signal Crosstalk
Interference between adjacent acoustic channels is quantified by the crosstalk measure $XT$ in decibels. It compares the induced noise voltage of the victim channel ($V_{victim}$) with the signal voltage of the aggressor channel ($V_{aggressor}$):

$$XT = 20 \log_{10} \left( \frac{V_{victim}}{V_{aggressor}} \right)$$

## 1.6 Magnetization Dynamics (LLG Equation)
Switching time, damping, and relaxation of the memory cell are modeled using the Landau-Lifshitz-Gilbert (LLG) equation:

$$\frac{d\mathbf{M}}{dt}=-\gamma(\mathbf{M} \times \mathbf{H}_{eff}) + \frac{\alpha}{M_s}\left(\mathbf{M} \times \frac{d\mathbf{M}}{dt}\right)$$

## 1.7 Error Propagation and Uncertainty Model
To scientifically evaluate the theoretical projections, the combined standard uncertainty $u_c$ for all derived functions $f$ is determined via:

$$u_c = \sqrt{ \sum_{i} \left( \frac{\partial f}{\partial x_i} u_i \right)^2 }$$

## 1.8 Acoustic Multiplexing Mitigation: Phononic Metamaterials and Impedance Matching
To overcome the critical high-risk challenges of acoustic attenuation (signal loss) and resonance-induced crosstalk, the PCME-RAM architecture implements two advanced wave-engineering techniques derived from optical physics and metamaterial science.

### 1.8.1 Quarter-Wave Acoustic Impedance Transformer
To prevent the exponential attenuation caused by reflection at the Silicon-Polymer boundaries ($Z_1 \to Z_2$), a thin-film matching layer is introduced. Analogous to optical anti-reflective coatings, we utilize a quarter-wave acoustic transformer. The required acoustic impedance $Z_{match}$ of this intermediate layer is calculated as the geometric mean of the two surrounding media:

$$Z_{match} = \sqrt{Z_{Si} Z_{Polymer}}$$

To achieve destructive interference of the reflected waves and perfect transmission ($T \to 1$), the thickness $d_{match}$ of this layer must strictly equal one-quarter of the acoustic wavelength $\lambda$ at the center frequency $f_c$ of the multiplexed signal:

$$d_{match} = \frac{\lambda}{4} = \frac{v_{match}}{4 f_c}$$

By doping a sub-layer of the h-BN epoxy to precisely match $Z_{match}$, the reflection coefficient $R$ is driven to near zero, effectively neutralizing the exponential layer-by-layer signal attenuation.

### 1.8.2 Phononic Bandgap Engineering (Crosstalk Elimination)
To prevent lateral signal leakage (crosstalk) between adjacent Acoustic Through-Silicon Vias (A-TSVs), the silicon substrate surrounding each acoustic pillar is structured into a **Phononic Crystal (PnC)**. By etching a periodic lattice of microscopic air holes (or filling them with a low-density polymer) around the pillars, an acoustic bandgap is created. 

Acoustic waves within this bandgap cannot propagate laterally through the lattice. The lattice constant $a$ (distance between holes) is designed to satisfy the Bragg scattering condition for the transverse leakage waves:

$$a = \frac{v_{transverse}}{2f}$$

Waves attempting to cross into adjacent memory cells fall into this forbidden frequency band and are exponentially dampened out laterally, acting as an absolute acoustic isolator and drastically lowering the $XT$ (Crosstalk) value.
