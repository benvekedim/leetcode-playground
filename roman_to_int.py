def roman_to_int(s):
  roman_dict = {"I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000}
  result = 0
  prev = 0
  for c in s:
    current = roman_dict[c]
    if current > prev:
      result += current - 2*prev
    else:
      result += current
    prev = current
  return result
