class Person:

    def __init__(self, person_id, name, phone_number):
        self._person_id = person_id
        self._name = name
        self._phone_number = phone_number

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def __str__(self):
        return f' Person_ID: {self._person_id}, Name: {self._name}, Phone Number: {self._phone_number}'
