import unittest

from src.domain.person import Person
from src.exception.repo_exception import RepoException
from src.repository.activity_repo import Activity_Repo
from src.repository.person_repo import Person_Repo
from src.services.person_service import PersonServices
from src.services.undo_redo_service import UndoRedoService


class Test_Person:
    def __init__(self):
        self._repository = Person_Repo()

        self._undo_service = UndoRedoService() # not used

        self.__test_person_service = PersonServices(self._repository, self._undo_service, None)

        self.test_add_fail()
        self.test_add_success()

    def test_add_fail(self):
        person  = Person(124, 'asd', '0123456789')
        self.__test_person_service.add(person)
        try:
            person  = Person(124, 'asd', '0123456789')
            self.__test_person_service.add(person)
            assert False
        except RepoException as ve:
            assert str(ve) == "Cannot add person because of duplicate person id: " + str(person.person_id)

    def test_add_success(self):
        person  = Person(3, 'asdfr', '012345689')
        self.__test_person_service.add(person)
        assert person in self.__test_person_service.get_all()


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self._repository = Person_Repo()

        undo_service = UndoRedoService() #not used


        activity_repository = Activity_Repo()   # not used
        #undo_service = UndoRedoService() # not used
        #self._activity_service = ActivityServices(activity_repository, undo_service)

        self.__test_person_service = PersonServices(self._repository, undo_service,activity_repository)

        # self.test_add_fail()
        # self.test_add_success()
    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass

    def test_add(self):
        person  = Person(124, 'asd', '0123456789')
        self.__test_person_service.add(person)
        self.assertEqual(person in self.__test_person_service.get_all(), True)  #todo add successfully

        person = Person(124, 'nu', '123456789')
        with self.assertRaises(RepoException) as re:
            self.__test_person_service.add(person)                       #todo add failed
        self.assertEqual("Cannot add person because of duplicate person id: " + str(person.person_id), str(re.exception))

        # try:
        #     person  = Person(124, 'asd', '0123456789')
        #     self.__test_person_service.add(person)
        #     assert False
        # except RepoException as ve:
        #     assert str(ve) == "Cannot add person because of duplicate person id: " + str(person.person_id)

    def test_remove(self):
        person = Person(124, 'asd', '0123456789')
        self.__test_person_service.add(person)
        self.assertEqual(person in self.__test_person_service.get_all(), True)
        self.__test_person_service.remove(person.person_id)
        self.assertEqual(person in self.__test_person_service.get_all(), False)   #todo deleted successfully

        person_id = 500
        with self.assertRaises(RepoException) as re:                              #todo deleted failed
            self.__test_person_service.remove(person_id)
        self.assertEqual("Given Person_ID does not exist in the person_list", str(re.exception))

    def test_update(self):
        person = Person(124, 'asd', '0123456789')
        self.__test_person_service.add(person)
        self.assertEqual(person in self.__test_person_service.get_all(), True)

        self.__test_person_service.update('change name', 124)
        self.assertEqual(person.name, 'change name', True)              #todo updated successfully

        with self.assertRaises(RepoException) as re:
            self.__test_person_service.update('name', 400)
        self.assertEqual("No such Person_ID exists in person_list", str(re.exception))          #todo updated failed