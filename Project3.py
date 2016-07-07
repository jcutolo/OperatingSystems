'''
FIFO page replacement algorithm
'''
def FIFO(size, pages):
    queue = list()
    faults = 0
    
    for page in pages:
        if page in queue:
            pass
        elif len(queue) < size:
            queue.append(page)
            faults = faults + 1
        else:
            queue.pop(0)
            queue.append(page)
            faults = faults + 1
    return faults

''' 
LRU page replacement algorithm
'''
def LRU(size, pages):
    stack = list()
    faults = 0
    
    for page1 in pages:
        if page1 in stack:
            index = 0
            for page2 in stack:
                if page2 == page1:
                    stack.pop(index)
                    stack.append(page1)
                index = index + 1
        elif len(stack) < size:
            stack.append(page1)
            faults = faults + 1
        else:
            stack.pop(0)
            stack.append(page1)
            faults = faults + 1
    return faults


def main():
    pages = (7,2,3,1,2,5,3,4,6,7,7,1,0,5,4,6,2,3,0,1)

    size = int(input('Enter number of frames: '))

    print('The FIFO algorithm had', FIFO(size,pages), 'page faults.')

    print('The LRU algorithm had', LRU(size,pages), 'page faults.')

main()
