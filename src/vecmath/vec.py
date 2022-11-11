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
    """A 4D Vector."""

    _x: cython.float
    _y: cython.float
    _z: cython.float
    _w: cython.float

    ############
    # Arithmetic
    ############

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

    def add_vec(self, other: "Vec") -> "Vec":
        """Adds a vector to self and returns the result

        Args:
            other (Vec): Other vector to add

        Returns:
            Vec: Self + Other
        """

        # dimensions
        x = self._x + other._x
        y = self._y + other._y
        z = self._z + other._z
        w = self._w + other._w
        return Vec(x, y, z, w)

    def add_scalar(self, other: cython.float) -> "Vec":
        """Adds a scalar to self and returns the result

        Args:
            other (Number): Scalar to add

        Returns:
            Vec: Self + Other
        """

        # dimensions
        x = self._x + other
        y = self._y + other
        z = self._z + other
        w = self._w + other
        return Vec(x, y, z, w)

    def sub_vec(self, other: "Vec") -> "Vec":
        """Subtracts a vector from self and returns result

        Args:
            other (Vec): Vector to subract

        Returns:
            Vec: Self - Other
        """
        x = self._x - other._x
        y = self._y - other._y
        z = self._z - other._z
        w = self._w - other._w
        return Vec(x, y, z, w)

    def sub_scalar(self, other: cython.float) -> "Vec":
        """Subtracts a scalar from self and returns result

        Args:
            other (float): Scalar to subtract

        Returns:
            Vec: Self - Other
        """
        x = self._x - other
        y = self._y - other
        z = self._z - other
        w = self._w - other
        return Vec(x, y, z, w)

    ################
    # Properties
    ################

    @property
    def x(self) -> float:
        """X Component of the vector."""
        return self._x

    @x.setter
    def x(self, value: cython.float):
        self._x = value

    @property
    def y(self) -> float:
        """Y Component of the vector."""
        return self._y

    @y.setter
    def y(self, value: cython.float):
        self._y = value

    @property
    def z(self) -> float:
        """
        Z Component of the vector.
        """
        return self._z

    @z.setter
    def z(self, value: cython.float):
        self._z = value

    @property
    def w(self) -> float:
        """
        W Component of the vector.
        """
        return self._w

    @w.setter
    def w(self, value: cython.float):
        self._w = value

    #####################
    # Dunder (__) methods
    #####################

    def __init__(
        self,
        x: cython.float = 0.0,
        y: cython.float = 0.0,
        z: cython.float = 0.0,
        w: cython.float = 0.0,
    ):
        """Creates a 4D vector.
        All components are assumed to be 0 if not specified.

        Args:
            x (float, optional): X Component. Defaults to 0.0.
            y (float, optional): Y Component. Defaults to 0.0.
            z (float, optional): Z Component. Defaults to 0.0.
            w (float, optional): W Component. Defaults to 0.0.
        """
        self._x = x
        self._y = y
        self._z = z
        self._w = w

    def __eq__(self, other: "Vec") -> bool:
        """Checks equality with other vector"""
        return self.x == other.x and self.y == other.y and self._z == other.z

    def __format__(self, spec):
        return (
            f"({self._x:{spec}}, {self._y:{spec}}, {self._z:{spec}}, {self._w:{spec}})"
        )

    def __str__(self) -> str:
        return self.__format__("")
