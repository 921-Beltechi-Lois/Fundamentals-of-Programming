from src.domain.person import Person
from src.exception.repo_exception import RepoException


class Person_Repo:

    def __init__(self):
        self.__person_list = []

    def get_available_list_of_person_id(self):
        list_of_available_person_id = []
        for person in self.__person_list:
            list_of_available_person_id.append(person.person_id)
        return list_of_available_person_id

    def update(self, given_string, given_person_id):
        """
        Updates <name> or <phone_number> of the person_list
        :param given_string: Can be numerical (phone_number) or non-numerical (name)
        :param given_person_id: Person_id as a string
        :return: New updated string, name or phone_number
        """
        for person in self.__person_list:
            if given_person_id == person.person_id:
                initial_string = ""
                if not (given_string.isnumeric()):
                    self.check_duplicity_of_an_updated_person(given_string, person.person_id)
                    initial_string = person.name  # for undo
                    person.name = given_string
                if given_person_id == person.person_id and given_string.isnumeric():
                    self.check_duplicity_of_an_updated_person(given_string, person.person_id)
                    initial_string = person.phone_number  # for undo
                    person.phone_number = given_string
                return initial_string
        raise RepoException("No such Person_ID exists in person_list")

    def check_duplicity_of_an_updated_person(self, given_string, person_id):
        for person in self.__person_list:
            if person.person_id != person_id:  # don't compare to the changed value, only to others
                if given_string.strip().title() == person.name.strip().title():
                    raise RepoException("Duplicate name given!")
                elif given_string == person.phone_number:
                    raise RepoException("Duplicate phone_number given!")

    def remove(self, given_id):
        """
        Removes a person from <person_list> by a given_id
        :param given_id: removing id
        :return: deleted_person for undo/redo
        """
        for person in self.__person_list:
            if person.person_id == given_id:
                self.__person_list.remove(person)
                return person
        raise RepoException("Given Person_ID does not exist in the person_list")

    def add(self, newPerson):
        """
        Adds a newPerson to the person_list
        :param newPerson: Contains [person_id, name, phone_number]
        :return: returns the added person
        """
        self.check_duplicity_of_a_new_person(newPerson)
        self.__person_list.append(newPerson)
        return newPerson

    def check_duplicity_of_a_new_person(self, newPerson):
        for person in self.__person_list:
            if person.person_id == newPerson.person_id:
                raise RepoException("Cannot add person because of duplicate person id: " + str(newPerson.person_id))
            if sorted(list(person.name)) == sorted(list(newPerson.name)):
                raise RepoException("Cannot add person because of duplicate name: " + str(newPerson.name))
            if person.phone_number == newPerson.phone_number:
                raise RepoException(
                    "Cannot add person because of duplicate phone number: " + str(newPerson.phone_number))

    def get_all(self):
        return self.__person_list

    def generate_people(self):
        self.__person_list = [
            Person(123, 'Popescu Adrian', '0743594501'),
            Person(124, 'Barna Doina', '0743594402'),
            Person(100, 'Bercovic Dan', '0743594511'),
            Person(122, 'Popescu Mircea', '0741354501'),
            Person(98, 'Ciorna Ioan', '0743591501'),
            Person(55, 'Antonescu Ioan', '0743599501'),
            Person(40, 'Ardelean Ioana', '0743594526'),
            Person(10, 'Burcea Gheorghe', '0731594501'),
            Person(600, 'Fagu Abel', '0723594501'),
            Person(900, 'Horalipa Rebeca', '0783594501'),
            Person(800, 'Ciuciu Felix', '0754594501'),
            Person(555, 'Deac Mirel', '0749024501'),
            Person(95, 'Radoi David', '0743567801'),
            Person(87, 'Vancea Alexandru', '0754370849'),
            Person(12, 'Garcia Eric', '0798794501'),
            Person(20, 'Ferrari Alberto', '0743186501'),
            Person(345, 'Dinu Rares', '0743851301'),
            Person(987, 'Hassan Victor', '0743569401'),
            Person(367, ' Bogosel Florina', '0743537801'),
            Person(145, 'Spiridon Cosmin', '0743107501')
        ]
