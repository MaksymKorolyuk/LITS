import re

# string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.(x86 or x64)
# """

# re.match()
# result = re.match(r'([A-Z])', string)
# print(result.group())

# re.search()
# result = re.search(r'in', string)
# print(result.group(), result.start(), result.end())

# re.findall()
# result = re.findall(r'^[lL]', string)
# print(result)

# re.split()
# result = re.split(r'.*\b', string)
# print(result)

# re.sub()
# result = re.sub(r'\s', '!', string)
# print(result)

# re.compile()
# pattern = re.compile(r'\(x\d{2}\s?(or)?\s(x\d{2})?\)')
# result = pattern.findall(string)
# print(result)

# phone1 = '0990299001'
# phone2 = '+380990299001'
#
# pattern = re.compile(r'((\+38)?[0-9]{10})')
# result1 = pattern.match(phone1).group()
# result2 = pattern.match(phone2).group()
#
# print(result1, result2)

time1 = '11:59'
time2 = '18:27'
date = '27/06/2019'

pattern1 = re.compile(r'(([01][01])|(0[1-9])):([0-5][0-9])')
pattern2 = re.compile(r'(([01][01])|([0-2][1-9])):([0-5][0-9])')
pattern3 = re.compile(r'[0-3][0-9]/[0][1-9]|1[0-2]/\d{4}')

result1 = pattern1.match(time1).group()
result2 = pattern2.match(time2).group()
result3 = pattern3.match(date).group()

print(result1,
      result2,
      result3
      )
