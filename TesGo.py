from pymongo import  MongoClient

host = "localhost"
port = 27017
client = MongoClient(host, port)
mydb = client["TesGo"]
item_collection = mydb["item"]
staff_collection = mydb["staff"]

client.close()

class Staff():
    
    def addstaff():
        name = input("Enter Name: ")
        role = input("Enter Role: ")
        salary = int(input("Enter Salary: "))
        store = input("Enter Store: ")
        
        new_staff = [{"name": name, "role": role, "salary": salary, "store": store}]
        new_ids = staff_collection.insert_many(new_staff)

        print ("Inserted IDs")
        for id in new_ids.inserted_ids:
            print(id)

    def removestaff():
        
        staff = {"name": input("Enter name of employee to remove: "), "role":input("Enter this employees current role: ")}
        results = staff_collection.delete_one(staff)
        print("\n Deleted %d user's" % (results.deleted_count))

    def updatestaff():
        cat = input("What would you like to change?: ")
        myquery = {"name": input("Enter the name of the person to update: ")}
        newvalues = {"$set": {cat: input("Enter the new value for this person: ")}}

        result = staff_collection.update_one(myquery, newvalues)
        print("%d documents matched, %d documents updated"
            %(result.matched_count, result.modified_count))

    def storestaff():
        inp = input("Enter store: ")
        storequery = {"store": inp }
        stores = staff_collection.find(storequery)


        for store in stores:
            print(store)
        if stores.retrieved == 0:
            print("store not found: "+ inp)
        else:
            print(" %s items found with the store: %s " % (stores.retrieved, inp))
    
    def TesGopy():
        
        userimp = input("select opperation (type help for a list): ")

        while userimp != exit:
            
            if userimp == "help":
                print("\n \"addstaff\" - Add staff to the system\n")
                print("\n \"removestaff\" - Remove staff from the system\n")
                print("\n \"updatestaff\" - Update staff details within the system\n")
                print("\n \"storestaff\" - View all staff from a perticular store\n")
                break
                
                
            elif userimp == "addstaff":
                Staff.addstaff()
                break

            elif userimp == "removestaff":
                Staff.removestaff()
                break

            elif userimp == "updatestaff":
                Staff.updatestaff()
                break

            elif userimp == "storestaff":
                Staff.storestaff()
                break


            else:
                break


        Staff.TesGopy()



class Item():
    
    def addtestdata():
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


    
    def deleteallitems():
        x = item_collection.delete_many({})

        print(x.deleted_count, " documents deleted.")


    def listitems():
        cursor = item_collection.find({}) 

        for document in cursor:
            print("\n %s" % document)

    


    def TesGopy():
        
        userimp = input("select opperation (type help for a list): ")

        while userimp != exit:
            
            if userimp == "help":
                print("\n \"listitems\" = Lists all current items in the database\n")
                print("\n \"findname\" = returns a specific item by name\n")
                print("\n \"findbrand\" = returns items with a matching brand\n")
                print("\n \"findcategory\" = returns items with a matching category\n")
                print("\n \"insertitem\" = adds an item to the database\n")
                print("\n \"stockupdate\" - updates the stock of a selected item\n")
                print("\n \"priceupdate\" - updates the price of a selected item\n")
                break

            elif userimp == "listitems":
                Item.listitems()
                break

            elif userimp == "findname":
                Item.findname()
                break

            elif userimp == "findbrand":
                Item.findbrand()
                break

            elif userimp == "findcategory":
                Item.findcategory()
                break

            elif userimp == "insertitem":
                Item.insertitem()
                break

            elif userimp == "stockupdate":
                Item.stockupdate()
                break

            elif userimp == "priceupdate":
                Item.priceupdate()
                break

            elif userimp == "inserttestdata":
                Item.inserttestdata()
                break

            elif userimp == "deleteallitems":
                Item.deleteallitems()
                break

            else:
                break


        Item.TesGopy()

   

def startup():
        
        colselect = input("select collection to access (type help for a list): ")

        while colselect != exit:
            
            if colselect == "help":
                print("\n \"items\" - Access and modify the item database\n")
                print("\n \"staff\" - Access and modify the staff database\n")
                break
            
            elif colselect == "items":
                Item.TesGopy()
                break
            
            elif colselect == "staff":
                Staff.TesGopy()
                break

            else:
                startup()
        
        startup()

startup()