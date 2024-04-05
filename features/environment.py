import base64
import os
from appium import webdriver
import time
import config.Config as config

import utilities.CustomLogger as cl
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()

logger = cl.custom_logger()
BASE_DIR = os.getcwd()
URL = config.URL
apps = config.APP_FILE

app = os.path.join(BASE_DIR, 'apps', apps)

print("baseDir = " + BASE_DIR)
print("app = " + app)


def before_feature(context, feature):
    print("appium start")
    appium_service.start()
    capabilities = {
        "app": app,
        "platformName": config.PLATFORM_NAME,
        "appium:platformVersion": config.PLATFORM_VERSION,
        "appium:automationName": config.AUTOMATION_NAME,
        "appium:udid": config.UDID,
        "appium:bundleId": config.BUNDLE_ID,
        "appium:xcodeOrgId": config.XCODE_ORG_ID,
        "autoAcceptAlerts": "true",
        "appium: xcodeSigningId": "iPhone Developer"
    }

    context.driver = webdriver.Remote(command_executor=URL, desired_capabilities=capabilities)
    start_recoding(context)


def start_recoding(context):
    '''
    iphone 14 pro 에서 h264 지원안됨. mjpeg로 변경.
    '''
    context.driver.start_recording_screen(videoType='mjpeg', videoQuality='high')
    logger.info("Recoding Start")


def stop_recoding(context):
    raw_video_data = context.driver.stop_recording_screen()
    video_file_name = f'{time.strftime("%Y%m%d_%H%M%S")}_.mp4'
    video_file_path = os.path.join(BASE_DIR + "/reports", "[" + "ios" + "]" + "-" + video_file_name)
    with open(video_file_path, "wb") as fd:
        fd.write(base64.b64decode(raw_video_data))
    logger.info("Recoding Stop")


def after_feature(context, feature):
    stop_recoding(context)
    context.driver.quit()
    appium_service.stop()
    print("appium stop")
