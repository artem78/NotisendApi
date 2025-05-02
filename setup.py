#!/usr/bin/env python

from distutils.core import setup

setup(
    name="NotisendApi",
    description='Send mails with notisend.ru API',
    version='1.0',
    author='artem78',
    #packages=['ваш пакет'],
    py_modules=['notisend_api'],
    install_requires=['requests'],
    url='https://github.com/artem78/NotisendApi'
)
