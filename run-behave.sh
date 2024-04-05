#!/bin/bash
LOCAL_PATH=$(pwd)

number=1

if [ $# -eq 0 ]; then
  repeat_count=1
else
  repeat_count="$1"
fi

while [ $number -le $repeat_count ]
do
  echo "Number: ${number}/$repeat_count"
  ((number++))
  behave  -f  allure_behave.formatter:AllureFormatter -o $LOCAL_PATH/reports/allureReports
done
sh view-allure-report.sh