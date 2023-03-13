import pickle
from datetime import datetime

from src.domain.activity import Activity
from src.repository.activity_repo import Activity_Repo


class ActivityTextFileRepo(Activity_Repo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._read_file()
        # super().generate_activities()
        # self._save_file()

    def _read_file(self):
        f = open(self._file_name, "rt")
        format = '%Y-%m-%d %H:%M:%S'
        for line in f.readlines():
            activity_id, string_list_id, start_date_time, end_date_time, description = line.strip().split(';')
            string_list_id = string_list_id.strip('][').split(', ')
            list_of_each_person_id = []
            for id in string_list_id:
                list_of_each_person_id.append(int(id))
            activity = Activity(int(activity_id), list_of_each_person_id, datetime.strptime(start_date_time, format),
                                datetime.strptime(end_date_time, format), description)
            super().add(activity)
        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')
        separator = ';'
        for activity in self.get_all():
            str_activity = str(activity.activity_id) + separator + \
                           str(activity.list_of_each_person_id) + separator + \
                           str(activity.start_date_time) + separator + \
                           str(activity.end_date_time) + separator + \
                           str(activity.description) + "\n"
            f.write(str_activity)
        f.close()

    def add(self, activity):
        activity = super().add(activity)
        self._save_file()
        return activity

    def remove(self, activity_id):
        deleted_activity = super().remove(activity_id)
        self._save_file()
        return deleted_activity

    def update(self, given_activity):
        updated_activty = super().update(given_activity)
        self._save_file()
        return updated_activty

class ActivityBinaryFileRepo(Activity_Repo):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._read_file()

        # self.generate_activities()
        # self._save_file()

    def _read_file(self):
        f = open(self._file_name, "rb")  # rt -> read, binary
        self.__activity_list = pickle.load(f)
        for activity in self.__activity_list:
            super().add(activity)
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self.get_all(), f)
        f.close()

    def add(self, activity):
        activity = super().add(activity)
        self._save_file()
        return activity

    def remove(self, activity_id):
        deleted_activity = super().remove(activity_id)
        self._save_file()
        return deleted_activity

    def update(self, given_activity):
        updated_activty = super().update(given_activity)
        self._save_file()
        return updated_activty