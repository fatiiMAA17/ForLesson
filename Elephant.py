numOfElephantsteps = int(input());
step = 5;
i = 1
while numOfElephantsteps > step:
    step += 5
    i += 1
print(i)

# if numOfElephantsteps >= 1 and numOfElephantsteps <= 1000000:
#   if str(numOfElephantsteps).split()[-1] == 9:
#     numOfElephantsteps += 1
#   if numOfElephantsteps % 5 == 0:
#     print(numOfElephantsteps // 5)
#   elif numOfElephantsteps % 4 == 0:
#     print(numOfElephantsteps // 4)
#   elif numOfElephantsteps % 3 == 0:
#     print(numOfElephantsteps // 3)
#   elif numOfElephantsteps % 2 == 0:
#     print(numOfElephantsteps // 2)
# else:
#   print("ERROR!!!")