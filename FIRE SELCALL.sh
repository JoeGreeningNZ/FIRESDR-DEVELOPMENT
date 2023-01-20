#!/bin/bash
echo "FIRESDR Created By Joe Greening"
for i in {1..3}
do
	{
	ps -ef | grep rtl_fm | grep -v grep | awk '{print $2}' | xargs kill
	ps -ef | grep multimon-ng | grep -v grep | awk '{print $2}' | xargs kill
	ps -ef | grep python3 | grep -v grep | awk '{print $2}' | xargs kill
	} &> /dev/null & echo "Cleaning up previous sessions... ($i/3)"
done
sleep 5
/usr/bin/rtl_fm -f 148500000 -s 22050 | multimon-ng -t raw -a DTMF -e -f alpha /dev/stdin >firecom.txt

