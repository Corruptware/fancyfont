#!/usr/bin/env python3

import unicodedata

#if platform.system() == 'Windows':
#    kernel32 = ctypes.windll.kernel32
#    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

print_mode = True

COMMANDS = {
    # familys
        #𝔈𝔵𝔞𝔪𝔭𝔩𝔢 𝔗𝔢𝔵𝔱
    'fraktur': 'MA­THE­MA­TI­CAL FRAKTUR',
        #𝕰𝖝𝖆𝖒𝖕𝖑𝖊 𝕿𝖊𝖝𝖙
    'bfraktur': 'MA­THE­MA­TI­CAL BOLD FRAKTUR',
    
        #𝐸𝓍𝒶𝓂𝓅𝓁𝑒 𝒯𝑒𝓍𝓉
    'script': 'MA­THE­MA­TI­CAL SCRIPT',
        #𝓔𝔁𝓪𝓶𝓹𝓵𝓮 𝓣𝓮𝔁𝓽
    'bscript': 'MA­THE­MA­TI­CAL BOLD SCRIPT',
    
        #𝔼𝕩𝕒𝕞𝕡𝕝𝕖 𝕋𝕖𝕩𝕥
    'doublestruck': 'MA­THE­MA­TI­CAL DOUBLE-STRUCK',
    
        #𝗘𝘅𝗮𝗺𝗽𝗹𝗲 𝗧𝗲𝘅𝘁
    'bsans': 'MA­THE­MA­TI­CAL SANS-SERIF BOLD',
        #𝘌𝘹𝘢𝘮𝘱𝘭𝘦 𝘛𝘦𝘹𝘵
    'isans': 'MA­THE­MA­TI­CAL SANS-SERIF ITALIC',
        #𝙀𝙭𝙖𝙢𝙥𝙡𝙚 𝙏𝙚𝙭𝙩
    'bisans': 'MA­THE­MA­TI­CAL SANS-SERIF BOLD ITALIC',
    
        #𝙴𝚡𝚊𝚖𝚙𝚕𝚎 𝚃𝚎𝚡𝚝
    'monospace': 'MA­THE­MA­TI­CAL MONO­SPACE',
}


def _gen(string, family, force_upper=False):
    #colored = family if family else string
    #not_colored = string if family else ''
    
    result = ""
    for letter in string:
            if letter.isalpha():
                result += unicodedata.lookup(family + " " + (letter.upper() if force_upper else letter))
            else:
                result += letter
                
    if print_mode:
        print(result)
    else:
        return result


for key, val in COMMANDS.items():
    value = val[0] if isinstance(val, tuple) else val
    family = val[1] if isinstance(val, tuple) else ''
    locals()[key] = lambda s, family=family: _gen(s, family)