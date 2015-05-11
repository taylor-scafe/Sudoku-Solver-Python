from myTable import *
from myStack import *

def solve(table,stack):
    """recusive function that uses a backtracking method to solve the sudoku puzzle"""
    table.simple(table.board)
    #Base Case 1
    if table.isBad(table.board):
        solve(stack.pop())
    #Base Case 2
    elif table.isFinished(table.board):
        return board
    else:
        a,b = table.guess(table.board)
        stack.push(a)
        stack.push(b)
        solve(stack.pop())
    
                

stack = myStack()
t = myTable()
t.board[0].setAnswer(6)
t.board[1].setAnswer(0)
t.board[2].setAnswer(7)
t.board[3].setAnswer(0)
t.board[4].setAnswer(3)
t.board[5].setAnswer(8)
t.board[6].setAnswer(0)
t.board[7].setAnswer(5)
t.board[8].setAnswer(0)
t.board[9].setAnswer(0)
t.board[10].setAnswer(0)
t.board[11].setAnswer(0)
t.board[12].setAnswer(0)
t.board[13].setAnswer(2)
t.board[14].setAnswer(1)
t.board[15].setAnswer(0)
t.board[16].setAnswer(0)
t.board[17].setAnswer(4)
t.board[18].setAnswer(4)
t.board[19].setAnswer(0)
t.board[20].setAnswer(0)
t.board[21].setAnswer(0)
t.board[22].setAnswer(0)
t.board[23].setAnswer(6)
t.board[24].setAnswer(7)
t.board[25].setAnswer(0)
t.board[26].setAnswer(0)
t.board[27].setAnswer(1)
t.board[28].setAnswer(0)
t.board[29].setAnswer(0)
t.board[30].setAnswer(0)
t.board[31].setAnswer(0)
t.board[32].setAnswer(0)
t.board[33].setAnswer(8)
t.board[34].setAnswer(9)
t.board[35].setAnswer(0)
t.board[36].setAnswer(0)
t.board[37].setAnswer(0)
t.board[38].setAnswer(0)
t.board[39].setAnswer(0)
t.board[40].setAnswer(0)
t.board[41].setAnswer(0)
t.board[42].setAnswer(0)
t.board[43].setAnswer(0)
t.board[44].setAnswer(0)
t.board[45].setAnswer(0)
t.board[46].setAnswer(7)
t.board[47].setAnswer(8)
t.board[48].setAnswer(0)
t.board[49].setAnswer(0)
t.board[50].setAnswer(0)
t.board[51].setAnswer(0)
t.board[52].setAnswer(0)
t.board[53].setAnswer(5)
t.board[54].setAnswer(0)
t.board[55].setAnswer(0)
t.board[56].setAnswer(4)
t.board[57].setAnswer(8)
t.board[58].setAnswer(0)
t.board[59].setAnswer(0)
t.board[60].setAnswer(0)
t.board[61].setAnswer(0)
t.board[62].setAnswer(7)
t.board[63].setAnswer(8)
t.board[64].setAnswer(0)
t.board[65].setAnswer(0)
t.board[66].setAnswer(2)
t.board[67].setAnswer(9)
t.board[68].setAnswer(0)
t.board[69].setAnswer(0)
t.board[70].setAnswer(0)
t.board[71].setAnswer(0)
t.board[72].setAnswer(0)
t.board[73].setAnswer(5)
t.board[74].setAnswer(0)
t.board[75].setAnswer(6)
t.board[76].setAnswer(4)
t.board[77].setAnswer(0)
t.board[78].setAnswer(1)
t.board[79].setAnswer(0)
t.board[80].setAnswer(2)
t.fill(t.board)
stack = myStack()
solve(t,stack)
