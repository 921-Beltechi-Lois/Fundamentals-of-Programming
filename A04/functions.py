"""
  Program functionalities module
"""


def split_command_params(command):
    """
    divide params
    :param command: given command from console
    :return: splitted words
    """

    if command.casefold() == 'list' or command.casefold() == 'exit' or command.casefold() == 'undo':
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


def sum_of_all_transactions_with_type(list_with_type):
    """

    :param list_with_type: list containing only aps with given type
    :return: sum of expenses of this type
    """
    sum = 0
    for ap in list_with_type:
        sum = sum + get_ap_amount(ap)
    return sum


def compute_sorted_amount_of_expenses_per_each_ap_id(apartment_list):
    """

    :param apartment_list: Ap list
    :return: sorted list of tuples, crt: total AMOUNT of each ap_id:   (id_ap, total_amount)
    """
    list_id_sum_ap = []                                 # [(ap, s), ()]
    for ap in apartment_list:
        ok_1 = 0
        for i in range(len(list_id_sum_ap)):
            if get_ap_id(ap) == list_id_sum_ap[i][0]:
                s = list_id_sum_ap[i][1] + get_ap_amount(ap)
                list_id_sum_ap[i] = (get_ap_id(ap), s)
                ok_1 = 1
                break
        if not ok_1: list_id_sum_ap.append((get_ap_id(ap), get_ap_amount(ap)))
    list_id_sum_ap = sorted(list_id_sum_ap, key=lambda x: x[1], reverse=False)
    return list_id_sum_ap


def compute_max_amount_of_a_given_id_ap(apartment_list, id_ap):
    """

    :param apartment_list: Ap list
    :param id_ap: id of an ap
    :return: Returns MAX amount of a given id_ap and its own expense TYPE
    """
    max_amount_expense_of_given_id_ap = 0
    expense_type_of_max_amount = ''
    for ap in apartment_list:
        if get_ap_id(ap) == id_ap and get_ap_amount(ap) > max_amount_expense_of_given_id_ap:
            max_amount_expense_of_given_id_ap = get_ap_amount(ap)
            expense_type_of_max_amount = get_ap_type(ap)
    return expense_type_of_max_amount, max_amount_expense_of_given_id_ap


def filter_type(apartment_list, type):
    """

    :param apartment_list: Ap list
    :param type: Given type
    :return: a new list that contains only given_type
    """
    copy_ap_list = apartment_list.copy()
    for ap in apartment_list:
        if get_ap_type(ap) != type:
            copy_ap_list.remove(ap)
    return copy_ap_list


def filter_amount_by_keeping_only_smaller_than_given_one(apartment_list, amount):
    """

    :param apartment_list: Ap list
    :param amount: given amount
    :return: list that contains ap list with amount < given_amount
    """
    copy_ap_list = apartment_list.copy()
    for ap in apartment_list:
        if get_ap_amount(ap) >= amount:
            copy_ap_list.remove(ap)
    return copy_ap_list


def undo(list):
    """
    undo
    :return: un-did
    """
    if len(list) >= 2:
        del list[len(list)-1]       # deletes last one in the list
        return list[len(list)-1]    # before last
    else:
        print('Nothing left to Undo')
        return list[0]


def compute_sorted_amount_of_expenses_per_each_type(apartment_list):
    """

    :param apartment_list: Ap list
    :return: sorted list of tuples, crt: total AMOUNT of each TYPE:   (type, total_amount)
    """
    list_of_expenses_per_each_type = []
    for ap in apartment_list:
        ok_1 = 0
        for i in range(len(list_of_expenses_per_each_type)):
            if get_ap_type(ap) == list_of_expenses_per_each_type[i][0]:
                s = list_of_expenses_per_each_type[i][1] + get_ap_amount(ap)
                list_of_expenses_per_each_type[i] = (get_ap_type(ap), s)
                ok_1 = 1
                break
        if ok_1 == 0:
            list_of_expenses_per_each_type.append((get_ap_type(ap), get_ap_amount(ap)))
    list_of_expenses_per_each_type = sorted(list_of_expenses_per_each_type, key=lambda x: x[1], reverse=False)
    return list_of_expenses_per_each_type