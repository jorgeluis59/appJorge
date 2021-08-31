from flask import Flask
import requests
from bs4 import BeautifulSoup
 
app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
	return "Not Found"

@app.route('/', methods=['GET'])
def index():

	#Nombre: Jorge Luis
	#Aplicación con EndPoint que consulta datos de Yahoo Finance - las cotizaciones
	# en bolsa de la empresa Ford, Facebook y Tesla

	link_ford='https://finance.yahoo.com/quote/F/financials?p=F'
	link_facebook='https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch'
	link_tesla='https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch'
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
	rford=requests.get(link_ford,headers=headers)
	rfacebook=requests.get(link_facebook,headers=headers)
	rtesla=requests.get(link_tesla,headers=headers)


	soupford=BeautifulSoup(rford.text,'lxml')
	soupfacebook=BeautifulSoup(rfacebook.text,'lxml')
	souptesla=BeautifulSoup(rtesla.text,'lxml')
	ford=soupford.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	facebook=soupfacebook.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	tesla=souptesla.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()

	
	return 'Por JORGE LUIS, Datos extraídos de Yahoo Finance' + '  ---' + ' COTIZACIÓN Ford Motor Company: $' + ' ' +ford + ' ---'+ '  COTIZACIÓN Facebook: $'+' '+ facebook+' ---'+'  COTIZACIÓN Tesla: $'+' '+tesla+''
	

if __name__ == '__main__':
	app.run(port = PORT,debug = DEBUG)
