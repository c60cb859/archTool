#!/usr/bin/env python

import argparse
import gitConfigs
from targets import LocalHost


CHOICES = ['arch', 'linuxConfigs', 'tmux', 'nvim', 'awesome', 'ssh']


def get_configurator(program, target):
    if program == 'linuxConfigs':
        configurator = gitConfigs.LinuxConfig(target)
    elif program == 'tmux':
        configurator = gitConfigs.TmuxConfig(target)
    elif program == 'nvim':
        configurator = gitConfigs.NeoVimConfig(target)
    elif program == 'awesome':
        configurator = gitConfigs.AwesomeConfig(target)
    elif program == 'arch':
        configurator = gitConfigs.ArchConfig(target)
    elif program == 'ssh':
        configurator = gitConfigs.SecureSSHConfig(target)

    return configurator


def install(program):
    print('=' * 10 + ' Installing ' + program + ' ' + '=' * 10)
    target = LocalHost()
    installer = get_configurator(program, target)
    installer.install()
    print('=' * 30)


def install_all_noui():
    noui = ['arch', 'linuxConfigs', 'tmux', 'nvim', 'ssh']
    for program in noui:
        install(program)


def update():
    target = LocalHost()
    for program in CHOICES:
        print('=' * 10 + ' Updating ' + program + ' ' + '=' * 10)
        configurator = get_configurator(program, target)
        configurator.update()
        print('=' * 30)


def status():
    target = LocalHost()
    print('=' * 10 + ' Status ' + '=' * 10)
    for program in CHOICES:
        configurator = get_configurator(program, target)
        if configurator.status():
            print(program + ' is installed')
        else:
            print(program + ' not installed')
        print('=' * 30)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--install',
                        help='Install and configure program',
                        choices=CHOICES)

    parser.add_argument('--install_all_noui',
                        help='Install all server programs program',
                        action='store_true')

    parser.add_argument('-u', '--update',
                        help='Update installed programs',
                        action='store_true')

    parser.add_argument('-s', '--status',
                        help='See status of installed programs',
                        action='store_true')

    args = parser.parse_args()

    if args.install:
        install(args.install)
    elif args.install_all_noui:
        install_all_noui()
    elif args.update:
        update()
    elif args.status:
        status()
