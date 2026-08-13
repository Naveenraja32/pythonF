try:
    number1 , number2 = int(input("Enter the first number: ")) , int(input("Enter the second number: "  ))
    result = number1/number2
    arr = [1,2,3,4,5]
    print(arr[5])  # This will cause an IndexError
except ZeroDivisionError as zero:
    print(f'{zero} error')
except IndexError as index:
    print(f'{index} error')
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
