def parse_rule(rule):
    if "IF (" in rule and ") THEN " in rule:
        condition = rule.split("IF (")[1].split(") THEN ")[0]
        consequent = rule.split(") THEN ")[1]
        return condition, consequent
    return None, None

def evaluate_condition(condition, facts):
    for var in facts:
        condition = condition.replace(var, facts[var])
    condition = condition.replace("AND", "and").replace("OR", "or").replace("NOT", "not")
    return eval(condition)

def inference_engine(rules, goal, facts):
    satisfied_goals = set()
    additional_goals = [goal]

    while additional_goals:
        new_goals = []
        for goal in additional_goals:
            for rule in rules:
                condition, consequent = parse_rule(rule)
                if consequent == goal:
                    if evaluate_condition(condition, facts):
                        satisfied_goals.add(goal)
                    else:
                        new_goals += [var for var in condition.replace("NOT", "").split("AND") + condition.replace("NOT", "").split("OR") if var.strip()]

        additional_goals = [g for g in new_goals if g not in satisfied_goals and g not in facts]
        if any(goal in facts for goal in additional_goals):
            satisfied_goals.update(goal for goal in additional_goals if goal in facts)

    return satisfied_goals

num_variables = int(input("Enter the number of variables (minimum 4 and maximum 26): "))
variables = [input(f"Enter variable {i+1}: ").strip() for i in range(num_variables)]

rules = [input(f"Enter rule {i+1} (in format 'IF (condition) THEN <variable>'): ").strip() for i in range(5)]

goal = input("Enter the variable that represents the goal: ").strip()

facts = {}
for _ in range(2):
    var, value = input("Enter a fact (variable and value separated by space, e.g., 'A T'): ").split()
    facts[var] = 'True' if value == 'T' else 'False'

satisfied_goals = inference_engine(rules, goal, facts)
print(f"Satisfied goals: {satisfied_goals}")
