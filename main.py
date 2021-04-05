N=25
K=5

count=0

while True:
  if N==1:
    break
  elif N%K != 0:
    N=N-1
    count=count+1
  elif N%K == 0:
    N=N//K
    count=count+1

print(count)
  
