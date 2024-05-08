# Qt_mini_project_bundle
임베디드 GUI를 위한 미니 Qt 과제 모음입니다. (PySide Framework 활용 - Qt designer)

## Enviroment
<h4>using interpreter </h4>
python 3.11 <br>

<h4>need to install</h4>
파이참 File - setting - 자신 프로젝트 - python interpreter - +버튼 누르고 설치 <br>
pyside6 <br>
matplotlib <br>
opencv-contrib-python <br>


## Qt_Image_Processing
![도전2](https://github.com/woodong11/Qt_mini_project_bundle/assets/91379630/c7948da1-3d2d-4d70-a757-fb4be263443b)
<br>
카메라로 촬영한 영상에 실시간 이미지를 처리하는 예제입니다. (canny, grayscale변환, blur, Morpho, Threshold) <br>
play 버튼: 카메라 촬영 시작 / 종료 <br>
mode 버튼: 클릭할 때마다, 이미지 처리 모드 변경 <br>


## Qt_Mouse_Training_Program
![ㅇㅇㅇ](https://github.com/woodong11/Qt_mini_project_bundle/assets/91379630/b3a48d30-7d17-4b81-bc97-f32baf3656ab)
<br>게임을 시작하면 레이블이 랜덤으로 움직이고, 10초 후 레이블을 클릭한 횟수를 메시지 박스로 출력하는 게임입니다. <br>
1.이름 버튼 : 레이블의 text 변경 기능 <br>
2.색상 버튼 : 레이블의 배경색 변경 기능<br>
3.시작 버튼 : 게임 시작 기능<br>

<h3> run </h3>

```python
pip install pyside6
python main.py
```


## Qt_chart_plot
![도전1](https://github.com/woodong11/Qt_mini_project_bundle/assets/91379630/c4725237-245f-41ef-8858-8f6502b5ae6a)
<br> 버튼을 클릭하면 차트를 GUI로 보여주고 버튼을 클릭할때마다 값을 랜덤으로 바꿔줍니다. <br>
3개의 다단 그래프로 이뤄진 샘플 코드를 분석하여 포팅 <br>
3개의 버튼으로 다단 그래프를 각각 출력 <br>
버튼을 클릭할 때마다 값이 랜덤으로 바뀜 <br>


## Qt_join_membership
![도전1](https://github.com/woodong11/Qt_mini_project_bundle/assets/91379630/73d3ef0f-91c5-41d5-a2bf-262bb57a9358)
<br>임베디드 환경에서 회원가입 폼을 위한 GUI입니다. <br>
이름 입력 허용 글자 수 : 1~4 <br>
나이 입력 허용 범위 : 1 ~ 30 <br>
해당 범위를 벗어나면 각각 경고 메시지 박스를 표시<br>
모두 만족 시, 회원가입 버튼 누르면, “회원가입 성공” 메시지 박스 표시<br>

## Qt_network_management 
![도전2](https://github.com/woodong11/Qt_mini_project_bundle/assets/91379630/c0fda1d3-a7bf-44c2-9db9-66e3b92c8a80)
<br>인맥을 관리할 수 있는 GUI입니다.<br>
1.추가 버튼
→ 새로운 이름만 추가 ( 최대 10개 ) <br>
→ 이름 길이 0 / 기존에 추가된 이름 → 경고<br>
2.제거 버튼
→ 길이 0 / 없는 이름 / 리스트 길이 0 → 경고<br>
3.메뉴바
→ 추가, 제거 구현, quit() 호출해서 프로그램 종료<br>
4.상태 바 → 메시지 출력
 → 추가되었습니다, 제거되었습니다 등<br>
→ 경고 메시지 출력<br>

## Qt_my_notepad
![도전3](https://github.com/woodong11/Qt_mini_project_bundle/assets/91379630/4f33d7f2-1ccd-4106-8e5c-45f9a451ffc8)
<br>QPlainTextEdit()를 사용하고, open, save, save as 기능이 있는 메모장입니다. <br>
