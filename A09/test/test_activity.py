import datetime
import unittest

from src.domain.activity import Activity
from src.exception.repo_exception import RepoException
from src.repository.activity_repo import Activity_Repo
from src.services.activity_service import ActivityServices
from src.services.undo_redo_service import UndoRedoService


class Test_Activity:
    def __init__(self):
        self.__repository = Activity_Repo()

        self.__undo_service = UndoRedoService() #not used  or put None

        self.__test_activity_service = ActivityServices(self.__repository, self.__undo_service)

        self.test_add_fail()
        self.test_add_success()

    def test_add_fail(self):
        newActivity = Activity(1, [123, 124], datetime.datetime(2025, 12, 24, 20), datetime.datetime(2025, 12, 24, 21),
                               'description')
        self.__test_activity_service.add(newActivity)
        try:
            newActivity = Activity(1, [123, 124], datetime.datetime(2025, 12, 24, 20),
                                   datetime.datetime(2025, 12, 24, 21), 'description')
            self.__test_activity_service.add(newActivity)
            assert False
        except RepoException as re:
            assert str(re) == "Duplicate Activity_ID given!"

    def test_add_success(self):
        newActivity = Activity(2, [123, 124], datetime.datetime(2026, 12, 24, 20), datetime.datetime(2026, 12, 24, 21),
                               'asd')
        self.__test_activity_service.add(newActivity)
        assert newActivity in self.__test_activity_service.get_all()

        # assert newActivity.activity_id == 1
        # assert newActivity.list_of_each_person_id == [123, 124]
        # assert newActivity.start_date_time == datetime.datetime(2025, 12, 24, 20)
        # assert newActivity.end_date_time == datetime.datetime(2025, 12, 24, 21)
        # assert newActivity.description == 'description'


class TestActivity(unittest.TestCase):
    def setUp(self) -> None:
        """
        Runs before every test method
        """
        self.__repository = Activity_Repo()

        self.__undo_service = UndoRedoService() # not used

        self.__test_activity_service = ActivityServices(self.__repository, self.__undo_service)

        # self.test_add_fail()
        # self.test_add_success()

    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass

    def test_add(self):
        newActivity = Activity(1, [123, 124], datetime.datetime(2025, 12, 24, 20), datetime.datetime(2025, 12, 24, 21),
                               'description')
        self.__test_activity_service.add(newActivity)

        self.assertEqual(newActivity in self.__test_activity_service.get_all(), True)   #todo add successfully

        newActivity = Activity(1, [123, 124], datetime.datetime(2025, 12, 24, 19), datetime.datetime(2025, 12, 24, 20),
                               'description1')

        with self.assertRaises(RepoException) as re:
            self.__test_activity_service.add(newActivity)                       #todo add failed
        self.assertEqual('Duplicate Activity_ID given!', str(re.exception))

    def test_delete(self):
        newActivity = Activity(1, [123, 124], datetime.datetime(2025, 12, 24, 20), datetime.datetime(2025, 12, 24, 21),
                               'description')
        self.__test_activity_service.add(newActivity)
        activity_id = 1
        self.__test_activity_service._remove(activity_id)

        self.assertEqual(newActivity in self.__test_activity_service.get_all(), False)  #todo deleted succesfully

        activity_id = 123
        with self.assertRaises(RepoException) as re:
            self.__test_activity_service._remove(activity_id)
        self.assertEqual("No activity removed! Given Activity_ID does not exist!", str(re.exception)) #todo deleted failed

    def test_update(self):
        newActivity = Activity(1, [123, 124], datetime.datetime(2025, 12, 24, 20), datetime.datetime(2025, 12, 24, 21),
                               'description')
        self.__test_activity_service.add(newActivity)
        activity_updated = Activity(1, None, None, None, 'change_description')
        self.__test_activity_service.update(activity_updated)
        self.assertEqual(newActivity.description, 'change_description', True)               #todo updated successfully

        with self.assertRaises(RepoException) as re:
            activity_updated = Activity(1000, None, None, None, 'description')
            self.__test_activity_service.update(activity_updated)
        self.assertEqual("Could not update any data, given Activity_ID does not exist", str(re.exception)) #todo up failed

