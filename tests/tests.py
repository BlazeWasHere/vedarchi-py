# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from archi import Archi

archi = Archi()

assert(isinstance(archi.lists(), dict)) 
assert(not archi.lists('should not exist')['list']) # []
assert(not archi.lists('a very long id over 16 chars')['success']) # false
assert('Donation ID not found' in archi.donations('fake'))