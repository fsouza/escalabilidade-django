# -*- coding: utf-8 -*-
from fabric.api import cd, lcd, env, local, put, roles, run

env.user = 'xikin'
env.presentation_name = 'escalabilidade-django'
env.url = 'http://p.souza.cc/%(presentation_name)s' % env
env.presentations_directory = '/home/xikin/p.souza.cc'
env.tmp_dir = '/tmp/escalabilidade'
env.remote_directory = '%(presentations_directory)s/%(presentation_name)s' % env
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

def compress():
    local('mkdir -p %s' % env.tmp_dir)
    local('cp -rv * %s' % env.tmp_dir)
    with lcd(env.tmp_dir):
        local('pyminify index.html > index_minified.html')
        local('mv index_minified.html index.html')
        local('java -jar yuicompressor.jar theme/css/screen.css > theme/css/screen-minified.css')
        local('java -jar yuicompressor.jar theme/css/print.css > theme/css/print-minified.css')
        local('java -jar yuicompressor.jar theme/js/slides.js > theme/js/slides-minified.js')
        local('java -jar yuicompressor.jar theme/js/init.ga.js >> theme/js/slides-minified.js')
        local('sed -i old "s/screen\.css/screen-minified.css/g" index.html')
        local('sed -i old "s/print\.css/print-minified.css/g" index.html')
        local('sed -i old "s/slides\.js/slides-minified.js/g" index.html')

def package():
    build()
    compress()
    with lcd(env.tmp_dir):
        local('tar -czvf /tmp/escalabilidade.tar.gz img index.html theme')

@roles('remote')
def deploy():
    package()

    run('mkdir -p %s' % env.remote_directory)
    put('/tmp/escalabilidade.tar.gz', env.remote_directory)

    with cd(env.remote_directory):
        run('tar -xvzf escalabilidade.tar.gz')
        run('rm -f escalabilidade.tar.gz')


    local('rm -rf /tmp/escalabilidade*')
    print 'Deployed, check this out: %(url)s' % env

@roles('remote')
def undeploy():
    with cd(env.presentations_directory):
        run('rm -rf %(presentation_name)s' % env)

    print 'Undeployed, the presentation is not live anymore.'
