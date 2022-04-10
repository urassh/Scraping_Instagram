from time import sleep
import pyautogui as pag
import pyautogui

class Instagram:
    def __init__(self, username, password, browser):
        self.username = username
        self.password = password
        self.browser = browser
        self.follows_list = []
        self.followers_list = []

    def access(self):
        self.browser.get('https://www.instagram.com')
        sleep(2)

        login_username = self.browser.find_element_by_name("username")
        login_password = self.browser.find_element_by_name("password")

        login_username.send_keys(self.username)
        login_password.send_keys(self.password)

        pyautogui.press('enter')
        sleep(5)

        self.click("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img")
        sleep(2)

        self.click("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div")
        sleep(2)

    #調査の対象が別ユーザーだった時の処理
    def others(self, target):
        search = self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys(target)
        sleep(2)
        pyautogui.press('enter')
        self.target_account = 1

    def followers(self, display):
        self.click("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        sleep(3)

        index = 1
        while index < 50:
            pag.scroll(-50, 700, 500)
            index += 1
            sleep(1)
        
        # フォロワー数のXpath
        followers = self.browser.find_elements_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/span")

        for follower in followers:
            self.followers_list.append(follower.text)
            print(f'{self.followers_list.text}')

        if display == "show":
            print('フォロワーリストです。')
            for follower_list in self.followers_list:
                print("------------------------------")
                print(follower_list)
            print("------------------------------")
        elif display == "none":
            pass

        pyautogui.moveTo(1000, 500)
        pyautogui.click()
        sleep(2)

    # def follows(self, display):

    #     follows = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span")

    #     self.click("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
    #     sleep(3)

    #     index = 1
    #     while index < 90:
    #         pag.scroll(-50, 700, 500)
    #         index += 1
    #         sleep(1)

    #     for follow in follows:
    #         self.follows_list.append(follow.text)

    #     if display == "show":
    #         print('フォローリストです。')
    #         for follow_list in self.follows_list:
    #             print("------------------------------")
    #             print(follow_list)
    #         print("------------------------------")
    #     elif display == "none":
    #         pass

    #     pyautogui.moveTo(1000, 500)
    #     pyautogui.click()

    # def results(self):
    #     user_name = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/h2").text
    #     print(f'アカウント名は{user_name}です。')
    #     print('フォロワーの人数は' + str(len(self.followers_list)) + '人です。')
    #     print('フォローの人数は' + str(len(self.follows_list)) + '人です。')

    #     results_list = list(set(self.follows_list) - set(self.followers_list))
    #     results_list.sort()
    #     if results_list == []:
    #         print("リムられたアカウントはありません。")
            
    #     else:
    #         print('リムられたリストです。')
    #         for result_list in results_list:
    #             print("------------------------------")
    #             print(result_list)
    #         print("------------------------------")
    #         print("リムられているアカウント数は" + str(len(results_list)) + "人です。")

    def browser_quit(self):
        self.browser.quit()

    def click (self, url):
        self.browser.find_element_by_xpath(url).click()
