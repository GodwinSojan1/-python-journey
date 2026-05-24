a = int(input('enter the mark of sub 1:'))
b = int(input('enter the mark of sub 2:'))
c = int(input('enter the mark of sub 3:'))
d = int(input('enter the mark of sub 4:'))
e = int(input('enter the mark of sub 5:'))
mark = [a,b,c,d,e]
for i in mark:
    print(f'mark is {i}')
highest_mark = max(mark)
print(f"Highest Mark: {highest_mark}")
lowest_mark = min(mark)
print(f"Lowest Mark: {lowest_mark}")
avg = sum(mark)/5
print(f"Average: {avg:.2f}")
