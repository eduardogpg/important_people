#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Eduardo Ismael García Pérez'
__contact__ = '@eduardo_gpg'


from flask import Flask

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/', methods = ['GET'])
def index():
	return 'Hello World!'

if __name__ == '__main__':
	app.run()