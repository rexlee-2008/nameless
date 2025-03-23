import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

Z1 = 2  # 알파 입자 (헬륨 핵, Z=2)
Z2 = 79  # 금 원자핵 (Z=79)
E = 5e6  # 알파 입자의 에너지 (eV)
e = 1.6e-19  # 기본 전하량 (C)w
k = 8.99e9  # 쿨롱 상수 (N·m²/C²)

def rutherford_scattering(num_particles=10000):
    theta = np.linspace(0.01, np.pi, num_particles)
    probability = (Z1 * Z2 * e**2 / (4 * E))**2 / (np.sin(theta / 2)**4)
    
    theta_samples = np.random.choice(theta, size=num_particles, p=probability / probability.sum())
    
    return theta_samples

theta_samples = rutherford_scattering()

plt.hist(np.degrees(theta_samples), bins=50, density=True, alpha=0.7, color='b')
plt.xlabel("산란각 (도)")
plt.ylabel("확률 밀도")
plt.title("러더퍼드 산란 시뮬레이션")
plt.grid()
plt.show()