def make_even (num_list):
    result = []
    for i in range (len(num_list)):
        if num_list [i] % 2 == 0:
            result.append(num_list[i])
    return result

def print_list (prompt, num_list):
    print(prompt,end= ': ')
    for i in range(len((num_list))):
        print(num_list[i], end= ' ')

