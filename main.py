import matplotlib.pyplot as plt
import math

def main():
	x1 = [0, 0, 2, 4, 6, 3, 0] # path x coordinates
	y1 = [0, 2, 4, 5, 3, 2, 0] # path y coordinates
	v1 = 3 # vehicle velocity
	s1 = 2 # vehicle search radius

	x2 = [0, 5, 3, 3, 1, 0] # path x coordinates
	y2 = [0, 0, 5, 3, 3, 0] # path y coordinates
	v2 = 2 # vehicle velocity
	s2 = 4 # vehicle search radius

	cost = calcCost(x1, y1, v1, x2, y2, v2)
	visualizePaths(x1, y1, v1, s1, x2, y2, v2, s2)


def visualizePaths(x1, y1, v1, s1, x2, y2, v2, s2):

	plt.plot(x1,y1)
	plt.plot(x2,y2)
	plt.show()

def calcSearchAreaConstraint():



	print('yes')

def calcCost(x1, y1, v1, x2, y2, v2):

	d1 = calcTotalDistance(x1, y1)
	t1 = d1 / v1
	print('Vehicle 1 Distance: ', d1)
	print('Vehicle 1 Time: ', t1)

	d2 = calcTotalDistance(x2, y2)
	t2 = d2 / v2
	print('Vehicle 2 Distance: ', d2)
	print('Vehicle 2 Time: ', t2)

	cost = min(t1,t2)
	print('Fleet Cost: ', cost)

	return cost

def calcTotalDistance(x1, y1):
	# Set initial distance to zero, and sum the distance of all segments
	distance = 0
	for i in range(len(x1)):
		# Skip the first element in each row
		if i is 0:
			continue
		# Add the distance of the next segment to the running variable
		distance = distance + calcDistance(x1[i-1], y1[i-1], x1[i], y1[i])
	# Return
	return distance

def calcDistance(x1, y1, x2, y2):
	# Distance between two points
	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == '__main__':
	main()


