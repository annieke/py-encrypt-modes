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
	
    # read the content of the input file into a buffer

    # generate initial counter as a random value
	
    # create AES cipher object
	
    # encrypt the buffer
	
    # write out initial counter and the encrypted buffer to the output file

	
# decryption
else:
    print 'Decrypting...',

    # read the saved counter and the encrypted payload from the input file

    # intialize counter with the value read 
	
    # create AES cipher object

    # decrypt encrypted buffer
	
    # write out the decrypted buffer into the output file

print 'Done.'

