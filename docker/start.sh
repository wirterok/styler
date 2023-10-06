#!/bin/sh -x

exec uvicorn --factory asgi:run --reload --workers 1 --port 8004