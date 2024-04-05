kill -9 $(ps -ef | grep "appium-webdriveragent" |grep -v "grep" | awk '{print $2}')
ps -ef | grep "appium-webdriveragent" |grep -v "grep" | awk '{print $2}'
