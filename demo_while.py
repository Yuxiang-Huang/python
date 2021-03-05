def sum_thing(n):
    # get the ones digit
    ones = n % 10
    # get the tens digit
    tens = n // 10 % 10
    # return the sum of ones + tens
    return ones + tens

#print(sum_thing(24))
#print(sum_thing(105))


# while loop
# repeat code until boolean_expression is false
i = 1
while i < 100:    
    print(i)
    i*= 2 #i = i * 2
   