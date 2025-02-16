import sympy as sp

def solve_equation(equation):
    x = sp.symbols('x')
    
    solution = sp.solve(equation, x)
    
    return solution

equation_input = input("Введите уравнение : ")
equation = sp.sympify(equation_input.replace('=', '-'))

result = solve_equation(equation)

print(f"Решение уравнения: {result}")