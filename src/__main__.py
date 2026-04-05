'''
copyright 2026 Finn Ossy-Orley

This file is part of FinnFs.

FinnFs is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

FinnFs is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with FinnFs. If not, see <https://www.gnu.org/licenses/>. 
'''

import pyfuse3
import trio
import argparse
import sqlite3
import faulthandler
import errno
import os

faulthandler.enable()

def parse_args():
    default_data_dir: str = os.path.realpath('data/content')
    default_mountpoint: str = os.path.realpath('data/mountpoint')
    default_config: str = os.path.realpath('config/')

    parser = argparse.ArgumentParser(
        prog='FinnFs',
        description='Content addressed, fully versioned file system with tagging functionality built on pyfuse3'
    )
    parser.add_argument(
        '-d', 
        '--data',
        help='File path for parent data directory',
        default=default_data_dir
    )
    parser.add_argument(
        '-m',
        '--mountpoint',
        help='Set the mount point for the fuse file system',
        default=default_mountpoint
    )
    parser.add_argument(
        '-c',
        '--config',
        help='Location of config file',
        default=default_config
    )
    args = parser.parse_args()
    return args

args = parse_args()



