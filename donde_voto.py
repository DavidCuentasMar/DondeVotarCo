import requests
from bs4 import BeautifulSoup

base_url = "https://wsp.registraduria.gov.co/censo/_censoResultado.php?nCedula=%s"
cedula = str(input("Ingresar numero de cedula: "))
url = base_url % cedula
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("table")
#print(table)
DEP = table.find_all('td')[1].get_text()
MUN = table.find_all('td')[3].get_text()
PUS = table.find_all('td')[5].get_text()
DIR = table.find_all('td')[7].get_text()
MES = table.find_all('td')[11].get_text()
#print(table.find_all('td')[0].get_text())
print("DEPARTAMENTO: " + DEP)
print("MUNICIPIO: " + MUN)
print("PUESTO: " + PUS)
print("DIR: " + DIR )
print("MESA: " + MES)

