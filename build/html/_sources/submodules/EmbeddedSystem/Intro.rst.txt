============================
Embedded system description
============================

.. automodules::index

Project from embedded systems consist of two separate HW solutions.

Detector is used for measurment of decibels, and after overrunning the set-up treshold, sends information to generator.
Also detector have ability to automatically pair with generator using push-up button.

Generator is used for generating audio signal after data has been recieved from detector.

.. toctree::
    :maxdepth: 2
    :titlesonly:

    Generator
    Detector
    Implementation


