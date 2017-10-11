#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_large_face_list_face.py
Description: Unittests for Large Face List Face section of the Cognitive Face
    API.
"""

import unittest

import cognitive_face as CF

from . import util


class TestFaceList(unittest.TestCase):
    """Unittests for Large Face List Face section."""

    def test_face(self):
        """Unittests for `large_face_list_face.add`,
        `large_face_list_face.update` and `large_face_list_face.delete`."""
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            util.BASE_URL_IMAGE)

        res = CF.large_face_list_face.add(image,
                                          util.DataStore.large_face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        persisted_face_id = res['persistedFaceId']

        res = CF.large_face_list_face.update(util.DataStore.large_face_list_id,
                                             persisted_face_id, "TempUserData")
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_face_list_face.delete(util.DataStore.large_face_list_id,
                                             persisted_face_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get(self):
        """Unittests for `large_face_list_face.get`."""
        res = CF.large_face_list_face.get(
            util.DataStore.large_face_list_id,
            util.DataStore.large_face_list_face_id['Dad'][0])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_list(self):
        """Unittest for `large_face_list_face.list`."""
        res = CF.large_face_list_face.list(util.DataStore.large_face_list_id)
        print(res)
        self.assertIsInstance(res, list)
        util.wait()
