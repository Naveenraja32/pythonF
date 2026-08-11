try:
    number1 , number2 = int(input()) , int(input())
    result = number1/number2
except ZeroDivisionError as zero:
    print(f'{zero} error')
except Exception as e:
    print(type(e).__name__)
else:
    print(result)
finally:
    print('Program Ended')
