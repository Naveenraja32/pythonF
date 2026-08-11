try:
    number1 , number2 = int(input("Enter the first number: ")) , int(input("Enter the second number: "  ))
    result = number1/number2
except ZeroDivisionError as zero:
    print(f'{zero} error')
except Exception as e:
    print(type(e).__name__)
# except ValueError :
#     print('Value Error')
# except ZeroDivisionError:
#     print('Zero Division Error')
else:
    print(result)
finally:
    print('Program Ended')
