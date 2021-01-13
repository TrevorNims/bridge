import pandas as pd
import sys

def download_data(*dataset):
	url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
	if (dataset[0]=='spokane_street'):
		url = 'https://data.seattle.gov/api/views/upms-nr8w/rows.csv?accessType=DOWNLOAD'
	dataframe=pd.read_csv(url)
	return dataframe

if __name__ == "__main__":
	if len(sys.argv) >= 2:
		print(download_data(sys.argv[1]))
	else:
		print(download_data())
