# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from typing import overload

import requests

class Archi(object):
    """
    Simple REST API wrapper of ved.archi

    For documentation -> https://ved.archi/api/
    """

    def __init__(self) -> None:
        self.base = "https://ved.archi/api/"

    @overload
    def lists() -> dict:
        """
        :param: None. Overloaded function

        :return: all lists 

        Example::
                { "success": true, "lists": [
                        {"id": ...},
                        {"name": ...},
                        {"date": ...}
                    ] 
                }
        """
        ...

    @overload
    def lists(id: str) -> dict:
        """
        :param id: id to search for

        :return: dict of the id, returns `[]` if none found

        Example::
                { "success": true, "lists": [
                        {"id": ...},
                        {"list_id": ...},
                        {"list": ...},
                        {"url": ...},
                        {"description": ...},
                        {"date": ...}
                    ] 
                }
        """
        ...

    def lists(self, id: str = None) -> dict:
        if id is None:
            r = requests.get(self.base + 'lists')
        else:
            r = requests.get(self.base + 'list/' + id)

        return r.json()

    @overload
    def posts() -> dict:
        """
        :param: None. Overloaded function

        :return: all posts

        Example::
                { "success": true, "lists": [
                        {"id": ...},
                        {"title": ...},
                        {"date": ...}
                    ] 
                }
        """
        ...

    @overload
    def posts(id: str) -> dict:
        """
        :param id: id to search for

        :return: dict of the id, returns `[]` if none found

        Example::
                { "success": true, "lists": [
                        {"id": ...},
                        {"title": ...},
                        {"content": ...},
                        {"date": ...}
                    ] 
                }
        """
        ...
    
    def posts(self, id: str = None) -> dict:
        if id is None:
            r = requests.get(self.base + 'posts')
        else:
            r = requests.get(self.base + 'post/' + id)

        return r.json()

    @overload
    def donations() -> dict:
        """
        :param: None. Overloaded function

        :return: all donations

        Example::
                { "success": true, "donated": [
                        ...
                    ] 
                }
        """
        ...

    @overload
    def donations(name: str) -> dict:
        """
        :param name: name to search for donation

        :return: dict of the name, returns `"Donation ID not found"` \
            if none found

        Example::
                { "success": true, 
                  "name": ... , 
                  "message": ... ,
                  "amount": ... ,
                  "cryptocurrency": ... ,
                  "date": ..., 
                }
        """
        ...

    def donations(self, name: str = None) -> dict:
        if name is None:
            r = requests.get(self.base + 'donations')
        else:
            r = requests.get(self.base + 'donated/' + id)

        return r.json()