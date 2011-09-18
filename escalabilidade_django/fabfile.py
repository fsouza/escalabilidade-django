# -*- coding: utf-8 -*-
from fabric.api import cd, env, local, put, roles, run

env.user = 'xikin'
env.presentation_name = 'escalabilidade-django'
env.url = 'http://p.souza.cc/%(presentation_name)s' % env
env.presentations_directory = '/home/xikin/p.souza.cc'
env.remote_directory = '%(presentations_directory)/%(presentation_name)s' % env
env.roledefs = {
    'remote' : ['p.souza.cc',],
}

def clean():
    local('git clean -dfX')

def build():
    clean()
    local('landslide escalabilidade.cfg')

def open():
    local('open index.html')

def package():
    build()
    local('tar -czvf /tmp/escalabilidade.tar.gz img index.html theme')

@roles('remote')
def deploy():
    package()

    run('mkdir -p %s' % env.remote_directory)
    put('/tmp/escalabilidade.tar.gz', env.remote_directory)

    with cd(env.remote_directory):
        run('tar -xvzf escalabilidade.tar.gz')
        run('rm -f escalabilidade.tar.gz')

    print 'Deployed, check this out: %(url)s' % env

@roles('remote')
def undeploy():
    with cd(env.presentations_directory):
        run('rm -rf %(presentation_name)s' % env)

    print 'Undeployed, the presentation is not live anymore.'
