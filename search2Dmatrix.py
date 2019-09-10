# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        flag = False
        for j in range(len(matrix[0])):
            if target == matrix[0][j]:
                flag = True
                return True

        if flag == False:
            for i in range(1, len(matrix)):
                if target >= matrix[i - 1][0] and target <= matrix[i][-1]:
                    for j in range(len(matrix[i])):
                        if target == matrix[i][j]:
                            flag = True
                            return True

                    if flag == False:
                        return False