X_COORDINATE = 0
Y_COORDINATE = 1

def main2(a):
    # Step 1. Sort array by x-coordinates using merge sort
    # Θx(n log(n))
    new_a = merge_sort(a)

    # Step 2. Compute number of y-coordinates greater than the y-coordinate of a smaller x-coordinate (load factor) 
    # use a monotonic increasing stack for linear time = Θ(n) *citing GeeksForGeeks*
    temp = {}
    stack = []
    count = 0   
    for point in reversed(new_a):
        while stack and stack[-1] > point[Y_COORDINATE]:
            count += 1
            stack.pop()

        temp[point] = count
        stack.append(point[Y_COORDINATE])
    # Step 3. Determine how many coordinates have the highest load factor 
    # Θ(n) because at most there can be n values with the highest load factor
    answer = []
    max_key = max(temp, key=temp.get)
    max_value = temp[max_key]
    temp.pop(max_key)
    answer.append(max_key)
    while max_value in temp.values():
        i_key = max(temp, key=temp.get)
        answer.append(i_key)
        temp.pop(i_key)
    return answer

def merge_sort(a):
    if len(a) <= 1:
        return a
    middle = len(a)//2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][X_COORDINATE] < right[j][X_COORDINATE]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list += right[j:]
    sorted_list += left[i:]
    return sorted_list

# Test the solution
print(main2([(1,2), (24,5), (2,4)]))