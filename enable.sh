#!/bin/bash

asteriskHost=""
loginDB=""
passwordDB=""
loginHost=""
passwordHost=""

mysql -u $loginDB -h $asteriskHost --password=$passwordDB -D asterisk -e \
'UPDATE `incoming` SET destination = "timeconditions,1,1" WHERE extension = "26401";' && \
sshpass -p $passwordHost ssh -o StrictHostKeyChecking=no $loginHost@$asteriskHost 'fwconsole reload' &>/dev/null