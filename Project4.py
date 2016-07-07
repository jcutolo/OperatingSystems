import sys

import pdb

LEFT = "LEFT"
RIGHT = "RIGHT"

LOWER_CYLINDER = 0
UPPER_CYLINDER = 4999

'''
SSTF algorithm
'''
def SSTF(requests, initialPosition):
    localRequests = list(requests)
    position = initialPosition
    movement = 0
    
    
    while localRequests:
        closest = abs(position - localRequests[0])
        index = 0
        for x in range(1, len(localRequests)):
            if abs(position - localRequests[x]) < closest:
                closest = abs(position - localRequests[x])
                index = x
    
        movement = movement + abs(position - localRequests[index])
        position = localRequests[index]
        print ("Servicing" + str(position))
        localRequests.remove(position)
    
    return movement

'''        
FCFS algorithm, fully implemented as example
'''
def FCFS(requests, initialPosition):
    position = initialPosition
    movement = 0
   
    for x in range(len(requests)):
        movement += abs(position - requests[x])
        position = requests[x]
        print ("Servicing " + str(position))
        
    return movement

''' 
SCAN algorithm, fully implemented as example
'''
def SCAN(requests, initialPosition):
    direction = RIGHT
    localRequests = list(requests)
    position = initialPosition
    movement = 0

    while localRequests:
        #pdb.set_trace() 
        if position in localRequests:
            print ("Servicing " + str(position))
            localRequests.remove(position)

            if not localRequests:
                break

        if direction == LEFT and position > LOWER_CYLINDER:
            position -= 1
        if direction == RIGHT and position < UPPER_CYLINDER:
            position += 1

        movement += 1

        if position == 0:
            direction = RIGHT
        if position == UPPER_CYLINDER:
            direction = LEFT

    return movement


'''
C-SCAN algorithm
'''
def C_SCAN(requests, initialPosition):
    localRequests = list(requests)
    position = initialPosition
    movement = 0
    
    while localRequests:
        if position in localRequests:
            print ("Servicing " + str(position))
            localRequests.remove(position)
            if not localRequests:
                break
        movement = movement + 1
        position = position + 1
        if position == UPPER_CYLINDER:
            position = 0
            movement = movement + UPPER_CYLINDER
    return movement

'''
LOOK algorithm
'''
def LOOK(requests, initialPosition):
    localRequests = list(requests)
    localRequests.sort()
    position = initialPosition
    movement = 0
    direction = RIGHT
    
    while localRequests:
        if position <= localRequests[0]:
            direction = RIGHT
        if position >= localRequests[-1]:
            direction = LEFT
        if position in localRequests:
            print ("Servicing " + str(position))
            localRequests.remove(position)
            if not localRequests:
                break
        if direction == LEFT and position > LOWER_CYLINDER:
            position = position - 1
        if direction == RIGHT and position < UPPER_CYLINDER:
            position = position + 1
        movement = movement + 1
    return movement

'''
C-LOOK algorithm, fully implemented as example
'''
def C_LOOK(requests, initialPosition):
    localRequests = list(requests)
    localRequests.sort()
    position = initialPosition
    movement = 0

    while localRequests:
        if position in localRequests:
            print ("Servicing " + str(position))
            localRequests.remove(position)
            
            if not localRequests:
                break
        
        if position > localRequests[-1]:
            movement += abs(position - localRequests[0])
            position = localRequests[0]
        else:
            movement += 1
            position += 1
           

    return movement


def tester(initialPosition):
    
    requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
    
    print ("\tFCFS = " + str(FCFS(requests, initialPosition)))
    
    print ("\tSSTF = " + str(SSTF(requests, initialPosition)))
    
    print ("\tSCAN = " + str(SCAN(requests, initialPosition)))
    
    print ("\tC-SCAN = " + str(C_SCAN(requests, initialPosition)))
    
    print ("\tLOOK = " + str(LOOK(requests, initialPosition)))
    
    print ("\tC-LOOK = " + str(C_LOOK(requests, initialPosition)))
