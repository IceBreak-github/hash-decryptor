import hashlib
import argparse
import sys

class decrypt(argparse.Action):
    def __init__(self, dest, option_strings=None, nargs=2, type=str, metavar=("[HASH_TYPE]","[HASH]"), **kwargs):
        super().__init__(dest=dest, option_strings=option_strings, nargs=nargs, metavar=metavar, **kwargs)
    
    def __call__(self, parser, namespace, values, option_string=None):
        input_hash = values[1]
        hash_type = values[0]
        try:
            print("Opening wordlist...")
            file = open("rockyou.txt", "r", encoding="ISO-8859-1")
        except Exception as e:
            print("Error: failed to open wordlist")
            
        lines = file.readlines()
        count = 0
        for line in lines:
            count += 1
            passwd =(line.strip()).encode("ISO-8859-1")
            new_hash = hashlib.new(hash_type)
            new_hash.update(bytes(passwd))
            the_hash= new_hash.hexdigest()
            print("\rAttemps: ", end = str(count))
            sys.stdout.flush()
            if(the_hash == input_hash):
                print("\n--- !MATCH FOUND! ---\nResult: ",passwd.decode("ISO-8859-1"))
                break
            else:
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hash decryptor', epilog='Press CTRL + C to stop the script\nVersion: 0.1', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--decrypt', help='hash decrypt', action=decrypt)
    args = parser.parse_args()
else:
    pass
