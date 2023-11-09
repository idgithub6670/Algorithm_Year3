from lib2to3.pytree import convert
from re import sub
import time

def drawcard(f):
    data = f.read()
    hand = data.split(',')
    if len(hand)!= 13:
        return 0
    else:
        print(hand)
        return(hand) 
        

def splitcard(hand):
    for i in hand :
        if i[-1] == 's':
            i = i.rstrip(i[-1])
            s.append(i)
        elif i[-1] == 'd':
            i = i.rstrip(i[-1])
            d.append(i)
        elif i[-1] == 'h':
            i = i.rstrip(i[-1])
            h.append(i)
        elif i[-1] == 'c':
            i = i.rstrip(i[-1])
            c.append(i)

def convertcard_to_int():

      global int_s,int_c,int_h,int_d
      for i in s :
            if i == 'j':
                  s.remove(i)
                  s.append(11)
            elif i == 'Q':
                  s.remove(i)
                  s.append(12)
            elif i == 'K':
                  s.remove(i)
                  s.append(13)
            elif i == 'A':
                  s.remove(i)
                  s.append(1)

      for i in h :
            if i == 'j':
                  h.remove(i)
                  h.append(11)
            elif i == 'Q':
                  h.remove(i)
                  h.append(12)
            elif i == 'K':
                  s.remove(i)
                  s.append(13)
            elif i == 'A':
                  h.remove(i)
                  h.append(1)

      for i in d :
            if i == 'j':
                  d.remove(i)
                  d.append(11)
            elif i == 'Q':
                  d.remove(i)
                  d.append(12)
            elif i == 'K':
                  d.remove(i)
                  d.append(13)
            elif i == 'A':
                  d.remove(i)
                  d.append(1)

      for i in c :
            if i == 'j':
                  c.remove(i)
                  c.append(11)
            elif i == 'Q':
                  c.remove(i)
                  c.append(12)
            elif i == 'K':
                  c.remove(i)
                  c.append(13)
            elif i == 'A':
                  d.remove(i)
                  d.append(1)

      int_s = [int(i) for i in s ]
      int_d = [int(i) for i in d ]
      int_h = [int(i) for i in h ]
      int_c = [int(i) for i in c ]
      
      
      int_d.sort(reverse=True)
      int_h.sort(reverse=True)
      int_c.sort(reverse=True)
      int_s = [1,2,3,4,5]
      int_s.sort(reverse=True)
      
      print(int_s)
      print(int_h)
      print(int_c)
      print(int_d)
      
      #return int_s,int_c,int_h,int_d
      return int_s,int_c,int_h,int_d
                  

def Straight_Flush(int_s,int_c,int_h,int_d):
            if len(int_s) >4:
                  st = []
                  i=0
                  x = 1
                  counter = 0
                  for i in int_s:
                        if i-1 == int_s[x]:
                              print('true')
                              st.append(i)
                              counter +=1
                              x +=1
                              if counter >= 4:
                                    st.append(int_s[x-1])
                                    print('st')
                                    print(st)
                                    int_s = (int_s)+(st)
                                    int_s = list( dict.fromkeys(int_s) )
                                    print(int_s)
                                    

                                    return


 
                                                      
                        else:
                              return 

            if len(int_h) >4:
                  st = []
                  i=0
                  x = 1
                  counter = 0
                  for i in int_h:
                        if i-1 == int_h[x]:
                              print('true')
                              st.append(i)
                              counter +=1
                              x +=1
                              if counter >= 4:
                                    st.append(int_h[x-1])
                                    print('st')
                                    print(st)
                                    return
                        else:
                              return 

            if len(int_d) >4:
                  st = []
                  i=0
                  x = 1
                  counter = 0
                  for i in int_d:
                        if i-1 == int_d[x]:
                              print('true')
                              st.append(i)
                              counter +=1
                              x +=1
                              if counter >= 4:
                                    st.append(int_d[x-1])
                                    print('st')
                                    print(st)
                                    return
                        else:
                              return 

            if len(int_c) >4:
                  st = []
                  i=0
                  x = 1
                  counter = 0
                  for i in int_c:
                        if i-1 == int_c[x]:
                              print('true')
                              st.append(i)
                              counter +=1
                              x +=1
                              if counter >= 4:
                                    st.append(int_c[x-1])
                                    print('st')
                                    print(st)
                                    return
                        else:
                              return 

                                          
                              
            

        
#card type
s = []
d = []
h = []
c = []


start_time = time.time()
f = open("card.txt", "r")

hand = drawcard(f)
splitcard(hand)

convertcard_to_int()
Straight_Flush(int_s,int_c,int_h,int_d)



elapsed_time = time.time() - start_time
time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print("%f" %((elapsed_time) / 1000),'ms')

f.close()
