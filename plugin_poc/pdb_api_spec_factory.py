# -*- coding: utf-8 -*-

""" This module allows PDB-SERVICES to discover the path to the API spec (.swagger.yaml )
"""
from os import path


def get_api_spec_fpath():
    my_path = path.abspath(__file__)
    my_dir = path.dirname(my_path)
    return path.join(my_dir, 'plugin_api.swagger.yaml')
