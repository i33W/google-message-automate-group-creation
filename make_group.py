from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 구글 메세지 주소
MESSAGE_LOGIN = 'https://messages.google.com/web/authentication'

o = webdriver.ChromeOptions()  # 에러 로그 안보이게 하는 옵션
o.add_experimental_option('excludeSwitches', ['enable-logging'])
s = Service(ChromeDriverManager().install())  # 구글 드라이버 자동으로 받아서 실행시켜줌

driver = webdriver.Chrome(service=s, options=o)  # 크롬 드라이버 실행
driver.get(MESSAGE_LOGIN)  # 주소 이동

try:
    input("1. 기기페어링 완료 후 채팅 시작 버튼이 보이면 엔터키를 눌러주세요.")
    start_elements = driver.find_elements(by=By.TAG_NAME, value="a")
    start_elements[1].click()

    input("2. 그룹 대화 시작 버튼이 보이면 엔터키를 눌러주세요.")
    startgroup_elements = driver.find_elements(
        by=By.CLASS_NAME, value="start-group-button")
    startgroup_elements[0].click()

    input("3. 전화번호 붙여넣기 후 입력을 시작하려면 엔터키를 눌러주세요.")
    input_elements = driver.find_elements(by=By.CLASS_NAME, value="input")
    phone_list = input_elements[0].get_attribute("value").split()
    input_elements[0].clear()
    for phone in phone_list:
        input_elements[0].send_keys(phone)
        input_elements[0].send_keys("\n")
    input("4. 그룹 등록 완료 후 종료하려면 엔터키를 눌러주세요.")
except Exception as e:
    print("예외 발생: ", e)
finally:
    print('종료합니다.')
    driver.close()
    driver.quit()
