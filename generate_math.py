# How do we generate 10 random math problems for addition subtraction multiplication and division
import random


class Problem:
    def __init__(self, operator, operand_a, operand_b):
        self.operator = operator
        self.operand_a = operand_a
        self.operand_b = operand_b
        self.result = hash(str(self.getResult()))
    
    def getResult(self):
        if self.operator is '+':
            return self.operand_a + self.operand_b
        elif self.operator is '-':
            return self.operand_a - self.operand_b
        elif self.operator is '*':
            return self.operand_a * self.operand_b
        elif self.operator is '/':
            return self.operand_a/self.operand_b
        else:
            print("UNSUPPORTED OPERATOR: PLEASE USE \"+\" \"-\" \"*\" OR \"/\" ")


    def __str__(self):
        return str(self.operand_a) +' '+ self.operator +' '+ str(self.operand_b) +' = '+str(self.result) +  '\n'

print("*****SIMPLE TEST*******\n")
print("Addition:")
problem1 = Problem('+', 2, 2)
print(problem1)
print(str(hash('4'))+"<-this proves I can validate answers")
print("Subtraction:")
problem2 = Problem('-', 6, 2)
print(problem2)

print("Multiplication:")
problem3 = Problem('*', 9, 81)
print(problem3)

print("Division:")
problem4 = Problem('/', 100, 12)
print(problem4)
print("******************\n\n")

operators = ['+','-','*','/']
random_problems = []
for i in range(10):
    random_problems.append(Problem(operators[random.randint(0,3)], random.randrange(100), random.randrange(100)))
    print(random_problems[i])