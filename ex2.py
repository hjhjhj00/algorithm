#숫자 카드 게임
N = 3
M = 3

list = [[7,3,1,8],[3,3,3,4]]

list0=[]
for i in list:
  i.sort()
  list0.append(i[0])

list0.sort()
print(list0[-1])