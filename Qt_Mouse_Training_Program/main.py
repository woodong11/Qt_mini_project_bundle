#   .\venv\Scripts\pyside6-uic.exe .\mainUI.ui -o .\mainUI.py

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from random import randint
from mainUI import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Ui를 Ui_MainWindow에서 갖고온다.
        self.setupUi(self)
        self.main()
    def main(self):
        pass

    lbl_x, lbl_y, num, count = 0, 0, 0, 0
    def colorChanged(self):
        # QColorDialog 창을 표시, 선택한 색상의 이름 값을 가져온다.
        color = QColorDialog.getColor().name()
        if color:
            self.frame.setStyleSheet("background-color:%s" % color)

    def run(self):
        self.num += 1
        lbl_x = randint(0, self.frame.width() - self.lbl.width())
        lbl_Y = randint(0, self.frame.height() - self.lbl.height())
        self.lbl.move(lbl_x, lbl_Y)

        if self.num > 10:
            # timer 종료
            self.timer.stop()
            self.submit_msg = QMessageBox()
            self.submit_msg.setText("10초 동안 클릭 수: {}".format(self.count))
            self.submit_msg.exec()
            print("game end")
            self.count, self.num = 0, 0


    def start(self):
        print("game start!")
        self.timer = QTimer()
        # timer 시작, 500ms 에 한번 timerEvent() 호출
        self.timer.timeout.connect(self.run)
        self.timer.start(700)

    def mousePressEvent(self, event):
        #마우스의 좌표 정보를 담고 있는 event.x(), event.y()
        x = event.x()
        y = event.y()
        #print(x, y)
        if ((self.num > 0) and (self.lbl_x <= x) and (x <= self.lbl_x + self.frame.width())) and ((self.lbl_y <= y) and (y <= self.lbl_y + self.frame.height())):
            print("hit!")
            self.count += 1

    def nameChanged(self):
        ret, ok = QInputDialog.getText(self, "변경할 레이블 이름 입력", "변경할 이름 입력하기")
        if ok:
            self.lbl.setText(ret)

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
