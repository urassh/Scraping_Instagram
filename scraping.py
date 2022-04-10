from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from instagram import Instagram

login_name = "09040151011"
login_password = "518312"
browser = webdriver.Chrome(ChromeDriverManager().install())

User = Instagram(login_name, login_password, browser)
sleep(1)

User.access()
sleep(1)

#User.others('')
sleep(1)

User.followers("show")
sleep(1)

# User.follows("none")
# sleep(1)

# User.results()
# sleep(1)

# User.browser_quit()