#!/bin/bash

./postgres_check_health.sh
./gunicorn_entrypoint.sh
