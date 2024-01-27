import numpy as np

def multiply_matrices(matrix_a, matrix_b):
    matrix_a = np.array(matrix_a).astype(float)
    matrix_b = np.array(matrix_b).astype(float)
    return np.matmul(matrix_a, matrix_b)

def calculate_determinant(input_matrix):
    return np.linalg.det(np.array(input_matrix).astype(float))

def calculate_inverse(input_matrix):
    return np.linalg.inv(np.array(input_matrix))

def custom_round(value, decimal_places):
    return np.round(value, decimals=decimal_places)

def round_and_replace(matrix_array, decimal_places):
    array_rounded = np.round(matrix_array, decimals=decimal_places)
    for i in range(matrix_array.shape[0]):
        for j in range(matrix_array.shape[1]):
            matrix_array[i, j] = array_rounded[i, j]

file_path = "C:/Users/pc/Desktop/maram/input.txt"
input_matrices = []

line_count, matrix_count, current_matrix_count, first_line = 0, 0, 1, True

with open(file_path, "r") as file_input:
    for line in file_input:
        if ''.join(filter(str.isdigit, line)):
            temp_data = line.replace("\n", "").split(" ")
            if first_line:
                first_line = False
                matrix_count = int(temp_data[1])
                for _ in range(int(temp_data[0])):
                    input_matrices.append([])
            else:
                input_matrices[line_count].append([float(x) for x in temp_data])
                if current_matrix_count != matrix_count:
                    current_matrix_count += 1
                else:
                    current_matrix_count = 1
                    line_count += 1

max_determinant_info = None

for matrix_idx in range(len(input_matrices)):
    for remaining_matrices_idx in range(matrix_idx + 1, len(input_matrices)):
        temp_multiplication = multiply_matrices(input_matrices[matrix_idx], input_matrices[remaining_matrices_idx])
        temp_determinant = float(calculate_determinant(temp_multiplication))
        if max_determinant_info is None or temp_determinant > float(max_determinant_info["determinant"]):
            max_determinant_info = {
                "determinant": temp_determinant,
                "matrix1": input_matrices[matrix_idx],
                "matrix2": input_matrices[remaining_matrices_idx]
            }

if float(calculate_determinant(max_determinant_info["matrix1"])) > float(calculate_determinant(max_determinant_info["matrix2"])):
    final_multiplication = multiply_matrices(max_determinant_info["matrix1"], max_determinant_info["matrix2"])
elif float(calculate_determinant(max_determinant_info["matrix2"])) > float(calculate_determinant(max_determinant_info["matrix1"])):
    final_multiplication = multiply_matrices(max_determinant_info["matrix2"], max_determinant_info["matrix1"])
else:
    final_multiplication = multiply_matrices(max_determinant_info["matrix1"], max_determinant_info["matrix2"])

inverse_array = np.array(calculate_inverse(final_multiplication))
round_and_replace(inverse_array, 3)

for row in inverse_array:
    print(" ".join(map("{:.3f}".format, row)))
