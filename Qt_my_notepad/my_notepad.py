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
        self.edit = QPlainTextEdit(self)
        self.setCentralWidget(self.edit)
        #self.plainTextEdit.setPlainText("여기에 텍스트를 입력하세요...")
        self.edit.setFrameStyle(QTextEdit.NoFrame)
        self.edit.setStyleSheet("QPlainTextEdit {background-color: #f7e1dc;}")

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
        open_action.triggered.connect(self.open)
        save_action.triggered.connect(self.save)
        save_as_action.triggered.connect(self.save_as)
        close_action.triggered.connect(self.close)
        about_action.triggered.connect(self.about)

        self.file_menu.addAction(open_action)
        self.file_menu.addAction(save_action)
        self.file_menu.addAction(save_as_action)
        self.file_menu.addSeparator()  # 메뉴 구분선 추가
        self.file_menu.addAction(close_action)
        self.help_menu.addAction(about_action)

    # class 변수 path 선언
    path = None
    def open(self):
        self.bar.showMessage("Open 메뉴 선택")
        # 동작 확인용 message
        # self.bar.showMessage("open 메뉴 클릭")
        # 파일 열기 후 파일 경로를 path에 저장
        path = QFileDialog.getOpenFileName(self, "Open File")[0]
        # 파일 열기 정상적으로 동작한다면
        if path:
            # 객체 변수 self.path 에 path 값 저장
            self.path = path
            # 파일 read 후 textEditor 의 text로 설정
            self.edit.setPlainText(open(self.path).read())

    def save(self):
        self.bar.showMessage("Save 메뉴 선택")
        self.bar.showMessage("save 메뉴 클릭")
        # 처음 파일 저장한다면
        # 파일을 처음 저장하면, 경로를 설정할 필요가 있으나, 저장된 파일을 수정한다면, 경로가 기록되어 있으니, 바로 덮어쓰기만 하기함위함
        if self.path is None:
            # save_as() 실행
            self.save_as()
        # 아니라면,
        else:
            # 파일 덮어쓰기 실행, textEditor는 수정됨으로 설정
            with open(self.path, 'w') as f:
                f.write(self.edit.toPlainText())
                self.edit.document().isModified()

    def save_as(self):
        self.bar.showMessage("Save As 메뉴 선택")
        self.bar.showMessage("save as 메뉴 클릭")
        # 파일 저장용 dialog 표시 후 경로를 path에 저장
        path = QFileDialog.getSaveFileName(self, "Save As")[0]
        if path:
            # 파일 경로를 self.path에 저장
            self.path = path
            # save() 호출
            self.save()

    def about(self):
        self.bar.showMessage("도움이 필요하시면 말하세요~")
        # HTML이 아니라 Qt의 rich text
        text = """<center>\
                   <h1>Text Editor</h1>\
                   </center>
                   <p>Version 1.2.3<br>
                   Copyright</p>
                   """
        # QMessageBox() 객체 생성
        msg = QMessageBox()
        # About messageBox, 현재 애플리케이션의 빌드 시기 or 버전을 표시하는 정보 창
        msg.about(self, "About", text)

    def close(self, event):
        # 수정된 사항이 없다면, 바로 종료
        if not self.edit.document().isModified():
            return
        # 저장된 경로가 없다면, 바로 종료
        if self.path is None:
            return

        # 파일 저장 경로가 User마다 다르므로, 가장 마지막 경로만 파싱해서 MessageBox에 출력하기 위한 파싱
        path_parsing = self.path.split('/')[-1]
        msg = "변경 사항을 " + path_parsing + "에 저장하시겠습니까?"
        # 선택할 버튼으로 Save, Discard, Cancel 가진, QMessageBox의 question 메시지창 생성
        answer = QMessageBox.question(self, "하하호호메모장", msg,
                                      QMessageBox.Save |
                                      QMessageBox.Discard |
                                      QMessageBox.Cancel)
        # Save 버튼 눌렀다면, save() 호출
        if answer & QMessageBox.Save:
            self.save()
        # Cancel 버튼 눌렀다면, ignore() 호출 후 종료
        if answer & QMessageBox.Cancel:
            event.ignore()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
