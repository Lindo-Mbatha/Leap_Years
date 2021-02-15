print("Check for Leap Year")
year = int(input("Which year do you want to check? "))

unknown1 = year / 4
unknown2 = year / 100
(unknown3) = year / 400

if unknown1 % 2 == 0 and unknown2 / 2 and unknown3 / 2:
  print("Leap Year")
elif unknown1 % 2 * 2 % 2 and unknown2 % 4 != 0 and unknown3 % 2 != 0:
  print("Not a Leap Year")
else:
  print("Leap Year")