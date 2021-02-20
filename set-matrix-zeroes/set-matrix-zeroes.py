class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        colList = []
        rowList = []
        
        for row in matrix:
            rowHasZero = False
            for x in range(len(row)):
                if row[x] == 0:
                    colList.append(x)
                    rowHasZero = True
            if rowHasZero:
                matrix[matrix.index(row)] = [0]*len(row)

        for row in matrix:
            for y in range(len(row)):
                if y in colList:
                    index = matrix.index(row)
                    matrix[index][y] = 0