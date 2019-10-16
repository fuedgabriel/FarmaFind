from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import re


def NameRemoveText(text):
    text = str(text)
    text = text.replace('</a>', '')
    text = text.replace('</strong>', '')
            
    m=re.sub(r'<(.*)">', '',text)
    return m

def search(bs, cod, preco, nome, loja):
    nm = len(nome)
    n = []
    for name in range(0, nm):
        if re.search('\\b'+nome[name]+'\\b', str(bs), re.IGNORECASE):
            n.append(str(nome[name]))
        else:
            pass
    print(n)

    
    cp = len(preco)
    pc = []
    for buy in range(0, cp):
        if re.search('\\b'+preco[buy]+'\\b', str(bs), re.IGNORECASE):
            pc.append(str(preco[buy]))
        else:
            pass
    lj = len(loja)
    jl = []
    for buy in range(0, lj):
        if re.search('\\b'+loja[buy]+'\\b', str(bs), re.IGNORECASE):
            jl.append(str(loja[buy]))
            print('Preco: '+ jl[buy] + '                                                            Loja: '+ pc[buy] )
        else:
            pass
    

    #print('Cod: '+ cod + '                 Nome: ' )
    
    
    
    
    
    

            
        
        
    
        
        


url = 'https://consultaremedios.com.br/advil-400mg/p'
def site(url):
    #read = input('Leia o código de barras: ')
    read = '7894916512718'
    #url = url + str(read) # headers={'User-Agent': 'Mozilla'}
    req = urllib.request.Request(url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})    

    html = urllib.request.urlopen(req)
    bs = BeautifulSoup(html, 'html.parser')
    
    
    a = bs
       
    
    desc = []
    i = 0
    for name in bs.find_all('h2', class_='presentation-offer-info__description'):
        name = name.find_all("a")
        name = NameRemoveText(name); name = name.replace('[','').replace(']','')
        #print(name)
        desc.append(str(name))
        i +=1

    buy = []
    i=0
    for preco in bs.find_all('strong', class_='offer__price-value'):
        preco = NameRemoveText(preco)
        #print(preco)
        buy.append(str(preco))
        i +=1
    store = []    
    for loja in bs.find_all('a', class_='btn-gts-track offer__wrapper'):
        loja = re.sub(r'.*n="', '', str(loja))
        loja = loja.split('" '); loja = loja[0]
        #print(loja)
        store.append(str(loja))


    i = 0
    key = []
    for cod in bs.find_all('span', class_='presentation-offer-info__ms'):
        
        cod = str(cod).replace('<span class="presentation-offer-info__ms">MS <strong>','').replace('</strong></span>','')
        bs = str(bs).split(cod)
        bs[i-1] = str(bs).split(cod)
        bs[i-1] = str(bs[i-1])+'   '+str(cod)
        key.append(str(cod))    
        i+=1

    
    #input()
    #quantHTM = len(bs)
    #quantCOD = len(cod)
    #by = []
    #loj = []

    pas = len(bs)
    print(desc)
    print(buy)
    print(store)
    print(key)
    for passo in range(0, pas):
        search(bs[passo], key[passo], buy, desc, store)
        
        
        
    '''
    for num in range(0, quantHTM):
        for quantia in range(0, quantCOD):
            valor = search(bs[num], cod[quantia])
            if valor == True:
                
                ran = len(store)
                for des in range(0, ran):
                    #print(des)
                    #print(store[des])
                    
                    if re.search('\\b'+str(store[des])+'\\b', bs[num], re.IGNORECASE):
                        loj.append(store[des])
                        
                        if re.search('\\b'+str(buy[des])+'\\b', bs[num], re.IGNORECASE):
                            by.append(buy[des])
                        else:
                            pass
                    else:
                        pass
                    
                    #valor = search(str(store[des]), bs[num])
                #print(True)
                break
            else:
                pass
                
                #print(False)
    rang = len(loj)
    print(rang)
    rang = len(by)
    print(rang)
    for t in range(0, rang):
        print('Loja: '+ str(loj[t]) + 'preco: '+ str(by[t]))
        
            
   
            '''
                
        
        
        

    
    #print(html.read().decode('utf-8'))



a = site(url)

