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
        i = data.find(b'\x89PNG')
        
        while True:
            
            if(data[i-4:i] == b'\x89PNG'):
                f = open("texture_"+str(i)+".png", "wb")
                
                pngend = data.find(b'\xAE\x42\x60\x82', i)
                    
                f.write(data[i-4:pngend]+b'\xAE\x42\x60\x82')
                f.close()
                i = data.find(b'\x89PNG', pngend)
                
                if i == -1:
                    print("Done extracting.")
                    sys.exit(0)
                    
                print("Wrote: texture_"+str(i)+".png")
            i += 1
            
        
    else:
        print("Not a GameMaker file.")
        sys.exit(-1)
