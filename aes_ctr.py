import sys, getopt
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random

operation = 'enc'
keystring = ''
inputfile = ''
outputfile = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],'hedk:i:o:')
except getopt.GetoptError:
    print 'Usage: aes_ctr.py [-e|-d] -k <keystring> -i <inputfile> -o <outputfile>'
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print 'Usage: aes_ctr.py [-e|-d] -k <keystring> -i <inputfile> -o <outputfile>'
        sys.exit()
    elif opt == '-e':
        operation = 'enc'    
    elif opt == '-d':
        operation = 'dec'    
    elif opt == '-k':
        keystring = arg
    elif opt == '-i':
        inputfile = arg
    elif opt == '-o':
        outputfile = arg

if (operation != 'enc') and (operation != 'dec'):
    print 'Error: Operation must be -e (for encryption) or -d (for decryption).'
    sys.exit(2)
    
if len(keystring) != 16:
    print 'Error: Key string must be 16 character long.'
    sys.exit(2)

if len(inputfile) == 0:
    print 'Error: Name of input file is missing.'
    sys.exit(2)

if len(outputfile) == 0:
    print 'Error: Name of output file is missing.'
    sys.exit(2)

# encryption
if operation == 'enc': 
    print 'Encrypting...',

    input_file = open(inputfile, 'rb')
    buffer = input_file.read()
    input_file.close()

    key = keystring.encode('hex')
    init_val = Random.new().read(8)
    ctr = Counter.new(128, initial_value=long(init_val.encode('hex'), 16))

    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

    enc_buffer = cipher.encrypt(buffer)

    output_file = open(outputfile, 'w')
    output_file.write(init_val + enc_buffer)
    output_file.close()


# decryption
else:
    print 'Decrypting...',

    input_file = open(inputfile, 'rb')
    buffer = input_file.read()
    input_file.close()

    key = keystring.encode('hex')
    init_val = buffer[:8]
    buffer = buffer[8:]
    ctr = Counter.new(128, initial_value=long(init_val.encode('hex'), 16))

    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

    dec_buffer = cipher.decrypt(buffer)

    output_file = open(outputfile, 'w')
    output_file.write(dec_buffer)
    output_file.close()


print 'Done.'

