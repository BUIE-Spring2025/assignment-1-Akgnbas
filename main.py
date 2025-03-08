def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    if not (1 <= num <= 3999):
        return "Number must be between 1 and 3999 inclusive."
    
    roman=""
    for i in range(num//1000):
        roman+="M"

    
    if (num//100)%10==9:
        roman+="CM"
    elif (num//100)%10>=5:
        roman+="D"+"C"*(((num//100)%10)-5)
    elif (num//100)%10==4:
        roman+="CD"
    else:
        roman+="C"*((num//100)%10)


    if (num//10)%10==9:
        roman+="XC"
    elif (num//10)%10>=5:
        roman+="L"+"X"*(((num//10)%10)-5)
    elif (num//10)%10==4:
        roman+="XL"
    else:
        roman+="X"*((num//10)%10)


    if num%10==9:
        roman+="IX"
    elif num%10>=5:
        roman+="V"+"I"*((num%10)-5)
    elif num%10==4:
        roman+="IV"
    else:
        roman+="I"*(num%10)


    return roman


