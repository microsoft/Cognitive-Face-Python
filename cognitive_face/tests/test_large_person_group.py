#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_large_person_group.py
Description: Unittests for Large Person Group section of the Cognitive Face
    API.
"""

import uuid
import unittest

import cognitive_face as CF

from . import util


class TestLargePersonGroup(unittest.TestCase):
    """Unittests for Large Person Group section."""

    def test_large_person_group(self):
        """Unittests for `large_person_group.create`,
        `large_person_group.train`, `large_person_group.update`,
        `large_person_group.get_status` and `large_person_group.delete`.
        """
        large_person_group_id = str(uuid.uuid1())

        res = CF.large_person_group.create(large_person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        # Fake a person and a face to satisfy training.
        res = CF.large_person_group_person.create(large_person_group_id,
                                                  'TempPerson')
        person_id = res['personId']
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            util.BASE_URL_IMAGE)
        res = CF.large_person_group_person_face.add(
            image, large_person_group_id, person_id)

        res = CF.large_person_group.train(large_person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_person_group.update(large_person_group_id, 'name')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_person_group.get_status(large_person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_person_group.delete(large_person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get(self):
        """Unittest for `large_person_group.get`."""
        res = CF.large_person_group.get(util.DataStore.large_person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_list(self):
        """Unittest for `large_person_group.list`."""
        res = CF.large_person_group.list()
        print(res)
        self.assertIsInstance(res, list)
        util.wait()
