import math
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
def distance(p1,p2):
    return ( (p1.x - p2.x) * (p1.x- p2.x) + (p1.y - p2.y) * (p1.y - p2.y) ) ** 0.5 

#Divide and conquer version of the nearest neighbor algorithm
#Input: points := unsorted array of (x,y) coordinates
#Output: tuple of smallest distance and coordinates (distance,(x1,y1),(x2,y2))
def divideAndConquerNearestNeighbor(points):
    size = len(points)
    if size <= 7
        return bruteForceNearestNeighbor(points)
    mid = ln_ax / 2;
    # first thing is to sort the x 
    points1 = sorted(points,key = lambda points: points[1]) 
    Lx = points1[:mid]
    Rx = points1[mid:]
    midpoint = points1[mid][0]
    
    for i in range(len(points1)){
        if
    }
    
    
    
    
    minimum_distance = 0;
    point1 = (-1,-1)
    point2 = (-1,-1)
    #TODO: Complete this function
    minimum_distance = distance(point1,point2) # initialize shorestDistance
    
    # it is jusr bad way to find the distance because it had go through the whole list 
    #for i in range(len(points)): 
    #    for j in range(i + 1, len(points)):
    #        d =  distance(points[i][0],points[i][1],points[j][0],points[j][1])
    #        if minimum_distance > d
    #            point1, point2 = i, j
    #            minimum_distance = d 
    
    print("Divide and Conquer algorithm is incomplete")
    return (minimum_distance,point1,point2)
#end def divide_and_conquer(points):

#Brute force version of the nearest neighbor algorithm
#Input: points := unsorted array of (x,y) coordinates 
#   [(x,y),(x,y),...,(x,y)]
#Output: tuple of smallest distance and coordinates (distance,(x1,y1),(x2,y2))
def bruteForceNearestNeighbor(points):
    minimum_distance = 0;
    point1 = (-1,-1)
    point2 = (-1,-1)
    #TODO: Complete this function
    print("Brute force algorithm is incomplete")
    return (minimum_distance,point1,point2)
#end def brute_force_nearest_neighbor(points):

#Parse the input file
#Input: filename := string of the name of the test case
#Output: points := unsorted array of (x,y) coordinates
#   [(x,y),(x,y),...,(x,y)]
def parseFile(filename):
    points = []
    f = open(filename,'r') 
    lines = f.readlines()
    for line in lines:
        coordinate = line.split(' ')
        points.append((float(coordinate[0]),float(coordinate[1])))
    return points
#end def parse_file(filename):

#Main
#Input: filename  := string of the name of the test case
#       algorithm := flag for the algorithm to run, 'a': all 'b': brute force, 'd': d and c
def main(filename,algorithm):
    points = parseFile(filename)
    result = bruteForceResult = divideAndConquerResult = None
    if algorithm == 'a' or algorithm == 'b':
        #TODO: Insert timing code here
        bruteForceResult = bruteForceNearestNeighbor(points)
    if algorithm == 'a' or algorithm == 'd':
        #TODO: Insert timing code here
        divideAndConquerResult = divideAndConquerNearestNeighbor(points)
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
