#!/bin/sh

service mongodb start
cd /home/crypto-rl
pip3 install -e .
#python3 recorder.py
