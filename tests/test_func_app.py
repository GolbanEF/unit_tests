import unittest

from app import add_new_doc, append_doc_to_shelf, delete_doc, add_new_shelf
from app import  documents, directories


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def test_add_new_shelf(self):
    #
    #     self.assertEqual(add_new_shelf('6'), ('6', True))

    # def test_add_new_doc(self):
    #
    #     self.assertEqual(add_new_doc(), "5")

    def test_delete_doc(self):

        self.assertEqual(delete_doc(), ("11-2", True))


