#!/bin/bash

print 'uvicorn main:app --host 0.0.0.0 --port 8448 --reload'

uvicorn main:app --host 0.0.0.0 --port 8448 --reload

