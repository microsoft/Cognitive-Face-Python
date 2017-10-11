#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: __init__.py
Description: Unittests for Python SDK of the Cognitive Face API.
"""

try:
    from . import config
except ImportError:
    raise Exception(
        'Please setup unittest configuration `config.py` properly by '
        'referring to `config.sample.py` so as to perform the unittests.')

import cognitive_face as CF

from . import util


def setUpModule():
    # pylint: disable=invalid-name
    """Setup for the whole unitests.

    - Set Subscription Key.
    - Set Base URL.
    - Setup needed data for unitests.
    """
    print("setUpModule Begin.")
    CF.Key.set(config.KEY)
    CF.BaseUrl.set(config.BASE_URL)
    util.DataStore.setup_face()
    util.DataStore.setup_face_list()
    util.DataStore.setup_large_face_list()
    util.DataStore.setup_large_person_group()
    util.DataStore.setup_person_group()
    print("setUpModule End.")


def tearDownModule():
    # pylint: disable=invalid-name
    """TearDown for the whole unittests.

    - Remove all the created persisted data.
    """
    print("tearDownModule Begin.")
    CF.util.clear_face_lists()
    CF.util.clear_person_groups()
    CF.util.clear_large_face_lists()
    CF.util.clear_large_person_groups()
    print("tearDownModule End.")
