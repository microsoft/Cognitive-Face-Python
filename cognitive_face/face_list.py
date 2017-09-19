#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: face_list.py
Description: Face List section of the Cognitive Face API.
"""
from . import util


def add_face(image, face_list_id, user_data=None, target_face=None):
    """Add a face to a face list.

    The input face is specified as an image with a `target_face` rectangle. It
    returns a `persisted_face_id` representing the added face, and
    `persisted_face_id` will not expire. Note `persisted_face_id` is different
    from `face_id` which represents the detected face by `face.detect`.

    Args:
        image: A URL or a file path or a file-like object represents an image.
        face_list_id: Valid character is letter in lower case or digit or '-'
            or '_', maximum length is 64.
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
    url = 'facelists/{}/persistedFaces'.format(face_list_id)
    headers, data, json = util.parse_image(image)
    params = {
        'userData': user_data,
        'targetFace': target_face,
    }

    return util.request(
        'POST', url, headers=headers, params=params, json=json, data=data)


def create(face_list_id, name=None, user_data=None):
    """Create an empty face list with user-specified `face_list_id`, `name` and
    an optional `user_data`. Up to 64 face lists are allowed to exist in one
    subscription.

    Args:
        face_list_id: Valid character is letter in lower case or digit or '-'
            or '_', maximum length is 64.
        name: Name of the created face list, maximum length is 128.
        user_data: Optional parameter. User-defined data for the face list.
            Length should not exceed 16KB.

    Returns:
        An empty response body.
    """
    name = name or face_list_id
    url = 'facelists/{}'.format(face_list_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    return util.request('PUT', url, json=json)


def delete_face(face_list_id, persisted_face_id):
    """Delete an existing face from a face list (given by a `persisted_face_id`
    and a `face_list_id`). Persisted image related to the face will also be
    deleted.

    Args:
        face_list_id: Valid character is letter in lower case or digit or '-'
            or '_', maximum length is 64.
        persisted_face_id: `persisted_face_id` of an existing face. Valid
            character is letter in lower case or digit or '-' or '_', maximum
            length is 64.

    Returns:
        An empty response body.
    """
    url = 'facelists/{}/persistedFaces/{}'.format(face_list_id,
                                                  persisted_face_id)

    return util.request('DELETE', url)


def delete(face_list_id):
    """Delete an existing face list according to `face_list_id`. Persisted face
    images in the face list will also be deleted.

    Args:
        face_list_id: Valid character is letter in lower case or digit or '-'
            or '_', maximum length is 64.

    Returns:
        An empty response body.
    """
    url = 'facelists/{}'.format(face_list_id)

    return util.request('DELETE', url)


def get(face_list_id):
    """Retrieve a face list's information, including `face_list_id`, `name`,
    `user_data` and faces in the face list. Face list simply represents a list
    of faces, and could be treated as a searchable data source in
    `face.find_similars`.

    Args:
        face_list_id: Valid character is letter in lower case or digit or '-'
            or '_', maximum length is 64.

    Returns:
        The face list's information.
    """
    url = 'facelists/{}'.format(face_list_id)

    return util.request('GET', url)


def lists():
    """Retrieve information about all existing face lists. Only `face_list_id`,
    `name` and `user_data` will be returned. Try `face_list.get` to retrieve
    face information inside face list.

    Returns:
        An array of face list.
    """
    url = 'facelists'

    return util.request('GET', url)


def update(face_list_id, name=None, user_data=None):
    """Update information of a face list, including `name` and `user_data`.
    Face List simply represents a list of persisted faces, and could be treated
    as a searchable data source in `face.find_similars`.

    Args:
        face_list_id: Valid character is letter in lower case or digit or '-'
            or '_', maximum length is 64.
        name: Name of the created face list, maximum length is 128.
        user_data: Optional parameter. User-defined data for the face list.
            Length should not exceed 16KB.

    Returns:
        An empty response body.
    """
    url = 'facelists/{}'.format(face_list_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    return util.request('PATCH', url, json=json)
