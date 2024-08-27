#Credit card validation
sum_odd_digits=0
sum_even_digits=0
total=0

#Remove any '-' or ' ' in the input
card_number=input("Enter credit card number: ")
card_number=card_number.replace("-","")
card_number=card_number.replace(" ","")
card_number=card_number[::-1]

#Add all digits in the odd places from right to left
for x in card_number[::2]:
    sum_odd_digits+=int(x)
    
#Double every second digit from left to right
for x in card_number[1::2]:
    x=int(x)*2
    if x>=10:
        sum_even_digits+=(1+(x%10))
    else:
        sum_even_digits+=int(x)

#Sum of both totals
total=sum_odd_digits+sum_even_digits

#If sum is divisible by 10, the credit card is valid
if total%10==0:
    print("VALID")
else:
    print("INVALID")