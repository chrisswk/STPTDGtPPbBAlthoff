my_tuple = tuple()
print(my_tuple)

my_tuple = ()
print(my_tuple)

rndm = ("M. Jackson", 1958, True)
print(rndm)

("self_taught",)

dys = ("1984", "Brave new World", "Fahrenheit 451")
print(dys[1])

#dys[1] = "Handmaid's Tale"
print("1984" in dys)
print("Handmaid's Tale" not in dys)

my_dict = dict()
my_dict
print(my_dict)

my_dict = {}
print(my_dict)

fruits = {"Apple": "Red", "Banana": "Yellow"}
print(fruits)

facts = dict()

# add a value
facts["code"] = "fun"
# look up a key
print(facts["code"])

facts["Bill"] = "Gates"
print(facts["Bill"])

facts["founded"] = 1776
print(facts["founded"])

bill = dict({"Bill Gates": "charitable"})
#print(bill["hey"])
print("Bill Gates" in bill)
print("Bill Doors" not in bill)

books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}
del books["The Trial"]
print(books)

rhymes = {"1": "fun", 
        "2": "blue",
        "3": "me",
        "4": "floor",
        "5": "live"
        }
n = 2
#n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")

lists = []
rap = ["Kanye West", "Jay Z", "Eminem", "Nas"]

rock = ["Bob Dylan", "The Beatles", "Led Zeppelin"]

djs = ["Zeds Dead", "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)

rap = lists[0]
print(rap)
rap.append("Kendrick Lamar")
print(lists)

locations = []
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)
print(locations)

eights = ["Edgar Allen Poe", "Charles Dickens"]

nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
print(authors)

bday = {"Hemingway": "7.21.1899", "Fitzgerald": "9.24.1896"}

my_list = [bday]
print(my_list)
my_tuple = (bday, )
print(my_tuple)

me = {"height": "72", "color": "green", "author": "say"}
print(me[input("height, color or author?")])

frank_black = ["Violet", "Don't Clip Your Wings", ]