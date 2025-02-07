def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]


input_text = "Mam"
if is_palindrome(input_text):
    print(f"{input_text} is a palindrome")
else:
    print(f"{input_text} is not a palindrome")

input_text = "Man"
if is_palindrome(input_text):
    print(f"{input_text} is a palindrome")
else:
    print(f"{input_text} is not a palindrome")

input_text = "A man, a plan, a canal, panama"
if is_palindrome(input_text):
    print(f"{input_text} is a palindrome")
else:
    print(f"{input_text} is not a palindrome")
