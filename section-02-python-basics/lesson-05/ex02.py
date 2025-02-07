import re

input_text = """
In this text there are several email addresses I want to replace.
FYI example1@mail.com, example2@email.com
"""

pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"
replacement = "[email]"

clean_text = result = re.sub(pattern, replacement, input_text)

print(clean_text)
