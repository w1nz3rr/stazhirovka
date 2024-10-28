def is_palindrome(string):
    # Валидация
    if string is None:
        return False
    # Код функции
    new_string = ''
    for el in str(string):
        if el.isalpha() == True or el.isdigit() == True:
            new_string += el.lower()
    if new_string == new_string[::-1]:
        return True
    else:
        return False

print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))