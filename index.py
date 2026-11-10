# Initial array of students' scores
scores = [45, 80, 65, 90, 55]

# LIST OPERATION
print("Original Array:", scores)

# SEARCH OPERATION
search_value = 65

if search_value in scores:
    print(search_value, "found at index", scores.index(search_value))
else:
    print(search_value, "not found")

# SORT OPERATION
scores.sort()
print("Sorted Array:", scores)

# DELETE OPERATION
delete_value = 80

if delete_value in scores:
    scores.remove(delete_value)
    print("After Deletion:", scores)
else:
    print("Value not found")

# INSERT OPERATION
insert_value = 70
insert_position = 2

scores.insert(insert_position, insert_value)
print("After Insertion:", scores)