# coding:utf-8
import os
import time
import unittest
from appium import webdriver
import sys
sys.path.append(os.path.dirname(os.path.normpath(sys.path[0])) + "/lib")
sys.path.append(os.path.dirname(os.path.normpath(sys.path[0])) + "/res")
from lib.module import Module
# import module
import util as ul
import PG_element as el

pyVesion = str(sys.version_info)
if 'major=2' in pyVesion:
    import HTMLTestRunner_2 as HTMLTestRunner
else:
    import HTMLTestRunner

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

parentFolder = os.path.dirname(os.path.normpath(sys.path[0]))


def PATH(p):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def checkFolder():
    if not os.path.exists(parentFolder + "/result"):
        os.makedirs(parentFolder + "/result")


# Result = dict (Manufacturer,Model,Brand,Androidversion,SDKversion,SerialNo)
Result = ul.getDeviceStatus()


class NeedClearData_test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = Result["Androidversion"]
        desired_caps['deviceName'] = Result["SerialNo"]
        desired_caps['appPackage'] = el.Package['appPackage']
        desired_caps['appActivity'] = el.Package['appActivity']

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        self.pgutil = ul.Util(self.driver, parentFolder +
                              "/screenshots/" + str(time.strftime("%Y%m%d")))
        self.pgmodule = module.Module(
            self.driver, parentFolder + "/screenshots/" + str(time.strftime("%Y%m%d")))

    def tearDown(self):
        self.driver.quit()

    """
    def test_PG_001_FirstTimeLaunchNeedHaveLoginPage(self):
        try:
            if(self.pgutil.clearDate()):
                self.pgutil.launchPG()
                isHaveSkip = self.pgutil.isEleClickable(el.LoginPage['skip'])
                isHaveTopImg = self.pgutil.isEleClickable(el.LoginPage['topImage'])
                isHaveMore = self.pgutil.isEleClickable(el.LoginPage['more'])
                if((isHaveMore) and (isHaveSkip) and (isHaveTopImg)):
                    self.assertTrue(True)
            else:
                raise
        except:
            self.pgutil.screenshot("test_PG_001_FirstTimeLaunchNeedHaveLoginPage")
            self.assertTrue(False)

    def test_PG_002_SecondTimeLaunchNeedHaveGuide(self):
        try:
            # second time launch
            if(self.pgutil.clearDate()):
                self.pgutil.launchPG()
                if(self.pgutil.isEleClickable(el.LoginPage['skip'])):
                    self.pgutil.closePG()
                    self.pgutil.launchPG()
                else:
                    raise

                # press back key then verify overlayout still display
                self.driver.press_keycode(4)  # Back Key
                isHaveWording = self.pgutil.isEleClickable(el.AllTool['wording'])
                isHaveArrow = self.pgutil.isEleClickable(el.AllTool['arrow_down'])
                if((isHaveWording) and (isHaveArrow)):
                    self.assertTrue(True, "點擊 Back key 後蒙層不應該不見")

                # tap + then verify overlayout undisplay
                self.pgutil.waitUntilAndGetElement("id", el.AllTool['tool'], "點擊+號").click()
                self.assertTrue(self.pgutil.isEleClickable(el.AllTool['tools_content']), "蒙層消失, 出現工具集")

                # verify 拼接 and Twinkle and Camera
                self.assertTrue(self.pgutil.isEleClickable(el.AllTool['multi']), "工具集裡有拼接")
                self.assertTrue(self.pgutil.isEleClickable(el.AllTool['twinkle']), "工具集裡有Twinkle")
                self.assertTrue(self.pgutil.isEleClickable(el.AllTool['camera']), "工具集最近照片裡有相機")

                # Tap x then verify tools layout undisplay
                self.pgutil.waitUntilAndGetElement("id", el.AllTool['close'], "點擊 X ").click()
                self.assertFalse(self.pgutil.isEleClickable(el.AllTool['tools_content']), "工具集取消")

        except:
            self.pgutil.screenshot("test_PG_002_SecondTimeLaunchNeedHaveGuide")
            self.assertTrue(False)"""


