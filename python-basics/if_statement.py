is_male = True
is_tall = False
if is_male or is_tall:
    print("You are a Male or Tall or Both.")
else:
    print("you are neither a Male nor Tall")

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a Tall Male")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are tall but not a male")
else:
    print("you are neither a male nor tall")

def max_num (num1,num2, num3):
    if num1 >= num2 and num1>=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(21,34,12))
print(max_num(357,149,70))

