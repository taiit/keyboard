#!/bin/bash
# run in 10s, x6 time => report every 1m

DEVICE_TOCKEN=w1q5zw45amq136ofs1eu
URL=http://demo.thingsboard.io/api/v1/$DEVICE_TOCKEN/telemetry

LOG_DIR=/home/dev/work/_log
TEMP_FILE=${LOG_DIR}/_get_cpu_info_temp.txt

touch $TEMP_FILE

CPU_TEMP=`vcgencmd measure_temp | cut -d"=" -f2 | cut -d"'" -f1`

echo ${CPU_TEMP} >> ${TEMP_FILE}

LINE_CNT=`cat ${TEMP_FILE} | wc -l`

if [[ $LINE_CNT -lt 7 ]]; then
    echo "LINE_CNT: $LINE_CNT less than 6 (=7-1)"
else
    CPU_TEMP_ARG=`awk '{s+=$1}END{print "",s/NR}' RS="\n" ${TEMP_FILE}`
    echo ${CPU_TEMP_ARG}
    curl -v -X POST $URL --header Content-Type:application/json --data "{cpu_temperature:${CPU_TEMP_ARG}}"

    # sed -i '1d' ${TEMP_FILE} # remove fist line
    #run again
    echo ${CPU_TEMP_ARG} > ${TEMP_FILE}
fi



