a = [7,13,5,2,9,5]

def second_largest(a):
    largest = a[0]
    sec_largest = a[0]
    
    for i in a:
        if i < largest and i > sec_largest:
            sec_largest = i
        elif i > largest and i > sec_largest:
            largest,sec_largest = i,largest
    
    return sec_largest

print(second_largest(a))