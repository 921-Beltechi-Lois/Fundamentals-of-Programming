import datetime

from src.domain.activity import Activity
from src.domain.person import Person
from src.exception.repo_exception import RepoException
from src.exception.service_exception import ServiceException


class UI:

    def __init__(self, person_service, activity_service, undo_service):
        self.__person_service = person_service
        self.__activity_service = activity_service
        self.__undo_service = undo_service

    def update_person_ui(self):
        given_person_id = int(input("Person_ID that you want to get updated: "))
        option = input("What do you want to update?: Type 'N' for name or 'P' for PHONE number (N / P): ")
        if option == 'N':
            replace_name_with = input("Update current name with following name: ")
            self.__person_service.update(replace_name_with, given_person_id)
        elif option == 'P':
            replace_phone_number_with = input("Update current phone number with following phone number: ")
            self.__person_service.update(replace_phone_number_with, given_person_id)
        else:
            print("wrong ussage of command update person")
        print("Person updated successfully!")

    def remove_person_ui(self):
        person_id = int(input("Person's ID to be deleted: "))
        self.__person_service.remove(person_id)
        print("Person_ID: " + str(person_id) + " has been successfully deleted")
        # self.__activity_service.remove_deleted_person_id_from_activity_list(person_id)

    def add_person_ui(self):
        person_id = int(input("Person ID: "))
        name = input("Name: ")
        name = name.title()
        phone_number = input("Phone number: ")
        person = Person(person_id, name, phone_number)
        if not (name.isnumeric()) and phone_number.isnumeric():
            self.__person_service.add(person)
            print("Person: " + str(person) + " successfully added")
        else:
            print("Given person name / phone number aren't introduced properly")

    def show_person_list_ui(self):
        for person in self.__person_service.get_all():
            print(person)

    def print_menu(self):
        print("Option 1: SHOW list of all people (person_list)")
        print("Option 2: ADD a new person to person_list ")
        print("Option 3: REMOVE a person from person_list")
        print("Option 4: UPDATE a person from person_list")
        print("Option 5: SHOW list of all activities (activity_list)")
        print("Option 6: ADD a new activity to activity_list")
        print("Option 7: REMOVE an activity from activity_list")
        print("Option 8: UPDATE an activity from activity_list")
        print("Option 9: SEARCH from person_list or activity_list")
        print("Option 10: Show different Statistics")
        print("Option 11: Undo")
        print("Option 12: Redo")
        print("Option 13: Exit")

    def start(self):
        while True:
            self.print_menu()
            try:
                option = input("option >> ")
                if option == '1':
                    self.show_person_list_ui()
                elif option == '2':
                    self.add_person_ui()
                elif option == '3':
                    self.remove_person_ui()
                elif option == '4':
                    self.update_person_ui()
                elif option == '5':
                    self.show_activity_list_ui()
                elif option == '6':
                    self.add_activity_ui()
                elif option == '7':
                    self.remove_activity_ui()
                elif option == '8':
                    self.update_activity_ui()
                elif option == '9':
                    self.search_handle_ui()
                elif option == '10':
                    self.statistic_handle_ui()
                elif option == '11':
                    self.__undo_service.undo()
                elif option == '12':
                    self.__undo_service.redo()
                elif option == '13':
                    return
                else:
                    print("bad command")
            except RepoException as error:
                print(str(error))
            except ServiceException as serror:
                print(str(serror))
            except ValueError as ve:
                print(str(ve))

    def show_activity_list_ui(self):
        for activity in self.__activity_service.get_all():
            print(activity)

    def add_activity_ui(self):
        activity_id = int(input("Activity_ID: "))

        list_of_available_person_id = []
        list_of_available_person_id = self.__person_service.get_available_list_of_person_id()
        list = []
        n = int(input("How many people do you want to add in updated_person_list?: "))
        print("Available Person_ID's are:", *sorted(list_of_available_person_id))
        for i in range(0, n):
            elem = int(input("Person_ID: "))
            list.append(elem)

        print("Person_ID: " + str(list))

        year = int(input("start_date_time >> Year: "))
        month = int(input("start_date_time >> Month: "))
        day = int(input("start_date_time >>  Day: "))
        hour = int(input("start_date_time >> Hour: "))
        # minute = int(input("start_date_time >> Minute: "))
        minute = 0
        start = datetime.datetime(year, month, day, hour, minute)

        year_2 = int(input("end_date_time >> Year: "))
        month_2 = int(input("end_date_time >> Month: "))
        day_2 = int(input("end_date_time >>  Day: "))
        hour_2 = int(input("end_date_time >> Hour: "))
        # minute_2 = int(input("end_date_time >> Minute: "))
        minute_2 = 0
        end = datetime.datetime(year_2, month_2, day_2, hour_2, minute_2)

        description = input("Activity name: ")

        activity = Activity(activity_id, list, start, end, description)
        self.__activity_service.add(activity)
        print("Activity: " + str(activity) + " successfully added")

    def remove_activity_ui(self):
        activity_id = int(input('Remove activity_id: '))
        self.__activity_service.remove(activity_id)
        print("Activity_ID " + str(activity_id) + " removed successfully")

    def update_activity_ui(self):
        update_activity_id = int(input("Activity_ID that you want to update: "))
        option = input("What do you want to update?: \nType 'P' to update person_list in this activity\n" \
                       "Type 'T' for changing start_date_time to end_date_time\n" \
                       "Type 'D' for changing description\n" \
                       "Your option: ")
        if option == 'P':
            list = []
            n = int(input("How many people do you want to add in updated_person_list?: "))
            list_of_available_person_id = self.__person_service.get_available_list_of_person_id()
            print("Available person_id:", *sorted(list_of_available_person_id))
            for i in range(0, n):
                elem = int(input("Person_ID: "))
                if elem in list_of_available_person_id:
                    list.append(elem)
            activity = Activity(update_activity_id, list, None, None, None)
            self.__activity_service.update(activity)
            print("Activity has been updated successfully!")
        elif option == 'T':
            year = int(input("start_date_time >> Year: "))
            month = int(input("start_date_time >> Month: "))
            day = int(input("start_date_time >>  Day: "))
            hour = int(input("start_date_time >> Hour: "))
            # minute = int(input("start_date_time >> Minute: "))
            minute = 0
            start_date_time = datetime.datetime(year, month, day, hour, minute)

            year = int(input("end_date_time >> Year: "))
            month = int(input("end_date_time >> Month: "))
            day = int(input("end_date_time >>  Day: "))
            hour = int(input("end_date_time >> Hour: "))
            # minute = int(input("end_date_time >> Minute: "))
            minute = 0
            end_date_time = datetime.datetime(year, month, day, hour, minute)

            activity = Activity(update_activity_id, None, start_date_time, end_date_time, None)
            self.__activity_service.update(activity)
            print("Activity has been updated successfully!")
        elif option == 'D':
            description = input("Set description name: ")
            activity = Activity(update_activity_id, None, None, None, description)
            self.__activity_service.update(activity)
            print("Activity has been updated successfully!")
        else:
            print("Bad command!")

    def search_handle_ui(self):
        option = input("What do you want to search?\n"
                       "(Type 'P' for <person_list> or 'A' for <activity list>): ")
        if option == 'P':
            person_option = input("person_list search >> Type 'N' for <name> OR 'P' for <phone_number>: ")
            if person_option == 'N':
                given_type_string = input("person_list search >> Name: ")
            elif person_option == 'P':
                given_type_string = input("person_list search >> Phone_number: ")
            else:
                print("Bad command")
                return
            given_type_string = given_type_string.title()
            filtered_list = []
            filtered_list = self.__person_service.get_searched_list_by_given_type_string(given_type_string)
            print(*filtered_list, sep="\n")

        elif option == 'A':
            activity_option = input("activity search >> Type 'T' for <time/date> OR 'D' for <description>: ")
            if activity_option == 'T':
                print("Search for activities from a given day (YEAR/MONTH/DAY)")
                year = int(input("activity search >> Year: "))
                month = int(input("activity search >> Month: "))
                day = int(input("activity search >> Day: "))
                filtered_list = []
                given_date = datetime.datetime(year, month, day)
                filtered_list = self.__activity_service.get_searched_list_by_given_date_time(given_date)
                print(*filtered_list, sep="\n")
            elif activity_option == 'D':
                description = input("activity_search >> Description: ")
                description = description.title()
                filtered_list = []
                filtered_list = self.__activity_service.get_searched_list_by_given_description(description)
                print(*filtered_list, sep="\n")
            else:
                print("Bad command")
        else:
            print("Bad command!")

    def statistic_handle_ui(self):
        option = input("Show statistics for: \n"
                       "Option 1: Activities for a given date. List the activities for a given date, \in the order of their start time.\n"
                       "Option 2: Busiest days. Provide the list of upcoming dates with activities, sorted in ascending order of the free time in that day (all intervals with no activities).\n"
                       "Option 3: Activities with a given person. List all upcoming activities to which a given person will participate.\n"
                       "Choose option ('1' / '2' / '3'): ")
        if option == '1':
            print("Type a date ~ (YEAR/MONTH/DAY) in order to list the activities for the given day")
            year = int(input("Year: "))
            month = int(input("Month: "))
            day = int(input("Day: "))
            full_date = datetime.datetime(year, month, day)
            filter_list = []
            filter_list = self.__activity_service.get_statistics_for_a_given_date(full_date)
            print(*filter_list, sep="\n")
        elif option == '2':
            list = []
            list = self.__activity_service.get_statistics_for_busiest_days()
            print(*list, sep="\n")

        elif option == '3':
            print("List all upcoming activities to which a given person will participate")
            person_id = int(input("person_ID: "))
            filtered_list = []
            filtered_list = self.__activity_service.get_statistics_for_a_given_person(person_id)
            print(*filtered_list, sep="\n")
        else:
            print("Bad command!")
