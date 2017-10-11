#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: large_face_list.py
Description: Large Face List section of the Cognitive Face API.
"""
from . import util


def create(large_face_list_id, name=None, user_data=None):
    """Create an empty large face list with user-specified
    `large_face_list_id`, `name` and an optional `user_data`.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.
        name: Name of the created large face list, maximum length is 128.
        user_data: Optional parameter. User-defined data for the large face
            list.  Length should not exceed 16KB.

    Returns:
        An empty response body.
    """
    name = name or large_face_list_id
    url = 'largefacelists/{}'.format(large_face_list_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    return util.request('PUT', url, json=json)


def delete(large_face_list_id):
    """Delete an existing large face list according to `large_face_list_id`.
    Persisted face images in the large face list will also be deleted.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.

    Returns:
        An empty response body.
    """
    url = 'largefacelists/{}'.format(large_face_list_id)

    return util.request('DELETE', url)


def get(large_face_list_id):
    """Retrieve a large face list's information, including
    `large_face_list_id`, `name`, `user_data`. Large face list simply
    represents a list of faces, and could be treated as a searchable data
    source in `face.find_similars`.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.

    Returns:
        The large face list's information.
    """
    url = 'largefacelists/{}'.format(large_face_list_id)

    return util.request('GET', url)


def get_status(large_face_list_id):
    """Retrieve the training status of a large face list (completed or
    ongoing). Training can be triggered by `large_face_list.train`. The
    training will process for a while on the server side.

    Args:
        large_face_list_id: `large_face_list_id` of the target large face list.

    Returns:
        The large face list's training status.
    """
    url = 'largefacelists/{}/training'.format(large_face_list_id)

    return util.request('GET', url)


def list(start=None, top=None):
    """Retrieve information about all existing large face lists. Only
    `large_face_list_id`, `name` and `user_data` will be returned.

    Args:
        start: Optional parameter. List large face lists from the least
            `large_face_list_id` greater than the "start". It contains no more
            than 64 characters. Default is empty.
        top: The number of large face lists to list, ranging in [1, 1000].
            Default is 1000.

    Returns:
        An array of large face lists.
    """
    url = 'largefacelists'
    params = {
        'start': start,
        'top': top,
    }

    return util.request('GET', url, params=params)


def train(large_face_list_id):
    """Queue a large face list training task, the training task may not be
    started immediately.

    Args:
        large_face_list_id: Target large face list to be trained.

    Returns:
        An empty JSON body.
    """
    url = 'largefacelists/{}/train'.format(large_face_list_id)

    return util.request('POST', url)


def update(large_face_list_id, name=None, user_data=None):
    """Update information of a large face list, including `name` and `user_data`.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.
        name: Name of the created large face list, maximum length is 128.
        user_data: Optional parameter. User-defined data for the large face
            list. Length should not exceed 16KB.

    Returns:
        An empty response body.
    """
    url = 'largefacelists/{}'.format(large_face_list_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    return util.request('PATCH', url, json=json)
