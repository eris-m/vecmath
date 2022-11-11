# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import cython

if cython.compiled:
    CYTH_VEC_COMPILED = True
else:
    CYTH_VEC_COMPILED = False


@cython.cclass
class Vec:
    """
    A 4-Dimensional Vector, _with components _x, _y, _z, _w.

    """

    _x: cython.float
    _y: cython.float
    _z: cython.float
    _w: cython.float

    def dot(self, other: "Vec") -> "Vec":
        r"""
        Dot product with other vector.

        :param other: Vector to calculate the dot product with.

        A Dot product is an operation defined as

        .. math::
            u \cdot v = \sum_i u_i v_i = u_x v_x + u_y v_y + u_z v_z + u_w v_w


        An alternative definition (only in Euclidean-like space) is:

        .. math::
            u \cdot v = ||u|| ||v|| cos \theta

        where theta is the angle between the two. Using this formula,
        if v and u are both unit vectors (their length = 1):

        .. math::
            cos \theta = u \cdot v


        Another useful formula to keep in mind is that

        .. math::
            u \cdot u = \sum_u u_i^2 = u_x^2 + u_y^2 + u_z^2 + u_w^2
            = ||u||^2

        """
        x = self._x * other._x
        y = self._y * other._y
        z = self._z * other._z
        w = self._w * other._w

        return Vec(x, y, z, w)

    ################
    # Properties
    ################

    @property
    def x(self) -> float:
        """
        X Component of the vector.
        """
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        """
        Y Component of the vector.
        """
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    @property
    def z(self) -> float:
        """
        Z Component of the vector.
        """
        return self._z

    @z.setter
    def z(self, value: float):
        self._z = value

    @property
    def w(self) -> float:
        """
        W Component of the vector.
        """
        return self._w

    @w.setter
    def w(self, value: float):
        self._w = value

    ################
    # Dunder methods
    ################

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0):
        """
        Creates a vector.

        By default all components = 0, this allows a shorthand way of creating 2d, and 3d vectors,
        ``Vec(x, y)`` compared to ``Vec(x, y, 0.0, 0.0)``


        :param x: X Component.
        :param y: Y Component.
        :param z: Z Component.
        :param w: W Component.
        """
        self._x = x
        self._y = y
        self._z = z
        self._w = w

    def add_vec(self, other: "Vec") -> "Vec":
        """
        Adds a vector to a self.

        :param other: Other vector to add.
        :return: Self + Other vector, as a vector.
        """

        # dimensions
        x = self._x + other._x
        y = self._y + other._y
        z = self._z + other._z
        w = self._w + other._w
        return Vec(x, y, z, w)

    def add_scalar(self, other) -> "Vec":
        """
        Adds a scalar to self.

        :param other: Scalar (regular number) to add.
        :return: Vector self+other
        """

        # dimensions
        x = self._x + other
        y = self._y + other
        z = self._z + other
        w = self._w + other
        return Vec(x, y, z, w)

    def sub_vec(self, other: "Vec") -> "Vec":
        x = self._x - other._x
        y = self._y - other._y
        z = self._z - other._z
        w = self._w - other._w
        return Vec(x, y, z, w)

    def sub_scalar(self, other):
        x = self._x - other
        y = self._y - other
        z = self._z - other
        w = self._w - other
        return Vec(x, y, z, w)

    def __eq__(self, other: "Vec") -> bool:
        return self.x == other.x and self.y == other.y and self._z == other.z

    def __format__(self, spec):
        return (
            f"({self._x:{spec}}, {self._y:{spec}}, {self._z:{spec}}, {self._w:{spec}})"
        )

    def __str__(self) -> str:
        return self.__format__("")
