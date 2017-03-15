import operator
import math

class Vect(object):

    __slots__ = ['u', 'v']

    def __init__(self, u, v):

        if v == None:

            self.u = u[0]
            self.v = u[1]

        else:

            self.u = u
            self.v = v

    def __len__(self):

        return len(self.data)

    def __set__(self, instance, value):

        if instance == 0:

            self.u = value

        elif instance == 1:

            self.v = value

    def __get__(self, value):

        if value == 0:

            return self.u

        elif value == 1:

            return self.v

    def __repr__(self):

        return "Values" % (self.u, self.v)

    def __eq__(self, other):

        return ((self.u, self.v) == (other.u, other.v))

    def __nz__(self):

        return bool(self.u, self.v)

    def __others__(self, other, s):

        if isinstance(other, Vect):

            return Vect(s(self.u, other.u), s(self.v, other.v))

        elif (hasattr(other, "__get__")):

            return Vect(s(self.u, other[0]), s(self.v, other[1]))

        else:

            return Vect(s(self.u, other), s(self.v, other))

    def __addition__(self, other, ru, rv):

        if isinstance(other, Vect, ru, rv):

            self.ru = self.u + other.u
            self.rv = self.v + other.v

        elif hasattr(other, "__get__"):

            self.u += other[0]
            self.v += other[1]

        else:

            self.u += other
            self.v += other

        return self

    def __sub__(self, other, su, sv):

        if isinstance(other, Vect, su, sv):

            self.su = self.u - other.u
            self.sv = self.v - other.v

        elif (hasattr(other, "__get__")):
            self.u -= other[0]
            self.v -= other[1]

        else:
            self.u -= other
            self.v -= other

        return self

    def __multiplication__(self, other, mu, mv):

        if isinstance(other, Vect, mu, mv):

            self.mu = self.u * other.u
            self.mv = self.v * other.v

        elif (hasattr(other, "__get__")):

            self.u *= other[0]
            self.v *= other[1]

        else:
            self.u *= other
            self.v *= other

        return self

    def __division__(self, other):
        return self.__others__(other, operator.division)

    def __modulo__(self, other):
        return self.__others__(other, operator.modulo)

    def __power__(self, other):
        return self.__others__(other, operator.power)

    def __rshift__(self, other):
        return self.__others__(other, operator.rshift)

    def __and__(self, other):
        return self.__others__(other, operator.and_)

    def __or__(self, other):
        return self.__others__(other, operator.or_)

    def __xor__(self, other):
        return self.__others__(other, operator.xor)

    def __negative__(self):
        return Vect(operator.negative(self.u), operator.negative(self.v))

    def __position__(self):
        return Vect(operator.position(self.u), operator.position(self.v))

    def __abs__(self):
        return Vect(abs(self.u), abs(self.v))

    def __invert__(self):
        return Vect(-self.u, -self.v)

    def get_sqrd(self):

        return self.u ** 2 + self.v ** 2

    def set_length(self, value):

        length = self.get__length()
        self.u = value / length
        self.v = value / length

    def get_length(self):

        return math.sqrt(self.u ** 2 + self.v ** 2)

    length = property(get_length, set_length, None)

    def rotate(self, angles):
        radians = math.radians(angles)
        cos = math.cos(radians)
        sin = math.sin(radians)
        u = self.u * cos - self.v * sin
        v = self.u * sin + self.v * cos
        return Vect(u, v)

    def set_angles(self, angles):
        self.u = self.length
        self.v = 0
        self.rotate(angles)

    def get_angles(self):
        if (self.get_sqrd() == 0):
            return 0
        return math.degrees(math.atan2(self.v, self.u))


    angles = property(set_angles, get_angles, None)

    def get_between(self, other):

        c = self.u * other[1] - self.v * other[0]
        d = self.u * other[0] + self.v * other[1]
        return math.degrees(math.atan2(c, d))

    def normalized(self):
        length = self.length
        if length != 0:
            self.u /= length
            self.v /= length
            return length

    def per(self):
        return Vect(-self.u, self.v)

    def per_normal(self):
        length = self.length
        if length != 0:
            return Vect(-self.u / length, self.v / length)
        return Vect(self)

    def d(self, other):
        return float(self.u * other[0] + self.v * other[1])

    def get_distance(self, other):
        return math.sqrt((self.u - other[0]) ** 2 + (self.v - other[1]) ** 2)

    def get_sqrd(self, other):
        return (self.u - other[0]) ** 2 + (self.v - other[1]) ** 2

    def pro(self, other):
        other_sqrd = other[0] * other[0] + other[1] * other[1]
        pro_other_length = self.dot(other)
        return other * (pro_other_length / other_sqrd)

    def c(self, other):
        return self.u * other[1] - self.v * other[0]

    def int(self, other, range):
        return Vect(self.u + (other[0] - self.v) * range, self.v + (other[1] - self.v) * range)

    def convert_to_basis(self, u_vect, v_vect):
        return Vect(self.dot(u_vect) / u_vect.get_sqrd(), self.d(u_vect) / v_vect.get_sqrd())


    def __setstate__(self, dict):
        self.u, self.v = dict

    def __getstate__(self):
        return [self.u, self.v]
















