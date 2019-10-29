from bs4 import BeautifulSoup
import urllib.request
import re
import os


def NameRemoveText(text):
    text = str(text)
    text = text.replace('</a>', '')
    text = text.replace('</strong>', '')
            
    m=re.sub(r'<(.*)">', '',text)
    return m

def search(bs, cod, preco, nome, loja):
    '''
    nm = len(nome)
    n = []
    for name in range(0, nm):
        if re.search('\\b'+nome[name]+'\\b', str(bs), re.IGNORECASE):
            n.append(str(nome[name]))
        else:
            pass
#    print(n)
    '''

    
    cp = len(preco)
    pc = []
    for buy in range(0, cp):
        if re.search('\\b'+preco[buy]+'\\b', str(bs), re.IGNORECASE):
            pc.append(str(preco[buy]))
        else:
            pass
    lj = len(loja)
    jl = []

    print(nome)
    for buy in range(0, lj):
        if re.search('\\b'+loja[buy]+'\\b', str(bs), re.IGNORECASE):
            jl.append(str(loja[buy]))
            print("{0:>30}".format(jl[buy]) + "{0:>30}".format(pc[buy]))
            #print('Loja: '+ jl[buy] + '                                                            Preco: '+ pc[buy] )
        else:
            pass 


def site(url):
   
   #url = url + str(read) # headers={'User-Agent': 'Mozilla'}


    req = urllib.request.Request(url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})    

    html = urllib.request.urlopen(req)
    bs = BeautifulSoup(html, 'html.parser')
    bz = bs
    
    



    
    i = 0
    key = []
    for cod in bs.find_all('span', class_='presentation-offer-info__ms'):
        cod = str(cod).replace('<span class="presentation-offer-info__ms">MS <strong>','').replace('</strong></span>','')
        bs = str(bs).split(cod)
        bs[i-1] = str(bs).split(cod)
        bs[i-1] = str(bs[i-1])+'   '+str(cod)
        key.append(str(cod))    
        i+=1
    
    bz = str(bz).split(key[1])
    bz = BeautifulSoup(bz[0], 'html.parser')

    
    
    buy = []
    i=0
    for preco in bz.find_all('strong', class_='offer__price-value'):
        preco = NameRemoveText(preco)
        #print(preco)
        buy.append(str(preco))
        i +=1

        
    desc = []
    i = 0
    for name in bz.find_all('h2', class_='presentation-offer-info__description'):
        name = name.find_all("a")
        name = NameRemoveText(name); name = name.replace('[','').replace(']','')
        #print(name)
        desc.append(str(name))
        i +=1

    
        
    store = []

    
    for loja in bz.find_all('a', class_='btn-gts-track offer__wrapper'):
        loja = re.sub(r'.*n="', '', str(loja))
        loja = loja.split('" '); loja = loja[0]
        #print(loja)
        store.append(str(loja))
        

    #print(bz)
    #print(key[0])
    #print(buy)
    #print(desc)
    #print(store)
    search(bz, key[0], buy, desc[0], store)
    
    '''
    print(desc)
    print(buy)
    print(store)
    print(key)
    
    for passo in range(0, pas):
        print("Passo : "+ str(passo))
        search(bs[passo], key[passo], buy, desc, store)
        '''

url = 'https://consultaremedios.com.br/busca?termo='
#url = 'https://consultaremedios.com.br/busca?termo=7894916512718'
#url = 'https://consultaremedios.com.br/advil-400mg/p'


while(True):
    
    url = 'https://consultaremedios.com.br/busca?termo='
    print('=======================================================================')
    read = input('Leia o código de barras: ')
    os.system('cls') or None
    if(read == ''):
        print("Digite um código de barras")
    else:
        try:
            url = url + str(read)
            site(url)
        except:
            print("Algo deu errado. \nVerifique se o código de barras digitado está correto.")

