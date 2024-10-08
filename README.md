# Linode Invoices to CSV Exporter

This Python script fetches all invoices and their corresponding line items from the Linode API and outputs them into a CSV file. The script handles pagination to ensure all invoices and items are retrieved, even when there are a large number of entries. I hope this saves you time, and I hope Linode/Akamai add some billing reporting features to the web in the future!

## Features

- Fetches all invoices from the Linode API.
- Fetches all line items for each invoice.
- Outputs invoice line items to a CSV file.
- Handles pagination for both invoices and invoice items.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
   ```bash
      git clone https://github.com/yourusername/linode-invoice-exporter.git
         cd linode-invoice-exporter
	    ```

	    2. Install dependencies:
	       ```bash
	          pip install requests
		     ```

		     3. Replace the `<PLACE TOKEN HERE>` with your actual Linode API token in the script.
		        Create a token here: https://cloud.linode.com/profile/tokens

		     ## Usage

		     1. Run the script:

		        ```bash
			   python export_invoices.py
			      ```

			         This will generate a CSV file named `invoice_items.csv` in the same directory, containing all invoice line items fetched from the Linode API.

				 2. Customize the output file path or fields if needed by editing the `csv_file_path` and field mappings in the script.

				 ## CSV Output

				 The script generates a CSV file with the following columns:

				 - `invoice_id`: The ID of the invoice.
				 - `label`: The description or label of the invoice item.
				 - `amount`: The total amount for the line item.
				 - `quantity`: The quantity of the service or item.
				 - `from`: The start date for the service/item usage.
				 - `to`: The end date for the service/item usage.
				 - `unit_price`: The unit price for the service/item.

				 Example of the CSV file:

				 | invoice_id | label           | amount | quantity | from       | to         | unit_price |
				 |------------|-----------------|--------|----------|------------|------------|------------|
				 | 27532475   | NodeBalancer     | 3.71   | 247      | 2024-08-31 | 2024-09-11 | 0.015      |
				 | 27582253   | Storage Volume   | 2.57   | 100      | 2024-09-21 | 2024-09-30 | 0.015      |

				 ## Linode API

				 This script uses the Linode API v4 to retrieve invoices and their items. You can read more about the API [here](https://www.linode.com/docs/api/).

				 Make sure to generate a Linode API token and replace the `Bearer asd` placeholder in the script with your actual token.

				 ## License

				 This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

				 ## Contributing

				 Feel free to submit a pull request or open an issue if you have any improvements or suggestions!

				 ---

				 This `README.md` provides a concise overview of the project, including installation steps, usage instructions, and the expected output. Adjust the repository URL and any specific details according to your project setup.
