# Problem: Given a positive number n check if the number is a palindrom or not

def isPalindrom(n):
  x = n
  reversedNum = 0
  while(x != 0):
      reversedNum = reversedNum* 10  + x%10
      x = x//10

  return n == reversedNum    

# Time Complexit: O(number of digits in n)

if __name__ == "__main__":
    flag = True
    while flag:
        try:
            n = int(input())
            flag = False if n >0 else True
        except ValueError:
            print("Please enter a valid integer number")

    print(f"Ite: {n} is palindrom? {isPalindrom(n)}")