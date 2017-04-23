"""
    visa - 13 or 16 digits - IIN 4
    mastercard - 16 digits - IIN 2221 - 2720 or 51-55
    discover - 16 digits - IIN 6011, 622126-622925, 644-649, 65
    american express - 15 digits - IIN 34, 37
    diners club - 14 digits (15 digits for enRoute)- IIN 300-305 (Carte Blanche)
                                2014,2149 (enRoute - No validation)
                                300-305, 309, 36, 38, 39 (diners club internationl)
                                54-55 (mastercard co-branded)
    maestro - 12 to 19 digits (Multi National) - IIN 50, 56-58, 6
    laser - 16 to 19 digits (Ireland) - IIN 6304, 6706, 6771, 6709
    switch - 16, 18, or 19 digits (UK) - IIN 4904, 4905, 4911, 4936, 564182, 633110, 6333, 6759
    solo - 16, 18, 19 digits (UK) - IIN 6334, 6767
    JCB - 15, 16 digits (Japan) - IIN 3528 - 3589
    China Union Pay - 16 (PRC) - IIN 62
    ** info sourced from validcreditcardnumber.com and wikipedia


    Luhn Algorithm -->
        1. reverse number
        2. first number becomes check digit
        3. double the value of every second digit after check digit
            i.e indexes 1, 3, 5, ...
        4. if doubled value is greater than 9 subtract 9
        5. sum all the digits
        6. multiply sum by 9
        7. add check digit
        8. modulo 10 and check that modulus == 0

"""


###################
# imports
###################
import re


###################
# Functions
###################
def clean_number(cc_number):
    """ cleans input stiping whitespace and punctuation leaving only
        alphanumeric characters
        alpha characters are left to test for possible failure reason in
        a later function
    """
    cc_number.strip()
    cc_number = "".join(cc_number.split())
    cc_number = "".join(re.split('\W+', cc_number))
    return cc_number


def cc_number_precheck(cc_number):
    """
        checks the cc number before validation to ensure that it is all digits
        and less than 20 characters in length
        assumes that number has been clened before input -> use clean_number()
        returns 1 for valid input
        returns -1 for not digits
        returns -2 for too long
    """

    if not cc_number.isdigit():
        return -1
    if len(cc_number) > 19:
        return -2

    return 1


def luhn_check(cc_number):
    """ runs the luhn algorithm on the credit card number to determine if it is
        theoretically valid
        returns 1 for valid, -1 for invalid
    """
    reversed_number = str(cc_number)[::-1]
    cc_nums_list = [int(n) for n in reversed_number]
    check_digit = cc_nums_list[0]
    cc_digit_sum = check_digit
    for i in range(1, len(cc_nums_list)):
        if i % 2 == 1:
            value = cc_nums_list[i] * 2
            if value > 9:
                value -= 9
            cc_digit_sum += value
        else:
            cc_digit_sum += cc_nums_list[i]
    if cc_digit_sum % 10 == 0:
        return 1
    else:
        return -1


###################
# Execution
###################
while True:
    print("\n\n\n\n\n\n\n\n\n\n")
    credit_card_number = input("Enter a credit card number to test: ")
    cleaned_cc_number = clean_number(credit_card_number)
    input_check = cc_number_precheck(cleaned_cc_number)

    if input_check == 1:
        luhn_test_result = luhn_check(cleaned_cc_number)
        if luhn_test_result == 1:
            print("{0} IS a theoretically valid credit card number".format(credit_card_number))
        else:
            print("{0} is NOT a theoretically valid credit card number".format(credit_card_number))
    elif input_check == -1:
        print("Credit card number must be digits only")
    elif input_check == -2:
        print("Card number too long, max length is less than 20 digits")

    cont_test = input("Would you like to test another number? (Y/n): ")
    if cont_test in "Nn":
        break
