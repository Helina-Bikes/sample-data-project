import csv
data=[

     {"name":"Helina","age":24,"city":"Addis Ababa"},
     {"name":"Abebe","age":30,"city":"Bahir Dar"},
     {"name":"aster","age":28,"city":"Mekelle"} 
]
filename="sample.csv"
with open(filename,'w',newline='', encoding="utf-8") as file:
    writer=csv.DictWriter(file,fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
print(f"Data has been written to {filename}")
print(f"number of records written: {len(data)}")
print("sample data generation completed successfully")
print("some changes form the remote repository")
