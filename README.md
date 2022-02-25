# ⚙ Google Message 그룹 생성 자동화 프로그램

#### 모듈 설치 및 실행
---
``` 
python3 install selenium
python3 install webdriver_manager
python3 make_group.py
```

#### 실행 파일 만드는 법
---
```
python3 install pyinstaller
pyinstaller --icon=./icon.ico --onefile make_group.py
```
- 관리자 권한으로 cmd 켜서 실행할 것
- pyinstaller 패스가 이상하게 잡힐 수 있어서 C 폴더에 넣고 할 것
- dist 폴더에 실행 파일(exe) 만들어짐