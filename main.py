import hashlib
import time
from datetime import datetime, timedelta

# Blockchain structure
blockchain = []

# Simulated list of drugs and their batch numbers
drugs_db = [
    {"drug_name": "DrugA", "batch_number": "BATCH001"},
    {"drug_name": "DrugB", "batch_number": "BATCH002"},
    {"drug_name": "DrugC", "batch_number": "BATCH003"},
]

# Sample carriers for transporting drugs
carriers = ["Carrier1", "Carrier2", "Carrier3"]

# Initialize the first block (genesis block)
def create_genesis_block():
    return {
        'index': 0,
        'timestamp': str(datetime.now()),
        'transactions': [],
        'previous_hash': '0',
        'hash': '',
    }

# Hashing the block
def hash_block(block):
    block_string = str(block).encode()
    return hashlib.sha256(block_string).hexdigest()

# Adding new block to the blockchain
def add_block(transactions):
    previous_block = blockchain[-1]
    new_block = {
        'index': len(blockchain),
        'timestamp': str(datetime.now()),
        'transactions': transactions,
        'previous_hash': previous_block['hash'],
        'hash': '',
    }
    new_block['hash'] = hash_block(new_block)
    blockchain.append(new_block)

# Function to simulate drug manufacturing
def manufacture_drug():
    print("\n-- Manufacturing Drug --")
    for i, drug in enumerate(drugs_db, start=1):
        print(f"{i}. {drug['drug_name']} (Batch: {drug['batch_number']})")
    choice = int(input("Select the drug to manufacture: "))
    selected_drug = drugs_db[choice - 1]
    
    transaction = {
        'type': 'Manufacture',
        'drug_name': selected_drug['drug_name'],
        'batch_number': selected_drug['batch_number'],
        'manufacturing_date': str(datetime.now().date()),
    }
    add_block([transaction])
    print(f"Manufactured {selected_drug['drug_name']} with batch number {selected_drug['batch_number']}.")

# Function to simulate drug packaging
def package_drug():
    print("\n-- Packaging Drug --")
    for i, drug in enumerate(drugs_db, start=1):
        print(f"{i}. {drug['drug_name']} (Batch: {drug['batch_number']})")
    choice = int(input("Select the drug to package: "))
    selected_drug = drugs_db[choice - 1]
    
    package_id = input("Enter package ID: ")
    transaction = {
        'type': 'Package',
        'drug_name': selected_drug['drug_name'],
        'batch_number': selected_drug['batch_number'],
        'package_id': package_id,
        'packaging_date': str(datetime.now().date()),
    }
    add_block([transaction])
    print(f"Packaged {selected_drug['drug_name']} (Batch: {selected_drug['batch_number']}) with package ID {package_id}.")

# Function to simulate drug shipping
def ship_drug():
    print("\n-- Shipping Drug --")
    for i, drug in enumerate(drugs_db, start=1):
        print(f"{i}. {drug['drug_name']} (Batch: {drug['batch_number']})")
    choice = int(input("Select the drug to ship: "))
    selected_drug = drugs_db[choice - 1]
    
    package_id = input("Enter package ID: ")
    for i, carrier in enumerate(carriers, start=1):
        print(f"{i}. {carrier}")
    carrier_choice = int(input("Select the carrier: "))
    selected_carrier = carriers[carrier_choice - 1]
    
    transaction = {
        'type': 'Ship',
        'drug_name': selected_drug['drug_name'],
        'batch_number': selected_drug['batch_number'],
        'package_id': package_id,
        'carrier_name': selected_carrier,
        'departure_date': str(datetime.now().date()),
    }
    add_block([transaction])
    print(f"Shipped {selected_drug['drug_name']} (Batch: {selected_drug['batch_number']}) with package ID {package_id} via {selected_carrier}.")

