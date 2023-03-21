even_digit_num=[]
for num in range(1000,3001):
    check_num=str(num)
    if (int(check_num[0])%2==0) and (int(check_num[1])%2==0) and (int(check_num[2])%2==0) and (int(check_num[3])%2==0):
        even_digit_num.append(check_num)


print(','.join(even_digit_num))
