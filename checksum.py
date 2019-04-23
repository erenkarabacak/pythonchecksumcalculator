import binascii
import sys

filename = sys.argv[1]
file = open(filename, "r")
content = file.read()

#content to binary

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))





def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

binary = text_to_bits(content)

n = 16

a = [binary[i:i+n] for i in range(0, len(binary), n)]





def add(x,y):
    x = str(x)
    y = str(y)
    maxlen = max(len((x)), len(y))

    # Normalize lengths
    x = x.zfill(maxlen)
    y = y.zfill(maxlen)

    result = ''
    carry = 0

    for i in range(maxlen - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0

        # r can be 0,1,2,3 (carry + x[i] + y[i])
        # and among these, for r==1 and r==3 you will have result bit = 1
        # for r==2 and r==3 you will have carry = 1

        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0: result = '1' + result

    return result.zfill(maxlen)

addedbinary  = ['0000000000000000']





for i in range(len(a)):


    if len(addedbinary[0]) > 16:
        temporal = addedbinary[0]

        addedbinary[0]=temporal[1:]

        addition2 = add(addedbinary[0],'0000000000000001')

        addedbinary[0]=addition2

    else:
        addition = add(addedbinary[0], a[i])

        addedbinary[0] = addition



splitted = list(addedbinary[0])

#substraction from 1111111111111111

for i in range(len(splitted)):
    if splitted[i] == '1':
        splitted[i] = '0'
    else:
        splitted[i] = '1'

print("checksum is",*splitted)

