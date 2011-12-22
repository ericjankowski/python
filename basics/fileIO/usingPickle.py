import pickle

with open('stupid_data.pickle', 'wb') as save_stupid_data:
	pickle.dump(['stupid','is','as','stupid','does'], save_stupid_data)
	
with open('stupid_data.pickle', 'rb') as restore_stupid_data:
	stupid_data = pickle.load(restore_stupid_data)
	
print(stupid_data)