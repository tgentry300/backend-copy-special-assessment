#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


import re
import os
import shutil
import commands
import argparse


"""Copy Special exercise
"""


def get_special_paths(dir):
    """returns list of special files meeting parameters"""
    abs_path_list = []
    for _root, _dirs, files in os.walk(dir):
        for file in files:
            abs_path_list.append(os.path.abspath(file))

    regex = re.compile(r'\w+__\w+_.\..+')
    special_files = filter(regex.search, abs_path_list)
    return special_files


def to_dir(new_dir):
    special_files = get_special_paths('./')

    for file in special_files:
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            shutil.copy(file, new_dir)
        else:
            shutil.copy(file, new_dir)


def to_zip(file_name):
    """Takes a file_name from command line and zips all files in
        directory into file_name"""

    command = 'zip -j {} '.format(file_name)
    special_files = get_special_paths('./')

    basenames = [os.path.basename(file) for file in special_files]

    print command + ' '.join(basenames)

    os.system(command + ' '.join(basenames))

    print commands.getoutput(command + ' '.join(basenames))


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    new_dir = args.todir
    zip_file = args.tozip

    if new_dir:
        to_dir(new_dir)

    elif zip_file:
        to_zip(zip_file)

    else:
        print '\n'.join(get_special_paths('./')) + '\n'


if __name__ == "__main__":
    main()
