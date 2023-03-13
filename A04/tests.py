from functions import split_command_params, delete_apartment_expenses, \
    replace_amount_of_given_ap_id_and_given_type_of_ap, remove_all_type_of_expenses, add_transaction, \
    remove_all_expenses_from_ap1_to_ap2, condition_for_comparisons, generate_apartments, create_apartments, get_ap_id, \
    get_ap_type, get_ap_amount, get_all_transactions_with_type, sum_of_all_transactions_with_type, \
    compute_sorted_amount_of_expenses_per_each_ap_id, compute_max_amount_of_a_given_id_ap, filter_type, \
    filter_amount_by_keeping_only_smaller_than_given_one, compute_sorted_amount_of_expenses_per_each_type, undo
from ui import add_transaction_ui, replace_amount_of_given_ap_id_and_given_type_of_ap_ui


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
    assert split_command_params('sum gas') == ('sum', 'gas')
    assert split_command_params('max 25') == ('max', '25')
    assert split_command_params('sort apartment') == ('sort', 'apartment')
    assert split_command_params('sort type') == ('sort', 'type')
    assert split_command_params('filter gas') == ('filter', 'gas')
    assert split_command_params('filter 300') == ('filter', '300')
    assert split_command_params('undo') == ('undo', None)


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


# get list
def test_get_all_transactions_with_type():
    test_apartment_list = [{'apartment_id': 12, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'other', 'amount': 19}]
    type = 'gas'
    new_list = get_all_transactions_with_type(type, test_apartment_list)
    assert len(new_list) == 2


def test_sum_of_all_transactions_with_type():
    list_with_same_type=[{'apartment_id': 12, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'gas', 'amount': 19}]
    assert sum_of_all_transactions_with_type(list_with_same_type) == 53


def test_compute_sorted_amount_of_expenses_per_each_ap_id():
    test_apartment_list = [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'water', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'electricity', 'amount': 19},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'other', 'amount': 100},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'electricity', 'amount': 200}]
    new_list = compute_sorted_amount_of_expenses_per_each_ap_id(test_apartment_list)
    assert new_list == [(25, 34), (26, 38), (20, 300)]


def test_compute_max_amount_of_a_given_id_ap():
    test_apartment_list = [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'water', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'electricity', 'amount': 19},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'other', 'amount': 100},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'electricity', 'amount': 200}]
    given_id_ap = 25
    received_expense, max_amount_of_ap_id = compute_max_amount_of_a_given_id_ap(test_apartment_list, given_id_ap)
    assert received_expense == 'water'
    assert max_amount_of_ap_id == 20


def test_filter_type():
    test_apartment_list = [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'water', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'electricity', 'amount': 19},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'other', 'amount': 100},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'heating', 'amount': 200}]
    given_type = 'heating'
    list_containing_only_given_type = filter_type(test_apartment_list, given_type)
    assert list_containing_only_given_type == [{'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                                               {'apartment_id': 20, 'type_of_apartment_expense': 'heating', 'amount': 200}]


def test_filter_amount_by_keeping_only_smaller_than_given_one():
    test_apartment_list = [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'water', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'electricity', 'amount': 19},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'other', 'amount': 100},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'heating', 'amount': 200}]
    given_amount = 19
    new_list = filter_amount_by_keeping_only_smaller_than_given_one(test_apartment_list, given_amount)
    assert new_list == [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14}]


def test_compute_sorted_amount_of_expenses_per_each_type():
    test_apartment_list = [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'water', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'gas', 'amount': 19},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'gas', 'amount': 100},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'heating', 'amount': 200}]
    new_list = compute_sorted_amount_of_expenses_per_each_type(test_apartment_list)
    assert new_list == [('water', 20), ('gas', 133), ('heating', 219)]


def test_undo():
    test_apartment_list = [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'water', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'gas', 'amount': 19},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'gas', 'amount': 100},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'heating', 'amount': 200}]
    id_ap = 25
    #l1 = []
    #l1[:] = test_apartment_list
    #undo_list = []
    #undo_list.append(l1)
    delete_apartment_expenses(id_ap, test_apartment_list)
    #undo_list.append(l1)  # x2
    # test_apartment_list = undo(undo_list)
    undo(test_apartment_list)
    assert test_apartment_list == [{'apartment_id': 25, 'type_of_apartment_expense': 'gas', 'amount': 14},
                           {'apartment_id': 25, 'type_of_apartment_expense': 'water', 'amount': 20},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'heating', 'amount': 19},
                           {'apartment_id': 26, 'type_of_apartment_expense': 'gas', 'amount': 19},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'gas', 'amount': 100},
                           {'apartment_id': 20, 'type_of_apartment_expense': 'heating', 'amount': 200}]


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
    test_get_all_transactions_with_type()
    test_sum_of_all_transactions_with_type()
    test_compute_sorted_amount_of_expenses_per_each_ap_id()
    test_compute_max_amount_of_a_given_id_ap()
    test_filter_type()
    test_filter_amount_by_keeping_only_smaller_than_given_one()
    test_compute_sorted_amount_of_expenses_per_each_type()
    test_for_exceptions()
