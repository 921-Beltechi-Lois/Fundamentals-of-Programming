import unittest

from src.repository.activity_repo import Activity_Repo
from src.repository.my_data_structure import MyDataStructure
from src.services.activity_service import ActivityServices
from src.services.undo_redo_service import UndoRedoService


class TestMyDataStructure_Activity(unittest.TestCase):
    def setUp(self) -> None:
        """
        Runs before every test method
        """

    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass

    def test_for(self):
        data_structure = MyDataStructure()
        data_structure['a'] = '1'
        data_structure['b'] = '2'
        data_structure['c'] = '3'
        data_structure['d'] = '4'
        a_list = ['1', '2', '3', '4']
        index = 0

        for it in data_structure:
            self.assertEqual(it, a_list[index])
            index += 1

        del data_structure['a']
        self.assertEqual(data_structure['a'] in data_structure, False)

        data_structure['d'] = '10'
        self.assertEqual(data_structure['d'], '10', True)
        value = data_structure.__getitem__('c')
        self.assertEqual(value, '3', True)

    def test_sort(self):
        a_list = [12, 3, 4, 6, 1, 24]
        result = MyDataStructure.sort(a_list, lambda x, y: x < y)
        self.assertEqual(result, sorted(a_list, reverse=True))

    def test_filter(self):
        a_list = [12, 3, 4, 6, 1, 24]
        result = MyDataStructure.filter_list(a_list, lambda x: x>3)
        self.assertEqual(result, [12,4,6,24])