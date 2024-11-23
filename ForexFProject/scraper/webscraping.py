import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

def webscraping(start_date, end_date, banks_list):
    """
    Scrape currency exchange rates from specified banks within a date range.

    Parameters:
    - start_date (datetime): The start date for scraping.
    - end_date (datetime): The end date for scraping.
    - banks_list (list): List of bank identifiers as used in the URL.

    Returns:
    - all_data (DataFrame): A pandas DataFrame containing the scraped data.
    """

    # Function to generate a list of dates from start_date to end_date
    def generate_dates(start_date, end_date):
        dates = []
        delta = timedelta(days=1)
        current_date = start_date
        while current_date <= end_date:
            dates.append(current_date.strftime('%d.%m.%Y'))
            current_date += delta
        return dates

    # Function to safely convert text to float
    def safe_float(value):
        try:
            return float(value.replace(',', '.').strip())
        except (ValueError, TypeError, AttributeError):
            return None

    # Function to parse a table row
    def parse_row(row):
        columns = row.find_all('td')
        data_length = len(columns)

        # Check if columns are sufficient
        if data_length < 8:
            print("Insufficient number of columns:", data_length)
            return None

        # Common data extraction
        currency_name = columns[0].get_text(strip=True)
        currency_code = columns[2].get_text(strip=True)
        unit_text = columns[3].get_text(strip=True)
        unit = int(unit_text.replace('&nbsp;', '').strip())

        buy_rate = safe_float(columns[5].get_text(strip=True))
        sell_rate = safe_float(columns[6].get_text(strip=True))
        mid_rate = safe_float(columns[7].get_text(strip=True))

        # Initialize cash rates
        cash_buy_rate = None
        cash_sell_rate = None
        cash_mid_rate = None

        # Determine if cash rates are included
        if data_length >= 13:
            # Check if cash rates are present
            if columns[9].get_text(strip=True):
                cash_buy_rate = safe_float(columns[9].get_text(strip=True))
            if columns[10].get_text(strip=True):
                cash_sell_rate = safe_float(columns[10].get_text(strip=True))
            if columns[11].get_text(strip=True):
                cash_mid_rate = safe_float(columns[11].get_text(strip=True))
        elif data_length >= 9:
            # Cash rates not included
            pass
        else:
            # Handle unexpected number of columns
            print("Unexpected number of columns:", data_length)
            return None

        # Compile the data into a list
        data = [
            currency_name,  # 0
            currency_code,  # 1
            unit,           # 2
            buy_rate,       # 3
            sell_rate,      # 4
            mid_rate,       # 5
            cash_buy_rate,  # 6
            cash_sell_rate, # 7
            cash_mid_rate,  # 8
        ]

        return data

    # Generate the list of dates
    date_list = generate_dates(start_date, end_date)

    # Initialize a list to collect DataFrames
    data_frames = []

    # Iterate over banks and dates
    for bank in banks_list:
        for date_str in date_list:
            # Create the URL
            url = f"https://www.kurzy.cz/kurzy-men/kurzovni-listek/nr/{bank}/D-{date_str}/"

            # Send a GET request
            try:
                response = requests.get(url, timeout=10)
                response.encoding = "windows-1250"  # Set the correct encoding
            except requests.exceptions.RequestException as e:
                print(f"Request failed for {bank} on {date_str}: {e}")
                continue

            # Check if the page exists
            if response.status_code != 200:
                print(f"Page for {bank} on {date_str} not found.")
                continue

            # Parse the HTML
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the table by class
            table = soup.find("table", {"class": "pd pdw rca rowcl"})
            if not table:
                print(f"Table for {bank} on {date_str} not found.")
                continue

            # Extract all table rows
            rows = table.find_all("tr")[2:]  # Skip headers

            # Skip if the table is empty
            if not rows:
                print(f"Table for {bank} on {date_str} is empty.")
                continue

            # Extract data
            data_rows = []
            for row in rows:
                data = parse_row(row)
                if data:
                    data_rows.append(data)

            # Skip if no data was extracted
            if not data_rows:
                print(f"No data for {bank} on {date_str}.")
                continue

            # Define column names
            columns = [
                'currency', 'ISO', 'amount', 'dev_buy', 'dev_sell', 'dev_middle',
                'vault_buy', 'vault_sell', 'vault_middle'
            ]

            # Create DataFrame
            df = pd.DataFrame(data_rows, columns=columns)

            # Add bank and date columns
            df['bank'] = bank
            df['date'] = date_str

            # Check if df is empty or contains only NaN values
            if df.empty or df.isnull().all().all():
                print(f"No valid data for {bank} on {date_str}. Skipping.")
                continue

            # Append df to the list of DataFrames
            data_frames.append(df)

            print(f"Processed: {bank} - {date_str}")

    # Concatenate all DataFrames if the list is not empty
    if data_frames:
        all_data = pd.concat(data_frames, ignore_index=True)
    else:
        all_data = pd.DataFrame()  # Create an empty DataFrame if no data was collected

    return all_data

# Example usage:

if __name__ == "__main__":
    # Set the start and end dates
    start_date = datetime(2024, 11, 19)  # Start date
    end_date = datetime(2024, 11, 19)    # End date

    # List of banks
    banks_list = [
        'max-banka', 'fio-banka', 'csob', 'ceska-sporitelna', 'air-bank',
        'exchange-vip', 'exchange', 'akcenta',
        'unicredit-bank', 'trinity-bank', 'raiffeisenbank', 'postovni-sporitelna',
        'oberbank-ag', 'moneta-money-bank'
    ]

    # Call the webscraping function
    data = webscraping(start_date, end_date, banks_list)
