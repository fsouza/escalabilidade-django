# -*- coding: utf-8 -*-
from fabric.api import local

def clean():
    local('git clean -dfX')

def build():
    clean()
    local('landslide escalabilidade.cfg')

def open():
    local('open escalabilidade.html')
