#!/bin/bash
api_key=CIMK9S8X63QMZDBF
ip_addy=192.168.1.53
port=8080
field1=Weather_Temperature
field2=Temperature_GF_Living
field3=Temperature_FF_Bed
field4=Temperature_GF_Kitchen
field5=Pressure_BMP_GF_Living
field6=Humidity_GF_Kitchen
field7=Weather_Humidity
field8=Humidity_FF_Bed
f1=`curl -s http://192.168.1.53:8080/rest/items/Weather_Temperature/state | cut -c 1-5`
f2=`curl -s http://192.168.1.53:8080/rest/items/Temperature_GF_Living/state | cut -c 1-5`
f3=`curl -s http://192.168.1.53:8080/rest/items/Temperature_FF_Bed/state | cut -c 1-5`
f4=`curl -s http://192.168.1.53:8080/rest/items/Temperature_GF_Kitchen/state | cut -c 1-5`
f5=`curl -s http://192.168.1.53:8080/rest/items/Pressure_BMP_GF_Living/state | cut -c 1-7`
f6=`curl -s http://192.168.1.53:8080/rest/items/Humidity_GF_Kitchen/state | cut -c 1-5`
f7=`curl -s http://192.168.1.53:8080/rest/items/Weather_Humidity/state | cut -c 1-5`
f8=`curl -s http://192.168.1.53:8080/rest/items/Humidity_FF_Bed/state | cut -c 1-5`
d=`date`
printf "%s = " "$d"; curl -k --data  "api_key=$api_key&field1=$f1&field2=$f2&field3=$f3&field4=$f4&field5=$f5&field6=$f6&field7=$f7&field8=$f8" https://api.thingspeak.com/update
