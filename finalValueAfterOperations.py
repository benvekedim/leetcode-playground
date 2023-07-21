def finalValueAfterOperations(operations):
  result = []
  
  for i in operations:
    if "--" in i:
      result.append(-1)
    else:
      result.append(1)
      
  return sum(result)
