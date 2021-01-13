import pandas as pd
import sys

def download_data(*dataset):
	url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
	if len(dataset) > 0:
		if dataset[0] =='spokane_street':
			url = 'https://data.seattle.gov/api/views/upms-nr8w/rows.csv?accessType=DOWNLOAD'
	dataframe=pd.read_csv(url, parse_dates=["Date"], infer_datetime_format=True)
	return dataframe

if __name__ == "__main__":
	df = 0
	if len(sys.argv) >= 2:
		df = download_data(sys.argv[1])
	else:
		df = download_data()
	print(df.dtypes)
