#!/usr/bin/python3
import os


def main():
    serv_name = input('Serv name [91.203.194.99]: ')
    domain = input('Domain name: ')
    zone = input('Zone [ru]: ')

    if serv_name == '':
        serv_name = '91.203.194.99'

    if zone == '':
        zone = 'ru'

    dirs = input('Dirs path: ')

    print('%s %s' % (serv_name, ' '.join(['%s.%s.%s' % (name, domain, zone) for name in os.listdir(dirs)])))

if __name__ == '__main__':
    main()