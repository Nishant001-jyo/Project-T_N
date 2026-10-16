# n=5
# for i in range(1,n):
#   print("*"*i)


def fibonacci(n):
  if(n==1):
    return 1
  elif(n==0):
    return 0
  else:
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(int(input("Enter a number: "))))