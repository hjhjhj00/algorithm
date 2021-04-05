#큰 수의 법칙
N=5
M=8
K=3


input=[2,4,5,4,6]

input.sort()
input.reverse()

print(input)

answer=0
for i in range(K):
  answer= answer + input[0]

answer=(M//K)*answer+ M%K*input[1]
print(answer)