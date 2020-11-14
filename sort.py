import sys # In order to read terminal args
from datetime import datetime # In order to calculate elapsed time

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def algorithmSelector(type,arr):
    # The input 'type' will be one of the strings -> "BubbleSort", "InsertionSort", "MergeSort"
    if type == "BubbleSort": bubbleSort(arr) # Sort with bubbleSort()
    elif type == "InsertionSort": insertionSort(arr) # Sort with insertionSort()
    elif type == "MergeSort": mergeSort(arr) # Sort with mergeSort()
    else: print("INVALID INPUT TYPE") # Print out error message

# ------ Read the whole file ------ #
fileToRead = open("data.txt", "r") 
numbers = fileToRead.readlines() # Sync the numbers in the file to an array.
fileToRead.close()

# ------ File to INT array ------ #
inputSize = int(sys.argv[1]) # Arguement1 represents the number of elements
numbers = numbers[:inputSize] # Ignore the rest of the items
for i in range(0,inputSize): numbers[i] = int(numbers[i]) # Convert the string elements to integer.

# ------ Sort the array with the desired algorithm ------ #
start = datetime.now() # timestamp1
algorithmSelector(str(sys.argv[2]),numbers)  # Arguement2 represents the algorithm type
end = datetime.now() # timestamp2
print("Algorithm: " + str(sys.argv[2]) + "\nInput Size: " + str(inputSize) + "\nElapsed Time: " + str(end-start))

# ------ Write the sorted array to a new file ------ #
fileToWrite = open("sorted.txt","w")
for number in numbers: fileToWrite.write(str(number)+'\n') # Write 
fileToWrite.close()