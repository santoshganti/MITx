x = 5
if x % 2 == 0:
    if x % 3 == 0:
        print('Divisible by 2 and 3')
    else:
          print('Divisiible by 2 and not by 3')
elif x % 3 == 0:
        print('Divisible by 3 and not by 2')
else:
    print('Not divisible by 2 or 3')
