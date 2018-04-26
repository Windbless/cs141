import math
import time
import argparse
import os
import sys
import time
import profile

# Command line arguments
parser=argparse.ArgumentParser(description='Calculate the nearest two points on a plan')
parser.add_argument('--algorithm',default='a',\
    help='Algorithm: Select the algorithm to run, default is all. (a)ll, (b)ruteforce only or (d)ivide and conquer only')
parser.add_argument('-v','--verbose',action='store_true')
parser.add_argument('--profile',action='store_true')
parser.add_argument('filename',metavar='<filename>',\
    help='Input dataset of points')
#help function to help to calcualte the distance between the two point
def sortthepoint(points):
    points1 = sorted(points,key = lambda xp:[xp[0],xp[1]])   
    return points1

def distance(p1,p2):
    return ( (p1[0] - p2[0]) * (p1[0]- p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]) ) ** 0.5 


def findCloseINmide(points,mid,minimum_distance):
    # get points between mid-d and mid+d

    midpointXvalue = points[mid][0] # get the x value 
    lowbone = midpointXvalue - minimum_distance
    upbone = midpointXvalue + minimum_distance
    lowplace = 0
    upplace = len(points) - 1 
    while points[lowplace][0] < lowbone:
        lowplace = lowplace + 1
    while points[upplace][0] > upbone:
        upplace = upplace - 1 

    points1 = points[lowplace:upplace]    

    points1 = sorted(points1,key = lambda y:[y[1],y[0]])

    #print(str(points1))
    point1F = (0,0)
    point2F = (0.0)
    for i in range (len(points1)):
        for j in range (i+1, min(i+7,len(points1))):
            if ((points1[j][1]-points1[i][1]) < minimum_distance):# in y we max is 7 and different is less d = min
                d = distance(points1[i],points1[j])
                if(d < minimum_distance):
                    minimum_distance = d
                    point1F = points1[i]
                    point2F = points1[j]

    return (minimum_distance,point1F,point2F)

#Divide and conquer version of the nearest neighbor algorithm
#Input: points := unsorted array of (x,y) coordinates
#Output: tuple of smallest distance and coordinates (distance,(x1,y1),(x2,y2))
def divideAndConquerNearestNeighbor(points):
    size = len(points)
    if size <= 3:
       return bruteForceNearestNeighbor(points)
    mid = size // 2
    # first thing is to sort the x 
    #points1 = sorted(points,key = lambda points: points[1]) 
    Lx = points[:mid]
    Rx = points[mid:]

    point1 = (-1,-1)
    point2 = (-1,-1)


    (min1,p1,q1) = divideAndConquerNearestNeighbor(Lx)
    (min2,p2,q2) = divideAndConquerNearestNeighbor(Rx)
    #print( "check both side " + str(min1) + " " + str(min2) + '\n')

    if(min1 < min2):
        mn = min1
        point1 = p1
        point2 = q1
    else:
        mn = min2
        point1 = p2
        point2 = q2
    #print("check the min in here " + str(mn) + '\n')
    #now we got the d = min(dl,dr) we had to make other function to check mid-point - d and mid-point + d 
    # we have already sort the x of points so just
    # this findcloseINmide() jusr input points and mid size and d
    (minnew,Lnew,Rnew) = findCloseINmide(points,mid,mn)
    minimum_distancef = 0

    #print("fianl check " + str(minnew) + " " + str(Lnew) + " " + str(Rnew) +'\n')
    if(minnew < mn):
        mn = minnew
        point1 = Lnew
        point2 = Rnew
    
    #print("fianl check 2 " + str(mn) + " " + str(point1) + " " + str(point2) +'\n')

    return mn,point1,point2

    # it is jusr bad way to find the distance because it had go through the whole list 
    #for i in range(len(points)): 
    #    for j in range(i + 1, len(points)):
    #        d =  distance(points[i][0],points[i][1],points[j][0],points[j][1])
    #        if minimum_distance > d
    #            point1, point2 = i, j
    #            minimum_distance = d 
    
    #print("Divide and Conquer algorithm is incomplete")
    
#end def divide_and_conquer(points):

#Brute force version of the nearest neighbor algorithm
#Input: points := unsorted array of (x,y) coordinates 
#   [(x,y),(x,y),...,(x,y)]
#Output: tuple of smallest distance and coordinates (distance,(x1,y1),(x2,y2))
def bruteForceNearestNeighbor(points):
    
    minimum_distance = distance(points[0],points[1])
    p1 = points[0]
    q1 = points[1]
    if len(points) <= 2:
        return(minimum_distance,p1,q1)


    point1 = (-1,-1)
    point2 = (-1,-1)


    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if(i != 0 and j != 1):
                dis = distance(points[j],points[i])
                if(dis < minimum_distance):
                    minimum_distance = dis
                    point1 = points[i]
                    point2 = points[j]

    #TODO: Complete this function
    #print("Brute force algorithm is incomplete")
    return (minimum_distance,point1,point2)
#end def brute_force_nearest_neighbor(points):

#Parse the input file
#Input: filename := string of the name of the test case
#Output: points := unsorted array of (x,y) coordinates
#   [(x,y),(x,y),...,(x,y)]
def parseFile(filename):
    point = []
    f = open(filename,'r') 
    lines = f.readlines()
    for line in lines:
        coordinate = line.split(' ')
        point.append((float(coordinate[0]),float(coordinate[1])))
    return point
#end def parse_file(filename):

#Main
#Input: filename  := string of the name of the test case
#       algorithm := flag for the algorithm to run, 'a': all 'b': brute force, 'd': d and c
def main(filename,algorithm):
    point = parseFile(filename)
    result = bruteForceResult = divideAndConquerResult = None
    points = sortthepoint(point);

    #print(str(points) + '\n')

    if algorithm == 'a' or algorithm == 'b':
        #TODO: Insert timing code here
        start = time.clock()
        bruteForceResult = bruteForceNearestNeighbor(points)
        stop = time.clock()
        print("Brute stop at " + str(stop - start))
        print("in main bruteForceResult min is " + str(bruteForceResult) + '\n')

    if algorithm == 'a' or algorithm == 'd':
        #TODO: Insert timing code here
        start = time.clock()
        divideAndConquerResult = divideAndConquerNearestNeighbor(points)
        stop = time.clock()
        print("divide_and_conquer stop at " + str(stop- start))
        print("In main the divide_and_conquer min is " + str(divideAndConquerResult))
    if algorithm == 'a': # Print whether the results are equal (check)
        if args.verbose:
            print('Brute force result: '+str(bruteForceResult))
            print('Divide and conquer result: '+str(divideAndConquerResult))
            print('Algorithms produce the same result? '+str(bruteForceResult == divideAndConquerResult))
        result = bruteForceResult if bruteForceResult == divideAndConquerResult else ('Error','N/A','N/A')
    else:  
        result = bruteForceResult if bruteForceResult is not None else divideAndConquerResult
    with open(os.path.splitext(filename)[0]+'_distance.txt','w') as f:
        f.write(str(result[1])+'\n')
        f.write(str(result[2])+'\n')
        f.write(str(result[0])+'\n')
#end def main(filename,algorithm):

if __name__ == '__main__':
    args=parser.parse_args()
    main(args.filename,args.algorithm)
#end if __name__ == '__main__':
