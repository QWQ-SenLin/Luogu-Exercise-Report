
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import os

def Get_RGB(x):
    return (x[0] / 255 , x[1] / 255 , x[2] / 255)

def init_var(ty_data):
    global x_data , y_data , colors , fig
    plt.rcParams["font.sans-serif"] = ['SimHei']
    plt.rcParams["axes.unicode_minus"] = False
    x_data = [
        ' ' ,
        '暂无评定' , '入门' , '普及-' ,
        '普及/提高-' , '普及+/提高' , '提高+/省选-' ,
        '省选/NOI-' , 'NOI/NOI+/CTSC'
    ]
    # y_data = [0 , 1 , 206 , 197 , 156 , 79 , 24 , 6 , 0]
    y_data = [0] + ty_data
    colors = [
        (10 , 10 , 10) ,
        (191, 191, 191) , (254 , 76 , 97) ,
        (243, 156, 17) , (255, 193, 22) , 
        (82, 196, 26) , (52, 152, 219) , 
        (157, 61, 207) , (14 , 29 , 105)
    ]
    fig = plt.figure(figsize = (8.2 , 4))
    fig.patch.set_facecolor(Get_RGB((10 , 10 , 10)))
    fig.patch.set_alpha(1.0)

def set_fig(ty_data):
    global qwq , datas , fig_len
    qwq = plt.axes()
    qwq.set_facecolor("black")
    fig_len = int((max(ty_data) + 5) * 1.05)
    qwq.set(xlim = (0 , fig_len), ylim = (0 , 9))
    qwq.patch.set_alpha(0.0)
    for tmp in ['top' , 'bottom' , 'left' , 'right']:
        qwq.spines[tmp].set_visible(False) #去掉边框
    
    datas = qwq.barh(x_data , y_data , 0.5 , color = [Get_RGB(colors[i]) for i in range(len(colors))])

    qwq.tick_params(
        axis = 'x',
        labelsize = 9, # 轴字体大小设置
        color = 'white',    # 轴标签颜色设置  
        labelcolor = 'white', # 轴字体颜色设置
        direction = 'in' , # 轴标签方向设置
        # family = 'smiley-sans'
    ) 
    qwq.tick_params(axis = 'y' , color = Get_RGB((10 , 10 , 10))) 

    y_labels = qwq.get_yticklabels()
    for i in range(len(y_labels)):
        y_labels[i].set_color(Get_RGB(colors[i]))
    
    qwq.axhline(linewidth = 2 , color = Get_RGB((250 , 250 , 250))) #改线
    qwq.axvline(linewidth = 4 , color = Get_RGB((250 , 250 , 250)))

def set_text(name):
    plt.title(
        f"{name} 的练习情况" ,
        color = 'white' , font = {'size' : 18} , loc = 'left'
    )

    plt.text(
        x = 180 ,#文本x轴坐标 
        y = 9 , #文本y轴坐标
        s = f'总 AC 数: {sum(y_data)}' , #文本内容
        ha = 'left' , #x=2.2是文字的左端位置，可选'center', 'right', 'left'
        va = 'baseline' , #y=8是文字的低端位置，可选'center', 'top', 'bottom', 'baseline', 'center_baseline'
        fontdict = dict(
            fontsize = 12 , color = 'white' ,
            weight = 'bold' , #磅值，可选'light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'     
            # family = 'smileay-sans'
        )#字体属性设置
    )
    
    show_data()

def show_data(): 
    tmp = get_sum_len()
    for i in range(1 , len(datas)):
        plt.text(
            datas[i].get_x() + datas[i].get_width() + tmp / 35 ,
            datas[i].get_y() ,
            f'{datas[i].get_width()}' ,
            size = 13 ,
            color = 'white'
        )

def get_sum_len():
    tmp = 0
    tmp2 = 0
    for i in range(1 , len(y_data)):
        if y_data[i] > tmp:
            tmp = y_data[i]
            tmp2 = i
    tmp = datas[tmp2].get_x() + datas[tmp2].get_width() # 总长
    return tmp

def rounded(ty_data):
    tmp = get_sum_len()
    for i in range(1 , len(datas)):
        x = datas[i].get_x() + datas[i].get_width()
        y = datas[i].get_y() + (datas[i].get_height() / 1.5) - 0.08
        c =  Ellipse(xy = (x , y), width = tmp / 40 , height = (datas[i].get_height() - 0.05) , color = Get_RGB(colors[i])) # 圆
        qwq.add_patch(c)

def show_fig(ty_data , name):
    init_var(ty_data)
    set_fig(ty_data)
    rounded(ty_data)
    set_text(name)
    path = f'{os.getcwd()}/{name}.png'
    plt.savefig(path)
    # plt.show()
    print(f'已保存在目录 {path}')
    return path

# if __name__ == '__main__':
#     show_fig([1 , 206 , 197 , 156 , 79 , 24 , 6 , 0] , 'QWQ_SenLin')