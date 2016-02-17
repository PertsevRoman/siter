#!/usr/bin/python3
import os

def check_init(conf_storage):
    """Проверка конфигурации
    :param conf_storage Словарь для проверки
    """
    names = ['third_name']

    for name in names:
        if name in list(conf_storage.keys()):
            raise KeyError('You can\'t assign key %s in conf file' % name)


def init(conf_storage):
    """Конфигурация
    :param conf_storage Словарь для хранения
    """
    f = open('options.conf')
    for line in f.read().splitlines():
        arr = line.split(' ')

        conf_storage[arr[0]] = arr[1]

    check_init(conf_storage)

def create_domain(stor):
    stor['root_dir'] = '%s/panel.%s.%s/sites/%s' % (stor['base_root'], stor['dom_name'], stor['zone'], stor['site_name'])
    stor['acc_log'] = '%s/%s/%s-acc.log' % (stor['logs_dir'], stor['dom_name'], stor['site_name'])
    stor['err_log'] = '%s/%s/%s-err.log' % (stor['logs_dir'], stor['dom_name'], stor['site_name'])

    f = open('template-apache')
    out = open('%s/%s-%s.conf' % (stor['out_dir'], stor['site_name'], stor['dom_name']), 'w')

    for line in f.read().splitlines():
        va = line
        for key in list(stor.keys()):
            va = va.replace('$%s$' % key, stor[key])
        out.write(va)
        out.write(os.linesep)

    f.close()
    out.close()


def main():
    """Точка входа"""
    stor = {}

    init(stor)

    from_dirs = input('Use folders list? ') in ('y', 'yes')
    dirs_location = ''

    if from_dirs:
        dirs_location = input('Using dir list: ')
    else:
        stor['site_name'] = input('Site name: ')

    stor['dom_name'] = input('Domain name: ')
    stor['zone'] = input('Zone [ru]: ')

    stor['out_dir'] = input('Out dir [/etc/nginx/sites-available]: ')

    if stor['zone'] == '':
        stor['zone'] = 'ru'

    if stor['out_dir'] == '':
        stor['out_dir'] = '/etc/nginx/sites-available'
    else:
        if not os.path.exists(stor['out_dir']) or not os.path.isdir(stor['out_dir']):
            raise Exception('Директория не существует или это не директория')

    if from_dirs:
        for name in os.listdir(dirs_location):
            stor['site_name'] = name
            create_domain(stor)
    else:
        create_domain(stor)

if __name__ == '__main__':
    main()
