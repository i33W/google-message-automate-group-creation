from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.utils import ChromeType

# 구글 메세지 주소
LOGIN_URL = 'https://messages.google.com/web/authentication'

o = webdriver.ChromeOptions()  # 에러 로그 안보이게 하는 옵션
o.add_experimental_option('excludeSwitches', ['enable-logging'])
# 구글 드라이버 자동으로 받아서 실행시켜줌
s = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

driver = webdriver.Chrome(service=s, options=o)  # 크롬 드라이버 실행
driver.get(LOGIN_URL)  # 주소 이동

try:
    input("1. 기기페어링 완료 후 채팅 시작 버튼이 보이면 엔터키를 눌러주세요.")
    startButton = driver.find_element(
        by=By.CSS_SELECTOR, value=".start-chat a")
    startButton.click()

    input("2. 그룹 대화 시작 버튼이 보이면 엔터키를 눌러주세요.")
    groupButton = driver.find_element(
        by=By.CSS_SELECTOR, value="button.start-group-button")
    groupButton.click()

    input("3. 전화번호 붙여넣기 후 입력을 시작하려면 엔터키를 눌러주세요.")
    phoneInput = driver.find_element(by=By.CSS_SELECTOR, value="input.input")
    phone_list = phoneInput.get_attribute("value").split()
    phoneInput.clear()
    for phone in phone_list:
        phoneInput.send_keys(phone)
        phoneInput.send_keys("\n")

    loop = input("    ▶ 새 그룹을 등록하려면 엔터키를 눌러주세요. (종료: 숫자 1 입력)")
    while loop != "1":
        start = driver.find_element(by=By.CSS_SELECTOR, value=".start-chat a")
        start.click()
        input("2. 그룹 대화 시작 버튼이 보이면 엔터키를 눌러주세요.")
        groupButton = driver.find_element(
            by=By.CSS_SELECTOR, value="button.start-group-button")
        groupButton.click()
        input("3. 전화번호 붙여넣기 후 입력을 시작하려면 엔터키를 눌러주세요.")
        phoneInput = driver.find_element(
            by=By.CSS_SELECTOR, value="input.input")
        phone_list = phoneInput.get_attribute("value").split()
        phoneInput.clear()
        for phone in phone_list:
            phoneInput.send_keys(phone)
            phoneInput.send_keys("\n")
        loop = input("    ▶ 새 그룹을 등록하려면 엔터키를 눌러주세요. (종료: 숫자 1 입력)")

except Exception as e:
    print("예외 발생: ", e)
finally:
    print('종료합니다.')
    driver.close()
    driver.quit()
