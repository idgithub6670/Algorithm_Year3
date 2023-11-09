import time
coins = [1,2,5]
change =  int(input('Please enter total number : '))
def coin_change(c = []):
  if sum(c) == change:
     yield tuple(sorted(c))
  else:
     for i in coins:
        if sum(c+[i]) <= change:
           yield from coin_change(c+[i])

start = time.process_time()
print(list(map(list, set(coin_change()))))
elapsed = (time.process_time() - start)
print("%.10f"%(elapsed))