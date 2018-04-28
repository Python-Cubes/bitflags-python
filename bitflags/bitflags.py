#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   bitflags.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from six import (
    add_metaclass,
)


class BitFlagsMeta(type):

    names = (
    )

    def __new__(cls, name, bases, attrs):
        cls = super(BitFlagsMeta, cls).__new__(cls, name, bases, attrs)

        def _create_property(mask_name, return_bool=True):
            property_getter = lambda self: getattr(self, mask_name) & self.bits

            if return_bool:
                return property(lambda self: bool(property_getter(self)))

            return property(property_getter)

        mask_names = []
        property_names = []
        for index, name in enumerate(getattr(cls, 'names', ())):
            bits = 1 << index

            mask_name = name.upper()
            mask_names.append(mask_name)
            setattr(cls, mask_name, cls(bits=bits))

            property_name = name.lower()
            property_names.append(property_name)
            setattr(cls, property_name, _create_property(
                mask_name=mask_name,
                return_bool=False,
            ))

            bool_name = 'is_' + property_name
            setattr(cls, bool_name, _create_property(
                mask_name=mask_name,
                return_bool=True,
            ))

        cls.MASK_NAMES = mask_names
        cls.PROPERTY_NAMES = property_names

        return cls


@add_metaclass(BitFlagsMeta)
class BitFlags(object):

    def __init__(self, bits):
        self.bits = bits

    @property
    def flags(self):
        return [
            property_name
            for property_name in self.PROPERTY_NAMES
            if getattr(self, property_name)
        ]

    def __bool__(self):
        return self.bits != 0

    def __nonzero__(self):
        return self.bits != 0

    def __or__(self, other):
        if isinstance(other, BitFlags):
            other = other.bits

        bits = self.bits | other

        return self.__class__(bits=bits)

    def __and__(self, other):
        if isinstance(other, BitFlags):
            other = other.bits

        bits = self.bits & other

        return self.__class__(bits=bits)

    def __xor__(self, other):
        if isinstance(other, BitFlags):
            other = other.bits

        bits = self.bits ^ other

        return self.__class__(bits=bits)

    def __repr__(self):
        return '%s(bits=%s)' % (self.__class__.__name__, self.bits)
