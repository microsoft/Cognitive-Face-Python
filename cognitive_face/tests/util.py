#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: config.sample.py
Description: Unittest shared utilities for Python SDK of the Cognitive Face
    API.
"""

import time
import uuid

import cognitive_face as CF

from . import config

# Base URL of online images.
BASE_URL_IMAGE = ('https://raw.githubusercontent.com/'
                  'Microsoft/Cognitive-Face-Windows/master/Data/')
# Notification of wait.
MSG_WAIT = 'Wait for {} seconds so as to avoid exceeding free quote.'


def wait():
    """Wait for some interval to avoid exceeding quote."""
    print(MSG_WAIT.format(config.TIME_SLEEP))
    time.sleep(config.TIME_SLEEP)


class DataStore(object):
    """Store the needed data for unittests."""

    @classmethod
    def setup_face(cls):
        """Setup Face related data."""
        image = '{}PersonGroup/Family1-Dad/Family1-Dad3.jpg'.format(
            BASE_URL_IMAGE)
        res = CF.face.detect(image)
        print('[face_id] res: {}'.format(res))
        cls.face_id = res[0]['faceId']
        print('[face_id]: {}'.format(cls.face_id))
        wait()

        image = '{}PersonGroup/Family1-Mom/Family1-Mom3.jpg'.format(
            BASE_URL_IMAGE)
        res = CF.face.detect(image)
        print('[another_face_id] res: {}'.format(res))
        cls.another_face_id = res[0]['faceId']
        print('[another_face_id]: {}'.format(cls.another_face_id))
        wait()

        image = '{}identification1.jpg'.format(BASE_URL_IMAGE)
        res = CF.face.detect(image)
        cls.face_ids = []
        print('[face_ids] res: {}'.format(res))
        for face in res:
            cls.face_ids.append(face['faceId'])
        print('[face_ids]: {}'.format(cls.face_ids))
        wait()

    @classmethod
    def setup_face_list(cls):
        """Setup Face List related data."""
        cls.face_list_id = str(uuid.uuid1())
        res = CF.face_list.create(cls.face_list_id)
        print('[face_list_id] res: {}'.format(res))
        print('[face_list_id]: {}'.format(cls.face_list_id))
        wait()

        cls.face_persisted_face_id = {}

        for name in ['Dad', 'Daughter', 'Mom', 'Son']:
            cls.face_persisted_face_id[name] = []
            for idx in range(1, 3):
                image = '{}PersonGroup/Family1-{}/Family1-{}{}.jpg'.format(
                    BASE_URL_IMAGE, name, name, idx)

                res = CF.face_list.add_face(image, cls.face_list_id)
                cls.face_persisted_face_id[name].append(res['persistedFaceId'])
                print('[face_persisted_face_id.{}.{}] res: {}'.format(
                    name, idx, res))
                print('[face_persisted_face_id.{}]: {}'.format(
                    name, cls.face_persisted_face_id[name]))
                wait()

    @classmethod
    def setup_person_group(cls):
        """Setup Person and Person Group related data."""
        cls.person_group_id = str(uuid.uuid1())
        res = CF.person_group.create(cls.person_group_id)
        print('[person_group_id] res: {}'.format(res))
        print('[person_group_id]: {}'.format(cls.person_group_id))
        wait()

        cls.person_id = {}
        cls.person_persisted_face_id = {}

        for name in ['Dad', 'Daughter', 'Mom', 'Son']:
            res = CF.person.create(cls.person_group_id, name)
            cls.person_id[name] = res['personId']
            print('[person_id.{}] res: {}'.format(name, res))
            print('[person_id.{}]: {}'.format(name, cls.person_id[name]))
            wait()

            cls.person_persisted_face_id[name] = []
            for idx in range(1, 3):
                image = '{}PersonGroup/Family1-{}/Family1-{}{}.jpg'.format(
                    BASE_URL_IMAGE, name, name, idx)

                res = CF.person.add_face(image, cls.person_group_id,
                                         cls.person_id[name])
                cls.person_persisted_face_id[name].append(
                    res['persistedFaceId'])
                print('[person_persisted_face_id.{}.{}] res: {}'.format(
                    name, idx, res))
                print('[person_persisted_face_id.{}]: {}'.format(
                    name, cls.person_persisted_face_id[name]))
                wait()

        res = CF.person_group.train(cls.person_group_id)
        print('[person_group.train]res: {}', res)
        wait()

    @classmethod
    def setup_large_face_list(cls):
        """Setup Large Face List related data."""
        cls.large_face_list_id = str(uuid.uuid1())
        res = CF.large_face_list.create(cls.large_face_list_id)
        print('[large_face_list_id] res: {}'.format(res))
        print('[large_face_list_id]: {}'.format(cls.large_face_list_id))
        wait()

        cls.large_face_list_face_id = {}

        for name in ['Dad', 'Daughter', 'Mom', 'Son']:
            cls.large_face_list_face_id[name] = []
            for idx in range(1, 3):
                image = '{}PersonGroup/Family1-{}/Family1-{}{}.jpg'.format(
                    BASE_URL_IMAGE, name, name, idx)

                res = CF.large_face_list_face.add(image,
                                                  cls.large_face_list_id)
                cls.large_face_list_face_id[name].append(
                    res['persistedFaceId'])
                print('[large_face_list_face_id.{}.{}] res: {}'.format(
                    name, idx, res))
                print('[large_face_list_face_id.{}]: {}'.format(
                    name, cls.large_face_list_face_id[name]))
                wait()

        res = CF.large_face_list.train(cls.large_face_list_id)
        print('[large_face_list.train]res: {}', res)
        wait()

    @classmethod
    def setup_large_person_group(cls):
        """Setup Large Person Group related data."""
        cls.large_person_group_id = str(uuid.uuid1())
        res = CF.large_person_group.create(cls.large_person_group_id)
        print('[large_person_group_id] res: {}'.format(res))
        print('[large_person_group_id]: {}'.format(cls.large_person_group_id))
        wait()

        cls.large_person_group_person_id = {}
        cls.large_person_group_person_face_id = {}

        for name in ['Dad', 'Daughter', 'Mom', 'Son']:
            res = CF.large_person_group_person.create(
                cls.large_person_group_id, name)
            cls.large_person_group_person_id[name] = res['personId']
            print(
                '[large_person_group_person_id.{}] res: {}'.format(name, res))
            print('[large_person_group_person_id.{}]: {}'.format(
                name, cls.large_person_group_person_id[name]))
            wait()

            cls.large_person_group_person_face_id[name] = []
            for idx in range(1, 3):
                image = '{}PersonGroup/Family1-{}/Family1-{}{}.jpg'.format(
                    BASE_URL_IMAGE, name, name, idx)

                res = CF.large_person_group_person_face.add(
                    image, cls.large_person_group_id,
                    cls.large_person_group_person_id[name])
                cls.large_person_group_person_face_id[name].append(
                    res['persistedFaceId'])
                print('[large_person_group_person_face_id.{}.{}] res: {}'.
                      format(name, idx, res))
                print('[large_person_group_person_face_id.{}]: {}'.format(
                    name, cls.large_person_group_person_face_id[name]))
                wait()

        res = CF.large_person_group.train(cls.large_person_group_id)
        print('[large_person_group.train]res: {}', res)
        wait()
