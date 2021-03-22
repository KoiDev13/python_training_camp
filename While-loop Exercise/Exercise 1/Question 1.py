#Rewrite the code without using "Break"
five_even_numbers = []
k_number = 1

while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    if k_number % 2 == 0: # nếu k_number là một số chẵn
        five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
    if len(five_even_numbers) == 5: # nếu list này đủ 5 phần tử
        break # thì kết thúc vòng lặp
    k_number += 1

print(five_even_numbers)
# >> [2, 4, 6, 8, 10]
print(k_number)
# >> 10