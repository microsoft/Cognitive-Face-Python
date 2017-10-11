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

    def test_find_similars_face_ids(self):
        """Unittest for `face.find_similars` with face ids."""
        res = CF.face.find_similars(
            util.DataStore.face_id, face_ids=util.DataStore.face_ids)
        print(res)
        self.assertIsInstance(res, list)
        util.wait()

    def test_find_similars_face_list(self):
        """Unittest for `face.find_similars` in face list."""
        res = CF.face.find_similars(
            util.DataStore.face_id, face_list_id=util.DataStore.face_list_id)
        print(res)
        self.assertIsInstance(res, list)
        util.wait()

    def test_find_similars_large_face_list(self):
        """Unittest for `face.find_similars` in large face list."""
        CF.util.wait_for_large_face_list_training(
            util.DataStore.large_face_list_id)

        res = CF.face.find_similars(
            util.DataStore.face_id,
            large_face_list_id=util.DataStore.large_face_list_id)
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

    def test_identify_person_group(self):
        """Unittest for `face.identify` in person gorup."""
        CF.util.wait_for_person_group_training(util.DataStore.person_group_id)

        res = CF.face.identify(
            util.DataStore.face_ids,
            person_group_id=util.DataStore.person_group_id)
        print(res)
        self.assertIsInstance(res, list)
        util.wait()

    def test_identify_large_person_group(self):
        """Unittest for `face.identify` in large person gorup."""
        CF.util.wait_for_large_person_group_training(
            util.DataStore.large_person_group_id)

        res = CF.face.identify(
            util.DataStore.face_ids,
            large_person_group_id=util.DataStore.large_person_group_id)
        print(res)
        self.assertIsInstance(res, list)
        util.wait()

    def test_verify_face_ids(self):
        """Unittest for `face.verify` with face ids."""
        res = CF.face.verify(
            util.DataStore.face_id,
            another_face_id=util.DataStore.another_face_id)
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_verify_person_group(self):
        """Unittest for `face.verify` in person group."""
        CF.util.wait_for_person_group_training(util.DataStore.person_group_id)

        res = CF.face.verify(
            util.DataStore.face_id,
            person_group_id=util.DataStore.person_group_id,
            person_id=util.DataStore.person_id['Dad'])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()

    def test_verify_large_person_group(self):
        """Unittest for `face.verify` in large person group."""
        CF.util.wait_for_large_person_group_training(
            util.DataStore.large_person_group_id)

        res = CF.face.verify(
            util.DataStore.face_id,
            large_person_group_id=util.DataStore.large_person_group_id,
            person_id=util.DataStore.large_person_group_person_id['Dad'])
        print(res)
        self.assertIsInstance(res, dict)
        util.wait()


if __name__ == '__main__':
    unittest.main()
