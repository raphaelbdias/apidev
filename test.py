import pandas as pd
import sqlite3

# Define the URL of the CSV file
url = 'https://storage.googleapis.com/kagglesdsdata/datasets/4545306/7769743/Planilha%20sem%20ttulo%20-%20birth-death-china-great-leap-forward-famine%20new.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240521%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240521T181553Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=7dd469640e6bfdd3c37c620003cf9b90855ec29fa2a7e7140bb9b3140688a74eba56b85a03fa420f63be0ccfac1e0c4f809af0b20808c1beb91a29039a41687c1b8c0403b836c1572f472be6f4bf55ec35fe65a29c4b65940d8571177f93d3e6e5cdec61298514d4e8db2a7b0aa5e67c09f6bc58ce1ea592e9b06f1fdc778328c39d987623b9ffcecd624079d3a9e8e8eeee97ebbadd6a3406fbb652446d889174ef68d12e18b17949d2a178ff2f96da2bddc2fe0a33da6d13b3c944728745e9ee7aec40535c827c8203339fd5900edd6a43c043c8bfe7eb98fe3cee521be9d242595932a60675bcc2a11f3983a6a4c57eaa3133266325c1302d11c0e015e20c'

# Load the CSV file into a DataFrame
df = pd.read_csv(url)

# Create a connection to a new SQLite database (or connect to an existing one)
conn = sqlite3.connect('birth_death_china_famine.db')

# # Save the DataFrame to the SQLite database
# df.to_sql('birth_death_china_famine', conn, if_exists='replace', index=False)

# # Confirm the table has been created by printing the names of the tables in the database
# tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
# print(tables)

# # Close the connection
# conn.close()
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

conn.row_factory = dict_factory

for row in conn.execute(f"SELECT * FROM birth_death_china_famine WHERE year=1957;"):
    print(row)