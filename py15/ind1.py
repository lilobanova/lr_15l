#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def dec_fun(func):
    def sorting(z):
        return sorted(func(z))
    return sorting


@dec_fun
def get_list(z):
    return [int(i) for i in z.split()]


if __name__ == '__main__':
    print(get_list(input('Введите числа через пробел: ')))
