def encode(a):
  a = input("enter a message: ")
  cooding = True
  words = a.split(" ")
  if (cooding):
    nwords =[]
    for word in words:
      if(len(word)>=3):
        r1 = "fsd"
        r2= "gdw"
        b = r1 + word[1:]+ word[0]+ r2
        nwords.append(b)
      else:
        nwords.append(word[::-1])
        # print(a[::-1])
    print(" ".join(nwords))

def decode(b):
  a = input("enter a message: ")
  cooding = True
  nwords =[]
  words = a.split(" ")
  for word in words:
    if(len(word)>=3):
      b =  word[3:-3]
      b= b[-1] + b[:-1]

      nwords.append(b)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
  
print("Welcome to ABC Encoding Decoding Center")
a = input("want to encode, decode or want to leave: ")

def default(a):

  cooding = True
  words = a.split(" ")
  if (cooding):
    nwords =[]
    for word in words:
      if(len(word)>=3):
        r1 = "fsd"
        r2= "gdw"
        b = r1 + word[1:]+ word[0]+ r2
        nwords.append(b)
      else:
        nwords.append(word[::-1])
    print(" ".join(nwords))


if (a=="encode" or a=="Encode" or a== "Decode" or a== "decode" or a=="Leave" or a=="leave"):
  if(a=="encode" or a=="Encode"):
    encode(a)
  elif(a=="decode" or a=="Decode"):
    decode(a)
  elif(a=="leave" or a=="Leave"):
    print("Thanks! you are out of the Program")
elif (len(a)>3):
  default(a)
# else:
#  encode(a)
