from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from mainUI import Ui_MainWindow
import cv2
import numpy as np
from time import sleep
from picamera2 import Picamera2

class MyThread(QThread):
    mySignal = Signal(QPixmap, QPixmap)

    def __init__(self):
        super().__init__()
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (480, 320)}))
        self.picam2.start()
        self.videoNum = 0

    def run(self):
        while True:
            imgBGR = self.picam2.capture_array()
            self.processImage(imgBGR)
            sleep(0.1)

    def stop(self):
        self.flag = False

    def processImage(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        grayImg = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte*w, QImage.Format_RGB888)
        q_img1 = QPixmap(img)

        if self.videoNum == 0:
            print('Canny Edge Detection')
            changeImg = cv2.Canny(grayImg, 50, 200)
        elif self.videoNum == 1:
            print('Blur')
            changeImg = cv2.blur(grayImg, (55, 55))
        elif self.videoNum == 2:
            print('Morphological Gradient')
            kernel = np.ones((3, 3), np.uint8)
            changeImg = cv2.morphologyEx(grayImg, cv2.MORPH_GRADIENT, kernel)
        elif self.videoNum == 3:
            print('Thresholding')
            _, changeImg = cv2.threshold(grayImg, 120, 255, cv2.THRESH_BINARY)
        elif self.videoNum == 4:
            print('Grayscale')
            changeImg = grayImg

        imgRGB = cv2.cvtColor(changeImg, cv2.COLOR_GRAY2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        q_img2 = QPixmap(img)


        self.mySignal.emit(q_img1, q_img2)

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()
        self.play_on = False

    def main(self):
        self.th = MyThread()
        self.th.mySignal.connect(self.setImage)

    def setImage(self, img, img2):
        self.cam_lbl.setPixmap(img)
        self.openCV_lbl.setPixmap(img2)

    def play(self):
        print('Play')
        self.th.start()

    def mode(self):
        print('Mode Change')
        self.th.videoNum = (self.th.videoNum + 1) % 5

    def closeEvent(self, event):
        self.th.stop()
        self.th.wait(3000)
        self.close()

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
