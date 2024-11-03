def find_common_participants(list1, list2, separator=","):
    fixed_list1 = set(list1.split(separator))
    fixed_list2 = set(list2.split(separator))
    intersection_list = fixed_list1.intersection(fixed_list2)
    return sorted(intersection_list)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(result)