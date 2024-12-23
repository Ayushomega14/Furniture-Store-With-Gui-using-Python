import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Function to connect to the MySQL database using provided credentials
def connect_to_database():
    try:
        # Get username and password from entry field
        username = username_entry.get()
        password = password_entry.get()

        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Display success message
        messagebox.showinfo("Success", "Connected to MySQL database successfully!")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

        # Remove username and password widgets from the screen
        username_label.pack_forget()
        username_entry.pack_forget()
        password_label.pack_forget()
        password_entry.pack_forget()
        connect_button.pack_forget()

        # Display welcome message
        welcome_label.config(text="Welcome to Furniture Store")

        # Create button to fetch and display store details
        store_details_button = tk.Button(root, text="Store Details", command=fetch_store_details)
        store_details_button.pack(pady=10)

        # Create button to show all employees
        show_employees_button = tk.Button(root, text="Show Employees", command=show_all_employees)
        show_employees_button.pack(pady=10)

        # Create button to show product details
        product_details_button = tk.Button(root, text="Product Details", command=show_product_details)
        product_details_button.pack(pady=10)

        # Create button to make a purchase
        purchase_button = tk.Button(root, text="Purchase", command=make_purchase)
        purchase_button.pack(pady=10)

        # Create button to display recent purchases
        recent_purchase_button = tk.Button(root, text="Recent Purchase", command=display_recent_purchase)
        recent_purchase_button.pack(pady=10)

        # Create button to display customer details
        customer_button = tk.Button(root, text="Customers", command=display_customer_details)
        customer_button.pack(pady=10)

        # Create button to display offers
        offers_button = tk.Button(root, text="Offers", command=display_offers)
        offers_button.pack(pady=10)

        # Create button to submit feedback
        feedback_button = tk.Button(root, text="Feedback", command=submit_feedback)
        feedback_button.pack(pady=10)

    except mysql.connector.Error as err:
        # Display error message if connection fails
        messagebox.showerror("Error", f"Failed to connect to MySQL database: {err}")

# Function to fetch and display store details
def fetch_store_details():
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to fetch store details in Chennai
        mycursor.execute("SELECT * FROM StoreDetails WHERE Address = 'Chennai'")
        store_details = mycursor.fetchall()

        # Display store details
        for store in store_details:
            messagebox.showinfo("Store Details", f"Branch ID: {store[0]}\nStore Branch: {store[1]}\nAddress: {store[2]}\nContact: {store[3]}\nManager ID: {store[4]}")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to fetch store details: {err}")

# Function to show employees based on selected position
def show_all_employees():
    # Create a new window for selecting position
    position_window = tk.Toplevel(root)
    position_window.title("Select Position")

    # Create label and dropdown menu for selecting position
    position_label = tk.Label(position_window, text="Select Position:")
    position_label.pack(pady=5)

    position_var = tk.StringVar(position_window)
    position_var.set("Manager")  # Default position

    position_options = ["Manager", "Assistant Manager", "Regular"]
    position_dropdown = tk.OptionMenu(position_window, position_var, *position_options)
    position_dropdown.pack(pady=5)

    # Create button to execute query based on selected position
    select_button = tk.Button(position_window, text="Select", command=lambda: execute_query(position_var.get()))
    select_button.pack(pady=10)

def execute_query(position):
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to fetch employees based on selected position
        mycursor.execute("SELECT Emp_ID, Emp_Name, Emp_Position, Emp_PhNo, Emp_Email FROM employee WHERE Emp_Position = %s", (position,))
        employees = mycursor.fetchall()

        # Display employee details
        for employee in employees:
            messagebox.showinfo("Employee Details", f"Employee ID: {employee[0]}\nName: {employee[1]}\nPosition: {employee[2]}\nPhone Number: {employee[3]}\nEmail: {employee[4]}")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to fetch employee details: {err}")

# Function to show product details based on selection
def show_product_details():
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to fetch all product names
        mycursor.execute("SELECT Prod_Name FROM PRODUCT")
        products = mycursor.fetchall()
        product_names = [product[0] for product in products]

        # Create a new window for selecting product
        product_window = tk.Toplevel(root)
        product_window.title("Select Product")

        # Create label and dropdown menu for selecting product
        product_label = tk.Label(product_window, text="Select Product:")
        product_label.pack(pady=5)

        product_var = tk.StringVar(product_window)
        product_var.set(product_names[0])  # Default product

        product_dropdown = tk.OptionMenu(product_window, product_var, *product_names)
        product_dropdown.pack(pady=5)

        # Function to execute when the stock button is clicked
        def show_stock():
            selected_product = product_var.get()
            check_stock_availability(selected_product)

        # Create button to execute query based on selected product
        select_button = tk.Button(product_window, text="Select", command=lambda: show_product(product_var.get()))
        select_button.pack(pady=10)

        # Create button to check stock availability
        stock_button = tk.Button(product_window, text="Check Stock Availability", command=show_stock)
        stock_button.pack(pady=10)

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to fetch product details: {err}")

