#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_large_face_list.py
Description: Unittests for Large Face List section of the Cognitive Face API.
"""

import uuid
import unittest

import cognitive_face as CF

from . import util


class TestFaceList(unittest.TestCase):
    """Unittests for Large Face List section."""

    def test_large_face_list(self):
        """Unittests for `large_face_list.create`, `large_face_list.train`,
        `large_face_list.update`, large_face_list.get_status` and
        `large_face_list.delete`.
        """
        large_face_list_id = str(uuid.uuid1())

        res = CF.large_face_list.create(large_face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        # Fake a face to satisfy training.
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            util.BASE_URL_IMAGE)
        res = CF.large_face_list_face.add(image, large_face_list_id)

        res = CF.large_face_list.train(large_face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_face_list.update(large_face_list_id, 'test')
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_face_list.get_status(large_face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

        res = CF.large_face_list.delete(large_face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_get(self):
        """Unittest for `large_face_list.get`."""
        res = CF.large_face_list.get(util.DataStore.large_face_list_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_list(self):
        """Unittest for `large_face_list.list`."""
        res = CF.large_face_list.list()
        print(res)
        self.assertIsInstance(res, list)
        util.wait()
