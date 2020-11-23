mail=input("Please enter your email adress:")
check="ceng113@example.com"

mail.lower()
for char in mail:
  if char=="." and mail.index(".")<mail.index("@"):
    mail.replace(".","")

if mail==check:
  print("Yes they are same.")
else:
    print("Yes they are same.")