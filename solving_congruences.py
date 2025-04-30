"""
This script provides tools to solve systems of linear congruences using the 
Chinese Remainder Theorem. It includes:

- `ex_euclid(a, b)`: Implements the extended Euclidean algorithm and returns 
  a representation of the greatest common divisor (gcd) of `a` and `b` as a 
  linear combination of `a` and `b`.

- `mod_inverse(a, m)`: Computes the modular inverse of `a` modulo `m` using 
  the extended Euclidean algorithm.

- `solve_congruence(a, m1, b, m2)`: Solves a system of two congruences:
     x ≡ a (mod m1)
     x ≡ b (mod m2)
  assuming that `m1` and `m2` are coprime.

The script also includes a command-line interface for interactive input.

Note: The code assumes that moduli are coprime and will prompt for valid input if not.
"""


def ex_euclid(a, b):
    m = a//b
    r = a-(m*b)
    #create our dictionary and insert the first equation
    dict = {}
    dict[r] = [[1,a],[-m,b]]

    gcd = 0 
    while r != 0:
        a = b
        b = r
        m = a//b
        r = a-(m*b)

        #first thing we want to do when we find the new b and r is solve for r, so:
        r_sub = [[1,a],[-m,b]]
        #then we need to check whether a and b can be subsituted for
        if a in dict and b in dict:
            a_sub = dict[a]
            b_sub = dict[b]
            scaled_b_sub = [[pair[0] * r_sub[1][0], pair[1]] for pair in b_sub]

           
            #and then combine with any like terms in a_sub
            #so for this step we gotta combine coefficients of like terms between the subs
            #create a new list of tuples to append to the dict
            comb_step = {}
            for pair in a_sub:
                comb_step[pair[1]] = pair[0]
            
            for pair in scaled_b_sub:
                if pair[1] in comb_step:
                    comb_step[pair[1]] += pair[0]
                else:
                    comb_step[pair[1]] = pair[0]
                
            r_sub = []
            for key, value in comb_step.items():
                r_sub.append([value, key])
            
            #then insert r, with the new updates, into our dictionary 
            dict[r] = r_sub
            gcd = b
    
        
        elif b in dict:
            b_sub = dict[b]
            scaled_b_sub = [[pair[0] * r_sub[1][0], pair[1]] for pair in b_sub]
            #and then combine with any like terms in a_sub
            #so for this step we gotta combine coefficients of like terms between the subs
            #create a new list of tuples to append to the dict
            comb_step = {}
            comb_step[a] = 1
            
            for pair in scaled_b_sub:
                if pair[1] in comb_step:
                    comb_step[pair[1]] += pair[0]
                else:
                    comb_step[pair[1]] = pair[0]
                
            r_sub = []
            for key, value in comb_step.items():
                r_sub.append([value, key])

            #then insert r, with the new updates, into our dictionary 
            dict[r] = r_sub
            gcd = b

    return dict[gcd]

def mod_inverse(a, m):
    result = ex_euclid(a, m)
    
    for coeff, var in result:
        if var == a:
            return coeff % m
        
def solve_congruence(a,m1, b, m2):
    M = m1*m2
    m1_inv = mod_inverse(m2, m1)
    m2_inv = mod_inverse(m1, m2)
    x = a * m2*m1_inv + b*m1*m2_inv
    return x % M

if __name__ == "__main__":
    while True:
        # Prompt the user for input
        a = int(input("Enter the first number: "))
        m1 = int(input("Enter the first modulus: "))
        b = int(input("Enter the second number: "))
        m2 = int(input("Enter the second modulus: "))

        # Check that m1 and m2 are coprime
        eq = ex_euclid(m1, m2)
        if eq[0][0] * eq[0][1] + eq[1][0] * eq[1][1] != 1:
            print("m1 and m2 must be coprime, choose different values")
        else:
            print(f"Solution: {solve_congruence(a, m1, b, m2)}")

        # Ask the user if they want to continue or exit
        cont = input("Do you want to solve another congruence? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Exiting the program.")
            break