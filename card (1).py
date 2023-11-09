f = open("card.txt", "r")
lst=f.read().split(",")
s=[]
h=[]
d=[]
c=[]
allc=[]
def sscard(ar):
    if str(i[-2]) == "J":
            ar.append(11)
    elif str(i[-2]) == "Q":
            ar.append(12)
    elif str(i[-2]) == "K":
            ar.append(13)
    elif str(i[-2]) == "A":
            ar.append(1)
    else:
            ar.append(int(i[:-1]))

lst.sort()
for i in lst:
    sscard(allc)
    if i[-1]=="s":
        sscard(s)
    elif i[-1]=="h":
        sscard(h)
    elif i[-1]=="d":
        sscard(d)
    elif i[-1]=="c":
        sscard(c)

def insertion_sort(array):

    for i in range(1, len(array)):

        key_item = array[i]


        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array

def allp(number):
    v = []
    d = []
    for x in range( len(number) ):
        if number[x] not in v:
            v.append( number[x] )
        elif number[x] in d:
            pass
        else:
            d.append( number[x] )
            
    return d

def pair(arr,d):
    cd=[]
    for i in d:
        cd.append(arr.count(i))
    return cd

s=insertion_sort(s)
h=insertion_sort(h)
d=insertion_sort(d)
c=insertion_sort(c)

a1=[]
a2=[]
a3=[]

def allarr(number):
    
    v = []
    dd = []
    for x in range( len(number) ):
        if number[x] not in v:
            v.append( number[x] )
        elif number[x] in dd:
            pass
        else:
            dd.append( number[x] )
    v.sort()        
    return v

def Straight(arr):
    bf=[]
    bf.append(arr[0])
    if 10 in arr and 11 in arr and 12 in arr and 13 in arr and 1 in arr :
        bf=[10,11,12,13,1]
        return bf
    for i in range(1,len(arr)):
        if len(bf)==5:
            return bf
        if arr[i]-arr[i-1]==1: 
            bf.append(arr[i])
        else:
            bf=[]
    return bf

def straightflush():
    if len(s)>=5:
        arr=Straight(allarr(s))
        print(arr)
        if len(arr)>5:
            if len(a3)== 0:
                for i in range(5) :
                    a3.append(str(arr[i])+"s")
                    s.pop(s.index(arr[i]))
            else:
                for i in range(5) :
                    a2.append(str(arr[i])+"s")
                    s.pop(s.index(arr[i]))
    
    if len(h)>=5:
        arr=Straight(allarr(h))
        print(arr,"hhhhhhhhhhhhhhhh")
        if len(arr)>5:
            if len(a3)== 0:
                for i in range(5) :
                    a3.append(str(arr[i])+"h")
                    h.pop(h.index(arr[i]))
            else:
                for i in range(5) :
                    a2.append(str(arr[i])+"h")
                    h.pop(h.index(arr[i]))

    if len(d)>=5:
        arr=Straight(allarr(d))
        print(arr,"dddddddddddddddddd")
        if len(arr)>0:
            if len(a3)== 0:
                for i in range(5) :
                    a3.append(str(arr[i])+"d")
                    d.pop(d.index(arr[i]))
            else:
                for i in range(5) :
                    a2.append(str(arr[i])+"d")
                    d.pop(d.index(arr[i]))
    
    if len(c)>=5:
        arr=Straight(allarr(c))
        print(arr,"cccccccccccccccccc")
        if len(arr)>0:
            if len(a3)== 0:
                for i in range(5) :
                    a3.append(str(arr[i])+"c")
                    c.pop(c.index(arr[i]))
            else:
                for i in range(5) :
                    a2.append(str(arr[i])+"c")
                    c.pop(c.index(arr[i]))

