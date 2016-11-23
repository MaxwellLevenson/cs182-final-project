import util, generate, random
import searchAgents as search
import time
import sys

n = 100

graph = generate.SocialGraph()
graph.train(100000)

start = time.time()
avg1 = 0.0
n1 = n

for i in xrange(n):
	# separation = len(search.BFS(random.choice(graph.students),random.choice(graph.students),graph))
	separation = len(search.BFS(graph.students[i],graph.students[i+1],graph))
	if separation != 0:
		avg1 += separation
	else:
		n1 -= 1

	progress = '|' + '.' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("BFS iter " + str(i+1) + '   ' + progress + "\r")
	sys.stdout.flush()
avg1 = avg1 / n1
end = time.time()
diff1 = end - start

print ""

start = time.time()
avg2 = 0.0
n2 = n
for i in xrange(n):
	separation = len(search.aStar(graph.students[i],graph.students[i+1],graph, ))
	if separation != 0:
		avg2 += separation
	else:
		n2 -= 1
	progress = '|' + '.' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("aStar iter " + str(i+1) + ' ' + progress + "\r")
	sys.stdout.flush()
avg2 = avg2 / n2
end = time.time()
diff2 = end - start

print ""

print "BFS -- Time:", diff1, " Avg:", avg1, " Iterations:", n
print "aStar -- Time:", diff2, " Avg:", avg2, " Iterations:", n