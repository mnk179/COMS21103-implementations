import numpy as np

class LinearProgram(object):
    """
        c: vector of numbers, the coefficients in the objective function, dimension n
        A: matrix of numbers, the coefficients in the constraint functions, dimension n * k
        b: vector of numbers, constraints, dimension k
        x: list of characters, the variables, length n

        internally, the vectors and matrices are represented as np.array objects
    """
    def __init__(self, c, A, b, x):
        self.c = c
        self.A = A
        self.b = b
        self.x = x

    def getFunctionString(self, d):
        functionString = ""
        firstSign = d[0] >= 0
        for di, xi in zip(d, self.x):
            coefficient = str(abs(di))
            if di < 0:
                sign = "-"
            else:
                sign = "+"
            functionString += sign + " " + coefficient + xi + " "
        # Trim unnecesary whitespace
        functionString = functionString[:-1]
        # Trim firstSign if it is "+"
        if firstSign:
            functionString = functionString[2:]
        return functionString

    def getConstraintsString(self):
        constraintString = ""
        for cf, bi in zip(self.A, self.b.T[0]):
            constraintString += self.getFunctionString(cf)
            constraintString += " <= " + str(bi) + "\n"
        for xi in self.x:
            constraintString += xi + ", "
        constraintString = constraintString[:-2] + " >= " + str(0)
        return constraintString

    def getConstraintsInSlackForm(self):
        slackMatrix = np.empty((0, len(self.A[0]) + 1))
        # For every row in constraint coefficient matrix
        for row, el in zip(self.A, self.b.T[0]):
            # Negate coefficients
            slackRow = np.array([-x for x in row])
            # Insert constraint at position 0 of coefficient matrix
            slackRow = np.insert(slackRow, 0, el)
            # Append newly created row to the slackMatrix
            slackMatrix = np.append(slackMatrix, [slackRow], axis=0)
        return slackMatrix

    def getSlackFormString(self):
        slackFormString = "A linear program in slack form with"
        slackFormString += "Objective function:\n"
        slackFormString += "maximise\n"
        slackFormString += self.getFunctionString(self.c.T[0]) + "\n"
        slackFormString += "Constraints\n"
        # slackFormString +=
        return slackFormString

    def __str__(self):
        linearProgramString = "A linear program with\n"
        linearProgramString += "Objective function:\n"
        linearProgramString += "maximise\n"
        linearProgramString += "{}\n".format(self.getFunctionString(self.c.T[0]))
        linearProgramString += "Constraints:\n"
        linearProgramString += self.getConstraintsString()
        return linearProgramString

    def __repr__(self):
        self.__str__()



# Let's create a LinearProgram
c1 = np.array([[5],[10],[4],[8]])
A1 = np.array([[-1,-1,0,0],
              [0,0,-1,-1],
              [1,0,1,0],
              [1,0,1,0]])
b1 = np.array([[-400],[-600],[700],[800]])
x1 = ['x','y','w','z']

lp1 = LinearProgram(c1, A1, b1, x1)

# We are aiming to minimise c.T @ x
# subject to A @ x <= b and x >= 0
