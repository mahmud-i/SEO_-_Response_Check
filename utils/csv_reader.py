# utils/csv_reader.py

import pandas as pd


def get_urls_from_csv(file_path):

    try:
         df = pd.read_csv(file_path)
         if 'url' in df.columns:
              urls = df['url'].tolist()
              return urls

         else:
              raise ValueError("The CSV file does not contain a 'url' column.")


    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return []