class Normal_test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = Result["Androidversion"]
        desired_caps['deviceName'] = Result["SerialNo"]
        desired_caps['appPackage'] = el.Package['appPackage']
        desired_caps['appActivity'] = el.Package['appActivity']

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        self.pgutil = ul.Util(self.driver, parentFolder +
                              "/screenshots/" + str(time.strftime("%Y%m%d")))
        self.pgmodule = module.Module(
            self.driver, parentFolder + "/screenshots/" + str(time.strftime("%Y%m%d")))

    def tearDown(self):
        self.driver.quit()

    """
    def test_PG_005_LoginByEmail(self):
        try:
            nickName = self.pgmodule.loginByEmail()
            self.assertNotEqual(nickName.text, "")
        except:
            self.pgutil.screenshot("test_PG_005_LoginByEmail")
            self.assertTrue(False)
    """

    def test_PG_007_CheckCanLogout(self):
        try:
            if(self.pgmodule.checkAccount()):
                self.pgmodule.loginByEmail()
                self.pgmodule.logoutAccount()
            else:
                self.pgmodule.logoutAccount()
            time.sleep(2)
            if(self.pgmodule.checkAccount()):
                self.assertTrue(True)
        except:
            self.pgutil.screenshot("test_PG_007_CheckCanLogout")
            self.assertTrue(False)
    """
    def test_PG_009_CheckSearchpage(self):
        try:
            if(self.pgmodule.checkAccount()):
                self.pgmodule.loginByEmail()
                self.pgutil.waitUntilAndGetElement("id", el.FivePage['home'], "Back to home").click()
            else:
                self.pgutil.waitUntilAndGetElement("id", el.FivePage['home'], "Back to home").click()

            if(self.pgmodule.searchResult("user", "koichipanhtc")):
                self.assertTrue(True)
            else:
                self.assertTrue(False)
            time.sleep(3)

            self.pgutil.waitUntilAndGetElement("id", el.PicPage['back'], "Back to SearchPage").click()
            time.sleep(1)
            self.pgutil.waitUntilAndGetElement("id", el.PicPage['back'], "Back to SearchPage").click()
            time.sleep(3)
            if(self.pgmodule.searchResult("hashtag", "2017")):
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.pgutil.screenshot("test_PG_009_CheckSearchpage")
            self.assertTrue(False)

    def test_PG_022_CheckComment(self):
        try:
            if(self.pgmodule.checkAccount()):
                self.pgmodule.loginByEmail()
            time.sleep(3)
            self.pgutil.waitUntilAndGetElement("id", el.FivePage['profile'], "Go to profile").click()
            time.sleep(3)
            self.pgmodule.SendAndCheckComments("test")
        except:
            self.assertTrue(False)

        # self.driver.find_element_by_id("com.roidapp.photogrid:id/feed_comment_image").click() """


if __name__ == '__main__':
    checkFolder()

    loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        loader.loadTestsFromTestCase(NeedClearData_test),
        loader.loadTestsFromTestCase(Normal_test)
    ))

    # unittest.TextTestRunner(verbosity=2).run(suite)
    file = open(str(PATH(parentFolder + '/result/' +
                         str(time.strftime("%Y%m%d") + '.html'))), "wb")

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file,
        title="[PG Automation] [Python+Appium] [Device: " + ' ' +
        Result["Manufacturer"] + ' ' + Result["Model"] +
        ' ' + Result["Brand"] + ']',
        description="[Platform Version: " + Result["Androidversion"] + ']' + "[SDK version: " + Result["SDKversion"] + ']' + "[Device S/N: " + Result["SerialNo"] + ']')
    runner.run(suite)
    # runner.run(suite_Normal)

    file.close()
