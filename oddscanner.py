import time
from selenium import webdriver

#abre o google chrome
navegador = webdriver.Chrome()
#entra no site do yahoofinance
navegador.get("https://finance.yahoo.com/quote/BTC-EUR/history/")

#listas de datas e valor de fechamento de mercados
datas = []
closes = []

datasi = [] #pra tirar o .text
closesi = [] #pra tirar o .text 
#pegando os valores do ultimos 10 dias + dia atual
for i in range(1,12):
    datas.append(navegador.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[%d]/td[1]'%i))  
    closes.append(navegador.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[%d]/td[5]/span'%i))
    
    datasi.append(navegador.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[%d]/td[1]'%i))  
    closesi.append(navegador.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[%d]/td[5]/span'%i))

#printando como teste para ver se está funcionando
for i in range(len(datas)):
    print(datas[i].text)
    print(closes[i].text)
    
#datasi = []
#closesi = []
for i in range(len(datas)):
    datasi[i] = datas[i].text
    closesi[i] = closes[i].text
    
for i in range(len(datas)):
    print("iii " + datasi[i])
    print("iii " + closesi[i])

import csv 

with open('eur_btc_rates.csv','w', newline='') as f:
    fieldnames = ['Date','BTC Closing Value']
    escritor = csv.DictWriter(f, fieldnames=fieldnames)
    
    escritor.writeheader()
    
    for i in range(len(datas)):
        escritor.writerow({'Date' : datasi[i] , 'BTC Closing Value' : closesi[i]})
