#!/bin/bash

lat=10.7329078
long=106.6442348


ACCESS_TOKEN=uyhvem7y67bh8uftsn6r

curl -v POST --data \
  "{"latitude":$lat, "longitude":$long  }" \
  https://demo.thingsboard.io/api/v1/$ACCESS_TOKEN/telemetry \
  --header "Content-Type:application/json"
