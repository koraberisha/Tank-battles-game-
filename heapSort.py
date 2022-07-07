#This function heaps the lists into trees(heaps).

def heapIt(arr, n, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2    
    try:
        if l < n and arr[i][1] < arr[l][1]:
            largest = l
    
        if r < n and arr[largest][1] < arr[r][1]:
            largest = r
     
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
     
            heapIt(arr, n, largest)
    except:
        None

# This function runs the heapIt function on all indexs.

def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapIt(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapIt(arr, i, 0)

    return arr

# This function allows the programme to sort a list from the second index if the items
# are lists/tuples/arrays.

def sortFromTwoArr(arr):
    for i in range(len(arr)):
        try:
            arr[i][1] = int(arr[i][1])
            
        except ValueError:
            arr[i][1] = float(arr[i][1])
            
            
        
    
    heapSort(arr)
    #print(arr)
    return arr
