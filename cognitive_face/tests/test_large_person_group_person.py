#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_large_person_group_person.py
Description: Unittests for Large Person Group Person section of the Cognitive
    Face API.
"""

import unittest

import cognitive_face as CF

from . import util


class TestLargePersonGroupPerson(unittest.TestCase):
    """Unittests for Large Person Group Person section."""

    def test_person(self):
        """Unittests for `large_person_group_person.create`,
        `large_person_group_person.update` and
        `large_person_group_person.delete`.
        """
        res = CF.large_person_group_person.create(
            util.DataStore.large_person_group_id, 'TempPerson')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        person_id = res['personId']

        res = CF.large_person_group_person.update(
            util.DataStore.large_person_group_id, person_id, 'TP')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_person_group_person.delete(
            util.DataStore.large_person_group_id, person_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get(self):
        """Unittest for `large_person_group_person.get`."""
        res = CF.large_person_group_person.get(
            util.DataStore.large_person_group_id,
            util.DataStore.large_person_group_person_id['Dad'])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_list(self):
        """Unittest for `large_person_group_person.list`."""
        res = CF.large_person_group_person.list(
            util.DataStore.large_person_group_id)
        print(res)
        self.assertIsInstance(res, list)
        util.wait()
