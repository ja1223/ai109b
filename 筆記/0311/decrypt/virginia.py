def encrypt(text, key):# 對 text 以 key = [0,2,4] 進行加密
  list = []
  klen = len(key)
  for i in range(len(text)):
    ki = i% klen
    n1 = (ord(text[i])+key[ki])%128
    list.append(chr(n1))
  return ''.join(list)

def neg(key):
  nkey = [0]*len(key)
  for i in range(len(key)):
    nkey[i] = -key[i]
  return nkey

def decrypt(text, key): # 對 text 以 -(key) 進行解密
  return encrypt(text, neg(key))

commons = ['is', 'of', 'am', 'the', 'a', 'in', 'at', 'on', 'go', 'to'] # 常用字彙

def fit(text):#算分數
  text = text.lower()
  score = 0
  for i in range(len(text)):
    if text[i].isalpha() : score += 0.05 #如果是英文就加分
    if i>0 and text[i-1].isalpha(): continue
    head = text[i:i+5]
    for word in commons:
      if head.startswith(word) and not head[len(word)].isalpha():
        score += 1
        break
  return score

# plain = "hello world!"
plain = "This is a book. That is a cat. I am a boy. One of my boy go to school today."
# plain = "This is a book"
key = [0,2,4]
etext = encrypt(plain, key)
dtext = decrypt(etext, key)
print('etext=', etext)
print('dtext=', dtext)
print('fit(plain)=', fit(plain))

