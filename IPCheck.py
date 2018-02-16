

number = input("Input IP Address:")
list_count = ''
count = 0

for i in range(0, len(number)):
    if number[i] in '0123456789':
        count += 1
    else:
        list_count += str(count) + ','
        count = 0
list_count += str(count)

print(list_count)
