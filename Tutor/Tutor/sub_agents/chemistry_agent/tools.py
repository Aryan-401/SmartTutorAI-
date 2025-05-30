import logging
logging.basicConfig(level=logging.ERROR)
import re
import io
import sys
from sympy import Matrix, lcm
print("Libraries imported.")

def parse_compound(compound):
    """Parses chemical formula like 'H2O' into a dict: {'H':2, 'O':1}"""
    pattern = '([A-Z][a-z]?)(\d*)'
    parsed = re.findall(pattern, compound)
    result = {}
    for elem, count in parsed:
        result[elem] = result.get(elem, 0) + int(count or '1')
    return result


def balance_equation(reactants: str, products: str) -> str:
    """Balances a chemical equation given as lists of reactants and products.
    Args:
        reactants: Space Separated string of reactant compounds (e.g., H2 O2)
        products: Space Separated string of product compounds (e.g., H2O )
        """
    reactants = reactants.split()
    products = products.split()
    elements = set()
    for compound in reactants + products:
        elements.update(parse_compound(compound).keys())
    elements = sorted(elements)

    matrix = []
    for elem in elements:
        row = []
        for compound in reactants:
            row.append(parse_compound(compound).get(elem, 0))
        for compound in products:
            row.append(-parse_compound(compound).get(elem, 0))
        matrix.append(row)

    mat = Matrix(matrix)
    null_space = mat.nullspace()
    if not null_space:
        raise ValueError("No solution found")
    coeffs = null_space[0]
    lcm_val = lcm([val.q for val in coeffs])
    coeffs = coeffs * lcm_val
    coeffs = [abs(int(c)) for c in coeffs]

    reactant_side = ' + '.join(f"{coeffs[i]} {reactants[i]}" for i in range(len(reactants)))
    product_side = ' + '.join(f"{coeffs[i + len(reactants)]} {products[i]}" for i in range(len(products)))
    return f"{reactant_side} → {product_side}"

