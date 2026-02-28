from multiprocessing import Process, Queue


def multiply_row(row_index, row_values, matrix_b, q):
    cols_b = len(matrix_b[0])
    result_row = []

    for j in range(cols_b):
        value = 0
        for k in range(len(row_values)):
            value += row_values[k] * matrix_b[k][j]
        result_row.append(value)

    print(f"Process row-{row_index}: {result_row}")
    q.put((row_index, result_row))


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

    print("Parallel Matrix Multiplication")
    print(f"A = {matrix_a}")
    print(f"B = {matrix_b}")

    q = Queue()
    processes = []

    for i, row in enumerate(matrix_a):
        process = Process(target=multiply_row, args=(i, row, matrix_b, q))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    result = [None] * len(matrix_a)
    while not q.empty():
        row_index, row_result = q.get()
        result[row_index] = row_result

    print(f"Result = {result}")