def four():
    if 4 in cd:
        pr=dd[cd.index(4)]
        while allc.count(pr)>0:
            allc.pop(allc.index(pr))
        s.pop(s.index(pr))
        h.pop(h.index(pr))
        d.pop(d.index(pr))
        c.pop(c.index(pr))
        cd.pop(dd.index(pr))
        dd.pop(dd.index(pr))
        if len(a3)!=5:
            a3.append(str(pr)+"s")
            a3.append(str(pr)+"h")
            a3.append(str(pr)+"d")
            a3.append(str(pr)+"c")
        else:
            a2.append(str(pr)+"s")
            a2.append(str(pr)+"h")
            a2.append(str(pr)+"d")
            a2.append(str(pr)+"c")

def fullhouse():
    if 3 in cd and 2 in cd:
        pr1=dd[cd.index(3)]
        pr2=dd[cd.index(2)]
        while allc.count(pr1)>0:
            allc.pop(allc.index(pr1))
        while allc.count(pr2)>0:
            allc.pop(allc.index(pr2))
        cd.pop(dd.index(pr1))
        dd.pop(dd.index(pr1))
        cd.pop(dd.index(pr2))
        dd.pop(dd.index(pr2))
        if len(a3) == 0 :
            if pr1 in s:
                a3.append(str(pr1)+"s")
                s.pop(s.index(pr1))
            if pr1 in h:
                a3.append(str(pr1)+"h")
                h.pop(h.index(pr1))
            if pr1 in d:
                a3.append(str(pr1)+"d")
                d.pop(d.index(pr1))
            if pr1 in c:
                a3.append(str(pr1)+"c")
                c.pop(c.index(pr1))
            if pr2 in s:
                a3.append(str(pr2)+"s")
                s.pop(s.index(pr2))
            if pr2 in h:
                a3.append(str(pr2)+"h")
                h.pop(h.index(pr2))
            if pr2 in d:
                a3.append(str(pr2)+"d")
                d.pop(d.index(pr2))
            if pr2 in c:
                a3.append(str(pr2)+"c")
                c.pop(c.index(pr2))
        else:
            if pr1 in s:
                a2.append(str(pr1)+"s")
                s.pop(s.index(pr1))
            if pr1 in h:
                a2.append(str(pr1)+"h")
                h.pop(h.index(pr1))
            if pr1 in d:
                a2.append(str(pr1)+"d")
                d.pop(d.index(pr1))
            if pr1 in c:
                a2.append(str(pr1)+"c")
                c.pop(c.index(pr1))
            if pr2 in s:
                a2.append(str(pr2)+"s")
                s.pop(s.index(pr2))
            if pr2 in h:
                a2.append(str(pr2)+"h")
                h.pop(h.index(pr2))
            if pr2 in d:
                a2.append(str(pr2)+"d")
                d.pop(d.index(pr2))
            if pr2 in c:
                a2.append(str(pr2)+"c")
                c.pop(c.index(pr2))

def flush():
    if len(s)>=5:
        if len(a3)== 0:
            for i in range(5) :
                a3.append(str(s[0])+"s")
                s.pop(0)
        else:
            for i in range(5) :
                a2.append(str(s[0])+"s")
                s.pop(0)
    
    if len(h)>=5:
        if len(a3)== 0:
            for i in range(5) :
                a3.append(str(h[0])+"h")
                h.pop(0)
        else:
            for i in range(5) :
                a2.append(str(h[0])+"h")
                h.pop(0)

    if len(d)>=5:
        arr=Straight(allarr(d))
        if len(a3)== 0:
            for i in range(5) :
                a3.append(str(d[0])+"d")
                d.pop(0)
        else:
            for i in range(5) :
                a2.append(str(d[0])+"d")
                d.pop(0)
    
    if len(c)>=5:
        arr=Straight(allarr(c))
        if len(a3)== 0:
            for i in range(5) :
                a3.append(str(c[0])+"c")
                c.pop(0)
        else:
            for i in range(5) :
                a2.append(str(c[0])+"c")
                c.pop(0)

