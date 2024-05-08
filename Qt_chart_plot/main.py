from PySide6.QtWidgets import *
from mainUI import Ui_MainWindow
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import random
import numpy as np

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.figure = pyplot.Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.lay.addWidget(self.canvas)

        # 전체 그림의 그리드를 설정하여 가로 폭을 조절합니다.
        gs = self.figure.add_gridspec(1, 3, width_ratios=[2, 2, 2])

        # 각 subplot을 추가합니다.
        self.graph1 = self.figure.add_subplot(gs[0])
        self.graph2 = self.figure.add_subplot(gs[1])
        self.graph3 = self.figure.add_subplot(gs[2])
        # self.figure.subplots(1, 3, gridspec_kw={'width_ratios': [2, 2, 2]})
        print(type(self.figure))
        print(type(self.graph1))

    def chart1(self):
        x = np.array([1, 2, 3, 4, 5])  # x를 numpy array로 변경
        y1 = [random.random() * 100 for _ in range(5)]
        y2 = [random.random() * 100 for _ in range(5)]
        bar_width = 0.4  # 바의 폭

        self.graph1.clear()
        self.graph1.bar(x - bar_width / 2, y1, width=bar_width, label="BBQ")
        self.graph1.bar(x + bar_width / 2, y2, width=bar_width, label="KFC")
        self.graph1.legend(loc="upper left")
        self.canvas.draw()

    def chart2(self):
        x = [1, 2, 3, 4, 5]
        y = [random.random() * 100 for _ in range(5)]
        self.graph2.clear()
        self.graph2.scatter(x, y)
        self.canvas.draw()

    def chart3(self):
        x = [1, 2, 3, 4, 5]
        y = [random.random() * 100 for _ in range(5)]
        self.graph3.clear()
        self.graph3.plot(x, y)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
