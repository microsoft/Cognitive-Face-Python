#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_face.py
Description: Unittests for Face section of the Cognitive Face API.
"""

import unittest

import cognitive_face as CF

from . import util


class TestFace(unittest.TestCase):
    """Unittests for Face section."""

    def test_detect(self):
        """Unittest for `face.detect`."""
        image = '{}detection1.jpg'.format(util.BASE_URL_IMAGE)
        res = CF.face.detect(image)
        print(res)
        self.assertIsInstance(res, list)
        util.wait()

    def test_find_similars(self):
        """Unittest for `face.find_similars`."""
        res = CF.face.find_similars(
            util.DataStore.face_id,
            face_ids=util.DataStore.face_ids
        )
        print(res)
        self.assertIsInstance(res, list)
        util.wait()

    def test_group(self):
        """Unittest for `face.group`."""
        temp_face_ids = util.DataStore.face_ids
        temp_face_ids.append(util.DataStore.face_id)
        temp_face_ids.append(util.DataStore.another_face_id)
        res = CF.face.group(temp_face_ids)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_identify(self):
        """Unittest for `face.identify`."""
        CF.util.wait_for_training(util.DataStore.person_group_id)

        res = CF.face.identify(
            util.DataStore.face_ids,
            util.DataStore.person_group_id,
        )
        print(res)
        self.assertIsInstance(res, list)
        util.wait()

    def test_verify(self):
        """Unittest for `face.verify`."""
        res = CF.face.verify(
            util.DataStore.face_id,
            person_group_id=util.DataStore.person_group_id,
            person_id=util.DataStore.person_id['Dad'],
        )
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

if __name__ == '__main__':
    unittest.main()
