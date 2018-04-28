#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   demo.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from bitflags import (
    BitFlags,
)


class IFF(BitFlags):

    names = (
       'UP',
       'BROADCAST',
       'DEBUG',
       'LOOPBACK',
       'POINTOPOINT',
       'NOTRAILERS',
       'RUNNING',
       'NOARP',
       'PROMISC',
       'ALLMULTI',
       'MASTER',
       'SLAVE',
       'MULTICAST',
       'PORTSEL',
       'AUTOMEDIA',
       'DYNAMIC',
       'LOWER_UP',
       'DORMANT',
       'ECHO',
    )

print(IFF.UP)
print(IFF.UP | IFF.BROADCAST)
print('')

iff = IFF(0x1043)
print(iff.flags)
print('')

print(iff.UP)
print(iff.up)
print(iff.is_up)
print('')

print(iff.DEBUG)
print(iff.debug)
print(iff.is_debug)
print('')

iff |= iff.DEBUG
print(iff.DEBUG)
print(iff.debug)
print(iff.is_debug)
print('')
