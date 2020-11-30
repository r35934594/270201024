mail=input("Please enter your email adress:")
check="ceng113@example.com"

mail.lower()
for char in mail:
  if char=="." and mail.index(".")<mail.index("@"):
    mail=mail.replace(".","",1)

if mail==check:
  print("Yes they are same.")
else:
    print("No they are not the same.")