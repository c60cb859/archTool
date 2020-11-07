#!/usr/bin/env python

import argparse
import linuxConfigs
from targets import LocalHost


CHOICES = ['arch', 'linuxConfigs', 'tmux', 'nvim', 'awesome', 'ssh']


def get_configurator(program, target):
    if program == 'linuxConfigs':
        configurator = linuxConfigs.LinuxConfig(target)
    elif program == 'tmux':
        configurator = linuxConfigs.TmuxConfig(target)
    elif program == 'nvim':
        configurator = linuxConfigs.NeoVimConfig(target)
    elif program == 'awesome':
        configurator = linuxConfigs.AwesomeConfig(target)
    elif program == 'arch':
        configurator = linuxConfigs.ArchConfig(target)

    return configurator


def install(program):
    print('=' * 10 + ' Installing ' + program)
    target = LocalHost()
    installer = get_configurator(program, target)
    installer.install()
    print('=' * 50)


def update():
    target = LocalHost()
    for program in CHOICES:
        print('=' * 10 + ' Updating ' + program)
        configurator = get_configurator(program, target)
        configurator.update()
        print('=' * 50)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--install',
                        help='Install and configure program',
                        choices=CHOICES)
    parser.add_argument('-u', '--update',
                        help='Update installed programs',
                        action='store_true')
    parser.add_argument('--ssh',
                        help='Configure openSSH',
                        choices=['install', 'update'])

    args = parser.parse_args()

    if args.install:
        install(args.install)
    elif args.update:
        update()
