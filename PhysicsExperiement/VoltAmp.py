import numpy as np
import matplotlib.pyplot as plt

# ========== 设置中文字体（兼容 Mac） ==========
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'STHeiti', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# ========== 1. 小灯泡数据（外接法 vs 内接法） ==========
# 外接法：U(V), I(mA)
U_bulb_ext = np.array([0.319, 0.725, 1.147, 1.579, 1.982, 2.446, 2.893, 3.342, 3.812, 4.254, 4.710, 5.166, 5.627, 6.081])
I_bulb_ext = np.array([18, 26, 34, 40, 46, 51, 56, 60, 66, 70, 74, 78, 82, 86])

# 内接法：U(V), I(mA)
U_bulb_int = np.array([0.490, 0.981, 1.473, 1.969, 2.465, 2.957, 3.454, 3.946, 4.450, 4.942, 5.435, 5.927, 6.407, 6.848])
I_bulb_int = np.array([17, 26, 34, 40, 46, 51, 56, 60, 66, 70, 74, 78, 82, 86])

# ========== 2. LED 数据（绿色 vs 蓝色） ==========
I_LED = np.array([1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50])
U_LED_green = np.array([2.355, 2.440, 2.560, 2.661, 2.740, 2.816, 2.960, 3.067, 3.151, 3.222, 3.284, 3.335, 3.385, 3.425])
U_LED_blue = np.array([2.808, 2.882, 2.990, 3.066, 3.134, 3.181, 3.300, 3.379, 3.459, 3.537, 3.618, 3.715, 3.790, 3.834])

# ========== 3. 稳压二极管数据（正向 vs 反向） ==========
I_zener_fwd = np.array([1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50])
U_zener_fwd = np.array([0.719, 0.742, 0.768, 0.782, 0.790, 0.798, 0.810, 0.817, 0.823, 0.827, 0.830, 0.833, 0.835, 0.836])

I_zener_rev = np.array([1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50])
U_zener_rev = np.array([2.620, 2.642, 3.078, 3.221, 3.339, 3.422, 3.582, 3.690, 3.768, 3.831, 3.883, 3.921, 3.955, 3.986])

# ========== 绘图 ==========
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 图1：小灯泡伏安特性（内接法 vs 外接法）
ax1 = axes[0, 0]
ax1.plot(U_bulb_ext, I_bulb_ext, 'o-', color='blue', linewidth=2, markersize=6, label='外接法')
ax1.plot(U_bulb_int, I_bulb_int, 's-', color='red', linewidth=2, markersize=6, label='内接法')
ax1.set_xlabel('电压 $U$ (V)', fontsize=12)
ax1.set_ylabel('电流 $I$ (mA)', fontsize=12)
ax1.set_title('钨丝小灯泡伏安特性曲线', fontsize=14)
ax1.legend(fontsize=11)
ax1.grid(True, linestyle='--', alpha=0.6)

# 图2：LED 伏安特性（绿色 vs 蓝色）
ax2 = axes[0, 1]
ax2.plot(U_LED_green, I_LED, 'o-', color='green', linewidth=2, markersize=6, label='绿色 LED')
ax2.plot(U_LED_blue, I_LED, 's-', color='blue', linewidth=2, markersize=6, label='蓝色 LED')
ax2.set_xlabel('电压 $U$ (V)', fontsize=12)
ax2.set_ylabel('电流 $I$ (mA)', fontsize=12)
ax2.set_title('LED 正向伏安特性曲线', fontsize=14)
ax2.legend(fontsize=11)
ax2.grid(True, linestyle='--', alpha=0.6)

# 图3：稳压二极管正向伏安特性
ax3 = axes[1, 0]
ax3.plot(U_zener_fwd, I_zener_fwd, 'o-', color='purple', linewidth=2, markersize=6)
ax3.set_xlabel('电压 $U$ (V)', fontsize=12)
ax3.set_ylabel('电流 $I$ (mA)', fontsize=12)
ax3.set_title('稳压二极管正向伏安特性曲线', fontsize=14)
ax3.grid(True, linestyle='--', alpha=0.6)

# 图4：稳压二极管反向伏安特性
ax4 = axes[1, 1]
ax4.plot(U_zener_rev, I_zener_rev, 'o-', color='orange', linewidth=2, markersize=6)
ax4.set_xlabel('电压 $U$ (V)', fontsize=12)
ax4.set_ylabel('电流 $I$ (mA)', fontsize=12)
ax4.set_title('稳压二极管反向伏安特性曲线', fontsize=14)
ax4.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('伏安特性曲线.png', dpi=300)
plt.show()