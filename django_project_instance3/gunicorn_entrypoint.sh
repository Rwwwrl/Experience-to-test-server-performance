#!/bin/bash

# num cores = 2 -> workers = 2 * 2 + 1 = 5
gunicorn --workers 5 --bind 0.0.0.0:$GUNICORN_PORT main.wsgi
