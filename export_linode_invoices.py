import requests
import csv

# Define the base URLs
invoices_url = "https://api.linode.com/v4/account/invoices?page={page}&page_size=500"
invoice_items_url = "https://api.linode.com/v4/account/invoices/{invoice_id}/items?page={page}&page_size=100"

# Define the headers (replace 'Bearer redacted' with your actual token)
headers = {
    "accept": "application/json",
    "authorization": "Bearer <PLACE TOKEN HERE>"  # replace with your token
}

# Function to fetch all invoices
def fetch_all_invoices():
    invoices = []
    page = 1
    while True:
        response = requests.get(invoices_url.format(page=page), headers=headers)
        data = response.json()
        
        # Append the invoices to our list
        invoices.extend(data.get("data", []))
        
        # Break the loop if we have fetched all pages
        if not data.get("pages") or page >= data["pages"]:
            break
        page += 1
    return invoices

# Function to fetch all items of a particular invoice
def fetch_invoice_items(invoice_id):
    items = []
    page = 1
    while True:
        response = requests.get(invoice_items_url.format(invoice_id=invoice_id, page=page), headers=headers)
        data = response.json()
        
        # Append the items to our list
        items.extend(data.get("data", []))
        
        # Break the loop if we have fetched all pages
        if not data.get("pages") or page >= data["pages"]:
            break
        page += 1
    return items

# Fetch all invoices
invoices = fetch_all_invoices()

# Define the CSV file path
csv_file_path = "invoice_items.csv"

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header for invoice items
    writer.writerow(["invoice_id", "label", "amount", "quantity", "from", "to", "unit_price"])

    # Iterate over each invoice and fetch its items
    for invoice in invoices:
        invoice_id = invoice.get("id")
        invoice_items = fetch_invoice_items(invoice_id)
        
        # Write each item of the invoice to the CSV file
        for item in invoice_items:
            writer.writerow([
                invoice_id,
                item.get("label"),
                item.get("amount"),
                item.get("quantity"),
                item.get("from"),
                item.get("to"),
                item.get("unit_price")
            ])

print(f"CSV file created at {csv_file_path}")


