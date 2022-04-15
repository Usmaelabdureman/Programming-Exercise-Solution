
def quickSort(ListToSort):
    QuickSortHlper(ListToSort,0,len(ListToSort)-1)
    
#Quicksort helper function do recursively
def QuickSortHlper(list,low,high):
    if len(list)==1:
        return list

    if low < high:
        pivot= get_median([list[low], list[high], list[(high+low)//2]])
        pivotIndex = partition(list,low,high,pivot)
        QuickSortHlper(list,low,pivotIndex-1)
        QuickSortHlper(list,pivotIndex,high)

#let's find Median of the first , middle and last number in array        
def get_median(list):
    for i in range(len(list)):
        for j in range(i+1):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    return list[1]
#Parition the array into two parts recursive
def partition(list, low, high, pivot):
    while low <= high:
        while list[low] < pivot:
            low += 1
        while list[high] >pivot:
            high -= 1 
        if low <= high:
            list[low], list[high] = list[high], list[low]
            low += 1
            high -=1
    return low

def test():
    ll=[5,3,6,-2,-5,0,8,45,60,96,28,11,6]
    print("list before sort:",ll)
    quickSort(ll)
    print("List after sorted:",ll)
if __name__=="__main__":
    test()