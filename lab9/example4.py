import time

def simple_timer(t=0):
  if t==-1:
    return 1
  time.sleep(1)
  print(t)
  return simple_timer(t-1)
  
simple_timer(t=int(input('Please enter an integer:')))