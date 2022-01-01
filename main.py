from os import system
try:
    from pyshorteners import Shortener
    from pyfiglet import Figlet
except:
    system('pip install pyshorteners pyfiglet')
from random import choice


def ent():
    input('\nenter para contiuar')

def cls():
    system('cls||clear')

def trat(option='', url='', enc=True):
    s = Shortener()
    opc_short = {
        '1': s.tinyurl,
        '2': s.chilpit,
        '3': s.clckru,
        '4': s.dagd,
        '5': s.gitio,
        '6': s.isgd,
        '7': s.osdb
    }
    return opc_short[option].short(url) if enc else opc_short[option].expand(url)


f = '\033[m'
verm = '\033[31;1m'
verd = '\033[32;1m'
amar = '\033[33;1m'
azul = '\033[34;1m'
roxo = '\033[35;1m'
cian = '\033[36;1m'
n = '\033[37;1m'
cores = verm, verd, amar, azul, roxo, cian
banner = Figlet(font='slant').renderText('Shortener').rstrip()

l_opc = 'EXPANDIR'
l = 'E'
shortners = True

while True:
    cls()
    c = choice(cores)
    print(c+banner)
    try:
        op = input(f'''\n{n}Escolha com qual API sua url será encurtada
[ {c}1{n} ] > {c}tinyurl.com{n}
[ {c}2{n} ] > {c}chilp.it{n}
[ {c}3{n} ] > {c}clck.ru{n}
[ {c}4{n} ] > {c}da.dg{n}
[ {c}5{n} ] > {c}git.io{n} (domínios github.com)
[ {c}6{n} ] > {c}is.gd{n}
[ {c}7{n} ] > {c}os.db{n}\n
[ {c}0{n} ] > {c}SAIR{n}
[ {c}{l}{n} ] > {c}{l_opc}
\n>>>{n} ''').strip().lower()[0]
    except: continue
    match op:
        case 'e':
            shortners = False
            l_opc = 'ENCURTAR'
            l = 'L'
            continue
        case 'l':
            shortners = True
            l_opc = 'EXPANDIR'
            l = 'E'
            continue
        case '0':
            break
    if not op in '1234567': continue
    try:
        url = input('URL >>> ').strip()
    except: continue
    if url == '': continue
    print('\033[34;1;4m'+trat(op, url, shortners)+f)
    ent()
cls()
print(c+'Até mais!'+f)
