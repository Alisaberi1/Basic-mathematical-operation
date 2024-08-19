
def basic_op(operator, value1, value2):
  
  if operator=="+":
    a=value1+value2
    print(value1+value2)
  if operator=="-":
    a=value1-value2
    return value1-value2
  if operator=="/":
    a=value1/value2
    return value1/value2
  if operator=="*":
    a=value1*value2
    return value1*value2
  else:
    print("not in 4 command!")
operator=input()
value1, value2=map(int,input().split())
result =(basic_op(operator, value1, value2))
print("Result:", result)