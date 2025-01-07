class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
    
    def apply_rules(self, expression):
        for rule in self.rules:
            new_expression = rule(expression)
            if new_expression != expression:
                print(f"Applied rule: {rule.__name__}")
                print(f"Transformed expression: {new_expression}")
                return new_expression
        return expression

def de_morgan_1(expr):
    return expr.replace("(A . B)'", "A' + B'")

def de_morgan_2(expr):
    return expr.replace("(A + B)'", "A' . B'")

def transposition(expr):
    return expr.replace("A.B + A'.C", "(A + C) . (A' + B)")

def duality(expr):
    return expr.replace("A.(B+C)", "(A+B).(A+C)")

def simplify_7(expr):
    return expr.replace("A.0", "0")

def simplify_8(expr):
    return expr.replace("A + 1", "1")

def simplify_9(expr):
    return expr.replace("A.1", "A")

def simplify_10(expr):
    return expr.replace("A + 0", "A")

def simplify_11(expr):
    return expr.replace("A + A", "A")

def simplify_12(expr):
    return expr.replace("A.A", "A")

def simplify_13(expr):
    return expr.replace("A + A'", "1")

def simplify_14(expr):
    return expr.replace("A.A'", "0")

def simplify_15(expr):
    return expr.replace("((A)')'", "A")

def commutativity_plus(expr):
    return expr.replace("A + B", "B + A")

def commutativity_dot(expr):
    return expr.replace("A . B", "B . A")

def associative_plus(expr):
    return expr.replace("A + (B + C)", "(A + B) + C")

def associative_dot(expr):
    return expr.replace("A . (B . C)", "(A . B) . C")

def distributivity(expr):
    return expr.replace("A . (B + C)", "(A . B) + (A . C)")

def absorption_21(expr):
    return expr.replace("A . (A + B)", "A")

def absorption_22(expr):
    return expr.replace("A + A.B", "A")

def absorption_23(expr):
    return expr.replace("A + A'.B", "A + B")

def absorption_24(expr):
    return expr.replace("A . (A' + B)", "A . B")

rules = [
    de_morgan_1,
    de_morgan_2,
    transposition,
    duality,
    simplify_7,
    simplify_8,
    simplify_9,
    simplify_10,
    simplify_11,
    simplify_12,
    simplify_13,
    simplify_14,
    simplify_15,
    commutativity_plus,
    commutativity_dot,
    associative_plus,
    associative_dot,
    distributivity,
    absorption_21,
    absorption_22,
    absorption_23,
    absorption_24
]

ie = InferenceEngine(rules)

initial_expression = "A.B + B.C' + A.C"
goal_expression = "A.C + B.C'"

current_expression = initial_expression
while current_expression != goal_expression:
    new_expression = ie.apply_rules(current_expression)
    if new_expression == current_expression:
        print("No more applicable rules.")
        break
    current_expression = new_expression

print(f"Final expression: {current_expression}")
print(f"Goal expression: {goal_expression}")

if current_expression == goal_expression:
    print("Proof successful!")
else:
    print("Proof not successful.")
