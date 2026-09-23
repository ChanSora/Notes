import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ========== 设置中文字体（兼容 Mac） ==========
# 尝试多个常见中文字体
font_candidates = ['PingFang SC', 'Heiti SC', 'STHeiti', 'Songti SC', 'Arial Unicode MS']
font_name = None
for font in font_candidates:
    try:
        # 检查字体是否存在
        if any(f.name == font for f in fm.fontManager.ttflist):
            font_name = font
            break
    except:
        continue
if font_name is None:
    # 如果都没找到，则使用默认英文
    font_name = 'sans-serif'
    print("警告：未找到中文字体，将使用英文标签")
    use_english = True
else:
    use_english = False

plt.rcParams['font.sans-serif'] = [font_name]
plt.rcParams['axes.unicode_minus'] = False
# =============================================

# ========== 实验数据（磁场分布，f=2kHz, I=20.0mA）==========
x_cm = np.arange(0, 22, 1)  # 0,1,...,21 cm
U_mV = np.array([334.4, 334.3, 334.4, 334.4, 334.5, 334.6, 334.6, 334.5, 334.3, 333.5,
                 332.7, 332.1, 327.7, 321.5, 307.6, 271.4, 211.0, 147.1, 90.8, 37.0, 13.5, 11.0])

# 螺线管参数
L_mm = 360.30
R_mm = 15.02
N = 2330
I_A = 0.020          # 20.0 mA
mu0 = 4 * np.pi * 1e-7

L = L_mm / 1000
R = R_mm / 1000

# 理论公式
def B_theory(x_m):
    halfL = L / 2
    term1 = (x_m + halfL) / np.sqrt((x_m + halfL)**2 + R**2)
    term2 = (x_m - halfL) / np.sqrt((x_m - halfL)**2 + R**2)
    return (mu0 * N * I_A) / (2 * L) * (term1 - term2)

x_m = x_cm / 100
B_theo = np.array([B_theory(x) for x in x_m])
U0 = U_mV[0]
B0 = B_theo[0]
k = U0 / B0
B_theo_scaled = B_theo * k

# ========== 绘图 ==========
plt.figure(figsize=(9, 6))
plt.plot(x_cm, U_mV, 'o-', color='blue', linewidth=2, markersize=6, label='实验测量电压 (mV)')
plt.plot(x_cm, B_theo_scaled, 's--', color='red', linewidth=2, markersize=4, label='理论磁场归一化曲线')
plt.xlabel('离中心点距离 x (cm)', fontsize=12)
plt.ylabel('磁感应强度相对值 (mV)', fontsize=12)
plt.title('螺线管轴线磁场分布 (f=2kHz, I=20.0mA)', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axvline(x=18.015, color='gray', linestyle=':', label='螺线管端点 (x = 18.0 cm)')
plt.annotate('端点', xy=(18.015, 200), xytext=(19, 250),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
plt.tight_layout()
plt.savefig('solenoid_B_distribution.png', dpi=300)
plt.show()