def show_product(product_name):
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to fetch product details based on selected product
        mycursor.execute("SELECT Prod_ID, Prod_Name, Prod_Price FROM PRODUCT WHERE Prod_Name = %s", (product_name,))
        product_details = mycursor.fetchone()

        # Display product details
        messagebox.showinfo("Product Details", f"Product ID: {product_details[0]}\nName: {product_details[1]}\nPrice: {product_details[2]}")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

        # Create a button to check stock availability
        stock_button = tk.Button(root, text="Check Stock Availability", command=lambda: check_stock_availability(product_name))
        stock_button.pack(pady=10)

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to fetch product details: {err}")

def check_stock_availability(product_name):
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to fetch stock availability based on selected product
        mycursor.execute("SELECT Stock_Capacity, Stock_Avail FROM STOCK WHERE Stock_ID = (SELECT StockID FROM PRODUCT WHERE Prod_Name = %s)", (product_name,))
        stock = mycursor.fetchone()

        # Display stock availability
        messagebox.showinfo("Stock Availability", f"Stock Capacity: {stock[0]}\nStock Available: {stock[1]}")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to fetch stock availability: {err}")

# Function to make a purchase
def make_purchase():
    # Create a new window for making a purchase
    purchase_window = tk.Toplevel(root)
    purchase_window.title("Make a Purchase")

    # Create labels and entry fields for purchase details
    customer_name_label = tk.Label(purchase_window, text="Customer Name:")
    customer_name_label.pack(pady=5)
    customer_name_entry = tk.Entry(purchase_window)
    customer_name_entry.pack(pady=5)

    contact_number_label = tk.Label(purchase_window, text="Contact Number:")
    contact_number_label.pack(pady=5)
    contact_number_entry = tk.Entry(purchase_window)
    contact_number_entry.pack(pady=5)

    order_id_label = tk.Label(purchase_window, text="Order ID:")
    order_id_label.pack(pady=5)
    order_id_entry = tk.Entry(purchase_window)
    order_id_entry.pack(pady=5)

    product_name_label = tk.Label(purchase_window, text="Product Name:")
    product_name_label.pack(pady=5)
    product_name_var = tk.StringVar(purchase_window)
    product_name_var.set("Table")  # Default product
    product_name_options = ["Table", "Sofa", "Cot", "Dresser", "Shelf"]
    product_name_dropdown = tk.OptionMenu(purchase_window, product_name_var, *product_name_options)
    product_name_dropdown.pack(pady=5)

    amount_label = tk.Label(purchase_window, text="Amount:")
    amount_label.pack(pady=5)
    amount_entry = tk.Entry(purchase_window, state='readonly')
    amount_entry.pack(pady=5)

    quantity_label = tk.Label(purchase_window, text="Quantity:")
    quantity_label.pack(pady=5)
    quantity_var = tk.IntVar(purchase_window)
    quantity_var.set(1)  # Default quantity
    quantity_entry = tk.Spinbox(purchase_window, from_=1, to=10, textvariable=quantity_var)
    quantity_entry.pack(pady=5)

    total_label = tk.Label(purchase_window, text="Total:")
    total_label.pack(pady=5)
    total_entry = tk.Entry(purchase_window, state='readonly')
    total_entry.pack(pady=5)

    payment_method_label = tk.Label(purchase_window, text="Payment Method:")
    payment_method_label.pack(pady=5)
    payment_method_var = tk.StringVar(purchase_window)
    payment_method_var.set("Cash")  # Default payment method
    payment_method_options = ["Cash", "UPI", "Card"]
    payment_method_dropdown = tk.OptionMenu(purchase_window, payment_method_var, *payment_method_options)
    payment_method_dropdown.pack(pady=5)

    # Function to update amount based on product selection
    def update_amount():
        product = product_name_var.get()
        if product == "Sofa":
            amount_entry.config(state='normal')
            amount_entry.delete(0, tk.END)
            amount_entry.insert(0, "12000")
            amount_entry.config(state='readonly')
        elif product == "Cot":
            amount_entry.config(state='normal')
            amount_entry.delete(0, tk.END)
            amount_entry.insert(0, "15000")
            amount_entry.config(state='readonly')
        elif product == "Dresser":
            amount_entry.config(state='normal')
            amount_entry.delete(0, tk.END)
            amount_entry.insert(0, "7000")
            amount_entry.config(state='readonly')
        elif product == "Shelf":
            amount_entry.config(state='normal')
            amount_entry.delete(0, tk.END)
            amount_entry.insert(0, "3000")
            amount_entry.config(state='readonly')
        else:
            amount_entry.config(state='normal')
            amount_entry.delete(0, tk.END)
            amount_entry.insert(0, "10000")
            amount_entry.config(state='readonly')

        update_total()

    # Function to update total based on amount and quantity
    def update_total():
        amount = float(amount_entry.get())
        quantity = int(quantity_entry.get())
        total = amount * quantity
        total_entry.config(state='normal')
        total_entry.delete(0, tk.END)
        total_entry.insert(0, total)
        total_entry.config(state='readonly')

    # Update amount and total when product selection changes
    product_name_var.trace('w', lambda *args: update_amount())

    # Update total when quantity changes
    quantity_var.trace('w', lambda *args: update_total())

    # Create button to place order
    place_order_button = tk.Button(purchase_window, text="Place Order", command=lambda: place_order(customer_name_entry.get(), contact_number_entry.get(), order_id_entry.get(), product_name_var.get(), total_entry.get(), payment_method_var.get()))
    place_order_button.pack(pady=10)

