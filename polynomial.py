def evaluate_polynomial(degree, x, constant_term, coefficients):
    # TODO: Implement polynomial evaluation using direct substitution method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result
    p = constant_term
    k = 1
    while k <= degree:
        c = coefficients[k - 1]
        p += x**k * c
        k += 1
    return p

if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial function
    # TODO: Ask user if they want to run again
    t = True
    while t:
        degree = int(input("Degree of polynomial: "))
        x = int(input("Value of x: "))
        constant_term = int(input("Value of constant term: "))
        coefficients = []
        for i in range(1, degree + 1):
            coefficients.append(int(input(f"Coefficient of the x^{i} term: ")))
        print(evaluate_polynomial(degree, x, constant_term, coefficients))
        if input("Run again (y/n)? ") == "n":
            t = False

