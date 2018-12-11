from xml.dom import minidom, Node


breakfast_menu = [
    'Clatite Belgiene',
    'Clatite Belgiene cu gem de capsune',
    'Clatite Belgiene cu nutella',
    'French Toast',
    'Mic dejun ca acasa',

]

doc = minidom.Document()

doc.appendChild(doc.createComment("Sample XML Document with Dom parser in python"))

menu = doc.createElement('breakfast_menu')
doc.appendChild(menu)


for foodElement in breakfast_menu:
    food = doc.createElement('food')
    menu.appendChild(food)

    name = doc.createElement('name')
    name.appendChild(doc.createTextNode(foodElement))
    food.appendChild(name)

    price = doc.createElement('price')

    calories = doc.createElement('calories')
    
    description= doc.createElement('description')
    if foodElement == 'Clatite Belgiene':
        #Set price tag
        price.appendChild(doc.createTextNode('12 Lei'))
        #Set calories tag
        calories.appendChild(doc.createTextNode('650'))
        #Set description tag
        description.appendChild(doc.createTextNode('Doua dintre famioasele clatite Belgiene cu foarte, foarte mult sirop de artar'))
    elif foodElement == 'Clatite Belgiene cu gem de capsune':
        #Set price tag
        price.appendChild(doc.createTextNode('15 Lei'))
        #Set calories tag
        calories.appendChild(doc.createTextNode('900'))
        #Set description tag
        description.appendChild(doc.createTextNode('Doua clatite Belgiene cu gem de capsune si putin iaurt'))
    elif foodElement == 'Clatite Belgiene cu nutella':
        #Set price tag
        price.appendChild(doc.createTextNode('7 Lei'))
        #Set calories tag
        calories.appendChild(doc.createTextNode('900'))
        #Set description tag
        description.appendChild(doc.createTextNode('Clatite simple cu umplutura de nutella'))
    elif foodElement == 'French Toast':
        #Set price tag
        price.appendChild(doc.createTextNode('3 Lei'))
        #Set calories tag
        calories.appendChild(doc.createTextNode('600'))
        #Set description tag
        description.appendChild(doc.createTextNode('Felii groase si proaspete din propia noastra bucatarie'))
    elif foodElement == 'Mic dejun ca acasa':
        #Set price tag
        price.appendChild(doc.createTextNode('12 Lei'))
        #Set calories tag
        calories.appendChild(doc.createTextNode('950'))
        #Set description tag
        description.appendChild(doc.createTextNode('Doua oua, bacon sau sos si French Toast'))
    else:
        print ("Momentan nu exista altceva in meniu")
    food.appendChild(price)   
    food.appendChild(calories)
    food.appendChild(description)


print (doc.toprettyxml(indent = '   '))