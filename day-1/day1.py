def calculate_total_distance_from_file(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)
    
    total_distance = sum(abs(l - r) for l, r in zip(left_list_sorted, right_list_sorted))
    
    return total_distance

file_path = '.\prova.txt'
total_distance = calculate_total_distance_from_file(file_path)
print(f"Total distance between the lists: {total_distance}")
