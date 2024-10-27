def create_array():
    n = 7
    array = [[0 for _ in range(n)] for _ in range(n)];

    for i in range(n):
        for j in range(i, n):
            array[i][j] = 1
            array[n - i - 1][j] = 1
    for row in array:
        print(''.join(map(str, row)))

create_array()
