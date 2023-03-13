# Have at least 10 items in your application at startup
# Provide specification and tests for all non-UI functions related to every functionality


"""
Jane is the administrator of an apartment building and she wants to manage the monthly expenses for each apartment.
Each expense is stored using the following elements:
     apartment (number of apartment, positive integer),
     amount (positive integer),
     type (from one of the predefined categories water, heating, electricity, gas and other).

Write a program that implements the functionalities exemplified below:

(A) Add new transaction add <apartment> <type> <amount>
e.g.
add 25 gas 100 – add to apartment 25 an expense for gas in amount of 100 RON

(B) Modify expenses
remove <apartment>
remove <start apartment> to <end apartment>
remove <type>
replace <apartment> <type> with <amount>
e.g.
remove 15 – remove all expenses for apartment 15
remove 5 to 10 – remove all expenses for apartments between 5 and 10
remove gas – remove all gas expenses from all apartments
replace 12 gas with 200 – replace the amount of the expense with type gas for apartment 12 with 200 RON

(C) Display expenses having different properties
list
list <apartment>
list [ < | = | > ] <amount>
e.g.
list – display all expenses
list 15 – display all expenses for apartment 15
list > 100 - display all apartments having total expenses >100 RON
list = 17 - display all apartments having total expenses =17 RON
"""
#todo tests


def test_for_exceptions():
    test_apartment_list = [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'water', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'gas', 'amount': 19},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'gas', 'amount': 100},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'heating', 'amount': 200}]

    try:
        command_params = '60 water wrong'
        add_transaction_ui(test_apartment_list, command_params)
    except ValueError as ve:
        assert True
    try:
        command_params = '25 gas with wrong'
        replace_amount_of_given_ap_id_and_given_type_of_ap_ui(test_apartment_list, command_params)
    except ValueError as ve:
        assert True


def test_split_command_params():
    # assert crashes if False, does nothing if True
    assert split_command_params('exit') == ('exit', None)
    assert split_command_params('eXiT') == ('exit', None)
    assert split_command_params('add 12 water 45') == ('add', '12 water 45')
    assert split_command_params('   ADD    70  gas  12   ') == ('add', '70 gas 12')
    assert split_command_params('remove 25') == ('remove', '25')
    assert split_command_params('  REMOVE   25 ') == ('remove', '25')
    assert split_command_params('remove 5 to 10') == ('remove', '5 to 10')
    assert split_command_params('REMOVE    5  TO   10') == ('remove', '5 to 10')
    assert split_command_params('remove gas') == ('remove', 'gas')
    assert split_command_params('REMOVE   GAS ') == ('remove', 'gas')
    assert split_command_params('undo     5') == ('undo', '5')
    assert split_command_params('replace 25 gas with 200') == ('replace', '25 gas with 200')
    assert split_command_params('REPLACE  25  GAS  WITH  200 ') == ('replace', '25 gas with 200')
    assert split_command_params('list') == ('list', None)
    assert split_command_params('LIST') == ('list', None)
    assert split_command_params('list 15') == ('list', '15')
    assert split_command_params('LIST   15 ') == ('list', '15')
    assert split_command_params('list > 15') == ('list', '> 15')
    assert split_command_params('LIST   >   15 ') == ('list', '> 15')
    assert split_command_params('list < 15') == ('list', '< 15')
    assert split_command_params('LIST   <   15 ') == ('list', '< 15')
    assert split_command_params('list = 15') == ('list', '= 15')
    assert split_command_params('LIST   =   15 ') == ('list', '= 15')
    assert split_command_params('add abcd') == ('add', 'abcd')


