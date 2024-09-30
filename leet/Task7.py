import numpy as np
grid =[["1","1","1"],["0","1","0"],["0","1","0"]]
class OBJ:
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Creating new matrix expended with None values
        # cuz i am a little lazy
        new_matrix = np.full(shape = (len(grid) + 2, len(grid[0]) + 2), fill_value= None)   
        for i in range(1,len(grid) + 1):
            for j in range(1, len(grid[i - 1]) + 1):
                new_matrix[i, j] = grid[i - 1][j - 1] 

        
        self.result_counter = 0
        def findAdjacentValues(self, row, col, new_island):
            if new_matrix[row, col] == "1" and new_island == True:
                self.result_counter += 1
                new_matrix[row, col] = None
            elif new_matrix[row, col] == "1":
                new_matrix[row,col] = None
            else:
                return
            
            for i in range(-1,2, 2):
                if (new_matrix[row - i][col] != None and new_matrix[row - i][col] != "0"):

                    findAdjacentValues(self, row - i, col, False)
            for i in range(-1,2, 2):
                if (new_matrix[row][col -i] != None and new_matrix[row][col - i] != "0"):

                    findAdjacentValues(self, row, col - i, False)
            


        # If first checked value will be "1" then we will go increase result_counter by one and go through all adjacentValues to clean them up
        # if value is None or "0" function will eather not go through or just break after first if statement

        for i in range(1, len(new_matrix) - 1):
            for j in range(1, len(new_matrix[0]) -1):
                if (new_matrix[i, j] != None):
                    findAdjacentValues(self, i,j, True)


        return self.result_counter
test = OBJ()
print(test.numIslands(grid))