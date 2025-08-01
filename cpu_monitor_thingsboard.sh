#!/bin/bash

cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)

cpuTemp1=$(($cpuTemp0/1000))

cpuTemp2=$(($cpuTemp0/100))

cpuTempM=$(($cpuTemp2 % $cpuTemp1))


echo CPU temp"="$cpuTemp1"."$cpuTempM"'C"

# Get initial CPU stats
cpu_prev=($(awk '/^cpu / {print $2, $3, $4, $5, $6, $7, $8, $9, $10}' /proc/stat))

sleep 1 # Wait for 1 second

# Get current CPU stats
cpu_curr=($(awk '/^cpu / {print $2, $3, $4, $5, $6, $7, $8, $9, $10}' /proc/stat))

# Calculate total and idle CPU time
total_prev=$((${cpu_prev[0]} + ${cpu_prev[1]} + ${cpu_prev[2]} + ${cpu_prev[3]} + ${cpu_prev[4]} + ${cpu_prev[5]} + ${cpu_prev[6]} + ${cpu_prev[7]} + ${cpu_prev[8]}))
idle_prev=${cpu_prev[3]}

total_curr=$((${cpu_curr[0]} + ${cpu_curr[1]} + ${cpu_curr[2]} + ${cpu_curr[3]} + ${cpu_curr[4]} + ${cpu_curr[5]} + ${cpu_curr[6]} + ${cpu_curr[7]} + ${cpu_curr[8]}))
idle_curr=${cpu_curr[3]}

# Calculate CPU usage percentage
cpu_usage=$((100 * (total_curr - total_prev - (idle_curr - idle_prev)) / (total_curr - total_prev)))

echo "CPU Usage: $cpu_usage%"


ACCESS_TOKEN=uyhvem7y67bh8uftsn6r

curl -v POST --data \
  "{"cpu_temperature":$cpuTemp1.$cpuTempM , "cpu_usage":$cpu_usage  }" \
  https://demo.thingsboard.io/api/v1/$ACCESS_TOKEN/telemetry \
  --header "Content-Type:application/json"
