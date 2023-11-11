def isValid(sudoku,row_i,col_i,val):
    colList = [row[col_i] for row in sudoku]
    boxI = (row_i//3)*3
    boxJ = (col_i//3)*3
    boxList = [sudoku[boxI][boxJ]  ,sudoku[boxI][boxJ+1]  ,sudoku[boxI][boxJ+2],
               sudoku[boxI+1][boxJ],sudoku[boxI+1][boxJ+1],sudoku[boxI+1][boxJ+2],
               sudoku[boxI+2][boxJ],sudoku[boxI+2][boxJ+1],sudoku[boxI+2][boxJ+2]]
    
    if (val in sudoku[row_i]) or (val in colList) or (val in boxList):return False
    else:return True
    
def solver(sudoku,index=0):
    pseudoku=[[j for j in i] for i in sudoku]
    row_i=index//9
    col_i=index%9
    if pseudoku[row_i][col_i]!=0:
            holder=solver(pseudoku,index+1)
            if holder==None:return None
            else:return holder
    else:    
        for num in range(1,10):
            if isValid(pseudoku,row_i,col_i,num):
                pseudoku[row_i][col_i]=num
                if index==80:
                    return pseudoku
                else:
                    holder=solver(pseudoku,index+1)
                    if holder!=None:
                        return holder
    return None

def psd(sudoku): #for debugging
    print()
    for i in sudoku:print(i)
    print()
        
sudoku = [[0,0,9,0,5,0,0,0,0],
          [0,0,0,0,0,0,7,0,6],
          [0,0,0,0,0,0,0,0,4],
          [4,7,0,0,0,0,6,0,0],
          [0,0,0,3,9,0,0,5,0],
          [0,0,0,8,0,0,0,0,0],
          [0,0,0,2,0,0,0,8,0],
          [6,1,0,0,0,0,0,0,0],
          [7,0,0,0,0,0,0,0,0]]

solved=solver(sudoku)
psd(solved)