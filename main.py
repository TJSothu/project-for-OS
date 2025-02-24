import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Dynamic Memory Management Visualizer")
root.geometry("500x400")


# Function to handle the "Simulate" button click
def simulate():
    memory_size = memory_size_entry.get()
    page_size = page_size_entry.get()
    algorithm = algorithm_combobox.get()

    processes = []
    for i, (arrival_time, burst_time) in enumerate(process_entries):
        processes.append({
            "Process ID": f"P{i + 1}",
            "Arrival Time": arrival_time.get(),
            "Burst Time": burst_time.get()
        })

    print(f"Memory Size: {memory_size}, Page Size: {page_size}, Algorithm: {algorithm}")
    print("Processes:")
    for process in processes:
        print(process)


# Memory Size Input
memory_size_label = tk.Label(root, text="Memory Size:")
memory_size_label.grid(row=0, column=0, padx=10, pady=10)
memory_size_entry = tk.Entry(root)
memory_size_entry.grid(row=0, column=1, padx=10, pady=10)

# Page Size Input
page_size_label = tk.Label(root, text="Page Size:")
page_size_label.grid(row=1, column=0, padx=10, pady=10)
page_size_entry = tk.Entry(root)
page_size_entry.grid(row=1, column=1, padx=10, pady=10)

# Replacement Algorithm Selection
algorithm_label = tk.Label(root, text="Replacement Algorithm:")
algorithm_label.grid(row=2, column=0, padx=10, pady=10)
algorithm_combobox = ttk.Combobox(root, values=["FIFO", "LRU"])
algorithm_combobox.grid(row=2, column=1, padx=10, pady=10)
algorithm_combobox.current(0)  # Set default to FIFO

# Process Input Table
process_label = tk.Label(root, text="Process Details:")
process_label.grid(row=4, column=0, padx=10, pady=10)

# Table Headers
tk.Label(root, text="Process ID").grid(row=5, column=0, padx=5, pady=5)
tk.Label(root, text="Arrival Time").grid(row=5, column=1, padx=5, pady=5)
tk.Label(root, text="Burst Time").grid(row=5, column=2, padx=5, pady=5)

# Process Entry Fields
process_entries = []
for i in range(3):  # Allow 3 processes for now
    process_id = tk.Label(root, text=f"P{i + 1}")
    process_id.grid(row=6 + i, column=0, padx=5, pady=5)

    arrival_time = tk.Entry(root, width=10)
    arrival_time.grid(row=6 + i, column=1, padx=5, pady=5)

    burst_time = tk.Entry(root, width=10)
    burst_time.grid(row=6 + i, column=2, padx=5, pady=5)

    process_entries.append((arrival_time, burst_time))

# Simulate Button
simulate_button = tk.Button(root, text="Simulate", command=simulate)
simulate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
