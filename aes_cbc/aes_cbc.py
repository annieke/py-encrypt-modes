import sys, getopt
from Crypto.Cipher import AES
from Crypto import Random

operation = 'enc'
keystring = ''
inputfile = ''
outputfile = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],'hedk:i:o:')
except getopt.GetoptError:
    print 'Usage: aes_cbc.py [-e|-d] -k <keystring> -i <inputfile> -o <outputfile>'
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print 'Usage: aes_cbc.py [-e|-d] -k <keystring> -i <inputfile> -o <outputfile>'
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

if operation == 'enc': 
    print 'Encrypting...',

    input_file = open(inputfile, 'rb')
    i_buffer = input_file.read()
    input_file.close()

    pad_len = AES.block_size - len(i_buffer) % AES.block_size
    i_buffer += chr(pad_len) * pad_len

    init_val = Random.new().read(AES.block_size)
    cipher = AES.new(keystring, AES.MODE_CBC, init_val)

    enc_buffer = cipher.encrypt(i_buffer)

    output_file = open(outputfile, 'w')
    output_file.write(init_val + enc_buffer)
    output_file.close()

else:
    print 'Decrypting...',

    input_file = open(inputfile, 'rb')
    i_buffer = input_file.read()
    input_file.close()

    init_val = i_buffer[:AES.block_size]
    i_buffer = i_buffer[AES.block_size:]

    cipher = AES.new(keystring, AES.MODE_CBC, init_val)

    dec_buffer = cipher.decrypt(i_buffer)
    dec_buffer = dec_buffer[:len(dec_buffer) - ord(dec_buffer[-1])]

    output_file = open(outputfile, 'w')
    output_file.write(dec_buffer)
    output_file.close()

print 'Done.'

