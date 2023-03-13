import pickle

from src.domain.person import Person
from src.repository.person_repo import Person_Repo


class PersonTextFileRepo(Person_Repo):

    def __init__(self, file_name):
        super().__init__()
        self._text_file = file_name
        self._read_file()

        # super().generate_people()
        # self.generate_people()
        # self._save_file()

    def _read_file(self):
        f = open(self._text_file, 'rt')
        for line in f.readlines():
            person_id, person_name, person_phone_number = line.strip().split(";")
            person_id = int(person_id)
            person = Person(person_id, person_name, person_phone_number)
            super().add(person)  # in memory
        f.close()

    def _save_file(self):
        f = open(self._text_file, 'wt')
        sep = ';'
        # for person in self.get_all():
        for person in super().get_all():
            f.write(str(person.person_id) + sep + person.name + sep + person.phone_number + '\n')
        f.close()

    def add(self, newPerson):
        newPerson = super().add(newPerson)
        self._save_file()
        return newPerson

    def remove(self, given_person_id):
        deleted_person = super().remove(given_person_id)  # person service will delete person_id from act_list
        self._save_file()
        return deleted_person

    def update(self, given_string, given_person_id):
        initial_string = super().update(given_string, given_person_id)
        self._save_file()
        return initial_string


class PersonBinaryFileRepo(Person_Repo):
    def __init__(self, file_name):
        super().__init__()

        self._file_name = file_name
        self._read_file()
        # self.generate_people()
        # self._save_file()

    def _read_file(self):
        f = open(self._file_name, "rb")  # rt -> read, binary
        self.__person_list = pickle.load(f)
        for person in self.__person_list:
            super().add(person)  # add in memory
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self.get_all(), f)
        f.close()

    def __len__(self):
        pass
        # Person_Repo.__len__(self)

    def add(self, newPerson):
        # super(PersonBinaryFileRepo, self).add(entity)
        newPerson = super().add(newPerson)
        self._save_file()
        return newPerson

    def remove(self, given_person_id):
        deleted_person = super().remove(given_person_id)  # person service will delete person_id from act_list
        self._save_file()
        return deleted_person

    def update(self, given_string, given_person_id):
        initial_string = super().update(given_string, given_person_id)
        self._save_file()
        return initial_string
