# -*- coding: utf-8 -*-
from fabric.api import local

def clean():
    local('git clean -dfX')

def generate():
    clean()
    local('landslide escalabilidade.cfg')
    local('open escalabilidade.html')
