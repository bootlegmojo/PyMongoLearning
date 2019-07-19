from pymongo import  MongoClient

host = "localhost"
port = 27017
client = MongoClient(host, port)
mydb = client["TesGo"]
item_collection = mydb["item"]


client.close()


def inserttestdata():
    new_items = [
        {"name": "TesGo's own, Bread", "brand":"TesGo Bakery","category":"Bakery", "price":1.00, "stock":120 },
        {"name": "TesGo's own, Muffins", "brand":"TesGo Bakery","category":"Bakery", "price":1.50, "stock":40 },
        {"name": "TesGo's own, Cookies", "brand":"TesGo Bakery","category":"Bakery", "price":1.50, "stock":46 },
        {"name": "Bepsi 500ml", "brand":"Bepsi","category":"Soft Drink", "price":0.59, "stock":221 },
        {"name": "Bepsi Max 2L", "brand":"Bepsi","category":"Soft Drink", "price":1.49, "stock":120 },
        {"name": "Badbury Dairy Milk", "brand":"Badbury","category":"Confectionary", "price":0.59, "stock":159 },
        {"name": "Spinder Egg", "brand":"Spinder","category":"Confectionary", "price":0.80, "stock":167 },
        {"name": "Spinder Bueno", "brand":"Spinder","category":"Confectionary", "price":0.79, "stock":123 },
        {"name": "Pomestos Pink Bleach", "brand":"Pomestos","category":"Kitchen/Bathroom", "price":1.29, "stock":79 },
        {"name": "Spandrex Skin Kind 16 Roll", "brand":"Spandrex","category":"Kitchen/Bathroom", "price":4.50, "stock":56 },
        {"name": "Medigree Dog Food Pouches", "brand":"Medigree","category":"Pet", "price":2.29, "stock":43 },
        {"name": "Coco Pups", "brand":"Gellogs","category":"Cereal", "price":1.50, "stock":53 }
    ]
    new_ids = item_collection.insert_many(new_items)

    print("Inserted IDs")
    for id in new_ids.inserted_ids:
        print(id)

def insertitem():
    name = input("Enter Name: ")
    brand = input("Enter Brand: ")
    category =input("Enter Category: ")
    price = float(input("Enter Price e.g.(00.00): "))
    stock = int(input("Enter Stock: "))

    new_item = [{"name": name, "brand": brand, "category": category, "price": price, "stock": stock}]
    new_ids = item_collection.insert_many(new_item)

    print ("Inserted IDs")
    for id in new_ids.inserted_ids:
        print(id)



def findname():
    inp = input("Enter name: ")
    namequery = {"name": inp }
    names = item_collection.find(namequery)


    for name in names:
        print(name)
    if names.retrieved == 0:
        print("name not found: "+ inp)
    else:
        print(" %s items found with the name: %s " % (names.retrieved, inp))


def findbrand():
    inp = input("Enter brand: ")
    brandquery = {"brand": inp }
    brands = item_collection.find(brandquery)


    for brand in brands:
        print(brand)
    if brands.retrieved == 0:
        print("Brand not found: "+ inp)
    else:
        print(" %s items found with the brand: %s " % (brands.retrieved, inp))

def findcategory():
    inp = input("Enter category: ")
    categoryquery = {"category": inp }
    categorys = item_collection.find(categoryquery)


    for category in categorys:
        print(category)
    if categorys.retrieved == 0:
        print("category not found: "+ inp)
    else:
        print(" %s items found with the category: %s " % (categorys.retrieved, inp))


def stockupdate():
    myquery = {"name": input("Enter the name of the item that you want to update the stock to: ")}
    newvalues = {"$set": {"stock": int(input ("Assign the new stock value: "))}}

    result = item_collection.update_one(myquery, newvalues)
    print("%d documents matched, %d documents updated"
        %(result.matched_count, result.modified_count))

def priceupdate():
    myquery = {"name": input("Enter the name of the item that you want to update the stock to: ")}
    newvalues = {"$set": {"price": float(input ("Assign the new price value(00.00): "))}}

    result = item_collection.update_one(myquery, newvalues)
    print("%d documents matched, %d documents updated"
        %(result.matched_count, result.modified_count))


#THIS WILL CLEAR ALL ITEMS--------------------------------------------
def deleteallitems():
    x = item_collection.delete_many({})

    print(x.deleted_count, " documents deleted.")


def listitems():
    cursor = item_collection.find({}) 

    for document in cursor:
        print(document)

#deleteallitems()
#inserttestdata()
#insertitem()
#findname()
#findbrand()
#findcategory()
#listitems()
#stockupdate()
#findname()



def TesGopy():
    
    userimp = input("select opperation (type help for list): ")

    while userimp != exit:
        
        if userimp == "help":
            print("\nlistitems = Lists all current items in the database")#
            print("findname = returns a specific item by name")
            print("findbrand = returns items with a matching brand")
            print("findcategory = returns items with a matching category")
            print("insertitem = adds an item to the database")
            print("stockupdate - updates the stock of a selected item")
            print("priceupdate - updates the price of a selected item\n")
            break

        elif userimp == "listitems":
            listitems()
            break

        elif userimp == "findname":
            findname()
            break

        elif userimp == "findbrand":
            findbrand()
            break

        elif userimp == "findcategory":
            findcategory()
            break

        elif userimp == "insertitem":
            insertitem()
            break

        elif userimp == "stockupdate":
            stockupdate()
            break

        elif userimp == "priceupdate":
            priceupdate()
            break

        elif userimp == "inserttestdata":
            inserttestdata()
            break

        elif userimp == "deleteallitems":
            deleteallitems()
            break

        else:
            break


    TesGopy()

TesGopy()