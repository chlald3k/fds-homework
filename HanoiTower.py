
# coding: utf-8

# In[34]:


#하노이타워

#반복횟수
count = 0

def moveHanoiTower(first, center, last, n) :
    if n == 1 :
        global count
        count+=1
        print("원판 [{}], {} -> {}".format(n, first, last))
    else :
        moveHanoiTower(first, last, center, n - 1) 
        count += 1
        print("원판 [{}], {} -> {}".format(n, first, last))
        moveHanoiTower(center, first, last, n - 1)
        
def resultNumber():
    return count


select = int(input("원판 개수 입력:"))

moveHanoiTower(1, 2, 3, select)
total = resultNumber()
print("*** 총 이동 횟수:{} ***".format(total))

