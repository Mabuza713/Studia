import numpy as np


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    """ It does rotatae the image but i wont replace numbers in same position lieke for what """
    
    matrix = np.matrix(matrix).T
    for i ,row in enumerate(matrix):
        row = np.array(row).tolist()[0]
        index = len(row) - 1
        row_copy = row.copy()
        for number in range(len(row)):
            row[number] = row_copy[index]
            index -= 1
        matrix[i, ] = row


    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)