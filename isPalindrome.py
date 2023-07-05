def isPalindrome(x):
  x = str(x)
  y = str(x[::-1])
  if x == y:
    return True
  else:
    False
