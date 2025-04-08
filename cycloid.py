import numpy as np
import matplotlib.pyplot as plt

# 기본 상수 설정
PI = np.pi
t_max = 10 * PI   # t의 최대값, 충분한 주기 확보
dt = 0.01         # t 간격
t = np.arange(0, t_max, dt)

# 1. 사이클로이드 (Cycloid)
# 원의 반지름 설정
r = 1.0
x_cycloid = r * (t - np.sin(t))
y_cycloid = r * (1 - np.cos(t))

# 2. 에피사이클로이드 (Epicycloid)
# 큰 원과 작은 원의 반지름 설정
R_epi = 3.0
r_epi = 1.0
x_epicycloid = (R_epi + r_epi) * np.cos(t) - r_epi * np.cos(((R_epi + r_epi) / r_epi) * t)
y_epicycloid = (R_epi + r_epi) * np.sin(t) - r_epi * np.sin(((R_epi + r_epi) / r_epi) * t)

# 3. 하이포사이클로이드 (Hypocycloid)
# 큰 원과 작은 원의 반지름 설정
R_hypo = 3.0
r_hypo = 1.0
x_hypocycloid = (R_hypo - r_hypo) * np.cos(t) + r_hypo * np.cos(((R_hypo - r_hypo) / r_hypo) * t)
y_hypocycloid = (R_hypo - r_hypo) * np.sin(t) - r_hypo * np.sin(((R_hypo - r_hypo) / r_hypo) * t)

# 3개의 서브플롯으로 나누어 그림
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 사이클로이드 그리기
axs[0].plot(x_cycloid, y_cycloid, color='red')
axs[0].set_title('Cycloid')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].grid(True)
axs[0].axis('equal')

# 에피사이클로이드 그리기
axs[1].plot(x_epicycloid, y_epicycloid, color='green')
axs[1].set_title('Epicycloid')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].grid(True)
axs[1].axis('equal')

# 하이포사이클로이드 그리기
axs[2].plot(x_hypocycloid, y_hypocycloid, color='blue')
axs[2].set_title('Hypocycloid')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].grid(True)
axs[2].axis('equal')

plt.tight_layout()
plt.show()
