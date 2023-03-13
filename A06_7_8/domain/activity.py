class Activity:
    def __init__(self, activity_id, list_of_each_person_id, start_date_time, end_date_time, description):
        self._activity_id = activity_id
        self._list_of_each_person_id = list_of_each_person_id
        self._start_date_time = start_date_time
        self._end_date_time = end_date_time
        self._description = description

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value

    @property
    def list_of_each_person_id(self):
        return self._list_of_each_person_id

    @list_of_each_person_id.setter
    def list_of_each_person_id(self, value):
        self._list_of_each_person_id = value

    @property
    def start_date_time(self):
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        self._start_date_time = value

    @property
    def end_date_time(self):
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, value):
        self._end_date_time = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __str__(self):
        return f' Activity_ID: {self._activity_id}'.ljust(30) + \
               f'List of each Person_ID:{self._list_of_each_person_id}'.ljust(50) + \
               f'Period: {self._start_date_time}'.ljust(40) + \
               f'to: {self._end_date_time}\''.ljust(40) + \
               f'Description: {self._description}'.ljust(40)
