import datetime
from copy import deepcopy

from src.domain.activity import Activity
from src.exception.repo_exception import RepoException


class Activity_Repo:
    def __init__(self):
        self.__activity_list = []

    def remove_deleted_person_id_from_activity_list(self, person_id):
        for activity in self.__activity_list:
            if person_id in activity.list_of_each_person_id:
                person_ids = []
                for p_id in activity.list_of_each_person_id:
                    if not person_id == p_id:
                        person_ids.append(p_id)
                activity.list_of_each_person_id = person_ids

    def update(self, given_activity):
        """
        :param given_activity: Updating values!
        :return: Changed activity (depending on what the UI gave)
        """
        self.check_duplicity_of_an_updated_activity(given_activity)
        for currentActivity in self.__activity_list:
            if given_activity.activity_id == currentActivity.activity_id:
                savedActivity = Activity(currentActivity.activity_id, currentActivity.list_of_each_person_id,
                        currentActivity.start_date_time, currentActivity.end_date_time, currentActivity.description)
                if not (given_activity.list_of_each_person_id is None):
                    currentActivity.list_of_each_person_id = given_activity.list_of_each_person_id
                if not (given_activity.start_date_time is None or given_activity.end_date_time is None):
                    currentActivity.start_date_time = given_activity.start_date_time
                    currentActivity.end_date_time = given_activity.end_date_time
                if not (given_activity.description is None):
                    currentActivity.description = given_activity.description
                return savedActivity
        raise RepoException("Could not update any data, given Activity_ID does not exist")

    def check_duplicity_of_an_updated_activity(self, given_activity):
        for activity in self.__activity_list:
            if given_activity.activity_id != activity.activity_id:
                if given_activity.description == activity.description:
                    raise RepoException("There is already an activity with this name / description!")
                if given_activity.start_date_time == activity.start_date_time or given_activity.end_date_time == activity.end_date_time:
                    raise RepoException("Given start_time or end_time already exists in the activity_list!")

    def remove(self, given_activity_id):
        """
        Removes a given activity_id from activity_list
        :param given_activity_id: int activity_id
        :return: Returns deleted_entity for the undo_redo service
        """
        list_of_activity_list = []
        list_of_activity_list[:] = self.__activity_list
        for activity in self.__activity_list:
            if given_activity_id == activity.activity_id:
                list_of_activity_list.remove(activity)
                deleted_entity = activity
        if len(list_of_activity_list) == len(self.__activity_list):
            raise RepoException("No activity removed! Given Activity_ID does not exist!")
        self.__activity_list.clear()
        self.__activity_list[:] = list_of_activity_list
        return deleted_entity

    def add(self, given_activity):
        """
        Adds an activity to activity_list
        :param given_activity: Contains (activity_id, list of person_id, start_date, end_date, description)
        :return: List of activity list with the added element
        """
        self.check_duplicity_of_a_new_activity(given_activity)
        self.__activity_list.append(given_activity)
        return given_activity

    def check_duplicity_of_a_new_activity(self, given_activity):
        for activity in self.__activity_list:
            if given_activity.activity_id == activity.activity_id:
                raise RepoException("Duplicate Activity_ID given!")
            if given_activity.start_date_time == activity.start_date_time or \
                    given_activity.end_date_time == activity.end_date_time:
                raise RepoException(
                    "Activities must not overlap (user cannot have more than one activity at a given time)")
            if given_activity.description == activity.description:
                raise RepoException("There is already an activity with this name / description!")

    def get_all(self):
        return self.__activity_list

    def generate_activities(self):
        self.__activity_list = [
            Activity(500, [100, 123, 124], datetime.datetime(2020, 5, 17, 20), datetime.datetime(2020, 5, 17, 21),"Swimming"),
            Activity(199, [122, 555, 600, 900], datetime.datetime(2021, 5, 17, 10), datetime.datetime(2021, 5, 17, 11),"General gardening"),
            Activity(600, [124, 800], datetime.datetime(2020, 6, 17, 19), datetime.datetime(2020, 6, 17, 20),"Cycling"),
            Activity(520, [100], datetime.datetime(2020, 6, 17, 16), datetime.datetime(2020, 6, 17, 17), "Meditating"),
            Activity(300, [98], datetime.datetime(2021, 1, 20, 12), datetime.datetime(2021, 1, 20, 13), "Aerobics"),
            Activity(333, [55, 87, 12], datetime.datetime(2021, 2, 18, 13), datetime.datetime(2021, 2, 18, 14),"Vacuuming"),
            Activity(569, [40, 95], datetime.datetime(2021, 9, 18, 11), datetime.datetime(2021, 9, 18, 12), "Football"),
            Activity(697, [10, 20, 145, 367, 987], datetime.datetime(2021, 7, 20, 22),datetime.datetime(2021, 7, 20, 23), "Basketball"),
            Activity(987, [600], datetime.datetime(2021, 6, 19, 18), datetime.datetime(2021, 6, 19, 19), "Volleyball"),
            Activity(178, [800, 900], datetime.datetime(2021, 4, 30, 8), datetime.datetime(2021, 4, 30, 9), "Handball"),
            Activity(43, [800], datetime.datetime(2021, 3, 23, 14), datetime.datetime(2021, 3, 23, 15), "Tennis"),
            Activity(66, [367, 555, 987], datetime.datetime(2021, 2, 16, 10), datetime.datetime(2021, 2, 16, 11),"Sweeping"),
            Activity(88, [95], datetime.datetime(2021, 11, 9, 7), datetime.datetime(2021, 11, 9, 8), "Mopping"),
            Activity(921, [12, 87], datetime.datetime(2021, 11, 20, 10), datetime.datetime(2021, 11, 20, 11),"Running"),
            Activity(31, [12], datetime.datetime(2021, 12, 24, 16), datetime.datetime(2021, 12, 24, 17), "Walking"),
            Activity(90, [20], datetime.datetime(2021, 12, 24, 18), datetime.datetime(2021, 12, 24, 19), "Pilates"),
            Activity(865, [345, 987], datetime.datetime(2021, 12, 24, 20), datetime.datetime(2021, 12, 24, 21), "Golf"),
            Activity(78, [100, 124, 987], datetime.datetime(2021, 12, 25, 13), datetime.datetime(2021, 12, 25, 14),"Dancing"),
            Activity(606, [55, 122, 87, 367, 145], datetime.datetime(2021, 12, 25, 15),datetime.datetime(2021, 12, 25, 16), "Jogging"),
            Activity(505, [122, 145], datetime.datetime(2022, 1, 1, 00), datetime.datetime(2022, 1, 1, 1),"Bike Riding")
        ]
