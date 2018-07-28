it = [1, 2, 3, 4, 7, 6, 5]
idx = 0
for i in reversed(it):
  print("reversed index:", idx, "value:", i)
  idx += 1

print()
for idx, val in enumerate(reversed(it)):
  print("index:", idx, "value:", val)

print()
for i in enumerate(reversed(it)):
  print("(index, value):", i)
 
i, j, k = (5, 6, 8)
print(i, j, k)

ft = [0.5, 2.7, 3.1, 0.8, 12.3, 8.3, 9.9]
comb = list(zip(it, ft, it, ft))
print(comb)
print()
print("\t".join(map(str, ft)))