from Animals import Animal, Fish, Dino, Bird, Sloth, Panda

def animals():
#     a = Animal("George", "Elephant", "Grey")
#     print(a)
#     
#     b = Fish("Nemo", "Clownfish", "Orange", 4, 2)
#     print(b)
#     
#     c = Dino("Rex", "T-Rex", "Orange", [True,True,True,True,True,True], "XXL")
#     print(c)
#     
#     d = Bird("Jimbo", "Cassowary", "Blueish", "Up to 6 feet!!! (XXXL)", "Not-so-terrifying")
#     print(d)
#     
#     e = Sloth("Neely", "Two-Toed", "Clean Grey", "Fiesty", "Slow")
#     print(e)
#     
#     f = Panda("Alfred", "Giant", "Black and White", "Like 300 lbs", "Little")
#     print(f)
#     
#     print("Animals: {0}".format(a.animal_count()))
#     print("Fish: {0}".format(b.fish_count()))
#     print("Dinos: {0}".format(c.dino_count()))
#     print("Birds: {0}".format(d.bird_count()))
#     print("Sloths: {0}".format(e.sloth_count()))
#     print("Pandas: {0}".format(f.panda_count()))
#     
#     fishL = []
#     
#     for i in range(500):
#         fishL.append(Fish())
#         
#     for f in fishL:
#         print(f)

    a = Animal("George", "Giraffe", "Blue")
    b = Animal("Jeff", "Jaguar", "Grey")
    c = Animal("Jeff", "Jaguar", "Grey")
    
    print(repr(a))
    
#     print("Eq: {0}".format(c == a))
#     print("NE: {0}".format(c != a))
#     print("LT: {0}".format(a < b))
#     print("LE: {0}".format(a <= b))
#     print("GT: {0}".format(a > b))
#     print("GE: {0}".format(a > b))

    d = Fish("Steve", "Clownfish", "Orange", 2, 2)
    d2 = Fish("Steve", "Clownfish", "Orange", 2, 2)
    e = Fish("Crystal", "Catfish", "Green", 14, 5)
    
    notafish = "Fish:Animal: Name=Steve, Species=Clownfish, Color=Orange, Fins=2, Eyes=2"
    
#     print("Eq: {0}".format(d == d2))
#     print("NE: {0}".format(d != d2))
#     print("LT: {0}".format(d < e))
#     print("LE: {0}".format(d <= e))
#     print("GT: {0}".format(d > e))
#     print("GE: {0}".format(d >= e))

    print(repr(a))
    print(repr(d))
    
if __name__ == '__main__':
    animals()
