# 구조
- 테스트 프레임워크 : Appium
- BDD : behave
- 디자인패턴 : PageObject
- Report : allure

# 사전설치 1. Apppium
1. Appium 설치 및 실행
- http://appium.io/docs/en/2.1/quickstart/install/ 참고

2. Appium Driver 설치
```
#Install
npm i --location=global appium
appium driver install uiautomator2
appium driver install xcuitest

```
# 사전설치 2 pip
```
pip install -r requirements.txt
```

# 실행
- behave를 통해서 실행해준다.

```
 sh run-behave.sh 
```


# 리포트 보기
- 리포트는 allure 리포트를 통해서 본다.
```
sh view-allure-report.sh
```

# 파일구조
<img width="615" alt="image" src="https://github.com/xmlangel/appium_allure/assets/8622992/b46fd515-474f-43a3-904f-dbc74619087b">

# appium_allure
