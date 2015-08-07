# class Ninja(object):
#     def __init__ (self, name,level): #different for all ninjas
#         self.name=name
#         self.level=level
#         self.outfit='black' #same for all ninjas
#     def fight(self, other):
#         if self.level > other.level:
#             print "I win!"
#         elif self.level == other.level:
#             print "We are equal and tied!"
#         else:
#             print "I lose, cause I am the weaker ninja!"
#
#     def describe(self):
#         print 'I am Ninja' + self.name + 'level' + self.level + 'and I wear' + self.outfit
#
#     def promote (self, other):
#         if self.level > other.level:
#             other.level=other.level+1
#
#     class Sensei (Ninja):
#         def __init__ (self, name, level):
#             self.name=name
#             self.level=level
#             self.outfit='yellow'
#
#
#
#     sensei1=Sensei1('Zohra', 1000)
#
# ninja1=Ninja('Tyson', 1)
# print ninja1.name
#
#
# ninja2.level ('Tyson',2 )
#
# ninja1.fight(ninja1) #tie
#
# ninja2.fight(ninja1) # I win. self is outside, ninja2 ,
#
# ninja1.fight(ninja2) # I lose
#
#
# class Monster(object):
#     def __init__ (self, name, height, type):
#         self.name=name
#         self.height=height
#         self.type=type
#
#     def taller_Monster(self,other):
#         if self.height > other. height:
#             print "I am Taller"
#         elif self.height == other.height:
#             print "Both of you are the same height"
#         else:
#             print "You are shorter!"
#
#     def fight_Ninja (self, other):
#         if self.height > other.level:
#             print "You win"
#         elif self.height == other.level:
#                 print "You are tied"
#             else self.heigh < other.level:
#                 print "You lose!"
#
# monster1=Monster('Godzilla', 1000, 'Earth')
#
# monster2=Monster('Loch Ness', 2000, 'Water')
#
# monster1.taller_Monster(monster2)
# monster1.fight_Ninja(ninja1)
