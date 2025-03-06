def input_matrix(rows, cols):
    """Input a matrix from the user."""
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            raise ValueError("Number of columns does not match.")
        matrix.append(row)
    return matrix

def multiply_matrices(matrix_a, matrix_b):
    """Multiply two matrices."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        raise ValueError("Number of columns in A must equal number of rows in B.")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def display_matrix(matrix):
    """Display a matrix."""
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Input matrices
    rows_a = int(input("Enter the number of rows for the first matrix: "))
    cols_a = int(input("Enter the number of columns for the first matrix: "))
    matrix_a = input_matrix(rows_a, cols_a)

    rows_b = int(input("Enter the number of rows for the second matrix: "))
    cols_b = int(input("Enter the number of columns for the second matrix: "))
    matrix_b = input_matrix(rows_b, cols_b)

    # Multiply matrices
    try:
        result_matrix = multiply_matrices(matrix_a, matrix_b)
        print("Result of multiplication:")
        display_matrix(result_matrix)
    except ValueError as e:
        print(e)
