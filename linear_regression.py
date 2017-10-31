
import numpy as np
import csv

# X = np.matrix([
# 		[100,10],
# 		[200,20],
# 		[300,30],
# 		[400,40]
# 	])

# y = np.matrix([
# 		[132],
# 		[309],
# 		[378],
# 		[460]
# 	])

# theta = np.matrix([
# 		[1],
# 		[5]
# 	])

# m = X.shape[0]
# h = X * theta
# alpha = .01


def cost_function(theta, X, y):
	m = X.shape[0]
	h = X * theta
	return np.sum(np.square((h - y))) / 2 * m

def linear_regression(theta, X, y, alpha):
	# reduce theta by alpha, and distance
	h = X * theta
	m = X.shape[0]
	hyp_update = (h - y).transpose() * X
	delta = alpha * 1/m * np.sum(hyp_update)
	return theta - delta

def gradient_decent(theta, X, y, alpha, iter):
	for i in range(iter):
		theta = linear_regression(theta, X, y, alpha)
		print "theta", theta
		print "cost", cost_function(theta, X, y)

	print
	print "End", theta
	print "end cost", cost_function(theta, X, y)


# gradient_decent(theta, X, y, alpha, )

def parse_data(file):
	# take in csv file then return matrix 
	arr = []
	with open(file, 'rb') as csvfile:
		file = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in file:
			# print row[0].split(',')
			arr.append(row[0].split(','))

	return np.matrix(arr)

# def main():
X = parse_data('x_data.txt')
y = parse_data('y_data.txt')
theta = np.matrix([
	[1],
	[5]
	])
alpha = .01
iterations = 100

	
	# cost_function(theta, X, y)




main()






