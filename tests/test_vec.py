# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from vecmath import Vec, CYTH_VEC_COMPILED


def test_create():
    x = 3.0
    y = 5.0
    z = -500.0

    v = Vec(x, y, z)
    assert(v.x == x)
    assert(v.y == y)
    assert(v.z == z)


def test_add():
    scalar = 1.5
    v = Vec(1.0, 5.0, 6.0)
    u = Vec(1.0, -5.0, 3.0)

    s_and_v = v.add_scalar(scalar)
    assert(s_and_v.x == scalar+v.x and s_and_v.y == scalar+v.y and s_and_v.z == scalar+v.z)

    w = v.add_vec(u)
    assert(w.x == v.x + u.x and w.y == v.y + u.y and w.z == v.z + u.z)


def test_eq():
    x = y = z = 50

    v = Vec(x, y, z)
    u = Vec(x, y, z)
    w = Vec(-x, -y, -z)

    assert(v == u)
    assert(w != v)


def test_dot_square():
    x = 100.0
    v = Vec(x)

    u = v.dot(v)
    assert(u.x == v.x * v.x)
