
# coding: utf-8

# In[1]:


# homework binary_search

def binary_search(data):
    
    data.sort();
    
    start = 0;
    end = len(data) - 1

    print(data)
    target = int(input("찾을 번호를 선택하세요:"))

    while 1 :
        mid = (start + end) // 2 
        if target == data[mid] :
            print("찾았습니다.{}은 data[{}]에 있습니다".format(target, mid))
            break
        elif target < data[mid] :
            end = mid - 1
        elif start > end :
            print("{}은 존재하지 않습니다.".format(target))
            break
        else :
            start = mid + 1
   
data = [3,5,7,8,9,1,2,6,12,15,18]
binary_search(data)