def place_order(customer_name, contact_number, order_id, product_name, total, payment_method):
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to insert purchase details into the database
        sql = "INSERT INTO Purchase (Customer_Name, Contact_Number, Order_ID, Product_Name, Total, Payment_Method) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (customer_name, contact_number, order_id, product_name, total, payment_method)
        mycursor.execute(sql, val)
        mydb.commit()

        # Display success message
        messagebox.showinfo("Success", "Purchase order placed successfully!")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to place purchase order: {err}")

# Function to display recent purchase based on order ID
def display_recent_purchase():
    # Create a new window for displaying recent purchase
    recent_purchase_window = tk.Toplevel(root)
    recent_purchase_window.title("Recent Purchase")

    # Create label and entry field for entering order ID
    order_id_label = tk.Label(recent_purchase_window, text="Enter Order ID:")
    order_id_label.pack(pady=5)
    order_id_entry = tk.Entry(recent_purchase_window)
    order_id_entry.pack(pady=5)

    # Create button to display purchase details based on order ID
    display_button = tk.Button(recent_purchase_window, text="Display", command=lambda: fetch_purchase_details(order_id_entry.get()))
    display_button.pack(pady=10)

def fetch_purchase_details(order_id):
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to fetch purchase details based on order ID
        mycursor.execute("SELECT customer_id, customer_name, contact_number, order_id, product_name, amount, quantity, total, payment_method FROM Purchase WHERE order_id = %s", (order_id,))
        purchase_details = mycursor.fetchone()

        # Display purchase details
        messagebox.showinfo("Purchase Details", f"Customer ID: {purchase_details[0]}\nCustomer Name: {purchase_details[1]}\nContact Number: {purchase_details[2]}\nOrder ID: {purchase_details[3]}\nProduct Name: {purchase_details[4]}\nAmount: {purchase_details[5]}\nQuantity: {purchase_details[6]}\nTotal: {purchase_details[7]}\nPayment Method: {purchase_details[8]}")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to fetch purchase details: {err}")

# Function to display customer details based on customer ID
def display_customer_details():
    # Create a new window for displaying customer details
    customer_window = tk.Toplevel(root)
    customer_window.title("Customer Details")

    # Create label and entry field for entering customer ID
    customer_id_label = tk.Label(customer_window, text="Enter Customer ID:")
    customer_id_label.pack(pady=5)
    customer_id_entry = tk.Entry(customer_window)
    customer_id_entry.pack(pady=5)

    # Create button to display customer details based on customer ID
    display_button = tk.Button(customer_window, text="Display", command=lambda: fetch_customer_details(customer_id_entry.get()))
    display_button.pack(pady=10)

def fetch_customer_details(customer_id):
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to fetch customer details based on customer ID
        mycursor.execute("SELECT customer_id, customer_name, customer_email, customer_Phno, Customer_Address FROM customer WHERE customer_id = %s", (customer_id,))
        customer_details = mycursor.fetchone()

        # Display customer details
        messagebox.showinfo("Customer Details", f"Customer ID: {customer_details[0]}\nCustomer Name: {customer_details[1]}\nEmail: {customer_details[2]}\nPhone Number: {customer_details[3]}\nAddress: {customer_details[4]}")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to fetch customer details: {err}")

