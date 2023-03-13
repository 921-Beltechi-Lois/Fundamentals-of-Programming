

from src.domain.activity import Activity
from src.exception.service_exception import ServiceException
from src.services.undo_redo_service import Call, CascadedOperation, Operation


class PersonServices:

    def __init__(self, repository, undo_service, activity_repository):
        self.__repository = repository
        self.__undo_service = undo_service
        self.__activity_repository = activity_repository  # remove person_id --> remove list_of_person_id from act_list

    def get_searched_list_by_given_type_string(self, given_type_string):
        filter_list = []
        for person in self.__repository.get_all():
            if given_type_string in person.name:
                filter_list.append(person)
            elif given_type_string.isnumeric() and given_type_string == person.phone_number:
                filter_list.append(person)
        if len(filter_list) == 0:
            raise ServiceException("given string does not exist")
        return filter_list

    def get_available_list_of_person_id(self):
        return self.__repository.get_available_list_of_person_id()

    def update(self, given_string, given_person_id):
        #self.__repository.check_duplicity_of_an_updated_person(given_string, given_person_id)
        initial_string = self._update(given_string, given_person_id)

        undo_call = Call(self._update, initial_string, given_person_id)
        redo_call = Call(self._update, given_string, given_person_id)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        self.__undo_service.record(cope)

    def _update(self, given_string, given_person_id):
        return self.__repository.update(given_string, given_person_id)

    def remove(self, person_id):

        deleted_person, initial_activities = self.__remove(person_id)

        undo_call = Call(self.__add, deleted_person)
        redo_call = Call(self.__remove, deleted_person.person_id)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        # ini_act = i only need to update / remove from the removed person_id from act_list, no checking for ==
        for activity in initial_activities:
            undo_call = Call(self.__activity_repository.update, activity)
            redo_call = Call(self.__activity_repository.remove_deleted_person_id_from_activity_list,
                             deleted_person.person_id)
            cope.add(Operation(undo_call, redo_call))

        self.__undo_service.record(cope)

    def __remove(self, person_id):
        deleted_person = self.__repository.remove(person_id)

        initial_activities = [] # only initial activities in which person_id participated
        for activity in self.__activity_repository.get_all():
            if person_id in activity.list_of_each_person_id:
                new_act_obj = Activity(activity.activity_id, activity.list_of_each_person_id,
                                       activity.start_date_time, activity.end_date_time, activity.description)
                initial_activities.append(new_act_obj)

        self.__activity_repository.remove_deleted_person_id_from_activity_list(person_id)

        return deleted_person, initial_activities

    def add(self, person):
        #self.__repository.check_duplicity_of_a_new_person(person)
        newPerson = self.__add(person)
        undo_call = Call(self.__remove, newPerson.person_id)
        redo_call = Call(self.__add, newPerson)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        self.__undo_service.record(cope)

    def __add(self, person):
        newPerson = self.__repository.add(person)
        return newPerson

    def get_all(self):
        return self.__repository.get_all()


"""
    def get_by_name_starts_with(self, name):
        filter_list = []
        for person in self.__repository.get_all():
            if person.name.startswith(name):
                filter_list.append(person)
        return filter_list
"""
