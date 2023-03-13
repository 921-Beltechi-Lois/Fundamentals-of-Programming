import random


class UI:
    def __init__(self, board, service):
        self._acc_board =board
        self._service = service

    def start(self):
        print(self._acc_board)
        print()
        print()
        print("------------------------")
        print()
        print()
        while True:
            try:
                if self._acc_board.no_of_X == self._acc_board.no_of_O:
                    sym = random.choice(['X', 'O'])
                else:
                    if self._acc_board.no_of_X > self._acc_board.no_of_O:
                        cond = False
                        while cond is False:
                            sym = random.choice(['X', 'O'])
                            if sym == 'X':
                                cond = True
                    if self._acc_board.no_of_O > self._acc_board.no_of_X:
                        cond = False
                        while cond is False:
                            sym = random.choice(['X', 'O'])
                            if sym == 'O':
                                cond = True

                final_list = self._acc_board.check_neighbours(sym)
                row1 = final_list[0][0]
                row2 = final_list[0][1]
                col1 = final_list[1][0]
                col2 = final_list[1][1]

                if self._acc_board.first_turn:
                    #print("Order (computer)'s turn: ")
                    valid_move = False
                    while valid_move == False:
                        row = random.randint(row1, row2)
                        col = random.randint(col1,col2)

                        valid_move = True
                        list = self._acc_board.list_of_row_col  # ??
                        for el in list:
                            if el[0] == row and el[1]== col:
                                valid_move = False






                    self._acc_board.place_symbol(row, col, sym)
                    print(self._acc_board)
                    print("Order (computer) picked row "+ str(row) + " column "+ str(col)+" and the symbol: "+ str(sym))
                    print()
                    print()


                    #won = self._acc_board.check_winner()

                    val = self._acc_board.is_board_full()
                    if val == True:
                        print("Chaos won!")
                        return



                if self._acc_board.first_turn == False:
                    print("Chaos (human)'s turn: ")
                    row = int(input("Row: "))
                    col = int(input("Col: "))
                    sym = input("Symbol X or O: ")

                    self._acc_board.place_symbol(row, col, sym)
                    print(self._acc_board)
                    print()
                    print()

                    # won = self._acc_board.check_winner()
                    val = self._acc_board.is_board_full()
                    if val == True:
                        print("Chaos won!")
                        return




            except Exception as e:
                print(str(e))

