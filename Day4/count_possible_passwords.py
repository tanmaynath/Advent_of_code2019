""" Input range: 235741-706948 """

# Check #1: 6 digits
def check_length(password):
    if len(str(password)) == 6:
        return True

    else:
        return False


# Check #2: Between the input range

# Check #3: It has at least one double digit (Eg: 122345)
def check_double_digits(password):
    i = 0
    flag = False
    password = str(password)
    while i < len(password)-1:
        if password[i] * 2 in password:
            if password[i] * 3 in password:
                flag = False
            else:
                return True

        i += 1
    return flag


# Check #4: Digits never decrease
def digit_order(password):
    digits = [x for x in str(password)]
    if digits == sorted(digits):
        return True


def count_possible_passwords():
    count = 0
    for password in range(235741, 706949):
        if check_length(password) and check_double_digits(password) and digit_order(password):
            count += 1

    return count


#print(check_double_digits(a))
print(count_possible_passwords())
