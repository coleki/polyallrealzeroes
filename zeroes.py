# All real zeroes of a polynomial

# Define the coefficients of the polynomial to solve for.
# Remember to include a 0 if that power of x does not have any term listed in the polynomial.
# E.g. 3x^2 - 2x + 7 is really 3x^3 + 0x^2 - 2x + 7.
polynomial_terms = [-7, 48, -77, -12]

# What is the highest power of x in this polynomial?
max_power = len(polynomial_terms)

# Function - Find the solution of the polynomial for a given x. (Test a possible zero.)
def evaluateFunction(x):
    value = 0
    for power in range(0, max_power, 1):
        value += polynomial_terms[power]*(x^power)
    return value

# Function - get_factors    
def get_factors(x):
    factors = []
    for i in range(1, x):
        if x % i == 0:
            factors.append(x)
    return factors

# Find our constant C, and our leading coefficient, a_n.
constant = int(polynomial_terms[max_power-1])
a_n = int(polynomial_terms[0])

# Print out what we have so far, for troubleshooting purposes...
print ("Polynomial terms:")
print polynomial_terms
print ("Constant:")
print constant
print ("A_n:")
print a_n

# Finds all the factors of the constant C. (Also the negatives)
c_factors = get_factors(abs(constant))
for factor in c_factors:
    c_factors.append(-1*factor)

# Finds all the factors of the leading coefficient, a_n. (Also the negatives)
a_factors = get_factors(abs(a_n))
for factor in a_factors:
    a_factors.append(-1*factor)

possible_factors = []

# Add all the factors of C and the factors of a_n into our list of possible factors.
possible_factors.append(c_factors)
possible_factors.append(a_factors)

# Remove duplicates from the list
possible_factors = list( dict.fromkeys(possible_factors) )

# Add in all the possible zeroes derived from +/-(c_factors/a_factors)
for cf in c_factors:
    for af in a_factors:
        if cf % af != 0:
            possible_factors.append(cf/af)
            possible_factors.append(-cf/af)

# Remove duplicates from the list, again.
possible_factors = list( dict.fromkeys(possible_factors) )

# Sort all the possible factors from least to greatest.
possible_factors.sort()

# Try all possible zeroes to determine whether they are real zeroes or not.
zeroes = []
for trying in possible_factors:
    if evaluateFunction(trying) == 0:
        zeroes.append(trying)

if len(zeroes) == 0:
    print("No real zeroes found.")
else:
    print("Zeroes: ")
    print zeroes
