from xml.dom import minidom
import time
start_time = time.time() #returneaza timpul procesorului, calculand doar tipul acestui proces
doc = minidom.parse('../tema3/database.xml')

#doc.getElementsByTagName returneaza NodeList

foods = doc.getElementsByTagName("food")
#print(foods.firstChild.data)
for food in foods:
    nume = food.getElementsByTagName("name")[0]
    pret = food.getElementsByTagName("price")[0]
    descriere = food.getElementsByTagName("description")[0]
    calorii = food.getElementsByTagName("calories")[0]
    print("nume:%s, pret:%s, calorii:%s, descriere:%s"%
    (nume.firstChild.data, pret.firstChild.data, calorii.firstChild.data, descriere.firstChild.data))
print("--- %s secunde ---" % (time.time() - start_time))