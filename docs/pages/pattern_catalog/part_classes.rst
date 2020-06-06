Part Classes
============
.. admonition:: Motivation

   Encapsulate how the geometry of a part is made.

Parts are often thought about as real world objects, and therefore fit nicely into the paradigm of `Object Oriented Programming (OOP) <https://en.wikipedia.org/wiki/Object-oriented_programming>`_ as **classes**.

Each part class has the `single-responsibility <https://en.wikipedia.org/wiki/Single-responsibility_principle>`_ to "make" the geometry for a given part.

For example, you might have a ``Box`` class with a ``make`` method that encapsulates and exposes how to create the geometry of a box.

.. code-block:: python

    import Part


    class Box:

        @staticmethod
        def make():
            box = Part.makeBox(10, 10, 10)
            return box

.. Note:: Naming the method ``make`` is a convention inspired by FreeCAD's ``make*`` `Part API <https://wiki.freecadweb.org/Part_API>`_.

While in this trivial example the ``Box`` class and ``make`` method don't provide much value, this abstraction offers a simple interface for "making" more complex and custom geometry.

For example, you may pass in the ``length`` and ``width`` into the ``make`` method as parameters for creating boxes of different sizes.

.. code-block:: python

    class Box:

        @staticmethod
        def make(length, width):
            height = 10
            box = Part.makeBox(length, width, height)
            return box

We could have defined a ``make_box`` **function** instead, but why is the ``class`` approach preferable?

Imagine the box is a **sub-part** of a more complex part, and that *parent* part needs to know about the static ``height`` of ``10`` for the box.

With a quick refactor, the parent part can now access the ``height`` of the ``Box`` as a static property, and that information stays close to the construction of the box geometry, as opposed to being defined somewhere else in the program via constants or some other approach.

.. code-block:: python

    class Box:

        height = 10

        @classmethod
        def make(cls, length, width):
            box = Part.makeBox(length, width, cls.height)
            return box