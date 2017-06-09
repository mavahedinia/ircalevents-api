#!/bin/bash
source env/bin/activate
until ./api.py; do
    echo "'api.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
