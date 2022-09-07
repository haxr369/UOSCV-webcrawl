#!/usr/bin/env python
# coding: utf-8

from helloflask import app

app.run(host="0.0.0.0") #127.0.0.1(=localhost)


#lazy loading은 처음부터 모든 것을 올리지 않겠다 차근차근~
#현재 5000포트 사용중... but 나중에 포트번호 상관 없이 접근하려면 80으로 만들어야함

#새로운 버전

