
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.name_list = []
        self.main()


    def main(self):
        self.setWindowTitle("하하호호 메모장")
        self.setGeometry(800, 400, 300, 300)

        # 메인 central에 객체 추가
        self.plainTextEdit = QPlainTextEdit(self)
        self.setCentralWidget(self.plainTextEdit)
        self.plainTextEdit.setPlainText("여기에 텍스트를 입력하세요...")
        self.plainTextEdit.setFrameStyle(QTextEdit.NoFrame)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {background-color: #f7e1dc;}")

        #statusBar, menuBar객체 menu 생성
        self.bar = self.statusBar()
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("&File")
        self.help_menu = self.menu.addMenu("&Help")

        # 메뉴 바 생성, 액션 추가
        open_action = QAction("&Open", self)
        save_action = QAction("&Save", self)
        save_as_action = QAction("Save &As", self)
        close_action = QAction("&Close", self)
        about_action = QAction("&About", self)
        open_action.triggered.connect(self.open_func)
        save_action.triggered.connect(self.save_func)
        save_as_action.triggered.connect(self.save_as_func)
        close_action.triggered.connect(QCoreApplication.instance().quit)
        about_action.triggered.connect(self.about_func)

        self.file_menu.addAction(open_action)
        self.file_menu.addAction(save_action)
        self.file_menu.addAction(save_as_action)
        self.file_menu.addSeparator()  # 메뉴 구분선 추가
        self.file_menu.addAction(close_action)
        self.help_menu.addAction(about_action)

    def open_func(self):
        self.bar.showMessage("Open 메뉴 선택")
    def save_func(self):
        self.bar.showMessage("Save 메뉴 선택")
    def save_as_func(self):
        self.bar.showMessage("Save As 메뉴 선택")
    def about_func(self):
        self.bar.showMessage("도움이 필요하시면 말하세요~")

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
