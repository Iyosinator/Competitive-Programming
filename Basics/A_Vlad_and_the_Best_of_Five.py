t = int(input())

for i in range(t):
   word = input()
   
   count_a = word.count("A")
   count_b = word.count("B")
   
   if count_a > count_b: print("A")
   else: print("B")
      