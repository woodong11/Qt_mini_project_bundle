# 인맥관리 프로그램
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.name_list = []
        self.main()

    def main(self):
        self.setWindowTitle("인맥 관리 프로그램")
        self.setGeometry(800, 400, 300, 300)

        # 요소
        self.name_label = QLabel("name")
        self.name_edit = QLineEdit()
        self.add_btn = QPushButton("추가")
        self.delete_btn = QPushButton("제거")
        self.names_label = QLabel("")  # 이름을 보여줄 QLabel
        self.names_label.setVisible(False)

        # 수평 레이아웃에 요소 추가
        self.name_hlay = QHBoxLayout()
        self.btn_hlay = QHBoxLayout()
        self.name_hlay.addWidget(self.name_label)
        self.name_hlay.addWidget(self.name_edit)
        self.btn_hlay.addWidget(self.add_btn)
        self.btn_hlay.addWidget(self.delete_btn)

        # 수직 박스에 수평 레이아웃들 추가
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.name_hlay)
        self.vbox.addLayout(self.btn_hlay)
        self.vbox.addWidget(self.names_label)
        self.vbox.addStretch(1)    # 레이아웃들 위로 정렬

        # 메인 central에 객체 추가
        mainWidget = QWidget()
        mainWidget.setLayout(self.vbox)
        self.setCentralWidget(mainWidget)

        #statusBar, menuBar객체 menu 생성
        self.bar = self.statusBar()
        self.menu = self.menuBar()
        self.main_menu = self.menu.addMenu("메뉴")
        self.exit_menu = self.menu.addMenu("종료")

        # 버튼들 액션 추가
        self.add_btn.clicked.connect(self.add_func)
        self.delete_btn.clicked.connect(self.del_func)

        # 메뉴 바 생성, 액션 추가
        addAction = QAction("추가", self)
        addAction.triggered.connect(self.add_func)
        delAction = QAction("제거", self)
        delAction.triggered.connect(self.del_func)
        exitAction = QAction("종료", self)
        exitAction.triggered.connect(QCoreApplication.instance().quit)

        self.main_menu.addAction(addAction)
        self.main_menu.addSeparator()  # 메뉴 구분선 추가
        self.main_menu.addAction(delAction)
        self.exit_menu.addAction(exitAction)


    def update_names_display(self):
        if self.name_list:
            self.names_label.setText(", ".join(self.name_list))
            self.names_label.setVisible(True)
        else:
            self.names_label.setVisible(False)
    def add_func(self):
        name = self.name_edit.text()  # 사용자 입력을 받아와 공백 제거
        if (len(name) == 0) or (name in self.name_list):
            self.bar.showMessage("경고: 이름이 없거나 이미 존재하는 이름입니다.")

        elif len(self.name_list) > 10:
            self.bar.showMessage("경고: 이름은 총 10개를 넘을 수 없습니다.")

        else:
            self.name_list.append(name)  # 리스트에 이름 추가
            self.bar.showMessage("{}을(를) 추가했습니다.".format(name))
        self.update_names_display()

    def del_func(self):
        name = self.name_edit.text().strip()
        if (len(name) == 0) or (name not in self.name_list):
            self.bar.showMessage("경고: 이름이 없거나 존재하지 않는 이름입니다.")
        else:
            self.name_list.remove(name)  # 리스트에서 해당 이름 제거
            self.bar.showMessage("{}을(를) 제거했습니다.".format(name))
        self.update_names_display()  # QLabel 업데이트


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
