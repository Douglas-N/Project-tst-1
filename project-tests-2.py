# practing try:except

def divide_1000_by_user_input():
    user_input = input("Please add a number ")
    try: 
        result = float(1000 /int(user_input))
        print(result)
    except ZeroDivisionError:
        print("Division by zero only possyble on Calculus. Try mmath lybrary")

divide_1000_by_user_input()





