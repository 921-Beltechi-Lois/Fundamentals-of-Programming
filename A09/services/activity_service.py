from src.exception.service_exception import ServiceException
from src.services.undo_redo_service import Call, CascadedOperation, Operation


class ActivityServices:
    def __init__(self, repository, undo_service):
        self._repository = repository
        self._undo_service = undo_service

    def get_statistics_for_busiest_days(self):
        day_remaining_hours = []
        activities = self._repository.get_all()
        for activity in activities:
            store_start_date = activity.start_date_time
            store_end_date = activity.end_date_time
            found = 0
            for activityReport in day_remaining_hours:
                if store_start_date.date() == activityReport[0]:
                    remaining_hours = activityReport[1] - (store_end_date.hour - store_start_date.hour)
                    activityReport[1] = remaining_hours
                    found = 1
            if found == 0:
                day_remaining_hours.append([store_start_date.date(), 24 - (store_end_date.hour - store_start_date.hour)])
        return sorted(day_remaining_hours, key=lambda x: x[1], reverse=True)

    def get_statistics_for_a_given_person(self, given_person_id):
        filter_list = []
        for activities in self._repository.get_all():
            if given_person_id in activities.list_of_each_person_id:
                filter_list.append(activities)
        if len(filter_list) == 0:
            raise ServiceException("given_person_id does not exist")
        return sorted(filter_list, key=lambda x: x.start_date_time, reverse=False)

    def get_statistics_for_a_given_date(self, given_date):
        filter_list = []
        for activities in self._repository.get_all():
            existing_activity = activities.start_date_time
            if existing_activity.strftime("%Y") == given_date.strftime("%Y") and \
                    existing_activity.strftime("%m") == given_date.strftime("%m") and \
                    existing_activity.strftime("%d") == given_date.strftime("%d"):
                filter_list.append(activities)
        if len(filter_list) == 0:
            raise ServiceException("given date does not exist")
        return sorted(filter_list, key=lambda x: x.start_date_time, reverse=False)

    def get_searched_list_by_given_description(self, given_description):
        filter_list = []
        for activities in self._repository.get_all():
            if given_description in activities.description:
                filter_list.append(activities)
        if len(filter_list) == 0:
            raise ServiceException("given description does not exist")
        return filter_list

    def get_searched_list_by_given_date_time(self, given_date):
        filter_list = []
        for activities in self._repository.get_all():
            existing_activity = activities.start_date_time
            if existing_activity.strftime("%Y") == given_date.strftime("%Y") and \
                    existing_activity.strftime("%m") == given_date.strftime("%m") and \
                    existing_activity.strftime("%d") == given_date.strftime("%d"):
                filter_list.append(activities)
        if len(filter_list) == 0:
            raise ServiceException("given date does not exist")
        return filter_list

    def update(self, activity):
        #self._repository.check_duplicity_of_an_updated_activity(activity)
        updated_activity = self._update(activity)

        undo_call = Call(self._update, updated_activity)
        redo_call = Call(self._update, activity)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        self._undo_service.record(cope)

    def _update(self, activity):
        return self._repository.update(activity)

    def remove(self, activity_id):
        deleted_activity = self._remove(activity_id)

        undo_call = Call(self.__add, deleted_activity)
        redo_call = Call(self._remove, deleted_activity.activity_id)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        self._undo_service.record(cope)

    def _remove(self, activity_id):
        deleted_activity = self._repository.remove(activity_id)
        return deleted_activity

    def add(self, activity):
        #self._repository.check_duplicity_of_a_new_activity(activity)
        added_activity = self.__add(activity)

        undo_call = Call(self._remove, added_activity.activity_id)
        redo_call = Call(self.__add, added_activity)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        self._undo_service.record(cope)

    def __add(self, activity):  # not a direct access because we want to know what operations have been made
        added_activity = self._repository.add(activity)
        return added_activity

    def get_all(self):
        return self._repository.get_all()