# Function to display offers based on offer type
def display_offers():
    # Create a new window for displaying offers
    offer_window = tk.Toplevel(root)
    offer_window.title("Offers")

    # Create label and dropdown menu for selecting offer type
    offer_type_label = tk.Label(offer_window, text="Select Offer Type:")
    offer_type_label.pack(pady=5)

    offer_type_var = tk.StringVar(offer_window)
    offer_type_var.set("Daily")  # Default offer type

    offer_type_options = ["Daily", "Weekend", "Holiday", "Monthly", "Clearance", "Festivals", "Yearly"]
    offer_type_dropdown = tk.OptionMenu(offer_window, offer_type_var, *offer_type_options)
    offer_type_dropdown.pack(pady=5)

    # Create button to display offers based on selected offer type
    display_button = tk.Button(offer_window, text="Display", command=lambda: fetch_offers(offer_type_var.get()))
    display_button.pack(pady=10)

def fetch_offers(offer_type):
    try:
        # Establish connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@Ayu1411",  # Replace with your MySQL password
            database="furniturestore"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to fetch offers based on selected offer type
        mycursor.execute("SELECT offer_id, offer_type, discount_percentage, product_included, conditions FROM offer WHERE offer_type = %s", (offer_type,))
        offers = mycursor.fetchall()

        # Display offers
        offer_details = ""
        for offer in offers:
            offer_details += f"Offer ID: {offer[0]}\nOffer Type: {offer[1]}\nDiscount Percentage: {offer[2]}\nProduct Included: {offer[3]}\nConditions: {offer[4]}\n\n"

        messagebox.showinfo("Offers", offer_details)

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Display error message if query fails
        messagebox.showerror("Error", f"Failed to fetch offers: {err}")

# Function to submit feedback
def submit_feedback():
    # Create a new window for submitting feedback
    feedback_window = tk.Toplevel(root)
    feedback_window.title("Submit Feedback")

    # Create labels and entry fields for feedback details
    order_id_label = tk.Label(feedback_window, text="Order ID:")
    order_id_label.pack(pady=5)
    order_id_entry = tk.Entry(feedback_window)
    order_id_entry.pack(pady=5)

    rating_label = tk.Label(feedback_window, text="Rating (1-5):")
    rating_label.pack(pady=5)
    rating_var = tk.IntVar(feedback_window)
    rating_entry = tk.Spinbox(feedback_window, from_=1, to=5, textvariable=rating_var)
    rating_entry.pack(pady=5)

    text_feedback_label = tk.Label(feedback_window, text="Text Feedback:")
    text_feedback_label.pack(pady=5)
    text_feedback_entry = tk.Text(feedback_window, height=5, width=50)
    text_feedback_entry.pack(pady=5)

    # Function to submit feedback to the database
    def submit_feedback_to_database():
        try:
            # Establish connection to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="@Ayu1411",  # Replace with your MySQL password
                database="furniturestore"
            )

            # Create a cursor object to execute SQL queries
            mycursor = mydb.cursor()

            # Get feedback details from entry fields
            order_id = order_id_entry.get()
            rating = rating_var.get()
            text_feedback = text_feedback_entry.get("1.0", tk.END)

            # Execute SQL query to insert feedback into the database
            sql = "INSERT INTO feedback (order_id, rating, text_feedback) VALUES (%s, %s, %s)"
            val = (order_id, rating, text_feedback)
            mycursor.execute(sql, val)
            mydb.commit()

            # Display success message
            messagebox.showinfo("Success", "Feedback submitted successfully!")

            # Close the cursor and connection
            mycursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            # Display error message if query fails
            messagebox.showerror("Error", f"Failed to submit feedback: {err}")

    # Create button to submit feedback
    submit_button = tk.Button(feedback_window, text="Submit", command=submit_feedback_to_database)
    submit_button.pack(pady=10)

# Create the main application window
root = tk.Tk()
root.title("Furniture Store Management System")
root.geometry("600x600")
root.configure(bg='sky blue')  # Set background color to sky blue

# Create labels and entry fields for MySQL database credentials
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Create button to connect to the database
connect_button = tk.Button(root, text="Connect", command=connect_to_database)
connect_button.pack(pady=10)

# Label to display welcome message
welcome_label = tk.Label(root, text="")
welcome_label.pack(pady=10)

root.mainloop()
