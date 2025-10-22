def evaluate_polynomial(degree, x, constant_term, *coefficients):
    # TODO: Implement polynomial evaluation using direct substitution method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result
    p = constant_term
    k = 1
    while k <= degree:
        p = p + x**k * coefficients
        k = k + 1
    return p

if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial function
    # TODO: Ask user if they want to run again

    t = True
    while t:
        degree = input()
        x = input()
        constant_term = input()
        coefficients = []
        for i in degree + 1:
            coefficients.append(input())
        print(evaluate_polynomial(degree, x, constant_term, coefficients))
        if input("Run again (y/n)? ") == "n":
            t = False

