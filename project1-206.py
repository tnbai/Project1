import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


# 1 PASS
def getData(file):
# Input: file name
	data=open(file,'r')
	master_lst=[]
	read_data=data.readlines()
	header=read_data[0]
	lines=read_data[1:]
	for line in lines:
		d=dict()
		info=line.split(',')
		first_name=info[0]
		last_name=info[1]
		email=info[2]
		year=info[3]
		dob=info[4][:-1]
		d['First']=first_name
		d['Last']=last_name
		d['Email']=email
		d['Class']=year
		d['DOB']=dob
		master_lst.append(d)
	data.close()
	return master_lst
# Output: return a list of dictionary objects where the keys are from the
# first row in the data and the values are each of the other rows


# 2 PASS
def mySort(data,col):
# Sort based on key/column
# Input: list of dictionaries and col (key) to sort on
	lst=sorted(data,key=lambda k: k[col])
	first=lst[0]['First']
	last=lst[0]['Last']
	name=first+' '+last
	return name
# Output: return the first item in the sorted list as a string of just: firstName lastName


# 3 PASS
def classSizes(data):
# Create a histogram
# Input: list of dictionaries
	fresh=0
	soph=0
	junior=0
	senior=0
	for d in data:
		if d['Class']=='Freshman':
			fresh+=1
		elif d['Class']=='Sophomore':
			soph+=1
		elif d['Class']=='Junior':
			junior+=1
		elif d['Class']=='Senior':
			senior+=1
	tup=[('Freshman',fresh),('Sophomore',soph),('Junior',junior),('Senior',senior)]
	sorted_tup=sorted(tup,key=lambda c: c[1],reverse=True)
	return sorted_tup
# Output: return a list of tuples sorted by the number of students in that
# class in descending order


# 4 PASS
def findMonth(a):
# Find the most common birth month
# Input: list of dictionaries
	num=0
	mo=''
	d=dict()
	for dictionary in a:
		birthdate=dictionary['DOB'].split('/')
		if birthdate[0] not in d:
			d[birthdate[0]]=1
		else: # if month is in dictionary
			d[birthdate[0]]+=1
	for month in d: # iterating through dict keys
		if d[month]>num:
			num=d[month]
			mo=month
	return int(mo)
# Output: return the month (1-12) that had the most births in the data


# 5 PASS
def mySortPrint(a,col,fileName):
# Similar to mySort, but instead of returning single student, the sorted
# data is saved to a csv file
# Input: list of dictionaries, col (key) to sort by and output file name
	out=open(fileName,'w')
	lst_dicts=sorted(a,key=lambda i: i[col])
	big_lst=[]
	csv_lst=[]
	for d in lst_dicts:
		first=d['First']
		last=d['Last']
		email=d['Email']
		small_lst=[first,last,email]
		big_lst.append(small_lst)
	for lst in big_lst:
		csv_lst.append(','.join(lst))
	out.write('\n'.join(csv_lst))
	out.close()
# Output: No return value, but the file is written


# 6 - EXTRA CREDIT
def findAge(a):
# Find the average age (rounded) of the students
# Input: list of dictionaries
	today_date=date.today()
	ages=[]
	for student in a:
		dob=student['DOB'].split('/')
		month=int(dob[0])
		day=int(dob[1])
		year=int(dob[2])
		born=date(year,month,day)
		age=today_date.year-born.year-((today_date.month,today_date.day)<(born.month,born.day))
		ages.append(age)
	avg=round(sum(ages)/len(ages))
	return avg
# Output: Return the average age of the students and round that age to the nearest
# integer. Work with the DOB and the current date to find the current age in years.



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
