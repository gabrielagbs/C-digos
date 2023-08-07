v = []
c = 0
p = 0

for i in range(0,100):
  aux=int(input())
  v.append(aux)

  if v[i] > c:
    c = v[i]
    p = i+1

print(c)
print(p)