def water_jug_dfs(jug1_capacity, jug2_capacity, target_amount):
    def dfs(jug1, jug2, path):
        print(f"State: ({jug1}, {jug2})")
        if jug1 == target_amount:
            return path
        visited.add((jug1, jug2))
        for action, action_name in actions:
            next_jug1, next_jug2 = action(jug1, jug2)
            if (next_jug1, next_jug2) not in visited:
                result = dfs(next_jug1, next_jug2, path + [action_name])
                if result:
                    return result
        return None

    def fill_jug1(jug1, jug2):
        return jug1_capacity, jug2

    def fill_jug2(jug1, jug2):
        return jug1, jug2_capacity

    def pour_jug1_to_jug2(jug1, jug2):
        amount_to_pour = min(jug1, jug2_capacity - jug2)
        return jug1 - amount_to_pour, jug2 + amount_to_pour

    def pour_jug2_to_jug1(jug1, jug2):
        amount_to_pour = min(jug2, jug1_capacity - jug1)
        return jug1 + amount_to_pour, jug2 - amount_to_pour

    def empty_jug1(jug1, jug2):
        return 0, jug2

    def empty_jug2(jug1, jug2):
        return jug1, 0

    actions = [
        (fill_jug1, "Fill jug1"),
        (fill_jug2, "Fill jug2"),
        (pour_jug1_to_jug2, "Pour jug1 to jug2"),
        (pour_jug2_to_jug1, "Pour jug2 to jug1"),
        (empty_jug1, "Empty jug1"),
        (empty_jug2, "Empty jug2"),
    ]

    visited = set()
    path = dfs(0, 0, [])
    if path:
        return path
    else:
        return "No solution found."


jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

solution = water_jug_dfs(jug1_capacity, jug2_capacity, target_amount)
print("Steps to reach the goal:", solution)
