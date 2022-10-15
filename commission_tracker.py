import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def initalise_firestore():
        
    # Setup Google Cloud Key - The json file is obtained by going to
    # Project Settings, Service Accounts, Create Service Account, and then
    # Generate New Private Key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cloud-database-a412e-firebase-adminsdk-p0f32-8834636a22.json"

    # Use the application default credentials. The projectID is obtianed
    # by going to Project Settings and then General.
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
    'projectId': 'cloud-database-a412e',
    })

    # Get reference to database
    db = firestore.client()

    # db = None
    return db

def add_new_commission(db):
    """
    Adds a new commission with the customer's name,
    the commission type, pricing, their request,
    completion status, and how much has been paid
    """
    name = input("Name: ").lower()

    result = db.collection("Commissions").document(name).get()
    if result.exists:
        print("This person already has a commission saved.")
        return

    type = input("Commission: ").lower()
    price = float(input("Price: "))
    request = input("Request: ").lower()
    status = input("Completed? (Y/N): ") in ['Y', 'y']
    pay = float(input("What have they paid?: "))

    data = {"Type": type,
            "Price" : price,
            "Request" : request,
            "Completed" : status,
            "Pay" : pay
            }

    db.collection("Commissions").document(name).set(data)

def update_payment(db):
    """
    If a customer has give money, it will be added
    into the "Pay" field
    """
    name = input("Who made the payment? ").lower()

    result = db.collection("Commissions").document(name).get()
    if not result.exists:
        print("This person does not exist.")
        return

    payment = float(input("How much was paid? "))

    data = result.to_dict()

    data["Pay"] += payment

    db.collection("Commissions").document(name).set(data)

def update_completion(db):
    """
    If a commission is completed, then this will update
    the "Completed" field to True
    """
    name = input("Who's commission did you complete? ").lower()
    
    result = db.collection("Commissions").document(name).get()
    if not result.exists:
        print("This person does not exist.")
        return
    
    db.collection("Commissions").document(name).update({"Completed" : True})

    print("Commission marked completed")

def delete_customer(db):
    """
    This will delete a customer from the collection.
    Requires a verification before it continues
    """
    name = input("Who would you like to delete? ").lower()

    result = db.collection("Commissions").document(name).get()
    if not result.exists:
        print("This person does not exist.")
        return

    print(f"WARNING: By deleting {name}, you will be permanently removing the customer and their info.")
    delete = input(f"To remove customer, please type '{name}': ")

    if delete == name:
        db.collection("Commissions").document(name).delete()
        print(f"Deleted {name}")

    else:
        print("Deletion cancelled")
        return
    
def display_data(db):
    """
    Searches the database based off their name, the
    commission type, or the completion status.
    """
    print("How would you like to search?")
    print("1. Name")
    print("2. Commission type")
    print("3. Completion Status")

    search = int(input(">> "))

    if search == 1:
        name = input("Who would you like to search for? ").lower()
        all_results = db.collection("Commissions").get()
        for results in all_results:
            data = results.to_dict()
            if results.id == name:
                print(f"Information: {data}")

    elif search == 2:
        #TODO: Fix the results, only showing the function location
        type = input("What type would you like to find? ").lower()
        all_results = db.collection("Commissions")
        print(all_results.where(type, '==', "type"))
        # for results in all_results:
        #     data = results.to_dict()
        #     print(results.id)
        #     print(data)
        #     print(results)

    elif search == 3:
        #TODO: Implement search by completion status
        pass

    

def main():
    # print("Loading Data...")

    db = initalise_firestore()
    choice = None

    while choice != 0:
        print("0. Exit")
        print("1. Add Commission")
        print("2. Update Payment")
        print("3. Mark Commission Completed")
        print("4. Delete Commission")
        print("5. Display data")
        choice = int(input(">> "))

        if choice == 1:
            add_new_commission(db)
        elif choice == 2:
            update_payment(db)
        elif choice == 3:
            update_completion(db)
        elif choice == 4:
            delete_customer(db)
        elif choice == 5:
            display_data(db)
        elif choice == 0:
            print("Exiting Program")
        else:
            print("Invalid number")

    # add_new_commission(db)
    # add_new_commission(db)
    # update_payment(db)
    # update_completion(db)
    # delete_customer(db)

if __name__ == "__main__":
    main()