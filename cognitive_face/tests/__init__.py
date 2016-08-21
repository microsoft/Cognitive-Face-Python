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
        'referring to `config.sample.py` so as to perform the unittests.'
    )

import cognitive_face as CF

from . import util


def setUpModule():
    # pylint: disable=invalid-name
    """Setup for the whole unitests.

    - Set Subscription Key.
    - Setup needed data for unitests.
    """
    CF.Key.set(config.KEY)
    util.DataStore.setup_person_group()
    util.DataStore.setup_face_list()
    util.DataStore.setup_face()


def tearDownModule():
    # pylint: disable=invalid-name
    """TearDown for the whole unittests.

    - Remove all the created persisted data.
    """
    CF.util.clear_face_lists()
    CF.util.clear_person_groups()
