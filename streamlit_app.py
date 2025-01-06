import csv
import streamlit as st

# Load wishlist from CSV
def load_wishlist():
    wishlist = []
    with open('wishlist.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            wishlist.append({
                'id': row['id'],  # Ensure you're using the correct column name 'id'
                'name': row['name'],
                'price': row['price'],
                'url': row['url']
            })
    return wishlist

# Streamlit app
def app():
    # Load the wishlist
    wishlist = load_wishlist()

    # Main UI for the app
    st.title("Wishlist Tool")

    # View wishlist
    choice = st.selectbox("Select an option", ["View Wishlist", "Add Item", "Delete Item"])

    if choice == "View Wishlist":
        st.header(f"Your Wishlist ({len(wishlist)} items)")  # Display number of items
        for item in wishlist:
            st.markdown(f"### ID: {item['id']}")
            st.markdown(f"**Name:** {item['name']}")
            st.markdown(f"**Price:** {item['price']}")
            st.markdown(f"**URL:** [{item['url']}]({item['url']})", unsafe_allow_html=True)

    elif choice == "Add Item":
        st.subheader("Add New Item to Wishlist")
        name = st.text_input("Product Name")
        price = st.text_input("Price")
        url = st.text_input("URL")
        if st.button("Add Item"):
            # Add the item to the wishlist
            with open('wishlist.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([len(wishlist) + 1, name, price, url])  # Example logic to create ID
            st.success(f"Product '{name}' added to your wishlist!")

    elif choice == "Delete Item":
        st.subheader("Delete an Item from Wishlist")
        item_id = st.text_input("Enter Product ID to Delete")
        if st.button("Delete Item"):
            # Delete the item from the wishlist
            wishlist = [item for item in wishlist if item['id'] != item_id]
            with open('wishlist.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'name', 'price', 'url'])  # Write headers again
                for item in wishlist:
                    writer.writerow([item['id'], item['name'], item['price'], item['url']])
            st.success(f"Product ID {item_id} removed from your wishlist!")

# Run the Streamlit app
if __name__ == "__main__":
    app()