def test_delete_apartment_expenses():
    test_apartment_list = [{'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 200}]
    test_id_ap = 12
    delete_apartment_expenses(test_id_ap, test_apartment_list)
    assert len(test_apartment_list) == 0


def test_replace_amount_of_given_ap_id_and_given_type_of_ap():
    test_apartment_list = [{'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14}]
    test_amount = 200
    test_id_ap = 12
    test_type = 'water'
    replace_amount_of_given_ap_id_and_given_type_of_ap(test_id_ap, test_type, test_amount, test_apartment_list)
    assert get_ap_amount(test_apartment_list[0]) == 200


def test_remove_all_type_of_expenses():
    test_apartment_list = [{'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14}]
    test_given_type_of_expense = 'water'
    remove_all_type_of_expenses(test_given_type_of_expense, test_apartment_list)
    assert test_apartment_list == []


def test_add_transaction():
    test_apartment_list = [{'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14}]
    test_id_ap = 13
    test_type = 'gas'
    test_amount = 100
    add_transaction(test_amount, test_apartment_list, test_id_ap, test_type)
    assert len(test_apartment_list) == 2


def test_remove_all_expenses_from_ap1_to_ap2():
    test_apartment_list = [{'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 10},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'other', 'amount': 11}]
    test_ap_final = 25
    test_ap_initial = 26
    at_least_one_found = remove_all_expenses_from_ap1_to_ap2(test_ap_final, test_ap_initial, test_apartment_list)
    if at_least_one_found == 1:             # there is such id
        assert len(test_apartment_list) == 1


def test_condition_for_comparisons():
    test_apartment_list = [{'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'other', 'amount': 19}]
    compare = '<'
    apartment = {'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14}
    given_amount = 17
    assert condition_for_comparisons(given_amount, apartment, compare) == 1     # amount < 17 found


def test_create_apartments():
    apartment_id = 12
    type = 'gas'
    amount = 100
    assert create_apartments(apartment_id, type, amount) == {'apartment_id': 12, 'type_of_apartment_expense': 'gas', 'amount': 100}


def test_generate_apartments():
    test_apartment_list = []
    test_apartment_list = generate_apartments()
    assert len(test_apartment_list) == 15            # 15 ap already generated in functions


def test_get_ap_id():
    apartment = {'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14}
    assert get_ap_id(apartment) == 12


def test_get_ap_type():
    apartment = {'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14}
    assert get_ap_type(apartment) == 'water'


def test_get_ap_amount():
    apartment = {'apartment_id': 12, 'type_of_apartment_expense': 'water', 'amount': 14}
    assert get_ap_amount(apartment) == 14


def run_all_tests():
    test_split_command_params()
    test_delete_apartment_expenses()
    test_replace_amount_of_given_ap_id_and_given_type_of_ap()
    test_remove_all_type_of_expenses()
    test_add_transaction()
    test_remove_all_expenses_from_ap1_to_ap2()
    test_condition_for_comparisons()
    test_create_apartments()
    test_generate_apartments()
    test_get_ap_id()
    test_get_ap_type()
    test_get_ap_amount()


"""
 Write non-UI functions below
"""


def get_all_transactions_with_type(type, apartment_list):
    """

    :param type: type
    :param apartment_list: ap list
    :return: list <type> - if exists
    """
    list_with_type = []
    for ap in apartment_list:
        if get_ap_type(ap) == type:
            list_with_type.append(ap)
    return list_with_type


def split_command_params(command):
    """
    divide params
    :param command: given command from console
    :return: splitted words
    """

    if command.casefold() == 'list' or command.casefold() == 'exit':
        return command.lower(), None
    tokens = command.split()                 # each element is divided in a list
    command_word = tokens[0].lower()           # ad/remove/list/replace
    tokens1 = ""
    for i in range(len(tokens)):
        if tokens[i].isnumeric() is False: tokens[i] = tokens[i].lower()            # character (TO)
        if i == len(tokens) - 1: tokens1 = tokens1 + tokens[i]                      # last character without " "
        elif i >= 1: tokens1 = tokens1 + tokens[i] + " "
    command_params = tokens1
    return command_word, command_params


def delete_apartment_expenses(id_ap, apartment_list):
    """
    Delete / remove all given id_ap from ap list
    :param id_ap: Ap id
    :param apartment_list: Ap list
    :return: True = ap id deleted successfully - list has been changed; False = no id ap deleted
    """
    list_of_remaining_id_ap = []
    for ap in apartment_list:
        if get_ap_id(ap) != id_ap:  # initial list copied without given ap id
            list_of_remaining_id_ap.append(ap)
    if len(apartment_list) == len(list_of_remaining_id_ap):
        return 0
    else:
        apartment_list[:] = list_of_remaining_id_ap
        return 1


def replace_amount_of_given_ap_id_and_given_type_of_ap(id_ap, type, amount, apartment_list):
    """

    :param id_ap: Ap id
    :param type: Type
    :param amount: Amount
    :param apartment_list: Ap list
    :return: True = amount has been replaced ; False = otherwise
    """
    id_ap = int(id_ap)
    amount = int(amount)
    for ap in apartment_list:
        if get_ap_id(ap) == id_ap and get_ap_type(ap) == type:
            ap['amount'] = amount
            return 1
    return 0


def remove_all_type_of_expenses(given_type_of_expenses, apartment_list):
    """
    Deletes ap id's based on given type of expenses
    :param given_type_of_expenses: Type of ap
    :param apartment_list: Ap list
    :return: True  = types have been eliminated ; False = not even one found in order to be deleted
    """
    list_of_remaining_types_of_ap_expenses = []
    for ap in apartment_list:
        if get_ap_type(ap) != given_type_of_expenses:
            list_of_remaining_types_of_ap_expenses.append(ap)
    if len(apartment_list) == len(list_of_remaining_types_of_ap_expenses):  # no type of exp found
        return 0
    else:
        apartment_list[:] = list_of_remaining_types_of_ap_expenses  # ap list = removed type of ap
        return 1


def add_transaction(amount, apartment_list, id_ap, type):
    """
    Adds transaction to the list of apartments
    :param amount: Given amount
    :param apartment_list: ap list
    :param id_ap: given ap id
    :param type: given type of expense
    :return: Adds to apartment list given parameters, in case of duplicity --> we return a message
    """
    for ap in apartment_list:
        if get_ap_type(ap) == type and get_ap_id(ap) == id_ap:
            raise ValueError("duplicate apartment ID with same type of an expense")
    apartment_list.append(create_apartments(int(id_ap), type, int(amount)))


def remove_all_expenses_from_ap1_to_ap2(ap_final, ap_initial, apartment_list):
    found = 0
    first_found = 0
    at_least_one_found = 0
    for index in range(ap_initial, ap_final + 1):
        found = delete_apartment_expenses(index, apartment_list)
        if found == 1 and first_found == 0:
            at_least_one_found = 1
            first_found = 1
    return at_least_one_found


def condition_for_comparisons(given_amount, apartment, compare):
    """
    :param given_amount: Quantity of an expense
    :param apartment: Apartment ID
    :param compare: Contains a string ( > / < / = ) that needs to  be compared
    :return: TRUE = CONDITION of given amount is true;   FALSE = otherwise
    """
    if compare == '>':
        return get_ap_amount(apartment) > given_amount  # if true show it
    elif compare == '<':
        return get_ap_amount(apartment) < given_amount
    elif compare == '=':
        return get_ap_amount(apartment) == given_amount


def create_apartments(apartment, type, quantity):
    if type.isnumeric() == 1:
        raise ValueError("Cannot create given apartment (type is defined only as string)")
    return {'apartment_id': apartment, 'type_of_apartment_expense': type, 'amount': quantity}


def generate_apartments():
    return [
        create_apartments(25, "water", 10),
        create_apartments(25, "heating", 110),
        create_apartments(25, "electricity", 120),
        create_apartments(25, "gas", 130),
        create_apartments(25, "other", 140),
        create_apartments(21, "water", 100),
        create_apartments(21, "heating", 110),
        create_apartments(21, "electricity", 120),
        create_apartments(21, "gas", 130),
        create_apartments(21, "other", 140),
        create_apartments(23, "water", 100),
        create_apartments(23, "heating", 110),
        create_apartments(23, "electricity", 120),
        create_apartments(23, "gas", 130),
        create_apartments(23, "other", 140)
    ]


def get_ap_id(apartment):
    return apartment['apartment_id']


def get_ap_type(apartment):
    return apartment['type_of_apartment_expense']


def get_ap_amount(apartment):
    return apartment['amount']


"""
  Write the command-driven UI below
"""


def print_list_ui(apartment_list):
    apartment_list.sort(reverse=False, key=get_ap_id)
    for apartment in apartment_list:
        print(get_ap_id(apartment), get_ap_type(apartment), get_ap_amount(apartment))


def print_specific_apartment_id_list_ui(apartment_list, tokens):
    id_apartment = int(tokens[0])
    found = 0
    try:
        for apartment in apartment_list:
            if get_ap_id(apartment) == id_apartment:
                print(apartment)
                found = 1
        if not found:
            raise ValueError("no such id of apartment")
    except ValueError as ve:
        print(str(ve))


def remove_all_expenses_from_ap1_to_ap2_ui(apartment_list, words):
    try:
        if words[1] != 'to':
            raise ValueError("wrong usage of remove command")
        ap_initial = int(words[0])
        ap_final = int(words[2])
        at_least_one_found = remove_all_expenses_from_ap1_to_ap2(ap_final, ap_initial, apartment_list)
        if at_least_one_found == 0:
            print("couldn't remove any expense from ap_id_initial to ap_id_final")
    except ValueError as ve:
        print(str(ve))


# [ > , 15 ]
def print_specific_amount_of_expenses_ui(apartment_list, tokens):
    found_data = 0
    try:
        apartment_list.sort(reverse=False, key=get_ap_id)
        compare = tokens[0]
        given_amount = int(tokens[1])
        for apartment in apartment_list:
            if condition_for_comparisons(given_amount, apartment, compare):
                print(apartment)
                found_data = 1
        if found_data == 0:
            print("given input, list of (>, <, =) has not found required data")
    except ValueError as ve:
        print(str(ve))


# [ <ap id> , <type of expense>, <amount>]
def add_transaction_ui(apartment_list, command_params):
    try:
        id_ap, type, amount = command_params.split(" ")
        id_ap = int(id_ap)
        add_transaction(amount, apartment_list, id_ap, type)
    except ValueError as ve:
        print(str(ve))


def remove_all_expenses_for_ap_id_ui(apartment_list, command_params):
    id_ap = int(command_params)
    if not delete_apartment_expenses(id_ap, apartment_list):
        print("ID of apartment could not be found.")


def remove_all_type_of_expenses_ui(apartment_list, command_params):
    given_type_of_expenses = command_params
    if not remove_all_type_of_expenses(given_type_of_expenses, apartment_list):
        print("no such type of apartment found")


def replace_amount_of_given_ap_id_and_given_type_of_ap_ui(apartment_list, command_params):
    try:
        id_ap, type, non_used_word, amount = command_params.split()
        if non_used_word != 'with':
            raise ValueError("wrong usage of replace command")
        if not replace_amount_of_given_ap_id_and_given_type_of_ap(id_ap, type, amount, apartment_list):
            print("given apartment id or given type of apartment doesn't exist, could not replace any amount")
    except ValueError as ve:
        print(str(ve))


# get LIST
def print_list_with_given_type_ui(apartment_list, tokens):
    type = tokens[0]
    list_with_type = get_all_transactions_with_type(type, apartment_list)
    print(list_with_type)



def handle_remove_ui(apartment_list, command_params):
    words = command_params.split(" ", maxsplit=3)  # [<id1> , to <id2>]
    if len(words) == 3:
        remove_all_expenses_from_ap1_to_ap2_ui(apartment_list, words)  # <id1> to <id2>
    elif len(words) == 1:
        command = words[0]
        if command.isnumeric():
            remove_all_expenses_for_ap_id_ui(apartment_list, command_params)  # <ap_id>
        else:
            remove_all_type_of_expenses_ui(apartment_list, command_params)  # <type_id>
    else:
        print("wrong usage of remove")


def handle_list_ui(apartment_list, command_params, command_word, tokens):
    if command_word == 'list' and len(tokens) == 2 and command_params is None:
        print_list_ui(apartment_list)                                                           # list
    elif command_word == 'list' and len(tokens) == 2 and command_params is not None:            # list = ID_ap / AMOUNT
        tokens = command_params.split()                                                         # token is a list now
        if len(tokens) == 1:
            if tokens[0].isnumeric():
                print_specific_apartment_id_list_ui(apartment_list, tokens)                     # list ID_AP
            else:
                print_list_with_given_type_ui(apartment_list, tokens)                           # get_list - of types @
        else:
            print_specific_amount_of_expenses_ui(apartment_list, tokens)                        # list = AMOUNT: >, <, =



def print_menu():
    print("1. (A) Add a new transaction: add <apartment> <type> <amount>")
    print("2. (B) Modify expenses: remove <apartment>, remove <start apartment> to <end apartment>, remove <type>")
    print("3. (B) replace <apartment> <type> with <amount>")
    print("4. (C) list, list <apartment>, list [ < | = | > ] <amount>")


def start_command():
    print_menu()
    apartment_list = generate_apartments()
    try:
        while True:
            command = input("prompt> ")
            command_word, command_params = split_command_params(command)
            tokens = [command_word, command_params]
            print(command_word, command_params)
            if command_word == 'add':
                add_transaction_ui(apartment_list, command_params)
            elif command_word == 'remove':
                handle_remove_ui(apartment_list, command_params)
            elif command_word == 'replace':
                replace_amount_of_given_ap_id_and_given_type_of_ap_ui(apartment_list, command_params)
            elif command_word == 'list':
                handle_list_ui(apartment_list, command_params, command_word, tokens)
            elif command_word == 'exit':
                return
            else:
                print("Bad command!")
    except ValueError as ve:
        print(str(ve))


run_all_tests()
start_command()


