import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create the database connection and table
conn = sqlite3.connect('safaritech.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        address TEXT NOT NULL
    )
''')
conn.commit() #Save the changes

# Function to insert data into the database
def save_entry():
    #Get values from input fields
    full_name = entry_full_name.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()
    date_of_birth = entry_date_of_birth.get()
    address = entry_address.get()
    
    #Check if all fields are filled
    if full_name and email and phone_number and date_of_birth and address:
        
        #insert data into the database
        cursor.execute('''
            INSERT INTO entries (full_name, email, phone_number, date_of_birth, address)
            VALUES (?, ?, ?, ?, ?)
        ''', (full_name, email, phone_number, date_of_birth, address))
        conn.commit()
        messagebox.showinfo("Success", "Entry saved successfully!") #Show the message of successful entry
        entry_full_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phone_number.delete(0, tk.END)
        entry_date_of_birth.delete(0, tk.END)
        entry_address.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields") #Show warning of empty field

# Function to display the report
def display_report():
    #Create a new window for the report
    report_window = tk.Toplevel(root)
    report_window.title("Entries Report")
    
    #Display the report
    report_text = tk.Text(report_window, wrap='word', width=80, height=20)
    report_text.pack(expand=True, fill='both')
    
    #Retrieve all the entries from the database
    cursor.execute('SELECT * FROM entries')
    entries = cursor.fetchall()
    
    report_text.insert(tk.END, f"{'ID':<5} {'Full Name':<20} {'Email':<30} {'Phone Number':<15} {'Date of Birth':<15} {'Address':<30}\n")
    report_text.insert(tk.END, "-"*115 + "\n")
    
    for entry in entries:
        report_text.insert(tk.END, f"{entry[0]:<5} {entry[1]:<20} {entry[2]:<30} {entry[3]:<15} {entry[4]:<15} {entry[5]:<30}\n")

# Create the main application window
root = tk.Tk()
root.title("SafariTech - Data Entry")

# Define and place the input fields and labels
tk.Label(root, text="Full Name").grid(row=0, column=0, padx=10, pady=5)
entry_full_name = tk.Entry(root, width=30)
entry_full_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number").grid(row=2, column=0, padx=10, pady=5)
entry_phone_number = tk.Entry(root, width=30)
entry_phone_number.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Date of Birth (YYYY-MM-DD)").grid(row=3, column=0, padx=10, pady=5)
entry_date_of_birth = tk.Entry(root, width=30)
entry_date_of_birth.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=4, column=0, padx=10, pady=5)
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=4, column=1, padx=10, pady=5)

# Define and place the buttons
tk.Button(root, text="Save Entry", command=save_entry).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="View Report", command=display_report).grid(row=5, column=1, padx=10, pady=10)

# Start the application
root.mainloop()

# Close the database connection when the application is closed
conn.close()
