import time

sol01 = ([1,2,5],0)
sol02 = ([1,2,5],11)
sol03 = ([1,5,6,9],11)
sol04 = ([1,12,20],48)
sol05 = ([2,3,6,7],12)
sol06 = ([1,2,5],30)
sol07 = ([1,2,5],35)
sol08 = ([1,2,5],40)

def removeDuplicates(combos):
  filtered = set()
  for combo in combos:
    combo.sort()
    filtered.add(tuple(combo))
  return [list(i) for i in filtered]

def coin_change(coins,c):
  if c == 0:
    return [[]]     
  if c < 0:
    return []      
  else:
    all_combos = []
    for i in coins:
      recursive_result = coin_change(coins,c-i)
      for combo in recursive_result:
        combo.append(i)
      all_combos.extend(recursive_result)

    return removeDuplicates(all_combos)



#result = greedy(input_item(), int(input("Enter coin to change : ")))
#print("Change coin :", result)

start = time.process_time()
result = coin_change(sol01[0],sol01[1])
for combo in result:
  print(combo)
elapsed = (time.process_time() - start)
print("Solution01 used %.5f second"%(elapsed))

start = time.process_time()
result = coin_change(sol02[0],sol02[1])
for combo in result:
  print(combo)
elapsed = (time.process_time() - start)
print("Solution02 used %.5f second"%(elapsed))

start = time.process_time()
result = coin_change(sol03[0],sol03[1])
for combo in result:
  print(combo)
elapsed = (time.process_time() - start)
print("Solution03 used %.5f second"%(elapsed))

start = time.process_time()
result = coin_change(sol04[0],sol04[1])
for combo in result:
  print(combo)
elapsed = (time.process_time() - start)
print("Solution04 used %.5f second"%(elapsed))

start = time.process_time()
result = coin_change(sol05[0],sol05[1])
for combo in result:
  print(combo)
elapsed = (time.process_time() - start)
print("Solution05 used %.5f second"%(elapsed))

start = time.process_time()
result = coin_change(sol06[0],sol06[1])
for combo in result:
  print(combo)
elapsed = (time.process_time() - start)
print("Solution06 used %.5f second"%(elapsed))


start = time.process_time()
result = coin_change(sol07[0],sol07[1])
for combo in result:
  print(combo)
elapsed = (time.process_time() - start)
print("Solution07 used %.5f second"%(elapsed))

start = time.process_time()
result = coin_change(sol08[0],sol08[1])
for combo in result:
  print(combo)
elapsed = (time.process_time() - start)
print("Solution08 used %.5f second"%(elapsed))


