odd = 0
even = 0
total_sum = 0

for x in range(1, 11):
    num = int(input(f"Enter {x}: "))
    total_sum += num
    if num % 2 == 0:
        even += num
    else:
        odd += num 

print(f"The sum of all numbers given is {total_sum}")
print(f"The sum of all odd numbers given is {odd}")
print(f"The sum of all even numbers given is {even}")