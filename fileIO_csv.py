################################################
#Working with CSV Dictwriter

from csv import writer, reader
with open ("jare.csv", "w") as file:
	file_writer = writer(file,delimiter="|",lineterminator="\n")
	file_writer.writerow(["Firstname", "Lastname", "Age"],)
	file_writer.writerow(["Idris", "Akintobi", 84])
with open ("jare.csv") as file:
	file_reader = reader(file)
	for line in file_reader:
		print(line)

################################################
#Working with CSV Dictwriter

from csv import DictWriter, reader
with open ("jare.csv", "w") as file:
	file_writer = DictWriter(file, fieldnames=["Firstname", "Lastname", "Age"],delimiter="|",lineterminator="\n")
	file_writer.writeheader()
	file_writer.writerow({"Firstname":"Idris","Lastname":"Akintobi","Age":84})
	file_writer.writerow({"Firstname":"Aminat","Lastname":"Adepoju","Age":78})
	file_writer.writerow(["Abdullah","Akintobi",78])
with open ("jare.csv") as file:
	file_reader = reader(file)
	for line in file_reader:
		print(line)