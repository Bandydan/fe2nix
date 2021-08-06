number1 = int(input())
number2 = int(input())
number3 = int(input())

str_result = ''
for i in range(1, number3+1):
  if (not i % number1) and (not i % number2):
    str_result += 'FB '
  if not i % number1:
    str_result += 'F '
  elif not i % number2:
    str_result += 'B '
  else:
    str_result += ' ' + str(i)

print(str_result)
