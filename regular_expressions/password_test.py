import re
pattern = re.compile(r"[A-Za-z0-9$%&#@]{8,}\d")

password = '12345678'

check = pattern.fullmatch(password)

print(check)