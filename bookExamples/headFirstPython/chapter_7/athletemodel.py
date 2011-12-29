import pickle
from athletelist import AthleteList

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		temp_list = data.strip().split(',')
		return(AthleteList(temp_list.pop(0),temp_list.pop(0),temp_list))
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

def put_to_store(files_list):
	all_athletes = {}
	for each_file in files_list:
		athlete = get_coach_data(each_file)
		all_athletes[athlete.name] = athlete
	try:
		with open('athletes.pickle', 'wb') as athlete_store:
			pickle.dump(all_athletes, athlete_store)
	except IOError as ioerror:
		print('File error (put_and_store): ' + str(ioerror))
	return(all_athletes)
	
def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle','rb') as athlete_store:
			all_athletes = pickle.load(athlete_store)
	except IOError as ioerror:
		print('File error (get_from_store): ' + str(ioerror))
	return(all_athletes)
	
the_files = ['sarah.txt','james.txt', 'mikey.txt', 'julie.txt']

data = put_to_store(the_files)
print(data)
print("\n")
for each_athlete in data:
	print(data[each_athlete].name + ' ' + data[each_athlete].dob)
print("\n")

data_copy = get_from_store()
for each_athlete in data_copy:
	print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)