def st():
    arr=Straight(allarr(allc))
    if len(arr)!=0:
        if len(a3) == 0 :
            for i in arr:
                if i in s:
                    a3.append(str(i)+"s")
                    s.pop(s.index(i))
                elif i in h:
                    a3.append(str(i)+"h")
                    h.pop(h.index(i))
                elif i in d:
                    a3.append(str(i)+"d")
                    d.pop(d.index(i))
                elif i in c:
                    a3.append(str(i)+"c")
                    c.pop(c.index(i))
        elif len(a2) == 0:
            for i in arr:
                if i in s:
                    a2.append(str(i)+"s")
                    s.pop(s.index(i))
                elif i in h:
                    a2.append(str(i)+"h")
                    h.pop(h.index(i))
                elif i in d:
                    a2.append(str(i)+"d")
                    d.pop(d.index(i))
                elif i in c:
                    a2.append(str(i)+"c")
                    c.pop(c.index(i))

def three():
    if 3 in cd:
            num=dd.pop(cd.index(3)) 
            print(num)
            if len(a3)==0:
                if num in s:
                    a3.append(str(num)+"s")
                    s.pop(s.index(num))
                if num in h:
                    a3.append(str(num)+"h")
                    h.pop(h.index(num))
                if num in d:
                    a3.append(str(num)+"d")
                    d.pop(d.index(num))
                if num in c:
                    a3.append(str(num)+"c")
                    c.pop(c.index(num))
            elif len(a2)==0:
                if num in s:
                    a2.append(str(num)+"s")
                    s.pop(s.index(num))
                if num in h:
                    a2.append(str(num)+"h")
                    h.pop(h.index(num))
                if num in d:
                    a2.append(str(num)+"d")
                    d.pop(d.index(num))
                if num in c:
                    a2.append(str(num)+"c")
                    c.pop(c.index(num))
            elif len(a1)==0:
                if num in s:
                    a1.append(str(num)+"s")
                    s.pop(s.index(num))
                if num in h:
                    a1.append(str(num)+"h")
                    h.pop(h.index(num))
                if num in d:
                    a1.append(str(num)+"d")
                    d.pop(d.index(num))
                if num in c:
                    a1.append(str(num)+"c")
                    c.pop(c.index(num))
            
def towpair():           
    if cd.count(2)>=2:
            if len(a3)==0:
                for i in range(2):
                    num=dd.pop(cd.index(2))
                    if num in s:
                        a3.append(str(num)+"s")
                        s.pop(s.index(num))
                    if num in h:
                        a3.append(str(num)+"h")
                        h.pop(h.index(num))
                    if num in d:
                        a3.append(str(num)+"d")
                        d.pop(d.index(num))
                    if num in c:
                        a3.append(str(num)+"c")
                        c.pop(c.index(num))
            elif len(a2)==0:
                for i in range(2):
                    num=dd.pop(cd.index(2))
                    if num in s:
                        a2.append(str(num)+"s")
                        s.pop(s.index(num))
                    if num in h:
                        a2.append(str(num)+"h")
                        h.pop(h.index(num))
                    if num in d:
                        a2.append(str(num)+"d")
                        d.pop(d.index(num))
                    if num in c:
                        a2.append(str(num)+"c")
                        c.pop(c.index(num))

def pairr():
    if 2 in cd:
            num=dd.pop(cd.index(2)) 
            print(num)
            if len(a3)==0:
                if num in s:
                    a3.append(str(num)+"s")
                    s.pop(s.index(num))
                if num in h:
                    a3.append(str(num)+"h")
                    h.pop(h.index(num))
                if num in d:
                    a3.append(str(num)+"d")
                    d.pop(d.index(num))
                if num in c:
                    a3.append(str(num)+"c")
                    c.pop(c.index(num))
            elif len(a2)<4:
                if num in s:
                    a2.append(str(num)+"s")
                    s.pop(s.index(num))
                if num in h:
                    a2.append(str(num)+"h")
                    h.pop(h.index(num))
                if num in d:
                    a2.append(str(num)+"d")
                    d.pop(d.index(num))
                if num in c:
                    a2.append(str(num)+"c")
                    c.pop(c.index(num))
            elif len(a1)<2:
                if num in s:
                    a1.append(str(num)+"s")
                    s.pop(s.index(num))
                if num in h:
                    a1.append(str(num)+"h")
                    h.pop(h.index(num))
                if num in d:
                    a1.append(str(num)+"d")
                    d.pop(d.index(num))
                if num in c:
                    a1.append(str(num)+"c")
                    c.pop(c.index(num))

