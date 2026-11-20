listA = [1,3,5]
ListB = [2,4,6]

def merge(listA, listB):
    listA = [1,3,5]
    ListB = [2,4,6] 
    listC = []
    i = 0
    j = 0
    while i < len(listA) and j < len(listB):
        if listA[i] < listB[j]:
            listC.append(listA[i])
            i += 1
        else:
            listC.append(listB[j])
            j += 1
    while i < len(listA):
        listC.append(listA[i])
        i += 1
    while j < len(listB):
        listC.append(listB[j])
        j += 1
    return listC
merged_list = merge(listA, ListB)
print(merged_list)