import random
def getChar():
  s = input("Enter a character: ")
  return s[0]
def char2bin(char):
  n = ord(char)
  bits1 = bin(n)[2:]
  bits2 = bits1.zfill(8)
  bits3 = list(bits2)
  bits4 = [ord(bit) - ord('0') for bit in bits3]
  return bits4
def bin2char(bits):
  bits1 = [chr(bit + ord('0')) for bit in bits]
  bits2 = ''.join(bits1)
  char1 = int(bits2, 2)
  char2 = chr(char1)
  return char2
def parityOf(bits, parity):
  p = sum(bits) % 2
  return 0 if p == parity else 1
def appendParity(bits, parity):
  parityBit = parityOf(bits, parity)
  return bits + [parityBit]
def addNoise(bits, errorProb):
  numFlips = 0
  def flip(bit):
    nonlocal numFlips
    n = random.random()
    if n < errorProb:
      numFlips += 1
      return 1 - bit
    return bit
  bits1 = [flip(bit) for bit in bits]
  return bits1, numFlips
def checkParity(bits, parity):
  data = bits[:8]
  p = parityOf(data, parity)
  return p == bits[8]
def main():
  EVEN = 0
  ODD = 0
  desiredParity = EVEN
  errorProb = 0.1
  char1 = getChar()
  bits = char2bin(char1)
  parityBit = parityOf(bits, desiredParity)
  txFrame = appendParity(bits, desiredParity)
  print("transmitted bits:", txFrame)
  (rxFrame, numFlips) = addNoise(txFrame, errorProb)
  print("number of flipped bits:", numFlips)
  print("received bits:", rxFrame)
  rxParity = rxFrame[-1]
  cxParity = checkParity(rxFrame, desiredParity)
  if rxParity == cxParity:
    print("no error detected")
  else:
    print("error detected")
  char2 = bin2char(rxFrame[:8])
  print("received character:", char2)
if __name__ == '__main__':
  main()
