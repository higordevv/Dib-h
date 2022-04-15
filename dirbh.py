#!/usr/bin/env python3
import requests, os, sys, argparse, queue
os.system('clear')
yellow='\u001b[1;93m'
cyan = '\u001b[1;96m'
red = '\u001b[1;91m'
green = '\u001b[1;92m'
white = '\u001b[1;37;40m'

banner = '''


8888888b.  d8b         888      888    888 
888  "Y88b Y8P         888      888    888 
888    888             888      888    888 
888    888 888 888d888 88888b.  8888888888 
888    888 888 888P"   888 "88b 888    888 
888    888 888 888     888  888 888    888 
888  .d88P 888 888     888 d88P 888    888 
8888888P"  888 888     88888P"  888    888

     >> URL Brute-Force Tool   v 1.0

                        Developed by Higor
'''

print(f'{yellow}{banner}{white}')

#Definindo os Argumentos!
args = []
passedArguments = argparse.ArgumentParser()
passedArguments.add_argument("--url", required=False, help="Passe a Url.")
passedArguments.add_argument("--wordlist", required=False, help="Selecione a WorldList.")
passedArguments.add_argument("--status", required=False, nargs='+', help="Filtra os status code da url.")
args = passedArguments.parse_args()
global orgns

#Usando os argumentos 
urltarget = str(args.url)

try:
    worldlist = open(args.wordlist,'r').read().split('\n')
except:
    print(f"{cyan}[{red}!{cyan}]{white} Pfvr leia os argumentos ultilizando '-h'")
    sys.exit(1)
    

começo = 0 
orgns = queue.Queue()
for lista in worldlist:
    orgns.put(lista)
    começo+=1

print(f"{cyan}[{red}*{cyan}]{white} URL ALVO: {targeturl}")
print(f"{cyan}[{red}*{cyan}]{white} Wordlist: {args.wordlist}")
print(f"{cyan}[{red}*{cyan}]{white} Status Codes: {args.status}")
print(f"\n{cyan}[{red}*{cyan}]{white} DirbH ESTÁ VERIFICANDO OS DIRETÓRIOS POR FAVOR, AGUARDE [CTRL+C STOP]...")
print("\n") 

def scanner():
    counter = 0
    try:
        while not orgns.empty():
            ingectorList = orgns.get()
            url = f'{urltarget}/{ingectorList}'
            r = requests.get(url)
            Reply = f'{r.status_code}'           
            if Reply in args.status:
                print(f"Status {green}{Reply}{white} => {green}{url}{white}")
                hits.append((url,Reply))

    except KeyboardInterrupt:
        print(f"\n{cyan}[{red}!{cyan}]{white} Programa terminado pelo usuario!.")

scanner()