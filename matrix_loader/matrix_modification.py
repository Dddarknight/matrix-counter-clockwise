def remove_spaces(str):
    result_list = []
    elem = ''
    for char in str:
        if char == ' ':
            if elem:
                result_list.append(int(elem))
            elem = ''
            continue
        elem += char
    return result_list


def make_list_matrix(given_str):
    string_cleaned = (
        (given_str.replace('+', '')).replace('-', '')).replace('|', '')
    matrix = string_cleaned.split('\n')
    matrix = list(filter(lambda x: x != '', matrix))
    matrix = [remove_spaces(elem) for elem in matrix]
    return matrix


def make_transported(matrix):
    return list(map(list, zip(*matrix)))


def make_counter_clockwise(input_matrix):
    list_matrix = make_list_matrix(input_matrix)
    matrix = make_transported(list_matrix)
    result_matrix = matrix.pop(0)
    while matrix:
        if len(matrix) == 1:
            last_str = matrix[0]
            last_str.reverse()
            result_matrix.extend(last_str)
            return result_matrix
        matrix = make_transported(matrix)
        matrix.reverse()
        result_matrix.extend(matrix.pop(0))
