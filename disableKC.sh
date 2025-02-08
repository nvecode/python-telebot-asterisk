#!/bin/bash

mysql -u adminos -h 10.174.0.10 --password=12qwaszxC -D asterisk -e \
'UPDATE `incoming` SET destination = "app-announcement-3,s,1" WHERE extension = "26401";' && \
sshpass -p 'kpAdUAvilIubgpcXFA' ssh -o StrictHostKeyChecking=no root@10.174.0.10 'fwconsole reload' &>/dev/null
