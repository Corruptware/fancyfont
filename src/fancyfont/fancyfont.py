'''
███████╗░█████╗░███╗░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░███╗░░██╗████████╗
██╔════╝██╔══██╗████╗░██║██╔══██╗╚██╗░██╔╝  ██╔════╝██╔══██╗████╗░██║╚══██╔══╝
█████╗░░███████║██╔██╗██║██║░░╚═╝░╚████╔╝░  █████╗░░██║░░██║██╔██╗██║░░░██║░░░
██╔══╝░░██╔══██║██║╚████║██║░░██╗░░╚██╔╝░░  ██╔══╝░░██║░░██║██║╚████║░░░██║░░░
██║░░░░░██║░░██║██║░╚███║╚█████╔╝░░░██║░░░  ██║░░░░░╚█████╔╝██║░╚███║░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░  ╚═╝░░░░░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░

==================================================================================================
Made With ❤️ ᴄᴏʀʀᴜᴘᴛᴡᴀʀᴇ™
'''

import unicodedata

#if platform.system() == 'Windows':
#    kernel32 = ctypes.windll.kernel32
#    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

print_mode = False

COMMANDS = {
    # familys
        #𝔈𝔵𝔞𝔪𝔭𝔩𝔢 𝔗𝔢𝔵𝔱
    'fraktur': 'MATHEMATICAL FRAKTUR',
        #𝕰𝖝𝖆𝖒𝖕𝖑𝖊 𝕿𝖊𝖝𝖙
    'bfraktur': 'MATHEMATICAL BOLD FRAKTUR',
    
        #𝐸𝓍𝒶𝓂𝓅𝓁𝑒 𝒯𝑒𝓍𝓉
    'script': 'MATHEMATICAL SCRIPT',
        #𝓔𝔁𝓪𝓶𝓹𝓵𝓮 𝓣𝓮𝔁𝓽
    'bscript': 'MATHEMATICAL BOLD SCRIPT',
    
        #𝔼𝕩𝕒𝕞𝕡𝕝𝕖 𝕋𝕖𝕩𝕥
    'doublestruck': 'MATHEMATICAL DOUBLE-STRUCK',
    
        #𝗘𝘅𝗮𝗺𝗽𝗹𝗲 𝗧𝗲𝘅𝘁
    'bsans': 'MATHEMATICAL SANS-SERIF BOLD',
        #𝘌𝘹𝘢𝘮𝘱𝘭𝘦 𝘛𝘦𝘹𝘵
    'isans': 'MATHEMATICAL SANS-SERIF ITALIC',
        #𝙀𝙭𝙖𝙢𝙥𝙡𝙚 𝙏𝙚𝙭𝙩
    'bisans': 'MATHEMATICAL SANS-SERIF BOLD ITALIC',
    
        #𝙴𝚡𝚊𝚖𝚙𝚕𝚎 𝚃𝚎𝚡𝚝
    'monospace': 'MATHEMATICAL MONOSPACE',
        
        #𝙴𝚡𝚊𝚖𝚙𝚕𝚎 𝚃𝚎𝚡𝚝
    'modifier': 'Modifier Letter',
    
        #𝙴𝚡𝚊𝚖𝚙𝚕𝚎 𝚃𝚎𝚡𝚝
    'negsquare': 'Negative Squared Latin',
}

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',0: 'Zero'}


def _gen(string, family):
    #colored = family if family else string
    #not_colored = string if family else ''
    
    result = ""
    for letter in string:
            if letter.isalpha():
                try:
                    result += unicodedata.lookup(family + " " + ("CAPITAL LETTER " + letter if family == "Negative Squared Latin" else ("CAPITAL " + letter if letter.isupper() else "SMALL " + letter)))
                except Exception as e:
                    result += letter
            elif letter.isnumeric():
                try:
                    result += unicodedata.lookup(family + " DIGIT " + num2words[int(letter)])
                except Exception as e:
                    result += letter
            else:
                result += letter
                
    if print_mode:
        print(family + ": " + result)
    else:
        return result


for key, val in COMMANDS.items():
    family = val[0] if isinstance(val, tuple) else val
    locals()[key] = lambda s, family=family: _gen(s, family)