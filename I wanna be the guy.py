n=int(input()) ; p=list(map(int, input().split()))[1:] ; q=list(map(int, input().split()))[1:]
total_pq=set(p+q)
if len(total_pq) == n:
  print("I become the guy.")
else:
  print("Oh, my keyboard!")
# for i in range(1,n+1):
    # if i not in total_pq:
    #     print('Oh, my keyboard!')
    #     exit()