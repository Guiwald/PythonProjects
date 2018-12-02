# Importing library random
import random
import csv

# for x in range(10):
#	print(random.randint(1,101))


nbphonenb = int(input("How many Irish phone number do you want to generate?"))
phonenumbers = []
for x in range(nbphonenb):
	num = []
	for y in range(7):
		num.append(random.randint(0,9))
		# print(num[y])
	phonenumbers.append(f"08 {num[0]}{num[1]}{num[2]} {num[3]}{num[4]}{num[5]}{num[5]}")
	print(phonenumbers[x])
	with open('phones.csv', mode='a') as csv_file:
        	writer = csv.writer(csv_file, delimiter=',')
        	writer.writerow([phonenumbers[x]])
