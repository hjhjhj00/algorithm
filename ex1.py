#큰 수의 법칙
N=5
M=7
K=2


input=[3,4,3,4,3]

input.sort()
input.reverse()

print(input)

answer=0
for i in range(K):
  answer= answer + input[0]

answer=(M//K)*answer+ M%K*input[1]
print(answer)