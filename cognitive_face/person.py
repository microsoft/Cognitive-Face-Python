#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: person.py
Description: Person section of the Cognitive Face API.
"""
from . import util


def add_face(image,
             person_group_id,
             person_id,
             user_data=None,
             target_face=None):
    """Add a representative face to a person for identification. The input face
    is specified as an image with a `target_face` rectangle. It returns a
    `persisted_face_id` representing the added face and this
    `persisted_face_id` will not expire. Note `persisted_face_id` is different
    from `face_id` which represents the detected face by `face.detect`.

    Args:
        image: A URL or a file path or a file-like object represents an image.
        person_group_id: Specifying the person group containing the target
            person.
        person_id: Target person that the face is added to.
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
    url = 'persongroups/{}/persons/{}/persistedFaces'.format(
        person_group_id, person_id)
    headers, data, json = util.parse_image(image)
    params = {
        'userData': user_data,
        'targetFace': target_face,
    }

    return util.request(
        'POST', url, headers=headers, params=params, json=json, data=data)


def create(person_group_id, name, user_data=None):
    """Create a new person in a specified person group. A newly created person
    have no registered face, you can call `person.add` to add faces to the
    person.

    Args:
        person_group_id: Specifying the person group containing the target
            person.
        name: Display name of the target person. The maximum length is 128.
        user_data: Optional parameter. User-specified data about the face list
            for any purpose. The maximum length is 1KB.

    Returns:
        A new `person_id` created.
    """
    url = 'persongroups/{}/persons'.format(person_group_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    return util.request('POST', url, json=json)


def delete(person_group_id, person_id):
    """Delete an existing person from a person group. Persisted face images of
    the person will also be deleted.

    Args:
        person_group_id: Specifying the person group containing the person.
        person_id: The target `person_id` to delete.

    Returns:
        An empty response body.
    """
    url = 'persongroups/{}/persons/{}'.format(person_group_id, person_id)

    return util.request('DELETE', url)


def delete_face(person_group_id, person_id, persisted_face_id):
    """Delete a face from a person. Relative image for the persisted face will
    also be deleted.

    Args:
        person_group_id: Specifying the person group containing the target
            person.
        person_id: Specifying the person that the target persisted face belongs
            to.
        persisted_face_id: The persisted face to remove. This
            `persisted_face_id` is returned from `person.add`.

    Returns:
        An empty response body.
    """
    url = 'persongroups/{}/persons/{}/persistedFaces/{}'.format(
        person_group_id, person_id, persisted_face_id)

    return util.request('DELETE', url)


def get(person_group_id, person_id):
    """Retrieve a person's information, including registered persisted faces,
    `name` and `user_data`.

    Args:
        person_group_id: Specifying the person group containing the target
            person.
        person_id: Specifying the target person.

    Returns:
        The person's information.
    """
    url = 'persongroups/{}/persons/{}'.format(person_group_id, person_id)

    return util.request('GET', url)


def get_face(person_group_id, person_id, persisted_face_id):
    """Retrieve information about a persisted face (specified by
    `persisted_face_ids`, `person_id` and its belonging `person_group_id`).

    Args:
        person_group_id: Specifying the person group containing the target
            person.
        person_id: Specifying the target person that the face belongs to.
        persisted_face_id: The `persisted_face_id` of the target persisted face
            of the person.

    Returns:
        The target persisted face's information (`persisted_face_id` and
        `user_data`).
    """
    url = 'persongroups/{}/persons/{}/persistedFaces/{}'.format(
        person_group_id, person_id, persisted_face_id)

    return util.request('GET', url)


def lists(person_group_id, start=None, top=None):
    """List `top` persons in a person group with `person_id` greater than
    `start`, and retrieve person information (including `person_id`, `name`,
    `user_data` and `persisted_face_ids` of registered faces of the person).

    Args:
        person_group_id: `person_group_id` of the target person group.
        start: List persons from the least `person_id` greater than this.
        top: The number of persons to list, rangeing in [1, 1000]. Default is
            1000;

    Returns:
        An array of person information that belong to the person group.
    """
    url = 'persongroups/{}/persons'.format(person_group_id)
    params = {
        'start': start,
        'top': top,
    }

    return util.request('GET', url, params=params)


def update(person_group_id, person_id, name=None, user_data=None):
    """Update `name` or `user_data` of a person.

    Args:
        person_group_id: Specifying the person group containing the target
            person.
        person_id: `person_id` of the target person.
        name: Target person's display name. Maximum length is 128.
        user_data: User-provided data attached to the person. Maximum length is
            16KB.

    Returns:
        An empty response body.
    """
    url = 'persongroups/{}/persons/{}'.format(person_group_id, person_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    return util.request('PATCH', url, json=json)


def update_face(person_group_id, person_id, persisted_face_id, user_data=None):
    """Update a person persisted face's `user_data` field.

    Args:
        person_group_id: Specifying the person group containing the target
            person.
        person_id: `person_id` of the target person.
        persisted_face_id: `persisted_face_id` of the target face, which is
            persisted and will not expire.
        user_data: Optional parameter. Attach `user_data` to person's
            persisted face. The size limit is 1KB.

    Returns:
        An empty response body.
    """
    url = 'persongroups/{}/persons/{}/persistedFaces/{}'.format(
        person_group_id, person_id, persisted_face_id)
    json = {
        'userData': user_data,
    }

    return util.request('PATCH', url, json=json)
