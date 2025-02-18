import pulp
import pandas as pd

# Problem Setup
# Define the problem as a Linear Programming Problem
problem = pulp.LpProblem("Business_Optimization_Problem", pulp.LpMaximize)

# Define Decision Variables
# Example: Production of Product A and B
product_A = pulp.LpVariable('Product_A', lowBound=0, cat='Continuous')
product_B = pulp.LpVariable('Product_B', lowBound=0, cat='Continuous')

# Define Objective Function
# Example: Maximize Profit
profit_A = 20  # Profit per unit of Product A
profit_B = 30  # Profit per unit of Product B
problem += profit_A * product_A + profit_B * product_B, "Total_Profit"

# Define Constraints
# Example: Resource Constraints
material_available = 100  # Total material available
labor_available = 80  # Total labor hours available

# Material required per unit of products
material_A = 2  # Material units for Product A
material_B = 3  # Material units for Product B

# Labor required per unit of products
labor_A = 4  # Labor hours for Product A
labor_B = 2  # Labor hours for Product B

# Adding constraints
problem += material_A * product_A + material_B * product_B <= material_available, "Material_Constraint"
problem += labor_A * product_A + labor_B * product_B <= labor_available, "Labor_Constraint"

# Solve the problem
problem.solve()

# Output results
print("Optimization Status:", pulp.LpStatus[problem.status])
print("Optimal Solution:")
print("Product A (units):", pulp.value(product_A))
print("Product B (units):", pulp.value(product_B))
print("Total Profit:", pulp.value(problem.objective))

# Insights
# Create a summary DataFrame
results = {
    "Variable": ["Product_A", "Product_B", "Total_Profit"],
    "Value": [pulp.value(product_A), pulp.value(product_B), pulp.value(problem.objective)]
}
summary_df = pd.DataFrame(results)
print("\nSummary:")
print(summary_df)
