#!/usr/bin/python3

import xml.sax
import time
class MenuHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.food = ""
      self.name = ""
      self.calories = ""
      self.description = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "food":
         print ("*****Mancare*****")

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "food":
         print ("Mancare:", self.food)
      elif self.CurrentData == "name":
         print ("Nume:", self.name)
      elif self.CurrentData == "calories":
         print ("Calorii:", self.calories)
      elif self.CurrentData == "description":
         print ("Descriere:", self.description)
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "food":
         self.food = content
      elif self.CurrentData == "name":
         self.name = content
      elif self.CurrentData == "calories":
         self.calories = content
      elif self.CurrentData == "description":
         self.description = content
  
if ( __name__ == "__main__"):
   start_time = time.time() #returneaza timpul procesorului, calculand doar tipul acestui proces
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MenuHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("../tema3/database.xml")
   print("--- %s secunde ---" % (time.time() - start_time))