# Function to simulate drug receiving
def receive_drug():
    print("\n-- Receiving Drug --")
    for i, drug in enumerate(drugs_db, start=1):
        print(f"{i}. {drug['drug_name']} (Batch: {drug['batch_number']})")
    choice = int(input("Select the drug to receive: "))
    selected_drug = drugs_db[choice - 1]
    
    package_id = input("Enter package ID: ")
    receiver_name = input("Enter receiver name: ")
    
    transaction = {
        'type': 'Receive',
        'drug_name': selected_drug['drug_name'],
        'batch_number': selected_drug['batch_number'],
        'package_id': package_id,
        'receiver_name': receiver_name,
        'received_date': str(datetime.now().date()),
    }
    add_block([transaction])
    print(f"Received {selected_drug['drug_name']} (Batch: {selected_drug['batch_number']}) with package ID {package_id} by {receiver_name}.")

# Function to simulate drug dispensing
def dispense_drug():
    print("\n-- Dispensing Drug --")
    for i, drug in enumerate(drugs_db, start=1):
        print(f"{i}. {drug['drug_name']} (Batch: {drug['batch_number']})")
    choice = int(input("Select the drug to dispense: "))
    selected_drug = drugs_db[choice - 1]
    
    package_id = input("Enter package ID: ")
    patient_name = input("Enter patient name: ")
    
    transaction = {
        'type': 'Dispense',
        'drug_name': selected_drug['drug_name'],
        'batch_number': selected_drug['batch_number'],
        'package_id': package_id,
        'patient_name': patient_name,
        'dispense_date': str(datetime.now().date()),
    }
    add_block([transaction])
    print(f"Dispensed {selected_drug['drug_name']} (Batch: {selected_drug['batch_number']}) with package ID {package_id} to patient {patient_name}.")

# Function to audit the supply chain (view the blockchain)
def audit_supply_chain():
    print("\n-- Audit Supply Chain --")
    
    if not blockchain:
        print("No transactions to display.")
        return

    # Define the table headers
    headers = ["Index", "Timestamp", "Transaction Type", "Drug Name", "Batch Number", 
               "Package ID", "Carrier Name", "Receiver/Patient", "Date", "Previous Hash", "Hash"]

    # Print the table headers
    print(f"{headers[0]:<6} | {headers[1]:<22} | {headers[2]:<16} | {headers[3]:<10} | {headers[4]:<15} | "
          f"{headers[5]:<12} | {headers[6]:<12} | {headers[7]:<15} | {headers[8]:<10} | {headers[9]:<65} | {headers[10]:<65}")

    print("-" * 230)

    # Print each block's transactions
    for block in blockchain:
        transactions = block['transactions']
        index = block['index']
        timestamp = block['timestamp']
        previous_hash = block['previous_hash']
        current_hash = block['hash']

        # Iterate through each transaction in the block
        for transaction in transactions:
            transaction_type = transaction['type']
            drug_name = transaction.get('drug_name', '')
            batch_number = transaction.get('batch_number', '')
            package_id = transaction.get('package_id', '')
            carrier_name = transaction.get('carrier_name', '')
            receiver_or_patient = transaction.get('receiver_name', transaction.get('patient_name', ''))
            date = transaction.get('manufacturing_date', transaction.get('packaging_date', 
                     transaction.get('departure_date', transaction.get('received_date', transaction.get('dispense_date', '')))))

            # Print the row in the table
            print(f"{index:<6} | {timestamp:<22} | {transaction_type:<16} | {drug_name:<10} | {batch_number:<15} | "
                  f"{package_id:<12} | {carrier_name:<12} | {receiver_or_patient:<15} | {date:<10} | {previous_hash:<65} | {current_hash:<65}")
    
    print("-" * 230)

# Initialize blockchain with the genesis block
def initialize_blockchain():
    genesis_block = create_genesis_block()
    genesis_block['hash'] = hash_block(genesis_block)
    blockchain.append(genesis_block)

# Main function to simulate the pharma supply chain system
def pharma_supply_chain_system():
    initialize_blockchain()
    while True:
        print("\n-- Pharma Supply Chain System --")
        print("1. Manufacture Drug")
        print("2. Package Drug")
        print("3. Ship Drug")
        print("4. Receive Drug")
        print("5. Dispense Drug")
        print("6. Audit Supply Chain")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            manufacture_drug()
        elif choice == '2':
            package_drug()
        elif choice == '3':
            ship_drug()
        elif choice == '4':
            receive_drug()
        elif choice == '5':
            dispense_drug()
        elif choice == '6':
            audit_supply_chain()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
pharma_supply_chain_system()
