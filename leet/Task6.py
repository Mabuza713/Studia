import numpy as np
def spiralOrder(matrix):
    """
    I'll make 4 pointers and 4 max/min values in every direction and 
    if pointer will achive max/min value it will add/substract a value from max/min
    
    other idea might be better
    """
    output = [0]
    new_matrix = np.full(fill_value= None, shape = (len(matrix) + 2, len(matrix[0]) + 2))
    for col_index in range(len(matrix[0])):
        for row_index in range(len(matrix)):
            new_matrix[row_index + 1, col_index + 1] = matrix[row_index][col_index]

    row, col = 1, 1
    print(new_matrix)
    while (len(output) != len(matrix) * len(matrix[0])):
        
        while (new_matrix[col, row + 1] != None):
            output.append(new_matrix[col, row])
            new_matrix[col, row] = None

            row += 1

        while(new_matrix[col + 1, row] != None):
            output.append(new_matrix[col, row])
            new_matrix[col, row] = None
            
            col += 1
        
        while (new_matrix[col, row - 1] != None):
            output.append(new_matrix[col, row])
            new_matrix[col, row] = None
            
            row -= 1
        
        while (new_matrix[col - 1, row] != None):
            output.append(new_matrix[col, row])
            new_matrix[col, row] = None
            
            col -= 1

    output.append(new_matrix[col,row])
    return output[1:]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiralOrder(matrix)
    
    
    
    