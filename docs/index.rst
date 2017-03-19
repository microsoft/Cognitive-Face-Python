.. Cognative_Face_Python documentation master file, created by
   sphinx-quickstart on Sun Mar 19 16:07:04 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. toctree::
   :maxdepth: 2

Microsoft Face API: Python SDK
==============================
The Python SDK for the Microsoft Face API, an offering within `Microsoft
Cognitive Services <https://www.microsoft.com/cognitive-services/>`_, formerly known as Project Oxford.

* `Learn about the Face API <https://www.microsoft.com/cognitive-services/en-us/face-api/>`_

* `Read the documentation <https://www.microsoft.com/cognitive-services/en-us/face-api/documentation/overview/>`_

* `Find more SDKs & Samples <https://www.microsoft.com/cognitive-services/en-us/SDK-Sample?api=face/>`_


Installation
^^^^^^^^^^^^
::

    pip install cognitive_face


Installation from Source Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    python setup.py install


Unit Tests
^^^^^^^^^^
Before running unittests, please refer to the `/cognitive_face/tests/config.sample.py <https://github.com/Microsoft/Cognitive-Face-Python/blob/master/cognitive_face/tests/config.sample.py/>`_ and set proper configuration with valid `Subscription Key <https://www.microsoft.com/cognitive-services/en-us/sign-up>`_ to make the unittests work.

::

    python setup.py test


Minimal Usage
^^^^^^^^^^^^^
::

    import cognitive_face as CF
    KEY = 'subscription key'  # Replace with a valid Subscription Key here.
    CF.Key.set(KEY)

    img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
    result = CF.face.detect(img_url)
    print result


Sample
^^^^^^
A Python SDK sample built with wxPython is also provided, before execution, please install all components listed below.


Sample Prerequisite
+++++++++++++++++++
* `Python 2.7 <https://www.python.org/downloads/>`_ (only Python 2 supported due to limitation of wxPython)
* `wxPython <https://wxpython.org/>`_
* `cognitive_face package <https://pypi.python.org/pypi/cognitive_face/>`_

Sample Execution
++++++++++++++++
::

    git clone https://github.com/Microsoft/Cognitive-Face-Python.git
    cd Cognitive-Face-Python
    python sample

Contributing
^^^^^^^^^^^^
We welcome contributions. Feel free to file issues and pull requests on the repo and we'll address them as we can. Learn more about how you can help on our `Contribution Rules & Guidelines <https://github.com/Microsoft/Cognitive-Face-Python/blob/master/CONTRIBUTING.md/>`_ .


You can reach out to us anytime with questions and suggestions using our communities below:

* Support questions: `StackOverflow <https://stackoverflow.com/questions/tagged/microsoft-cognitive/>`_
* Feedback & feature requests: `Cognitive Services UserVoice Forum <https://cognitive.uservoice.com/>`_

This project has adopted the `Microsoft Open Source Code of Conduct <https://opensource.microsoft.com/codeofconduct/>`_ . For more
information see the `Code of Conduct FAQ <https://opensource.microsoft.com/codeofconduct/faq/>`_ or contact opencode@microsoft.com with any additional questions or comments. 

Updates
^^^^^^^

* `Face API Release Notes <https://www.microsoft.com/cognitive-services/en-us/face-api/documentation/ReleaseNotes>`_


License
^^^^^^^
All Microsoft Cognitive Services SDKs and samples are licensed with the MIT License. For more details, see `LICENSE <https://github.com/Microsoft/Cognitive-Face-Python/blob/master/LICENSE.md/>`_ .Sample images are licensed separately, please refer to `LICENSE-IMAGE <https://github.com/Microsoft/Cognitive-Face-Python/blob/master/LICENSE-IMAGE.md/>`_


Developer Code of Conduct
^^^^^^^^^^^^^^^^^^^^^^^^^
Developers using Cognitive Services, including this sample, are expected to follow the “Developer Code of Conduct for Microsoft Cognitive Services”, found at http://go.microsoft.com/fwlink/?LinkId=698895.


