#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_person_group.py
Description: Unittests for Person Group section of the Cognitive Face API.
"""

import uuid
import unittest

import cognitive_face as CF

from . import util


class TestPersonGroup(unittest.TestCase):
    """Unittests for Person Group section."""

    def test_person_group(self):
        """Unittests for `person_group.create`, `person_group.train`,
        `person_group.update`, `person_group.get_status` and
        `person_group.delete`.
        """
        person_group_id = str(uuid.uuid1())

        res = CF.person_group.create(person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        # Fake a person and a face to satisfy training.
        res = CF.person.create(person_group_id, 'TempPerson')
        person_id = res['personId']
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            util.BASE_URL_IMAGE)
        res = CF.person.add_face(image, person_group_id, person_id)

        res = CF.person_group.train(person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.person_group.update(person_group_id, 'name')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.person_group.get_status(person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.person_group.delete(person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get(self):
        """Unittest for `person_group.get`."""
        res = CF.person_group.get(util.DataStore.person_group_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_lists(self):
        """Unittest for `person_group.lists`."""
        res = CF.person_group.lists()
        print(res)
        self.assertIsInstance(res, list)
        util.wait()
