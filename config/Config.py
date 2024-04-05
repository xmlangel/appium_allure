import os
BASE_DIR = os.getcwd()

#appium
APP_FILE = "app.ipa"
URL = 'http://127.0.0.1:4723'
PLATFORM_NAME="ios"
PLATFORM_VERSION="16.2"
AUTOMATION_NAME="XCUITest"
UDID = "00008110-"
BUNDLE_ID="com.test.app.test.qa"
XCODE_ORG_ID="Gtest"


#google
#https://console.cloud.google.com/apis/credentials 의 서비스 계정등록된 Json 파일 구글 문서에 권한을 추가해줘야함.
GOOGLE_AUTH_FILE_NAME= BASE_DIR + "/config/auth.json"
GOOGLE_SPREADSHEET_URL = "" 
GOOGLE_WORKSHEET="" # WORKSHEET Name
