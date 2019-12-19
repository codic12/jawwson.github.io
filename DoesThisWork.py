isyes = input("Hi, does this work? ")
isyes = isyes.lower().strip()
if "yes" in isyes:
  print('yay it works!')
else:
  print("Well... you either typed extra spaces or didn't type yes. LIAR THIS WORKS!!!")
