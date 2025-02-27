import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Connect to the database and create it if not exists
def create_db():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cities (
            CityID INTEGER PRIMARY KEY,
            CityName TEXT,
            Population REAL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert new city into the database
def insert_city(city_name, population):
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cities (CityName, Population) VALUES (?, ?)", (city_name, population))
    conn.commit()
    conn.close()
    load_data()

# Function to fetch data from the Cities table
def fetch_data(order_by="CityID ASC"):
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Cities ORDER BY {order_by}")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to load data into the treeview
def load_data(order_by="CityID ASC"):
    for row in tree.get_children():
        tree.delete(row)
    rows = fetch_data(order_by)
    for row in rows:
        tree.insert("", "end", values=row)

# Function to calculate and display total population
def display_total_population():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Population) FROM Cities")
    total_population = cursor.fetchone()[0]
    conn.close()
    total_label.config(text=f"Total Population: {total_population}")

# Initialize main window
root = tk.Tk()
root.title("Cities Database GUI")
root.geometry("600x400")

# Create and place treeview for displaying data
tree = ttk.Treeview(root, columns=("CityID", "CityName", "Population"), show="headings")
tree.heading("CityID", text="City ID")
tree.heading("CityName", text="City Name")
tree.heading("Population", text="Population")
tree.column("CityID", width=80, anchor="center")
tree.column("CityName", width=200, anchor="center")
tree.column("Population", width=120, anchor="center")
tree.pack(fill="x", pady=10)

# Frame for buttons and actions
button_frame = tk.Frame(root)
button_frame.pack(fill="x")

# Create buttons for sorting
asc_population_btn = tk.Button(button_frame, text="Display Population Ascending", command=lambda: load_data("Population ASC"))
desc_population_btn = tk.Button(button_frame, text="Display Population Descending", command=lambda: load_data("Population DESC"))
desc_name_btn = tk.Button(button_frame, text="Display City Name Descending", command=lambda: load_data("CityName DESC"))
total_population_btn = tk.Button(button_frame, text="Display Total Population", command=display_total_population)

asc_population_btn.pack(side="left", padx=5, pady=5)
desc_population_btn.pack(side="left", padx=5, pady=5)
desc_name_btn.pack(side="left", padx=5, pady=5)
total_population_btn.pack(side="left", padx=5, pady=5)

# Label to display total population
total_label = tk.Label(root, text="Total Population: N/A")
total_label.pack()

# Frame for adding new data
add_data_frame = tk.Frame(root)
add_data_frame.pack(fill="x", pady=10)

# Entry fields for new city data
tk.Label(add_data_frame, text="City Name:").grid(row=0, column=0, padx=5)
city_name_entry = tk.Entry(add_data_frame)
city_name_entry.grid(row=0, column=1, padx=5)

tk.Label(add_data_frame, text="Population:").grid(row=0, column=2, padx=5)
population_entry = tk.Entry(add_data_frame)
population_entry.grid(row=0, column=3, padx=5)

# Function to handle adding new city data
def add_city():
    city_name = city_name_entry.get()
    try:
        population = float(population_entry.get())
        if city_name:
            insert_city(city_name, population)
            city_name_entry.delete(0, tk.END)
            population_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "City Name cannot be empty.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid population number.")

# Button to add new city data
add_city_btn = tk.Button(add_data_frame, text="Add City", command=add_city)
add_city_btn.grid(row=0, column=4, padx=5)

# Initialize database and load data
#create_db()
load_data()

# Run the application
root.mainloop()
