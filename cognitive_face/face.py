#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: face.py
Description: Face section of the Cognitive Face API.
"""
from . import util


def detect(image, face_id=True, landmarks=False, attributes=''):
    """Detect human faces in an image and returns face locations, and
    optionally with `face_id`s, landmarks, and attributes.

    Args:
        image: A URL or a file path or a file-like object represents an image.
        face_id: [Optional] Return faceIds of the detected faces or not. The
            default value is true.
        landmarks: [Optional] Return face landmarks of the detected faces or
            not. The default value is false.
        attributes: [Optional] Analyze and return the one or more specified
            face attributes in the comma-separated string like
            "age,gender". Supported face attributes include age, gender,
            headPose, smile, facialHair, glasses, emotion, makeup, accessories,
            occlusion, blur, exposure, noise. Note that each face attribute
            analysis has additional computational and time cost.

    Returns:
        An array of face entries ranked by face rectangle size in descending
        order. An empty response indicates no faces detected. A face entry may
        contain the corresponding values depending on input parameters.
    """
    url = 'detect'
    headers, data, json = util.parse_image(image)
    params = {
        'returnFaceId': face_id and 'true' or 'false',
        'returnFaceLandmarks': landmarks and 'true' or 'false',
        'returnFaceAttributes': attributes,
    }

    return util.request(
        'POST', url, headers=headers, params=params, json=json, data=data)


def find_similars(face_id,
                  face_list_id=None,
                  large_face_list_id=None,
                  face_ids=None,
                  max_candidates_return=20,
                  mode='matchPerson'):
    """Given query face's `face_id`, to search the similar-looking faces from a
    `face_id` array, a `face_list_id` or a `large_face_list_id`.

    Parameter `large_face_list_id`, `face_list_id` and `face_ids` should not be 
    provided at the same time.

    Args:
        face_id: `face_id` of the query face. User needs to call `face.detect`
            first to get a valid `face_id`. Note that this `face_id` is not
            persisted and will expire in 24 hours after the detection call.
        face_list_id: An existing user-specified unique candidate face list,
            created in `face_list.create`. Face list contains a set of
            `persisted_face_ids` which are persisted and will never expire.
        large_face_list_id: An existing user-specified unique candidate face
            list, created in `large_face_list.create`. Large Face list contains
            a set of `persisted_face_ids` which are persisted and will never
            expire.
        face_ids: An array of candidate `face_id`s. All of them are created by
            `face.detect` and the `face_id`s will expire in 24 hours after the
            detection call. The number of `face_id`s is limited to 1000.
        max_candidates_return: Optional parameter. The number of top similar
            faces returned. The valid range is [1, 1000]. It defaults to 20.
        mode: Optional parameter. Similar face searching mode. It can be
            "matchPerson" or "matchFace". It defaults to "matchPerson".

    Returns:
        An array of the most similar faces represented in `face_id` if the
        input parameter is `face_ids` or `persisted_face_id` if the input
        parameter is `face_list_id` or `large_face_list_id`.
    """
    url = 'findsimilars'
    json = {
        'faceId': face_id,
        'faceListId': face_list_id,
        'largeFaceListId': large_face_list_id,
        'faceIds': face_ids,
        'maxNumOfCandidatesReturned': max_candidates_return,
        'mode': mode,
    }

    return util.request('POST', url, json=json)


def group(face_ids):
    """Divide candidate faces into groups based on face similarity.

    Args:
        face_ids: An array of candidate `face_id`s created by `face.detect`.
            The maximum is 1000 faces.

    Returns:
        one or more groups of similar faces (ranked by group size) and a
        messyGroup.
    """
    url = 'group'
    json = {
        'faceIds': face_ids,
    }

    return util.request('POST', url, json=json)


def identify(face_ids,
             person_group_id=None,
             large_person_group_id=None,
             max_candidates_return=1,
             threshold=None):
    """Identify unknown faces from a person group or a large person group.

    Args:
        face_ids: An array of query `face_id`s, created by the `face.detect`.
            Each of the faces are identified independently. The valid number of
            `face_ids` is between [1, 10].
        person_group_id: `person_group_id` of the target person group, created
            by `person_group.create`.
        large_person_group_id: `large_person_group_id` of the target large
            person group, createdJ by `large_person_group.create`.
        max_candidates_return: Optional parameter. The range of
            `max_candidates_return` is between 1 and 5 (default is 1).
        threshold: Optional parameter. Confidence threshold of identification,
            used to judge whether one face belongs to one person. The range of
            confidence threshold is [0, 1] (default specified by algorithm).

    Returns:
        The identified candidate person(s) for each query face(s).
    """
    url = 'identify'
    json = {
        'personGroupId': person_group_id,
        'largePersonGroupId': large_person_group_id,
        'faceIds': face_ids,
        'maxNumOfCandidatesReturned': max_candidates_return,
        'confidenceThreshold': threshold,
    }

    return util.request('POST', url, json=json)


def verify(face_id,
           another_face_id=None,
           person_group_id=None,
           large_person_group_id=None,
           person_id=None):
    """Verify whether two faces belong to a same person or whether one face
    belongs to a person.

    For face to face verification, only `face_id` and `another_face_id` is
    necessary. For face to person verification, only `face_id`,
    `person_group_id` (or `large_person_group_id`) and `person_id` is needed.

    Args:
        face_id: `face_id` of one face, comes from `face.detect`.
        another_face_id: `face_id` of another face, comes from `face.detect`.
        person_group_id: Using existing `person_group_id` and `person_id` for
            fast loading a specified person. `person_group_id` is created in
            `person_group.create`.
        large_person_group_id: Using existing `large_person_group_id` and
            `person_id` for fast loading a specified person.
            `large_person_group_id` is created in `large_person_group.create`.
        person_id: Specify a certain person in a person group. `person_id` is
            created in `person.create`.

    Returns:
        The verification result.
    """
    url = 'verify'
    json = {}
    if another_face_id:
        json.update({
            'faceId1': face_id,
            'faceId2': another_face_id,
        })
    else:
        json.update({
            'faceId': face_id,
            'personGroupId': person_group_id,
            'largePersonGroupId': large_person_group_id,
            'personId': person_id,
        })

    return util.request('POST', url, json=json)
