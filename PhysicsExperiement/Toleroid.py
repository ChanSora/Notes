import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.font_manager as fm

# ========== 自动查找中文字体 ==========
# 获取系统所有字体
font_list = fm.findSystemFonts()
chinese_fonts = []
for font in font_list:
    try:
        prop = fm.FontProperties(fname=font)
        # 检查字体是否包含中文字符（简单方法：判断名称中是否有 'CJK' 或 'SC'）
        if 'CJK' in prop.get_name() or 'SC' in prop.get_name() or 'Heiti' in prop.get_name() or 'Songti' in prop.get_name():
            chinese_fonts.append(prop.get_name())
    except:
        continue

# 备选常见中文字体名称
possible_fonts = ['PingFang SC', 'Heiti SC', 'STHeiti', 'Songti SC', 'Arial Unicode MS', 'Apple LiGothic']
for font in possible_fonts:
    if font in chinese_fonts:
        plt.rcParams['font.sans-serif'] = [font]
        break
else:
    # 如果上面都没找到，使用 findfont 自动匹配第一个可用的中文字体
    try:
        plt.rcParams['font.sans-serif'] = [fm.FontProperties(fname=chinese_fonts[0]).get_name()]
    except:
        # 实在找不到就使用英文
        print("警告：未找到中文字体，将使用英文标签")
        USE_ENGLISH = True
    else:
        USE_ENGLISH = False

plt.rcParams['axes.unicode_minus'] = False
# =====================================

# 数据
I_4k = np.array([10.0, 15.0, 20.0, 25.0, 30.0])
U_4k = np.array([331.9, 500.0, 667.0, 837.5, 1005.3])

I_2k = np.array([10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0])
U_2k = np.array([165.3, 249.8, 334.3, 418.5, 502.3, 586.0, 668.5])

I_1k = np.array([10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0])
U_1k = np.array([83.9, 125.0, 166.8, 209.4, 251.0, 293.0, 335.0])

def linear_fit(x, y):
    slope, intercept, r_value, _, _ = stats.linregress(x, y)
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = slope * x_fit + intercept
    return slope, intercept, r_value**2, x_fit, y_fit

plt.figure(figsize=(8, 6))
colors = ['red', 'blue', 'green']
markers = ['o', 's', '^']
freqs = [4000, 2000, 1000]
data = [(I_4k, U_4k), (I_2k, U_2k), (I_1k, U_1k)]

for (I, U), freq, color, marker in zip(data, freqs, colors, markers):
    slope, intercept, r2, x_fit, y_fit = linear_fit(I, U)
    plt.scatter(I, U, color=color, marker=marker, label=f'{freq} Hz 实测点')
    plt.plot(x_fit, y_fit, color=color, linestyle='-',
             label=f'{freq} Hz 拟合: U = {slope:.2f} I + {intercept:.1f}, R²={r2:.4f}')

# 标签（根据是否找到中文字体决定语言）
if 'USE_ENGLISH' in dir() and USE_ENGLISH:
    plt.xlabel('I (mA)', fontsize=12)
    plt.ylabel('U (mV)', fontsize=12)
    plt.title('Center Field: U vs I', fontsize=14)
else:
    plt.xlabel('励磁电流 I (mA)', fontsize=12)
    plt.ylabel('感应电压 U (mV)', fontsize=12)
    plt.title('螺线管中心磁场感应电压与励磁电流的关系', fontsize=14)

plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('V_I_fitting.png', dpi=300)
plt.show()