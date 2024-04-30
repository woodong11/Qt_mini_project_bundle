# 회원가입화면 만들기
from PySide6.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("회원가입 GUI")
        self.setGeometry(800, 400, 300, 200)

        # 요소들
        self.form = QFormLayout(self)
        self.name_edit = QLineEdit()
        self.age_edit = QLineEdit()
        self.age_btn = QPushButton("나이 확인")
        self.submit_btn = QPushButton("회원가입")
        self.age_alert = QLabel("경고: 나이가 너무 많습니다.")
        self.age_alert.setVisible(False)

        # 레이아웃 생성
        name_hlay = QHBoxLayout()
        age_hlay = QHBoxLayout()
        age_alert_hlay = QHBoxLayout()
        submit_hlay = QHBoxLayout()

        # 수평배치 레이아웃에 텍스트에디터와 버튼을 추가
        name_hlay.addWidget(self.name_edit)
        age_hlay.addWidget(self.age_edit)
        age_hlay.addWidget(self.age_btn)
        submit_hlay.addWidget(self.submit_btn)
        age_alert_hlay.addWidget(self.age_alert)

        # Form 레이아웃에 수평배치 레이아웃을 text와 함께 추가
        self.form.addRow("name", name_hlay)
        self.form.addRow("age", age_hlay)
        self.form.addRow("", age_alert_hlay)
        self.form.addRow("", submit_hlay)

        # 함수들 연결
        self.name_edit.textChanged.connect(self.check_name_length)
        self.age_btn.clicked.connect(self.check_age_length)
        self.submit_btn.clicked.connect(self.check_submit)

    def check_name_length(self):
        if len(self.name_edit.text()) > 4:
            self.name_msg = QMessageBox()
            self.name_msg.setText("이름이 너무 깁니다")
            self.name_msg.exec() # User가 닫기 버튼을 누를 때까지 실행될 수 있게 .exec() 사용

    def check_age_length(self):
        if int(self.age_edit.text()) > 30:
            self.age_alert.setVisible(True)
        else:
            self.age_alert.setVisible(False)

    def check_submit(self):
        self.submit_msg = QMessageBox()
        if (len(self.age_edit.text()) <= 4) and (int(self.age_edit.text()) <= 30):
            self.submit_msg.setText("회원가입 성공!")
        else:
            self.submit_msg.setText("회원가입 실패")
        self.submit_msg.exec()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
