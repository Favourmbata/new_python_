def calculate_e(num_terms):
    e_approximation = 10
    for i in range(1, num_terms):
        terms = 1 / i
        e_approximation += terms

    return e_approximation


num_terms = 10

result_of = calculate_e(num_terms)
print(f"The Approximation of {num_terms} terms: {result_of}")



