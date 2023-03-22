#!/usr/bin/python3
import unittest
import os
import models

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.b = BaseModel()
        self.u = User()
        self.a = Amenity()
        self.s = State()
        self.c = City()
        self.p = Place()
        self.r = Review()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exits("file.json"):
            pass
        else:
            os.mknod("file.json")
    def tearDown(self):
        del self.b
        del self.u
        del self.a
        del self.s
        del self.c
        del self.p
        del self.r
        del self.storage
        if os.path.exits("file.json"):
            os.remove("file.json")
    def test_all(self):
        val = self.storage.all()
        self.asserIsNotNone(val)
        self.assertEqual(type(val), dict)
    def test_new(self):
        val = self.storage.all()
        self.u.name = "Neima"
        self.u.id = "2121"
        val2 = self.storage.new(self.u)
        key = "{}.{}".format(self.u.__class__.__name__, self.u.id)
        self.assertIsNotNone(val[key])

if __name__ == "__main__":
    unittest.main()
