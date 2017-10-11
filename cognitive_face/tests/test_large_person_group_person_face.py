#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_large_person_group_person_face.py
Description: Unittests for Large Person Group Person Face section of the
    Cognitive Face API.
"""

import unittest

import cognitive_face as CF

from . import util


class TestLargePersonGroupPersonFace(unittest.TestCase):
    """Unittests for Large Person Group Person Face section."""

    def test_face(self):
        """Unittests for `large_person_group_person_face.add`,
        `large_person_group_person_face.update` and
        `large_person_group_person_face.delete`.
        """
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            util.BASE_URL_IMAGE)

        res = CF.large_person_group_person_face.add(
            image, util.DataStore.large_person_group_id,
            util.DataStore.large_person_group_person_id['Dad'])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        persisted_face_id = res['persistedFaceId']

        res = CF.large_person_group_person_face.update(
            util.DataStore.large_person_group_id,
            util.DataStore.large_person_group_person_id['Dad'],
            persisted_face_id, 'TempUserData')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_person_group_person_face.delete(
            util.DataStore.large_person_group_id,
            util.DataStore.large_person_group_person_id['Dad'],
            persisted_face_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get(self):
        """Unittest for `large_person_group_person_face.get`."""
        res = CF.large_person_group_person_face.get(
            util.DataStore.large_person_group_id,
            util.DataStore.large_person_group_person_id['Dad'],
            util.DataStore.large_person_group_person_face_id['Dad'][0])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()
