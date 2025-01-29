# The calculate_tax function computes the total tax based on salary and tax brackets.

# Approach:
# - Iterate through the tax brackets (`levels`), calculating tax for each range.
# - Stop when the salary falls within a bracket or reaches the highest bracket.
# - Add tax based on the portion of the salary within each bracket.

# TC: O(n) - Iterate through tax brackets.
# SC: O(1) - Constant space usage.

def calculate_tax(levels, salary):
    tax = 0.0
    previous_limit = 0

    for level in levels:
        limit, rate = level
        if limit is None:
            tax += (salary - previous_limit) * rate
            break
        if salary > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (salary - previous_limit) * rate
            break

    return tax