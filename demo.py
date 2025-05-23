evens = []

for number in range(100):
    is_even = number % 2 ==0
    if is_even:
        evens.append(number)

print(evens)
