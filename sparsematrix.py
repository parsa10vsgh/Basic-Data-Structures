class SparseMatrix:
    def __init__(self, matrix):
        self.sparse_matrix = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    self.sparse_matrix.append((i, j, matrix[i][j]))

    def transpose(self):
        transposed_matrix = []
        for element in self.sparse_matrix:
            transposed_matrix.append((element[1], element[0], element[2]))
        self.sparse_matrix = transposed_matrix

    def change_element(self, address, new_value):
        for i in range(len(self.sparse_matrix)):
            if (self.sparse_matrix[i][0], self.sparse_matrix[i][1]) == address:
                self.sparse_matrix[i] = (address[0], address[1], new_value)
                break

    def print_sparse_matrix(self):
        for element in self.sparse_matrix:
            print(element)

matrix = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
]

sparse_mat = SparseMatrix(matrix)
print("Sparse Matrix:")
sparse_mat.print_sparse_matrix()

print("\nTransposing the Sparse Matrix:")
sparse_mat.transpose()
sparse_mat.print_sparse_matrix()

print("\nChanging an Element:")
sparse_mat.change_element((1, 1), 5)
sparse_mat.print_sparse_matrix()
