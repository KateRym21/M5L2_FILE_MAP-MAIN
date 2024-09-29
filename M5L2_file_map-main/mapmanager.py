
class Mapmanager():
   """ Управління карткою """
   def __init__(self):
       self.model = 'block' # модель кубика лежить у файлі block.egg
       # # використовуються такі текстури:
       self.texture = 'block.png'        
       self.color = (0.2, 0.2, 0.35, 1) #rgba

       # створюємо основний вузол картки:
       self.startNew()
        # створюємо будівельні блоки   
       self.addBlock((0,10, 0))
       self.addBlock((10,10, 0))
       self.addBlock((0,10, 10))


   def startNew(self):
       """створює основу для нової картки"""
       self.land = render.attachNewNode("Land") # вузол, до якого прив'язані всі блоки картки
  
   def addBlock(self, position):
       self.block = loader.loadModel(self.model)
       self.block.setTexture(loader.loadTexture(self.texture))
       self.block.setPos(position)
       self.block.setColor(self.color)
       self.block.reparentTo(self.land)
   def loadLand(self, fileName):
       with open(fileName) as file:
           y = 0
           for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x,y, z0))
                    x +=1
                y +=1


  def clear(self):
      self.land.removeNode()
      self.starNew()
