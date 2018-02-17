"""
Created on Sat Feb 17 20:05:22 2018

@author: Abdallah Elshamy
"""

###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time


#================================
# Part A: Transporting Space Cows
#================================
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict
     



def best_cow(cows, weight):
    """
    input: a dict of cows that needs to be transported, remaining weight
    returns: the best cow to be transported
    """ 
    best = ''
    maxi = 0
    for key in cows:
        if cows[key] <= weight:
            if cows[key]> maxi:
                maxi = cows[key]
                best = key
    return best


def trip(cows,limit= 10):
    """
    input: a dict of cows that needs to be transported and maximum wait for one trip
    returns: a list of cows that will be transfared in one trip
    """
    weight = 0
    trip = []
    while True:
        best = best_cow(cows, limit - weight)
        if len(best) == 0:
            return trip
        else:
            trip.append(best)
            weight += cows[best]
            del(cows[best])
    return trip
        

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    ans = []
    cows_copy = cows.copy()
    while len(cows_copy) != 0:
        newtrip = trip(cows_copy,limit)
        ans.append(newtrip)
        
    return ans


    

def isvalid(partition,cows,limit=10):
    """
    returns the weight of each trip
    """
    isvalid = True
    for element in partition:
        weight= 0 
        for item in element:
            weight += cows[item]
        if weight > limit:
            isvalid = False
    return isvalid


def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    ans = []
    max_len = 1000000
    cows_copy = cows.copy()
    for partition in get_partitions(cows_copy.keys()):
        if isvalid(partition,cows_copy,limit) == True and len(partition)<max_len:
            ans = partition[:]
            max_len =len(partition)
    return ans
            
        
        


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


