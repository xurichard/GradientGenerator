def calculate(width, length, n, endConc):
	conc = []
	for i in range(len(endConc)):
		conc[i] = [0] * len(endConc)
	for alpha in map(lambda i:i*0.01, range(100)):
		newConc = []
		for i in range(len(endConc)):
			conc[i] = [0] * len(endConc)


memoized = {}
def enumerate_alpha(n):
	if n == 1:
		return map(lambda x: [x], [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
	enumerated = []
	if n-1 not in memoized:
		memoized[n-1] = enumerate_alpha(n-1)
	for i in map(lambda x: [x], [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]):
		enumerated += map(lambda x: i + x, memoized[n-1])
	return enumerated

# def check_alphas(intial1, initial2, endVals):
# 	alphas = enumerate_alpha(len(endVals)-1)
# 	for i in alphas:


def createflow(initial1, length1, initial2, length2, endVals, alphas, ratio):
	channels = []
	lengths = []
	for i in range(len(alphas)+2):
		channel = []
		length = []
		for j in range(len(alphas)+1):
			if i == 0:
				channel.append(initial1)
			elif j+1 == i:
				channel.append(initial2)
			else:
				channel.append(0)
			length.append(0)
		channels.append(channel)
		lengths.append(length)

	lengths[0][0] = length1
	lengths[1][0] = length2

	for i in range(1,len(alphas)+2):
		for j in range(i, len(alphas)+1):
			lengths[i][j] = (length1+length2)*ratio/(j+1)


	for i in range(1,len(alphas)+2):
		for j in range(i,len(alphas)+1):
			# print i,j
			# print "something", channels[i-1][j-1]
			# print "length", lengths[i-1][j-1]
			# print "alpha", alphas[j-1]
			# lengths[i][j] = (lengths[i][j-1]*alphas[j-1] + lengths[i-1][j-1]*(1-alphas[j-1]))
			channels[i][j] = (channels[i-1][j-1]*lengths[i-1][j-1]*alphas[j-1] + channels[i][j-1]*lengths[i][j-1]*(1-alphas[j-1]))/lengths[i][j]
	# print("channels")
	# printMatrix(channels)
	# print("lengths")
	# printMatrix(lengths)
	
	return (channels,lengths)


def printMatrix(n):
	for i in n:
		print i

def checkflow(m, endVals, tolerance):
	for i in range(len(m)):
		if (endVals[i]/ m[i][len(m[i])-1] )%1 > tolerance:
			return False
	return True


def checkflow2(m, endVals, tolerance):
	temp = 0
	for i in range(len(m)):
		if m[i][len(m[i])-1] <= temp:
			return False
		if m[i][len(m[i])-1] > 100 or m[i][len(m[i])-1] <= 0:
			return False
		temp = m[i][len(m[i])-1]
	return True

def printLastCol(m):
	print "\n"
	for i in range(len(m)):
		print m[i][len(m[i])-1]


# def createlengths(initial1, length1, initial2, length2, alphas):

# 	lengths = []
# 	for i in range(len(alphas)+2):
# 		length = []
# 		for j in range(len(alphas)+1):
# 			length.append(0)
# 		lengths.append(length)
# 	lengths[0][0] = length1
# 	lengths[1][0] = length2

# 	for j in range(len(alphas)+1):
# 		for i in range(len(alphas)+2):

		


if __name__ == '__main__':
	width = 3000
	length = 30000
	n = 3
	endConc = [1,2,3]

	alphas = [0.2,0.5,0.6]
	ratio = 0.8
	initial1 = 0.0001
	initial2 = 100
	length1=375
	length2=375
	endVals = []
	
	createflow(initial1, length1, initial2, length2, endVals, alphas, ratio)

	tolerance = 0.25

	for i in enumerate_alpha(2):
		flow, lengths = createflow(initial1, length1, initial2, length2, endVals, i, ratio)
		# printMatrix(flow)
		# print "\n"
		# # printLastCol(flow)

		if checkflow2(flow, endVals, tolerance):
			print "alphas",  i
			print "flow"
			printMatrix(flow)
			print "lengths"
			printMatrix(lengths)
			print "\n"



