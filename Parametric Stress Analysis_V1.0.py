import numpy as np

import matplotlib.pyplot as plt



# 1. Configurações Iniciais

P = 800          # Carga em Newtons

L = 0.04         # Lado em metros (40mm)

A0 = L * L       # Área em m2

sigma_ref = (P / A0) / 1000  # Convertendo para kPa (500 kPa)



# 2. Definição do domínio (Theta de 0 a 180 graus para ciclo completo)

theta_deg = np.linspace(0, 180, 500)

theta_rad = np.radians(theta_deg)



# 3. Cálculo das Tensões

sigma = sigma_ref * (np.sin(theta_rad)**2)

tau = sigma_ref * np.sin(theta_rad) * np.cos(theta_rad)



def format_plot(title, ylabel):

    plt.title(title, fontsize=12, fontweight='bold')

    plt.xlabel('Ângulo Theta (graus)', fontsize=10)

    plt.ylabel(ylabel, fontsize=10)

    plt.grid(True, linestyle='--', alpha=0.6)

    plt.xlim(0, 180)



# 4. Geração do Gráfico de Tensão Normal com anotação do pico

plt.figure(figsize=(8, 5))

plt.plot(theta_deg, sigma, color='blue', linewidth=2, label=r'$\sigma$ (Normal)')

format_plot('Tensão Normal Média vs. Theta', 'Tensão (kPa)')

plt.annotate(f'Máximo: {sigma_ref:.0f} kPa (90°)', xy=(90, sigma_ref), xytext=(110, sigma_ref-50),

             arrowprops=dict(facecolor='black', shrink=0.05, width=1))

plt.legend()

plt.tight_layout()

plt.savefig('tensao_normal.png', dpi=300)

plt.show()



# 5. Geração do Gráfico de Tensão de Cisalhamento com anotação dos picos

plt.figure(figsize=(8, 5))

plt.plot(theta_deg, tau, color='red', linewidth=2, label=r'$\tau$ (Cisalhamento)')

format_plot('Tensão de Cisalhamento Média vs. Theta', 'Tensão (kPa)')

plt.axhline(0, color='black', linewidth=1)



# Destaque dos picos de cisalhamento (45° e 135°)

tau_max = sigma_ref / 2

plt.annotate(f'Máx: {tau_max:.1f} kPa (45°)', xy=(45, tau_max), xytext=(10, tau_max+20),

             arrowprops=dict(facecolor='black', shrink=0.05, width=1))

plt.annotate(f'Mín: {-tau_max:.1f} kPa (135°)', xy=(135, -tau_max), xytext=(145, -tau_max-20),

             arrowprops=dict(facecolor='black', shrink=0.05, width=1))



plt.legend()

plt.tight_layout()

plt.savefig('tensao_cisalhamento.png', dpi=300)

plt.show()



print("Relatório: Gráficos gerados e salvos como 'tensao_normal.png' e 'tensao_cisalhamento.png'")
