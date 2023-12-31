import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建一个新的窗口
root = tk.Tk()

# 定义变量
name = "Collapser"
year = 2023
total_posts = 666
calculate = round(total_posts / (20+total_posts) * 100, 2)
public_posts = 555
private_posts = 111
goods = 100
if (total_posts - public_posts) / total_posts < 0.5:
    comment = "坦坦荡荡是好文明！"
else:
    comment = "常设小圈是好文明！"
if goods > 50:
    comment1 = "可真是位社交达人！"
else:
    comment1 = "还需努力啊！"
date = "2023.1.10"
pyqnum = 10
if pyqnum > 5:
    comment2 = "像一枚自激辐射的高能粒子！"
else:
    comment2 = "一定记忆深刻吧！"



# 使用字符串格式化将变量插入到字符串中
images = [
    f'微信用户{name}\n这是您的\n{year}\n年度报告\n请注意查收哦',
    f'今年您总共发布了\n{total_posts}\n条朋友圈\n打败了{calculate}%的用户！！\n（上面是瞎算的）',
    f'其中，公开朋友圈数量为\n{public_posts}\n部分朋友可见朋友圈数量为\n{private_posts}\n{comment}',
    f'您今年最多得到了\n{goods}\n位朋友的点赞\n{comment1}\n',
    f'在{date}这特殊一天内\n您总共发布了\n{pyqnum}\n条朋友圈！\n{comment2}',
    f'\n感谢您的观看！\n祝您新年快乐！\n（本报告由Collapser制作）\n'
]
current_image = 0

# 创建一个新的图形
fig = Figure(figsize=(5, 7), facecolor='yellow')

# 添加一个子图
ax = fig.add_subplot(111)

# 添加文本
texts = []
for i in range(5):
    x = 0.35 + random.uniform(-0.07, 0.07)
    y = 0.9 - i*0.2 + random.uniform(-0.07, 0.07)
    text = ax.text(x, y, images[current_image].split('\n')[i], horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=20, rotation=20)
    if random.random() < 0.5:
        text.set_fontsize(24)
    # 如果文本是数字，则增大为32号字体
    if images[current_image].split('\n')[i].isdigit():
        text.set_fontsize(36)
    texts.append(text)

# 去除坐标轴
ax.axis('off')

# 创建一个画布
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# 将画布添加到窗口
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 创建一个按钮
next_button = tk.Button(master=root, text='下一页', command=lambda: change_text(texts, 1))

# 将按钮添加到窗口
next_button.pack(side=tk.LEFT, expand=True)

# 创建一个按钮
prev_button = tk.Button(master=root, text='上一页', command=lambda: change_text(texts, -1))

# 将按钮添加到窗口
prev_button.pack(side=tk.LEFT, expand=True)

def change_text(texts, direction):
    global current_image
    # 改变图像
    if current_image + direction < len(images) and current_image + direction >= 0:
        current_image += direction
    for i in range(5):
        x = 0.35 + random.uniform(-0.07, 0.07)
        y = 0.9 - i*0.2 + random.uniform(-0.07, 0.07)
        text = images[current_image].split('\n')[i]
        texts[i].set_text(text)
        texts[i].set_position((x, y))
        # 50%的概率增大一号字体
        if random.random() < 0.5:
            texts[i].set_fontsize(24)
        else:
            texts[i].set_fontsize(20)
        # 如果文本是数字，则增大为36号字体
        if text.isdigit():
            texts[i].set_fontsize(36)
    # 更改背景颜色
    fig.set_facecolor(random_color())
    # 重新绘制图形
    canvas.draw()

def random_color():
    # 生成一个带有透明度的随机颜色
    return "#{:06x}".format(random.randint(0, 0xFFFFFF)) + "80"  # 80表示透明度为50%

# 运行窗口
tk.mainloop()