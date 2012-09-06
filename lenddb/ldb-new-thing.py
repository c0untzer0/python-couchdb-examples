#!/usr/bin/env python

# This program is used to create a new empty database
#
# Synopsis
#   ./new-thing.py name [key1=val2 [key2=val2 [...]]]
#

from couchdbkit import Database
from couchdbkit.exceptions import ResourceNotFound

from models import Thing


def create_item(username, itemname, kwargs):
    thing = Thing(owner=username, name=itemname)

    for key, value in kwargs.items():
        thing.key = value

    thing.save()

    print thing, 'saved with _id', thing._id


if __name__ == '__main__':
    import sys
    from settings import USERNAME

    kwargs = dict( arg.split('=') for arg in sys.argv[2:] )

    create_item(USERNAME, sys.argv[1], kwargs)
