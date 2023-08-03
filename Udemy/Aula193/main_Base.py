import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

print('Hello World')

Root_Folder = Path(__file__).parent
# print(Root_Folder)
CHROMEDRIVER_EXEC = Root_Folder / 'drivers' / 'chromedriver.exe'
# print(CHROMEDRIVER_EXEC)
chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options)
# chrome_options.add_argument('--headless') #Para não abrir a interface do navegador

chrome_browser.get('https://www.google.com.br')
time.sleep(30)
