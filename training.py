import pandas as pd
import numpy as np
from numpy import array
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__ == '__main__':
	# Reading CSV File

	df = pd.read_csv('data.csv')
	train, test = data_split(df, 0.2)

	X_train = train[['smoke', 'radonExpo', 'alchohol', 'bloodCough', 'breatheDiff', 'cancerProb']].to_numpy()
	X_test = test[['smoke', 'radonExpo', 'alchohol', 'bloodCough', 'breatheDiff', 'cancerProb']].to_numpy()

	Y_train = train[['cancerProb']].to_numpy().reshape(2400,)
	Y_test = test[['cancerProb']].to_numpy().reshape(599,)

	# Initializing + Training the model

	clf = LogisticRegression()
	clf.fit(X_train, Y_train)

	file = open('model.pkl', 'wb')
	pickle.dump(clf, file)
	file.close()