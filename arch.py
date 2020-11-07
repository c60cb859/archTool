#!/usr/bin/env python

import argparse
import linuxConfigs
from targets import LocalHost


CHOICES = ['arch', 'linuxConfigs', 'tmux', 'nvim', 'awesome']


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
    target = LocalHost()
    installer = get_configurator(program, target)
    installer.install()


def update():
    target = LocalHost()
    for program in CHOICES:
        configurator = get_configurator(program, target)
        configurator.update()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--install',
                        help='Install and configure program',
                        choices=CHOICES)
    parser.add_argument('-u', '--update',
                        help='Update installed programs',
                        action='store_true')

    args = parser.parse_args()

    if args.install:
        install(args.install)
    elif args.update:
        update()
