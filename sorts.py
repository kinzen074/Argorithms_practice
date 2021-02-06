def insert_sort(arr):
    for i in range(len(arr)):
        num=arr[i]
        idx=i-1
        while(idx>=0 and arr[idx]>num):
            arr[idx+1]=arr[idx]
            idx-=1
        arr[idx+1]=num
    print(arr)
def bb_sort(arr):
    flag=1
    while(flag):
        flag=0
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=1
    print(arr)
if __name__ == '__main__':
    list1 = [5, 2, 3, 1, 4]
    insert_sort(list1)
    bb_sort(list1)
    print("test")