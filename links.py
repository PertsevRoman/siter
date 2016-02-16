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

    f = open('out', 'w')

    w = ['%s %s.%s.%s' % (serv_name, name, domain, zone) for name in os.listdir(dirs)]

    for dom in w:
        f.write(dom)

    f.close()

if __name__ == '__main__':
    main()