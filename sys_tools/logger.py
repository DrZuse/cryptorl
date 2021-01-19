#!/usr/bin/env python
# coding: utf-8
import os
import logging
from logging.handlers import RotatingFileHandler

logs_path = 'logs'

if not os.path.exists(logs_path):
    os.makedirs(logs_path)

logging.basicConfig(
        handlers=[
          RotatingFileHandler(logs_path+'/log', maxBytes=5*1024*1024, backupCount=10), 
          logging.StreamHandler(),
        ], # 5*1024*1024 = 5 MB
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s [%(filename)s.%(process)d.%(thread)d.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')
        
#asctime - время ивента
#levelname - уровень логируемого ивента
#filename - скрипт сгенерировавший ивент
#process - Process ID (if available)
#thread - поток (для мультипоточности)
#funcName - имя функции
#lineno - номер строки
#message - сообщение
        
#logging.warning('Im a warning. Beware!')
#logging.error('your error text goes here')
#logging.info('your info text goes here')
#logging.debug('your debug text goes here')