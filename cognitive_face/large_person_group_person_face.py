#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: large_person_group_person_face.py
Description: Large Person Group Person Face section of the Cognitive Face API.
"""
from . import util


def add(image,
        large_person_group_id,
        person_id,
        user_data=None,
        target_face=None):
    """Add a representative face to a person for identification. The input face
    is specified as an image with a `target_face` rectangle. It returns a
    `persisted_face_id` representing the added face and this
    `persisted_face_id` will not expire.

    Args:
        image: A URL or a file path or a file-like object represents an image.
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        user_data: Optional parameter. User-specified data about the face list
            for any purpose. The maximum length is 1KB.
        target_face: Optional parameter. A face rectangle to specify the target
            face to be added into the face list, in the format of
            "left,top,width,height". E.g. "10,10,100,100". If there are more
            than one faces in the image, `target_face` is required to specify
            which face to add. No `target_face` means there is only one face
            detected in the entire image.

    Returns:
        A new `persisted_face_id`.
    """
    url = 'largepersongroups/{}/persons/{}/persistedFaces'.format(
        large_person_group_id, person_id)
    headers, data, json = util.parse_image(image)
    params = {
        'userData': user_data,
        'targetFace': target_face,
    }

    return util.request(
        'POST', url, headers=headers, params=params, json=json, data=data)


def delete(large_person_group_id, person_id, persisted_face_id):
    """Delete a face from a person. Relative image for the persisted face will
    also be deleted.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        persisted_face_id: The persisted face to remove.

    Returns:
        An empty response body.
    """
    url = 'largepersongroups/{}/persons/{}/persistedFaces/{}'.format(
        large_person_group_id, person_id, persisted_face_id)

    return util.request('DELETE', url)


def get(large_person_group_id, person_id, persisted_face_id):
    """Retrieve information about a persisted face (specified by
    `persisted_face_ids`, `person_id` and its belonging
    `large_person_group_id`).

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        persisted_face_id: The `persisted_face_id` of the target persisted face
            of the person.

    Returns:
        The target persisted face's information (`persisted_face_id` and
        `user_data`).
    """
    url = 'largepersongroups/{}/persons/{}/persistedFaces/{}'.format(
        large_person_group_id, person_id, persisted_face_id)

    return util.request('GET', url)


def update(large_person_group_id, person_id, persisted_face_id, user_data):
    """Update a person persisted face's `user_data` field.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        persisted_face_id: The `persisted_face_id` of the target persisted face
            of the person.
        user_data: Attach `user_data` to person's persisted face. The size
            limit is 1KB.

    Returns:
        An empty response body.
    """
    url = 'largepersongroups/{}/persons/{}/persistedFaces/{}'.format(
        large_person_group_id, person_id, persisted_face_id)
    json = {
        'userData': user_data,
    }

    return util.request('PATCH', url, json=json)
