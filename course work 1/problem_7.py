# PROBLEM  7

# Write a program to Use a loop to display elements from a given list present at odd index position



n = int(input('Enter Integer :'))
def elements_at_odd_indices(n):
    result = [] # empty list
    
    for i in range(len(n)):
        if i % 2 != 0:
            result.append(n[i])
    
    return result

output_list = elements_at_odd_indices(n)
print(output_list)

