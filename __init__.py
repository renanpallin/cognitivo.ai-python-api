import csv

def populate_db():
	with open('./AppleStore - AppleStore.csv') as file:
		reader = csv.DictReader(file, delimiter=',')
		headers = reader.fieldnames
		# headers.pop(0) # remove blank space for line numbers

		for row in reader:
			# print(row.keys())
			if row['prime_genre'] != 'News':
				continue
			for header in headers:
				print(f"{header}:> {row[header]}")
			break

def main():
	populate_db()

if __name__ == "__main__":
	main()