def highcard():
    if len(s)>0:
        for i in s:
            if len(a3)<5:
                a3.append(str(i)+"s")
            elif len(a2)<5:
                a2.append(str(i)+"s")
            elif len(a1)<3:
                a1.append(str(i)+"s")
    if len(h)>0:
        for i in h:
            if len(a3)<5:
                a3.append(str(i)+"h")
            elif len(a2)<5:
                a2.append(str(i)+"h")
            elif len(a1)<3:
                a1.append(str(i)+"h")

    if len(d)>0:
        for i in d:
            if len(a3)<5:
                a3.append(str(i)+"d")
            elif len(a2)<5:
                a2.append(str(i)+"d")
            elif len(a1)<3:
                a1.append(str(i)+"d")
    
    if len(c)>0:
        for i in c:
            if len(a3)<5:
                a3.append(str(i)+"d")
            elif len(a2)<5:
                a2.append(str(i)+"d")
            elif len(a1)<5:
                a1.append(str(i)+"d")

straightflush()
allc=s+h+d+c
dd=allp(allc)
dd.sort()
cd=pair(allc,dd)


four()
allc=s+h+d+c
dd=allp(allc)
dd.sort()
cd=pair(allc,dd)


fullhouse()
allc=s+h+d+c
dd=allp(allc)
dd.sort()
cd=pair(allc,dd)


flush()
allc=s+h+d+c
dd=allp(allc)
dd.sort()
cd=pair(allc,dd)


st()
allc=s+h+d+c
dd=allp(allc)
dd.sort()
cd=pair(allc,dd)


three()
allc=s+h+d+c
dd=allp(allc)
dd.sort()
cd=pair(allc,dd)

towpair()
allc=s+h+d+c
dd=allp(allc)
dd.sort()
cd=pair(allc,dd)

pairr()
allc=s+h+d+c
dd=allp(allc)
dd.sort()
cd=pair(allc,dd)

highcard()
na1=[]
na2=[]
na3=[]
for i in a1:
    if int(i[:-1])==11:
        na1.append("J"+i[-1])
    elif int(i[:-1])==12:
        na1.append("Q"+i[-1])
    elif int(i[:-1])==13:
        na1.append("K"+i[-1]) 
    elif int(i[:-1])==1:
        na1.append("A"+i[-1]) 
    else:
        na1.append(i)

for i in a2:
    if int(i[:-1])==11:
        na2.append("J"+i[-1])
    elif int(i[:-1])==12:
        na2.append("Q"+i[-1])
    elif int(i[:-1])==13:
        na2.append("K"+i[-1]) 
    elif int(i[:-1])==1:
        na2.append("A"+i[-1])
    else:
        na2.append(i)

for i in a3:
    if int(i[:-1])==11:
        na3.append("J"+i[-1])
    elif int(i[:-1])==12:
        na3.append("Q"+i[-1])
    elif int(i[:-1])==13:
        na3.append("K"+i[-1]) 
    elif int(i[:-1])==1:
        na3.append("A"+i[-1])
    else:
        na3.append(i)

print(na1)
print(na2)
print(na3)
    
f = open("output.txt", "w")
for i in na1:
    if na1.index(i)<len(na1)-1:
        f.write(i+",")
    else:
        f.write(i)
f.write("\n")
for i in na2:
    if na2.index(i)<len(na2)-1:
        f.write(i+",")
    else:
        f.write(i)
        
f.write("\n")
for i in na3:
    if na3.index(i)<len(na3)-1:
        f.write(i+",")
    else:
        f.write(i)

