

def mergesort(arr,byfunc):
    if len(arr) >1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
#recursive call to split array into array of length 1
        mergesort(left_arr,byfunc)
        mergesort(right_arr,byfunc)
#merge the arrays 
#i is the index of the left array
#j is the index of the right array
#k is the index of the merged array
        i = j = k = 0
        while i<len(left_arr) and j<len(right_arr):
            if byfunc(left_arr[i]) < byfunc(right_arr[j]):
                arr[k] = left_arr[i]
                i+=1
            elif byfunc(left_arr[i]) > byfunc(right_arr[j]):
                arr[k] = right_arr[j]
                j+=1
            else:
                arr[k] = left_arr[i]
                i+=1
            k+=1

        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1

        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        pass

    def pop(self):
        return self.__items.pop() if not self.is_empty else None
        pass

    def peek(self):
        return self.__items[-1]
        pass
    

    @property
    def is_empty(self):
        return self.__items == []
        pass
    

    @property
    def size(self):
        return len(self.__items)
        pass

class EvaluateExpression:
  # copy the other definitions
  # from the previous parts
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expr =string 

  @property
  def expression(self):
    return self.expr 

  @expression.setter
  def expression(self, new_expr):
    valid_char = '0123456789+-*/() '
    for i in new_expr:
      ### if i is inside valid_char, find fn will not return -1 // if i is not inside valid_char it will return -1 
      if self.valid_char.find(i) == -1:
        self.expr = ""
        #print(self.expr)
        break
      ### code will run until here if i is a valid character and assign new_expr to self.expr
      else: 
        self.expr = new_expr 
        #print(self.expr)
        continue

      
  def insert_space(self):
    operators = '+-*/()'
    newstr = ''
    for i in self.expr: 
      ### using the same logic as the expression setter, iterate through the input and look for operator
      if operators.find(i) != -1:
        newstr = newstr + ' ' + str(i) + ' '
      else: 
        newstr += str(i)
    return newstr 


  def process_operator(self, operand_stack, operator_stack):
    right = str(operand_stack.pop())
    left = str(operand_stack.pop())
    operator = str(operator_stack.pop())
    ### changing / into // 
    divide = '//'
    if operator == '/':
      result = str(eval(f'{left} {divide} {right}'))
    else:
      result = str(eval(f'{left} {operator} {right}'))
    #print (result)
    operand_stack.push(int(result))
    #print (operand_stack.peek())



  #def evaluate(self):
    # operand_stack = Stack()
    # operator_stack = Stack()
    # expression = self.insert_space()
    # tokens = expression.split()
    # pass
    ### replaces '/' with '//' 
    ### 
    # x=self.expr.replace('/','//')
    # #print(x)
    # return eval(x)

  def evaluate(self):
    operand_l = "0123456789"
    operator_l = "+-*/()"

    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()

    for i in tokens:
        if (i in operand_l):
            operand_stack.push(i)
        
        elif (i == "("):
            operator_stack.push(i)
        
        elif (i == ")"):
            while operator_stack.peek() != "(":
                self.process_operator(operand_stack, operator_stack)
            operator_stack.pop()

        elif (i in operator_l):
            while (not operator_stack.is_empty) and (operator_stack.peek() in "*/"):
                self.process_operator(operand_stack, operator_stack)
            
            operator_stack.push(i)
    
    while (not operator_stack.is_empty):
        self.process_operator(operand_stack, operator_stack)

    return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





