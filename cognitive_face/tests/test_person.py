#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_person.py
Description: Unittests for Person section of the Cognitive Face API.
"""

import unittest

import cognitive_face as CF

from . import util


class TestPerson(unittest.TestCase):
    """Unittests for Person section."""

    def test_face(self):
        """Unittests for `person.add_face`, `person.update_face` and
        `person.delete_face`.
        """
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            util.BASE_URL_IMAGE)

        res = CF.person.add_face(image, util.DataStore.person_group_id,
                                 util.DataStore.person_id['Dad'])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        persisted_face_id = res['persistedFaceId']

        res = CF.person.update_face(util.DataStore.person_group_id,
                                    util.DataStore.person_id['Dad'],
                                    persisted_face_id, 'TempUserData')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.person.delete_face(util.DataStore.person_group_id,
                                    util.DataStore.person_id['Dad'],
                                    persisted_face_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_person(self):
        """Unittests for `person.create`, `person.update` and
        `person.delete`.
        """
        res = CF.person.create(util.DataStore.person_group_id, 'TempPerson')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        person_id = res['personId']

        res = CF.person.update(util.DataStore.person_group_id, person_id, 'TP')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.person.delete(util.DataStore.person_group_id, person_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get(self):
        """Unittest for `person.get`."""
        res = CF.person.get(util.DataStore.person_group_id,
                            util.DataStore.person_id['Dad'])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get_face(self):
        """Unittest for `person.get_face`."""
        res = CF.person.get_face(
            util.DataStore.person_group_id, util.DataStore.person_id['Dad'],
            util.DataStore.person_persisted_face_id['Dad'][0])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_lists(self):
        """Unittest for `person.lists`."""
        res = CF.person.lists(util.DataStore.person_group_id)
        print(res)
        self.assertIsInstance(res, list)
        util.wait()
