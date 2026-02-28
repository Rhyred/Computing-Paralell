def matrix_multiply_sequential(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


if __name__ == "__main__":
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    matrix_b = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

    print("Sequential Matrix Multiplication")
    print(f"A = {matrix_a}")
    print(f"B = {matrix_b}")

    result = matrix_multiply_sequential(matrix_a, matrix_b)
    print(f"Result = {result}")