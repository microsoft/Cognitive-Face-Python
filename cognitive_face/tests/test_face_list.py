#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_face_list.py
Description: Unittests for Face List section of the Cognitive Face API.
"""

import uuid
import unittest

import cognitive_face as CF

from . import util


class TestFaceList(unittest.TestCase):
    """Unittests for Face List section."""

    def test_face(self):
        """Unittests for `face_list.add_face` and `face_list.delete_face`."""
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            util.BASE_URL_IMAGE)

        res = CF.face_list.add_face(image, util.DataStore.face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        persisted_face_id = res['persistedFaceId']

        res = CF.face_list.delete_face(util.DataStore.face_list_id,
                                       persisted_face_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_face_list(self):
        """Unittests for `face_list.create`, `face_list.update` and
        `face_list.delete`.
        """
        face_list_id = str(uuid.uuid1())

        res = CF.face_list.create(face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.face_list.update(face_list_id, 'test')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.face_list.delete(face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get(self):
        """Unittest for `face_list.get`."""
        res = CF.face_list.get(util.DataStore.face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_lists(self):
        """Unittest for `face_list.lists`."""
        res = CF.face_list.lists()
        print(res)
        self.assertIsInstance(res, list)
        util.wait()
