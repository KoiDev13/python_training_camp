five_even_numbers = []
k_number = 1

while len(five_even_numbers) < 5:
    if k_number % 2 == 0:
        five_even_numbers.append(k_number)
    k_number += 1
