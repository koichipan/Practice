import util
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.normpath(sys.path[0])) + "/res")
import PG_element as el
from selenium.webdriver.common.by import By

parentFolder = os.path.abspath(os.pardir)


class Module:
    def __init__(self, mDevice, dir):
        self.driver = mDevice
        self.util = util.Util(self.driver, dir)

    def loginByEmail(self):
        self.util.waitUntilAndGetElement("id", el.FivePage['profile'], "Try to go profile page").click()
        self.util.waitUntilAndGetElement("id", el.ProfilePage['Mail'], "Try to click email").click()
        self.util.waitUntilAndGetElement("id", el.emailLoginPage['account'], "Try to click account").click()
        util.osCommand('adb shell input text yan.work.tw@gmail.com')
        self.util.waitUntilAndGetElement("id", el.emailLoginPage['pwd'], "Try to click passowrd").click()
        util.osCommand('adb shell input text pgtest')
        self.util.waitUntilAndGetElement("id", el.emailLoginPage['submit'], "Try to click submit").click()
        return self.util.waitUntilAndGetElement("id", el.ProfilePageAfterLogin['nickName'], "Try to get Nick Name")

    def checkAccount(self):
        # Verify if FB login icon exist in proile page
        # self.util.waitUntilAndGetElement("id", el.FivePage['profile'], "Try to go profile page").click()
        ProfileXpath = self.util.waitUntilAndGetElement("xpath", el.FivePageXpath['profile'], str="Tap by xpath", timeout=3).click()
        # ProfileXpath.click()
        return self.util.isEleClickable(el.ProfilePage['FB'])

    def logoutAccount(self):
        self.util.waitUntilAndGetElement("id", el.ProfilePageAfterLogin['setting'], "Try to go setting").click()
        self.util.clickEle("text", "Settings")
        self.util.scrollUntilGetElement("text", "Log Out", "Scroll to logout and click").click()
        self.util.clickEle("text", "Log Out")

    def searchResult(self, type, key):
        try:
            self.util.waitUntilAndGetElement("id", el.HomePage['Search'], "Try to go Search").click()
            if(type == 'user'):
                time.sleep(2)
                util.osCommand('adb shell input text ' + str(key))
                time.sleep(5)
                self.util.scrollUntilGetElement("text", key, "click search result").click()
                result = self.util.waitUntilAndGetElement("id", el.ProfilePageAfterLogin['userName'], "Get result name").text
            elif(type == 'hashtag'):
                time.sleep(2)
                self.util.waitUntilAndGetElement("id", el.SearchPage['Hashtag'], "Click hashtag").click()
                time.sleep(1)
                util.osCommand('adb shell input text ' + str(key))
                time.sleep(5)
                self.util.scrollUntilGetElement("text", key, "click search result").click()
                key = '#' + key
                result = self.util.waitUntilAndGetElement("id", el.ProfilePageAfterLogin['userName'], "Get result name").text
            if(self.util.isNotMatch(result, key, "Check search result")):
                print("Result name " + str(result) + " not match to search name " + str(key))
                return False
            else:
                print("Result name " + str(result) + " match to search name " + str(key))
                return True
        except:
            self.pgutil.screenshot("test_PG_009_SearchResult_function")
            self.assertTrue(False)

    def SendAndCheckComments(self, key):
        # self.driver.find_element_by_id(el.HomePage['Comment']).click()
        try:
            # self.driver.find_element(By.xpath("//android.widget.FrameLayout[contains(@index,0)]"))
            # _by_class_name("android.widget.FrameLayout")
            # self.driver.findElementByXpath("//android.widget.FrameLayout[contains(@index,0)]")
            self.driver.findElementByXpath("//android.widget.FrameLayout[contains(@index,0)]")
        # time.sleep(3)
        # util.osCommand('adb shell input text' + str(key))
        except:
            self.assertTrue(False)
