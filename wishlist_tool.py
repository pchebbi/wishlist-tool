import csv
import random
import os

# Path to the CSV file where the wishlist will be saved
wishlist_file = 'wishlist.csv'

# Function to load the wishlist from the CSV file
import csv

def load_wishlist():
    wishlist = []
    try:
        with open('wishlist.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, quotechar='"')
            for row in reader:
                # Ensure data is cleaned and properly parsed
                wishlist.append({
                    'id': int(row['ID']),
                    'name': row['Name'],
                    'price': row['Price'],
                    'url': row['URL']
                })
    except FileNotFoundError:
        print("Wishlist file not found!")
    return wishlist



# Function to save the wishlist to the CSV file
def save_wishlist(wishlist):
    with open(wishlist_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['ID', 'Name', 'Price', 'URL']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  # Write header row
        for item in wishlist:
            writer.writerow(item)

# Function to generate a random ID for each product
def generate_random_id():
    return random.randint(1000, 9999)

# Function to add an item to the wishlist
def add_item(wishlist):
    name = input("Enter the name of the product: ")
    price = input("Enter the price of the product: ")
    url = input("Enter the URL of the product: ")
    product = {
        'id': generate_random_id(),
        'name': name,
        'price': price,
        'url': url
    }
    wishlist.append(product)
    print("Product added successfully!")
    save_wishlist(wishlist)  # Save to CSV after adding the item

# Function to view the wishlist
def view_wishlist(wishlist):
    if not wishlist:
        print("Your wishlist is empty.")
    else:
        print("Your Wishlist:")
        for item in wishlist:
            print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, URL: {item['url']}")

# Function to delete an item from the wishlist
def delete_item(wishlist):
    item_id = int(input("Enter the ID of the product you want to delete: "))
    for item in wishlist:
        if item['id'] == item_id:
            wishlist.remove(item)
            print(f"Product with ID {item_id} has been removed from your wishlist!")
            save_wishlist(wishlist)  # Save to CSV after deleting the item
            return
    print("Product not found!")

# Main program logic
def main():
    wishlist = load_wishlist()  # Load the wishlist from the file

    while True:
        print("\n1. Add Item")
        print("2. View Wishlist")
        print("3. Delete Item")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(wishlist)
        elif choice == '2':
            view_wishlist(wishlist)
        elif choice == '3':
            delete_item(wishlist)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == '__main__':
    main()
