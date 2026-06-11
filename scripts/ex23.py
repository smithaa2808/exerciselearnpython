import sys # imports the sys module 
script, input_encoding, error = sys.argv # 

def main(language_file, encoding, errors): # 
    line = language_file.readline() 
    if line: 
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # recursion the fuction  is called by itself 


def print_line(line, encoding, errors): # defining 
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors) 
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8") # opening the file and assigning 
main(languages, input_encoding, error)  


