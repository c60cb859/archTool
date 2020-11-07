#!/usr/bin/env python

import os


class GitConfig:
    def __init__(self, target):
        self.target = target
        self.git = ''
        self.home_path = ''
        self.location = ''

    def git_repo_exists(self):
        if os.path.isdir(self.location + '.git'):
            return True
        else:
            return False

    def get_git_repo(self):
        if self.git_repo_exists():
            print('Pulling form git')
            self.target.run_cmd('cd ' + self.location + '; git pull -q')
        else:
            print('Cloning git repo')
            self.target.run_cmd('git clone ' + self.git + ' ' + self.location)

    def install_dependencies(self):
        cmd = 'sudo pacman -S --needed --quiet --noconfirm '
        with open(self.location + 'dependencies', 'r') as deps:
            cmd += ''.join(deps.readlines()).replace('\n', ' ')
        cmd += ' 2>/dev/null'
        print('Installing dependencies')
        self.target.run_cmd(cmd)

    def setup_config(self):
        cmd = self.location + 'setupConfig.sh'
        print('Setting up configurations')
        self.target.run_cmd(cmd)

    def update_config(self):
        cmd = self.location + 'updateConfig.sh'
        print('Updateing configurations')
        self.target.run_cmd(cmd)

    def install(self):
        self.get_git_repo()
        self.install_dependencies()
        self.setup_config()

    def update(self):
        if self.git_repo_exists():
            self.get_git_repo()
            self.install_dependencies()
            self.setup_config()

    def status(self):
        if self.git_repo_exists():
            return True
        else:
            return False


class ArchConfig(GitConfig):
    def __init__(self, target):
        self.target = target
        self.git = 'https://github.com/c60cb859/archTool.git'
        self.home_path = os.path.expanduser('~')
        self.location = self.home_path + '/.config/archTool/'


class LinuxConfig(GitConfig):
    def __init__(self, target):
        self.target = target
        self.git = 'https://github.com/c60cb859/.linuxConfigs.git'
        self.home_path = os.path.expanduser('~')
        self.location = self.home_path + '/.config/.linuxConfigs/'


class TmuxConfig(GitConfig):
    def __init__(self, target):
        self.target = target
        self.git = 'https://github.com/c60cb859/tmux.git'
        self.home_path = os.path.expanduser('~')
        self.location = self.home_path + '/.config/tmux/'


class NeoVimConfig(GitConfig):
    def __init__(self, target):
        self.target = target
        self.git = 'https://github.com/c60cb859/nvim.git'
        self.home_path = os.path.expanduser('~')
        self.location = self.home_path + '/.config/nvim/'


class AwesomeConfig(GitConfig):
    def __init__(self, target):
        self.target = target
        self.git = 'https://github.com/c60cb859/awesomewm.git'
        self.home_path = os.path.expanduser('~')
        self.location = self.home_path + '/.config/awesomewm/'


class SecureSSHConfig(GitConfig):
    def __init__(self, target):
        self.target = target
        self.git = 'https://github.com/c60cb859/secureSSH.git'
        self.home_path = os.path.expanduser('~')
        self.location = self.home_path + '/.config/secureSSH/'

    def update(self):
        if self.git_repo_exists():
            self.get_git_repo()
            self.update_config()
