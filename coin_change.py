import time

def greedy(coins, c):
    if c <= 0:
        return 0 # base case

    result = [0 for _ in range(len(coins))]
    sum = 0
    p = len(coins)-1

    for _ in range(len(coins)):
        while coins[p] + sum <= c: 
            sum += coins[p]
            result[p] += 1
        p -= 1

    return(result)

def input_item():
    lst = [int(item) for item in input("Enter coins the list : ").split()]
    return lst

sol01 = ([1,2,5],0)
sol02 = ([1],300)
sol03 = ([1,5,6,9],11)
sol04 = ([1,12,20],48)
sol05 = ([2,3,6,7],12)
sol06 = ([2,4,6,7,10,14,20],150)
sol07 = ([186,419,83,408],6249)

result = greedy(input_item(), int(input("Enter coin to change : ")))
print("Change coin :", result)
'''
print()
print("Change coin 01 :", greedy(sol01[0], sol01[1]))
print("Change coin 02 :", greedy(sol02[0], sol02[1]))
print("Change coin 03 :", greedy(sol03[0], sol03[1]))
print("Change coin 04 :", greedy(sol04[0], sol04[1]))
print("Change coin 05 :", greedy(sol05[0], sol05[1]))
print("Change coin 06 :", greedy(sol06[0], sol06[1]))
print("Change coin 07 :", greedy(sol07[0], sol07[1]))
print()
'''

'''
print()
s = time.process_time()
greedy(sol01[0], sol01[1])
print("sol01 Time is",s - time.process_time())
s = time.process_time()
greedy(sol02[0], sol02[1])
print("sol02 Time is", s - time.process_time())
s = time.process_time()
greedy(sol03[0], sol03[1])
print("sol03 Time is", s - time.process_time())
s = time.process_time()
greedy(sol04[0], sol04[1])
print("sol04 Time is", s - time.process_time())
s = time.process_time()
greedy(sol05[0], sol05[1])
print("sol05 Time is", s - time.process_time())
s = time.process_time()
greedy(sol06[0], sol06[1])
print("sol06 Time is", s - time.process_time())
s = time.process_time()
greedy(sol07[0], sol07[1])
print("sol07 Time is", s - time.process_time())
print()
'''