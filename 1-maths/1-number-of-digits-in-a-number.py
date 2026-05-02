# problem: given a number n find the number of digits in it 

def numberOfDigits(n):
  if(-10 < n < 10):
    return 1
  if(n<0):
    n = -1 * n

  digits = 0
  while(n >0):
    digits += 1
    n = n//10
  return digits



if __name__ == "__main__":
  flag = True
  while(flag):
    try:
      n = int(input())
      flag = False
    except ValueError:
      print("Please enter a valid integer number")
  # One liner 
  # print(len(str(n)))
  print(f"number of digits in {n} = {numberOfDigits(n)}")

