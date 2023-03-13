"""
  User interface module
"""
from copy import deepcopy

from functions import get_ap_id, get_ap_type, get_ap_amount, delete_apartment_expenses, condition_for_comparisons, \
    add_transaction, remove_all_type_of_expenses, replace_amount_of_given_ap_id_and_given_type_of_ap, \
    generate_apartments, split_command_params, remove_all_expenses_from_ap1_to_ap2, get_all_transactions_with_type, \
    sum_of_all_transactions_with_type, compute_max_amount_of_a_given_id_ap, \
    filter_amount_by_keeping_only_smaller_than_given_one, filter_type, undo, compute_sorted_amount_of_expenses_per_each_ap_id, \
    compute_sorted_amount_of_expenses_per_each_type


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
    try:
        if not delete_apartment_expenses(id_ap, apartment_list):
            print("ID of apartment could not be found.")
    except ValueError as ve:
        print(str(ve))


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


def display_total_amount_of_ap_expenses_having_given_type_ui(apartment_list, command_params):
    if command_params.isnumeric():
        raise ValueError("wrong usage of command sum, use instead: sum <type>")
    try:
        type = command_params
        list_with_type = get_all_transactions_with_type(type, apartment_list)
        sum = sum_of_all_transactions_with_type(list_with_type)
        print(list_with_type)
        print(sum)
    except ValueError as ve:
        print(str(ve))


def display_list_of_sorted_ap_by_total_amount_of_expenses_ui(apartment_list):
    try:
        list_of_an_ap_with_total_amount_of_expenses = []
        list_of_an_ap_with_total_amount_of_expenses = compute_sorted_amount_of_expenses_per_each_ap_id(apartment_list)
        print(list_of_an_ap_with_total_amount_of_expenses)
    except ValueError as ve:
        print(str(ve))


def display_maximum_amount_per_each_expense_type_for_given_id_ap_ui(apartment_list, command_params):
    try:
        id_ap = command_params
        id_ap = int(id_ap)
        expense_type_of_max_amount, max_amount_expense_of_given_id_ap = compute_max_amount_of_a_given_id_ap(apartment_list,
                                                                                                            id_ap)
        if max_amount_expense_of_given_id_ap == 0:
            raise ValueError("no such id of ap found")
        for ap in apartment_list:
            if get_ap_id(ap) == id_ap and get_ap_amount(ap) == max_amount_expense_of_given_id_ap and \
                    get_ap_type(ap) == expense_type_of_max_amount:
                print(ap)
                break
    except ValueError as ve:
        print(str(ve))


def display_total_amount_of_expenses_for_each_type_sorted_by_amount_of_money_ui(apartment_list):
    try:
        list_of_expenses_per_each_type = compute_sorted_amount_of_expenses_per_each_type(apartment_list)
        print(list_of_expenses_per_each_type)
    except ValueError as ve:
        print(str(ve))


def filter_ui(apartment_list, command_params):
    try:
        new_list = []
        if command_params.isnumeric():                      # filter amount
            amount = command_params
            amount = int(amount)
            new_list = filter_amount_by_keeping_only_smaller_than_given_one(apartment_list, amount)
        else:                                              # filter type
            type = command_params
            new_list = filter_type(apartment_list, type)
        if new_list == []:
            raise ValueError("filtered list couldn't be created because given type / amount haven't been found or given input is wrong")
        apartment_list.clear()
        apartment_list[:] = new_list
        for ap in apartment_list:
            print(ap)
    except ValueError as ve:
        print(str(ve))


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
                print_list_with_given_type_ui(apartment_list, tokens)                          # noget_list - of types @
        else:
            print_specific_amount_of_expenses_ui(apartment_list, tokens)                        # list = AMOUNT: >, <, =


def handle_sort_ui(apartment_list, command_params):
    if command_params == 'apartment':
        display_list_of_sorted_ap_by_total_amount_of_expenses_ui(apartment_list)
    elif command_params == 'type':
        display_total_amount_of_expenses_for_each_type_sorted_by_amount_of_money_ui(apartment_list)
    else:
        raise ValueError("wrong usage of sort command, type instead: sort apartment or sort type")


def print_menu():
    print("1. (A) Add a new transaction: add <apartment> <type> <amount>")
    print("2. (B) Modify expenses: remove <apartment>, remove <start apartment> to <end apartment>, remove <type>")
    print("3. (B) replace <apartment> <type> with <amount>")
    print("4. (C) list, list <apartment>, list [ < | = | > ] <amount>")
    print("5. (D) Different characteristics of the expenses:sum <type>, max <apartment>, sort apartment, sort type")
    print("6. (E) Filter: filter <type>, filter <value>")
    print("7. (F) Undo: undo")

def start_command():
    print_menu()
    apartment_list = generate_apartments()
    l1 = deepcopy(apartment_list)            # current list
    undo_list = [l1]                         # undo_list[0] = initial list   [ [],   ]
    try:
        while True:
            command = input("prompt> ")
            command_word, command_params = split_command_params(command)
            tokens = [command_word, command_params]
            print(command_word, command_params)
            if command_word == 'add':
                l1 = deepcopy(apartment_list)  # current list after been modified
                add_transaction_ui(apartment_list, command_params)
                undo_list.append(l1)                                        # [0] - initial, [1] - added af modified one
            elif command_word == 'remove':
                handle_remove_ui(apartment_list, command_params)
                l1 = deepcopy(apartment_list)
                undo_list.append(l1)
            elif command_word == 'replace':
                l1 = deepcopy(apartment_list)
                replace_amount_of_given_ap_id_and_given_type_of_ap_ui(apartment_list, command_params)
                undo_list.append(l1)
            elif command_word == 'list':
                handle_list_ui(apartment_list, command_params, command_word, tokens)
            elif command_word == 'sum':
                display_total_amount_of_ap_expenses_having_given_type_ui(apartment_list, command_params)
            elif command_word == 'max':
                display_maximum_amount_per_each_expense_type_for_given_id_ap_ui(apartment_list, command_params)
            elif command_word == 'sort':
                handle_sort_ui(apartment_list, command_params)
            elif command_word == 'filter':
                l1 = deepcopy(apartment_list)
                filter_ui(apartment_list, command_params)
                undo_list.append(l1)
            elif command_word == 'undo':
                apartment_list = undo(undo_list)
            elif command_word == 'exit':
                return
            else:
                print("Bad command!")
    except ValueError as ve:
        print(str(ve))
