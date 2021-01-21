def password_check(pass1,num=0,alpha=0,special=0):
  if len(pass1)<8 or " " in pass1:
    return 0
  for i in pass1:
    if i.isdigit():
      num=1
    elif i.isalpha():
      alpha=1
    else:
      special=1
  return num+alpha+special

print(password_check("abc1234567"))
