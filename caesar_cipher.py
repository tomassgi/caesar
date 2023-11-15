a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypted(t, o):  #define burtu e un enkode tekstu
  r = ""
  for c in t:  #cikls kas panem katru burtu no teksta
    if (a.find(c) == -1):  # ja atrod c tad tiek nonemts viens burts
      r += c
    else:  # ja neatrod c tad tiek pievienots viens burts
      r += (a[(a.find(c) + o) % len(a)])
  return r


def decrypted(t, o):  #define burtu d un dekode tekstu
  r = ""
  for c in t:  # cikls kas tiek izmantots lai parveidoto burtus
    if (a.find(c) == -1):  # ja atrod c tad tiek nonemts viens burts
      r += c
    else:  # ja neatrod c tad tiek nonemts viens burts
      r += (a[(a.find(c) - o) % len(a)])
  return r


w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1:  #ja ievada 1 tad printe teksts un prasa lai ievada rotaciju
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encrypted(text, rotation))
elif mode == 2:  #ja ievada 2 tad printets teksts un prasa lai ievada rotaciju
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decrypted(text, rotation))
elif mode == 3:  #ja ievada 3 tad printe teksts un prasa lai ievada rotaciju
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
