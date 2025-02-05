def gauss_elimination(A, b):
    n = len(A)
    
    augmented_matrix = [A[i] + [b[i]] for i in range(n)]
    
    for i in range(n):
        if augmented_matrix[i][i] == 0:
            raise ValueError("Zero pivot encountered, the system might have no unique solution")
        
        for j in range(i + 1, n):
            ratio = augmented_matrix[j][i] / augmented_matrix[i][i]
            for k in range(i, n + 1):
                augmented_matrix[j][k] -= ratio * augmented_matrix[i][k]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i][n] / augmented_matrix[i][i]
        for j in range(i - 1, -1, -1):
            augmented_matrix[j][n] -= augmented_matrix[j][i] * x[i]

    return x

A = [[2, -1], [3, 3]]
b = [3, 0]

solution = gauss_elimination(A, b)
print("Solution:", solution)
