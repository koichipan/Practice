import time
import os
import sys
# from appium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def getDeviceStatus():
    getadbState = osCommand("adb get-state")
    getadbStateA = getadbState.find("device")
    if getadbStateA is not -1:
        print("adb connection is available to use. getadbState = " + getadbState)
    else:
        print("adb connection is unavailable to use. getadbState = " + getadbState)

    getPropManufacturer = osCommand("adb shell getprop ro.product.manufacturer")
    getPropModel = osCommand("adb shell getprop ro.product.model")
    getPropBrand = osCommand("adb shell getprop ro.product.brand")
    getPropAndroidversion = osCommand("adb shell getprop ro.build.version.release")
    getPropSDKversion = osCommand("adb shell getprop ro.build.version.sdk")
    getPropSerialNo = osCommand("adb shell getprop ro.serialno")

    Result = dict(
        Manufacturer=getPropManufacturer,
        Model=getPropModel,
        Brand=getPropBrand,
        Androidversion=getPropAndroidversion,
        SDKversion=getPropSDKversion,
        SerialNo=getPropSerialNo)
    return Result


def osCommand(cmd):
    pyVesion = str(sys.version_info)
    if 'major=2' in pyVesion:
        import commands
        return commands.getoutput(cmd)
    else:
        import subprocess
        return subprocess.getoutput(cmd)


class Util:
    def __init__(self, mDevice, dir):
        self.pkg = os.getenv('PGPKG')
        self.driver = mDevice
        # self.screenshot_count = 1
        self.screenshot_dir = dir
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def clearDate(self):
        result = osCommand('adb shell pm clear ' + self.pkg)
        if 'Success' in result:
            return True
        else:
            print("Clear Data Failed: " + result)
            return False

    def launchPG(self):
        osCommand('adb shell am start -n ' + self.pkg + '/.MainPage')

    def closePG(self):
        osCommand('adb shell am force-stop ' + self.pkg)

    def isEleClickable(self, rid):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, rid)))
            return True
        except TimeoutException:
            print("Check element " + str(rid) + " clickable fail.")
            return False

    def isElePresence(self, rid):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, rid)))
            return True
        except TimeoutException:
            print("Check element " + str(rid) + " presence fail.")
            return False

    def ieEleVisible(self, rid):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, rid)))
            return True
        except TimeoutException:
            print("Check element " + str(rid) + " visible fail.")
            return False

    def clickEle(self, type, rid):
        try:
            if(type == 'id'):
                self.driver.find_element_by_id(rid).click()
            if(type == 'text'):
                # self.driver.find_element_by_name(rid).click()
                self.driver.find_element_by_android_uiautomator('new UiSelector().text(\"' + rid + '\")').click()
        except TimeoutException:
            print("Click element " + str(rid) + " Error.")

    def getTextELe(self, rid):
        try:
            return self.driver.find_element_by_id(rid).text
        except TimeoutException:
            print("Get element " + str(rid) + " Text Error.")

    def scrollTo(self, rid):
        try:
            self.driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId(\"' + rid + '\").instance(0));')
            return True
        except TimeoutException:
            print("Scroll to element " + str(rid) + " Timeout.")
            return False

    def isNotMatch(self, resultA, resultB, str=""):
        try:
            if(resultA != resultB):
                self.logv2(str, "done")
                return True
            else:
                self.logv2(str, "FAIL")
                return False
        except:
            self.logv2(str, "FAIL")
            raise

    def waitUntilAndGetElement(self, type, key, str="", timeout=3):
        try:
            if(type == 'name'):
                ele = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.Name, key))
                )
                self.logv2(str, "done")
                return ele
            if(type == 'id'):
                ele = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.ID, key))
                )
                self.logv2(str, "done")
                return ele
            if (type == 'xpath'):
                ele = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, key))
                )
                self.logv2(str, "done")
                return ele
        except:
            # return False
            self.logv2(str, "FAIL")
            raise

    def scrollUntilGetElement(self, type, key, str=""):
        if(type == 'text'):
            selector = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\"' + key + '\").instance(0));'
        if(type == "id"):
            selector = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId(\"' + key + '\").instance(0));'
        try:
            ele = self.driver.find_element_by_android_uiautomator(selector)
            self.logv2(str, "done")
            return ele
        except:
            self.logv2(str, "FAIL")
            raise

    def screenshot(self, name):
        screenshot_name = str(time.strftime("%Y%m%d%H%M%S")) + "_" + name + ".png"
        self.log("Taking screenshot: " + self.screenshot_dir + "/" + screenshot_name)
        # on Android, switching context to NATIVE_APP for screenshot
        # taking to get screenshots also stored to Testdroid Cloud
        # device run view. After screenshot switching back to
        # WEBVIEW. Works ok for Safari too.
        orig_context = self.driver.current_context
        self.driver.switch_to.context("NATIVE_APP")
        self.driver.save_screenshot(self.screenshot_dir + "/" + screenshot_name)
        # only change context if originally context was WEBVIEW
        if orig_context not in self.driver.current_context:
            self.driver.switch_to.context("WEBVIEW")
        # self.screenshot_count += 1

    def log(self, msg):
        print(time.strftime("%H:%M:%S") + ": " + msg)
        return

    def logv2(self, msg, type):
        if (msg != ""):
            str = '{0:-<60}'.format(msg)
            print(str + type)
