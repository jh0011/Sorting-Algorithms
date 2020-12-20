"""
Counting Sort algorithm
https://www.geeksforgeeks.org/counting-sort/
"""
def counting_sort(toSortArray, maxNum): #Only for positive numbers

    #initialise the indexArray with all 0s
    indexArray = [0] * maxNum

    #update the indexArray with the count of unique elements in toSortArray
    for x in toSortArray:
        indexArray[x] = indexArray[x] + 1

    #update the indexArray with the addition of previous counts
    for x in range(1, len(indexArray)):
        indexArray[x] = indexArray[x-1] + indexArray[x]
    
    #the number of elements in total to be sorted
    maxPlaces = indexArray[maxNum - 1]

    #initialise the sorted array with all 0s
    placesArray = [0] * maxPlaces

    #sort the elements based on the places value
    #decrement the places value after the placesKey is accessed
    for x in toSortArray:
        placesKey = indexArray[x] - 1
        placesArray[placesKey] = x
        indexArray[x] = indexArray[x] - 1

    return placesArray

toSortArray = [17, 14, 1, 8, 17, 5, 0]
print("Sorted array: ", counting_sort(toSortArray, 20))