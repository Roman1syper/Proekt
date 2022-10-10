# напиши здесь код третьего экрана приложения
from operator import index
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

class FinalWin(QWidget):
  def __init__(self, exp):
    super().__init__()
    self.exp = exp
    self.set_appear() # отвечает за отображение окна
    self.initUI() # отвечает за виджеты и их расположение
    self.show() # делает окно видимым

  def results(self):
    self.exp.age = int(self.exp.age)
    self.exp.t1 = float(self.exp.t1)
    self.exp.t2 = float(self.exp.t2)
    self.exp.t3 = float(self.exp.t3)
    if self.exp.age < 7:
      self.index = 0
      return 'нет данных такого возраста'
    self.index = (4 * (self.exp.t1 + self.exp.t2 + self.exp.t3) - 200) / 10
    if self.exp.age == 7 or self.exp.age == 8:
      if self.index >= 21:
        return txt_res1
      if self.index >= 17 and self.index <= 20.9:
        return txt_res2
      if self.index >= 12 and self.index <= 16.9:
        return txt_res3
      if self.index >= 6.5 and self.index <= 11.9:
        return txt_res4
      if self.index <= 6.4:
        return txt_res5
    if self.exp.age == 9 or self.exp.age == 10:
      if self.index >= 19.5:
        return txt_res1
      if self.index >= 15.5 and self.index <= 19.4:
        return txt_res2
      if self.index >= 10.5 and self.index <= 15.4:
        return txt_res3
      if self.index >= 5 and self.index <= 10.4:
        return txt_res4
      if self.index <= 4.9:
        return txt_res5
    if self.exp.age == 11 or self.exp.age == 12:
      if self.index >= 18:
        return txt_res1
      if self.index >= 14 and self.index <= 17.9:
        return txt_res2
      if self.index >= 9 and self.index <= 13.9:
        return txt_res3
      if self.index >= 3.5 and self.index <= 8.9:
        return txt_res4
      if self.index <= 3.4:
        return txt_res5
    if self.exp.age == 13 or self.exp.age == 14:
      if self.index >= 16.5:
        return txt_res1
      if self.index >= 12.5 and self.index <= 16.4:
        return txt_res2
      if self.index >= 7.5 and self.index <= 12.4:
        return txt_res3
      if self.index >= 2 and self.index <= 7.4:
        return txt_res4
      if self.index <= 1.9:
        return txt_res5
    if self.exp.age >= 15:
      if self.index >= 15:
        return txt_res1
      if self.index >= 11 and self.index <= 14.9:
        return txt_res2
      if self.index >= 6 and self.index <= 10.9:
        return txt_res3
      if self.index >= 0.5 and self.index <= 5.9:
        return txt_res4
      if self.index <= 0.4:
        return txt_res5
    # дописать метод
  
  def initUI(self):
    self.work_text = QLabel(txt_workheart + self.results())
    self.index_text = QLabel(txt_index + str(self.index))

    self.layout_line = QVBoxLayout()
    self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
    self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
    self.setLayout(self.layout_line)
  
  def set_appear(self):
    self.setWindowTitle(txt_finalwin)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)