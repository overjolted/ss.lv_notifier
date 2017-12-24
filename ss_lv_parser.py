from selenium import webdriver

URL = 'https://www.ss.com/msg/ru/work/i-search-for-work/computer-technician/ehble.html'
browser = webdriver.Chrome('d://chromedriver_win32//chromedriver.exe')
browser.implicitly_wait(10)
browser.get(URL)
pokazat_nomer = browser.find_element_by_link_text('Показать номер')
pokazat_nomer.click()












from selenium import webdriver

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

options = webdriver.ChromeOptions('d://chromedriver_win32//chromedriver.exe')
# specify headless mode
options.add_argument('headless')
# specify the desired user agent
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=options)