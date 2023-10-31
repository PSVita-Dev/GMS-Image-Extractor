#The most cursed texture extractor for GM:S
#Created on the spooky day 2023
#By jicama

import sys

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage: python extract-png.py game.symbian")
        sys.exit(-1)
        
    f = open(sys.argv[1], "rb")
    data = f.read()
    f.close()
    
    if data[:4] == b'FORM':
        print("Found FORM")
        i = 4
        
        while(data[:i]):
            if(data[i:i+4] == b'\x89PNG'):
                f = open("texture_"+str(i)+".png", "wb")
                pngend = i
                while(data[pngend:pngend+4] != b'\xAE\x42\x60\x82'):
                    pngend += 1
                    
                f.write(data[i:pngend])
                f.close()
            i += 1
            if(data[i:i+4] == b'AUDO'):
                print("Done extracting.")
                sys.exit(0)
            
        
    else:
        print("Not a GameMaker file.")
        sys.exit(-1)
