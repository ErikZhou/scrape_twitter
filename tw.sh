#!/bin/bash
#先载入环境变量
source /etc/profile
#其他代码不变

processcount=$(pgrep tw.py|wc -l)
cd $(cd $(dirname $0) && pwd)
if [[ 0 -eq $processcount ]]
then
        echo "[ $(date) ] : tw.py is down, start it!" | tee -ai ./checkprocess.log
        #bash ./start.sh #这里是项目的重启脚本
        python3 /home/rslsync/vps/scrape_twitter/tw.py ErickZhou
else
        echo tw.py is OK!
fi
