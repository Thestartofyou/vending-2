import random
import pandas as pd
from datetime import datetime

# Simulate Vending Machine Data
machines = [
    {'machine_id': 1, 'location': 'Gym', 'inventory': 50, 'sales_today': random.randint(10, 50)},
    {'machine_id': 2, 'location': 'School', 'inventory': 50, 'sales_today': random.randint(10, 50)},
    {'machine_id': 3, 'location': 'Mall', 'inventory': 50, 'sales_today': random.randint(10, 50)},
    # Add more machines as needed
]

# Function to track machine performance
def track_sales(machines):
    print("Machine Performance Summary:")
    for machine in machines:
        print(f"Machine {machine['machine_id']} at {machine['location']} sold {machine['sales_today']} items today.")
    print()

# Function to check inventory and flag machines for restocking
def check_inventory(machines, threshold=20):
    machines_needing_restock = []
    print("Checking inventory levels...")
    for machine in machines:
        machine['inventory'] -= machine['sales_today']
        if machine['inventory'] < threshold:
            machines_needing_restock.append(machine)
            print(f"Machine {machine['machine_id']} at {machine['location']} needs restocking! Current inventory: {machine['inventory']}")
    print()
    return machines_needing_restock

# Function to optimize restocking route based on low inventory
def optimize_restock_route(machines_needing_restock):
    if machines_needing_restock:
        print("Suggested Restocking Route (based on location):")
        for machine in machines_needing_restock:
            print(f"Restock Machine {machine['machine_id']} at {machine['location']} with {machine['inventory']} items left.")
    else:
        print("No machines need restocking.")
    print()

# Function to generate performance report as CSV for future reference
def generate_report(machines):
    df = pd.DataFrame(machines)
    df['date'] = datetime.now().strftime('%Y-%m-%d')
    df.to_csv('vending_machine_report.csv', index=False)
    print("Report generated: vending_machine_report.csv\n")

# Simulate the expansion plan over time
def expand_machines(current_machines, new_machine_count=50):
    next_id = len(current_machines) + 1
    for i in range(new_machine_count):
        new_machine = {'machine_id': next_id, 'location': f"Location_{next_id}", 'inventory': 50, 'sales_today': 0}
        current_machines.append(new_machine)
        next_id += 1
    print(f"Successfully added {new_machine_count} new machines.")
    return current_machines

# Main function to run the operations
def run_vending_machine_operations():
    # Track sales
    track_sales(machines)
    
    # Check inventory and flag machines for restocking
    machines_needing_restock = check_inventory(machines)
    
    # Optimize restocking route
    optimize_restock_route(machines_needing_restock)
    
    # Generate a performance report
    generate_report(machines)

# Expand the number of machines (simulates expansion over 18 months)
machines = expand_machines(machines)

# Run the vending machine operations
run_vending_machine_operations()
