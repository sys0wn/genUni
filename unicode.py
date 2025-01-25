import unicodedata
import urllib.parse

# Unicode range from 0 to 0x10FFFF. Iterates over all 1114111 unicode code-points and then checks if they have a name -> are actually defined and not just reserved for later use

for code_point in range(0, 0x10FFFF + 1):   
    try:
        char = chr(code_point)  # Get the character for the current code point
        name = unicodedata.name(char)  # Get the name of the character
        print(urllib.parse.quote(char, safe=""))
    except:
        continue
        

#Every othere char is not defined by unicode(no name/function just reserved), so we only print one as representation for that

print(urllib.parse.quote(chr(1098392), safe=""))
