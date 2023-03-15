from PyQt5 import QtWidgets , QtCore , uic , QtGui
from config.config import Read
from qt_material import apply_stylesheet
from main import startWork
import sys , json

class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.config = Read.read_config()
        self.m_flag = False
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        self.init_ui()
        self.clicked_Base()

    def init_ui(self):
        self.ui = uic.loadUi("ui/Qtui.ui" , self)
        self.setWindowIcon(QtGui.QIcon('ui/icon.ico'))
        self.set_close_button()
        self.show()

        self.init_right()
        self.ui.Right_Layout.addWidget(self.right_widget_difficulty)
        self.ui.Right_Layout.addWidget(self.right_widget_base)

        self.ui.DifficultyButton.clicked.connect(self.clicked_difficulty)
        self.ui.BaseButton.clicked.connect(self.clicked_Base)
        self.ui.ColorButton.clicked.connect(self.clicked_Color)
        self.ui.StartButton.clicked.connect(startWork)
    
    def set_close_button(self):
        self.ui.CloseButton.setFixedSize(15 ,15) # 设置关闭按钮的大小
        self.ui.MaxButton.setFixedSize(15 , 15) # 设置按钮大小
        self.ui.MinButton.setFixedSize(15 , 15) # 设置最小化按钮大小
        self.ui.CloseButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.ui.MaxButton.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.ui.MinButton.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.ui.CloseButton.clicked.connect(self.close)
        self.ui.MinButton.clicked.connect(self.showMinimized)
        self.ui.MaxButton.clicked.connect(self.slot_max_or_recv)

    def slot_max_or_recv(self): #最大化最小化
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def init_right_difficulty(self):
        difficulty = self.config['difficulty']
        self.right_widget_difficulty = QtWidgets.QWidget()
        self.right_layout_difficulty = QtWidgets.QVBoxLayout()
        self.right_widget_difficulty.setLayout(self.right_layout_difficulty)

        self.right_layout_difficulty.addStretch(2) #增加空行

        self.right_difficulty_Label = QtWidgets.QLabel("难度设置")
        self.right_difficulty_Label.setFont(QtGui.QFont('得意黑' , 20 , QtGui.QFont.Black)) #设置字体颜色大小
        self.right_difficulty_Label.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding , QtWidgets.QSizePolicy.Fixed)
        self.right_difficulty_Label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) #居中
        self.right_layout_difficulty.addWidget(self.right_difficulty_Label)

        self.right_difficulty_inputs = []
        pos = 1
        self.right_layout_difficulty.addStretch(2) #增加空行
        for qwq in difficulty:
            right_difficulty_input = QtWidgets.QHBoxLayout()
            right_difficulty_input_text = QtWidgets.QLabel()
            right_difficulty_input_text.setText(f'第 {pos} 个难度')
            # right_difficulty_input_text.setFont(QtGui.QFont('得意黑' , 10 , QtGui.QFont.Black))
            right_difficulty_input.addWidget(right_difficulty_input_text)

            right_difficulty_input_box = QtWidgets.QLineEdit(self)
            right_difficulty_input_box.setText(qwq)
            right_difficulty_input_box.editingFinished.connect(self.update_config) #更新设置
            # print(type(QtWidgets.QLineEdit()) == type(right_difficulty_input_box))
            right_difficulty_input.addWidget(right_difficulty_input_box)
            # right_difficulty_input_box.setFont(QtGui.QFont('得意黑' , 10 , QtGui.QFont.Black))
            self.right_layout_difficulty.addLayout(right_difficulty_input)
            self.right_difficulty_inputs.append(right_difficulty_input)
            self.right_layout_difficulty.addStretch(1) #增加空行
            pos += 1

    def init_right_base(self):

        def init_base_fig_input(textstr , qaq , l = 114514 , r = 1919810):
            tmp_input = QtWidgets.QHBoxLayout()
            tmp_input.addStretch(1)
            tmp_input_lable = QtWidgets.QLabel()
            tmp_input_lable.setText(textstr)
            tmp_input_lable.setFont(QtGui.QFont('得意黑' , 13 , QtGui.QFont.Black)) #设置字体颜色大小
            tmp_input_lable.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) #居中
            tmp_input_box = QtWidgets.QDoubleSpinBox(self)
            tmp_input_box.setValue(qaq)
            tmp_input_box.setMaximum(l)
            tmp_input_box.setMinimum(r)
            tmp_input.addWidget(tmp_input_lable)
            tmp_input.addStretch(1)
            tmp_input.addWidget(tmp_input_box)
            tmp_input.addStretch(1)
            return tmp_input
        
        def init_png_size_input():
            tmp = QtWidgets.QVBoxLayout()
            tmp_label = QtWidgets.QLabel()
            tmp_label.setText("图片大小：")
            tmp_label.setFont(QtGui.QFont('得意黑' , 20 , QtGui.QFont.Black)) #设置字体颜色大小
            tmp_label.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding , QtWidgets.QSizePolicy.Fixed)
            tmp_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) #居中
            tmp.addStretch(5)
            tmp.addWidget(tmp_label)
            tmp.addStretch(1)
            tmp.addLayout(init_base_fig_input("图片长：" , self.config["fig_size"]["row"] , 1 , 20))
            tmp.addLayout(init_base_fig_input("图片宽：" , self.config["fig_size"]["column"] , 0.1 , 10))
            tmp.addLayout(init_base_fig_input("图片圆角：" , self.config["png_radii"] , 0 , 50))
            tmp.addStretch(5)
            return tmp

        def init_luogu_id():
            tmp = QtWidgets.QVBoxLayout()
            tmp_label = QtWidgets.QLabel()
            tmp_label.setText("你的洛谷 id :")
            tmp_label.setFont(QtGui.QFont('得意黑' , 15 , QtGui.QFont.Black))
            tmp_label.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding , QtWidgets.QSizePolicy.Fixed)
            tmp_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) #居中
            tmp_input = QtWidgets.QLineEdit(self)
            tmp_input.setText(self.config["Your_luogu_id"])
            tmp_input.editingFinished.connect(self.update_config)
            # tmp_input.setSizePolicy(QtWidgets.QSizePolicy.Fixed , QtWidgets.QSizePolicy.Fixed)
            tmp.addWidget(tmp_label)
            tmp.addWidget(tmp_input)
            return tmp

        self.right_widget_base = QtWidgets.QWidget()
        self.right_layout_base = QtWidgets.QVBoxLayout()
        self.right_widget_base.setLayout(self.right_layout_base)
        self.right_layout_base.addStretch(2) #增加空行
    
        self.right_layout_base.addLayout(init_png_size_input())
        self.right_layout_base.addStretch(1) #增加空行
        self.right_layout_base.addLayout(init_luogu_id())

        self.right_layout_base.addStretch(2) #增加空行

    def init_right_color(self):
        pass

    def clicked_difficulty(self): #按下difficulty调用的函数
        self.right_widget_difficulty.show()
        self.right_widget_base.hide()

    def clicked_Base(self): #按下base调用的函数
        self.right_widget_difficulty.hide()
        self.right_widget_base.show()

    def clicked_Color(self): #按下color调用的函数
        self.right_widget_difficulty.hide()
        self.right_widget_base.hide()
        pass

    def init_right(self): #顾名思义
        self.init_right_difficulty()
        self.init_right_base()
        self.init_right_color()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_Position = event.globalPos() - self.pos() #获取鼠标相对窗口的位置
            if self.m_Position.y() > 50:
                self.m_flag = False
            else:
                self.m_flag = True
                # print(self.m_Position.y())
                event.accept()
                self.setCursor(QtCore.Qt.OpenHandCursor)  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos() - self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self , QMouseEvent):
        self.m_flag = False
        self.setCursor(QtCore.Qt.ArrowCursor)

    def update_config(self):
        difficulty = []
        for i in self.right_difficulty_inputs:
            item = i.itemAt(1)
            difficulty.append(item.widget().text())
        self.config["difficulty"] = difficulty
        with open("config/config.json" , "w" , encoding = "utf-8") as f:
            json.dump(self.config , sort_keys = True , indent = 4 , separators = (',' , ': ') , fp = f)

app = QtWidgets.QApplication(sys.argv)
apply_stylesheet(app , theme = 'light_blue.xml')
myapp = Window()
sys.exit(app.exec_())
