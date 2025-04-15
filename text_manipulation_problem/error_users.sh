#!/bin/bash


LOG_FILE="webserver.log"

if [[ ! -f "$LOG_FILE" ]]; then
  echo "Log file $LOG_FILE not found!"
  exit 1
fi

grep "ERROR" "$LOG_FILE" | awk '{for(i=1;i<=NF;i++){if($i ~ /^User:/){user=$i}; if($i ~ /^IP:/){ip=$i}} print user, ip}' | sort | uniq

