#!/usr/bin/local python

################################
#
#        PDB PARSER
#
################################

# <insert MIT License> (c) 2012 James Crooks

class Atom:
    '''Fine grained data structure that captures essential information
from the pdb ATOM and HETATM lines.'''
    def __init__(self, data):
        self._key = data[0]
        self._index = data[1]
        self._name = data[2]
        self._resname = data[3]
        self._chain =  data[4]
        self._resid = data[5]
        self._x =  data[6]
        self._y = data[7]
        self._z = data[8]
        self._occupancy = data[9]
        self._beta = data[10]
        self._element = data[11]

    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, value):
        self._key = value

    @property
    def index(self):
        return self._index
    @index.setter
    def index(self, value):
        self._index = value

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def resname(self):
        return self._resname
    @resname.setter
    def resname(self, value):
        self._resname = value

    @property
    def chain(self):
        return self._chain
    @chain.setter
    def chain(self, value):
        self._chain = value

    @property
    def resid(self):
        return self._resid
    @resid.setter
    def resid(self, value):
        self._resid = value

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z
    @z.setter
    def z(self, value):
        self._z = value

    @property
    def occupancy(self):
        return self._occupancy
    @occupancy.setter
    def occupancy(self, value):
        self._occupancy =  value

    @property
    def beta(self):
        return self._beta
    @beta.setter
    def beta(self, value):
        self._beta = value

    @property
    def element(self):
        return self._element
    @element.setter
    def element(self, value):
        self._element = value

    def formatPDBEntry(self):
        print self.key + self.element
