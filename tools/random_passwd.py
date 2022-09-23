#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：deploy-compose
@File    ：random_passwd.py.py
@Author  ：于川
@Date    ：2022/8/17 18:10
'''

# params:
# - 1: password length
# - 2. num of password type
# how to use:
# - ./tools/random_passwd.py 8
# - ./tools/random_passwd.py 18 3

import sys
import random


def get_random_password(passwd_length, type_num=4):
    pwd = ""
    pass_dict = {
        0: "0123456789",
        1: "abcdefghijklmnopqrstuvwxyz",
        2: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        3: "!@#$%^*()_+-="
    }
    target_types = random.sample(pass_dict.keys(), type_num)
    # print("contain type: {}".format(target_types))

    for i in target_types:
        pwd += random.choice(pass_dict[i])

    for i in range(0, passwd_length - len(pwd)):
        pwd += random.choice(pass_dict[random.choice(target_types)])

    return ''.join(random.sample(pwd, len(pwd)))


if __name__ == "__main__":
    params = sys.argv[1:]
    if len(params) == 0:
        print(get_random_password(8))
    elif len(params) == 1:
        print(get_random_password(int(params[0])))
    else:
        print(get_random_password(int(params[0]), int(params[1])))
