from calculations import calculate_ld_ratio
import matplotlib.pyplot as plt
import numpy as np

def plot_ld_vs_aoa(cl_alpha, cd0, k, angulo_inicio = -5, angulo_fin = 20, salto = 1):
    
    angulos_grados = np.arange(angulo_inicio, angulo_fin, salto)
    angulos_radianes = np.radians(angulos_grados)

    cl_values = cl_alpha * angulos_radianes
    cd_values = cd0 + k * (cl_values **2)

    ld_values = calculate_ld_ratio(cl_values, cd_values)

    plt.plot(angulos_grados, ld_values)
    plt.xlabel("Angle of Attack (deg)")
    plt.ylabel("L/D")
    plt.title("L/D vs Angle of Attack")
    plt.show()

