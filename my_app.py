from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear() # отвечает за отображение окна
    self.initUI() # отвечает за виджеты и их расположение
    self.connects() # отвечает за обработку событий
    self.show() # делает окно видимым
  
  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
  
  def initUI(self):
    self.btn_next = QPushButton(txt_next, self)
    self.hello_text = QLabel(txt_hello)
    self.instructions = QLabel(txt_instruction)

    self.line = QVBoxLayout()
    self.line.addWidget(self.hello_text, alignment=Qt.AlignLeft)
    self.line.addWidget(self.instructions, alignment=Qt.AlignLeft)
    self.line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

    self.setLayout(self.line)

  def next_click(self):
    self.hide()
    self.tw = TestWin()

  def connects(self):
    self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
nw = MainWin()
app.exec_()