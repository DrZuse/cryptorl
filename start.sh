#!/bin/sh

service mongodb start
cd /home/cryptorl
pip3 install -e .
python3 recorder.py
