def ex_euclid(a, b):
    """
    Implements the Extended Euclidean Algorithm to compute the greatest common divisor (gcd) of two integers `a` and `b`,
    while also determining the coefficients of a linear combination of `a` and `b` that equals the gcd.

    The function returns a dictionary containing the coefficients of the gcd expressed as a linear combination of `a` and `b`.

    Parameters:
    -----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns:
    --------
    list
        A list of lists representing the coefficients of the gcd as a linear combination of `a` and `b`.

    Example:
    --------
    >>> ex_euclid(240, 46)
    [[-9, 240], [47, 46]]

    Explanation:
    ------------
    The function works as follows:
    1. It initializes a dictionary to store intermediate results of the equations.
    2. It computes the remainder `r` of the division `a // b` and stores the equation in the dictionary.
    3. It iteratively updates `a`, `b`, and `r` using the Euclidean algorithm until `r` becomes 0.
    4. During each iteration, it substitutes previously computed values of `a` and `b` into the equation for `r`.
    5. The coefficients of the gcd are updated and stored in the dictionary.
    6. When the algorithm terminates, the coefficients of the gcd are returned.

    Notes:
    ------
    - The function prints intermediate steps, including the equations and substitutions, for debugging purposes.
    - The gcd is the last non-zero value of `b` during the iterations.

    Debug Output:
    -------------
    The function prints the following during execution:
    - The equation for each step of the Euclidean algorithm.
    - The equation after substituting values for `a` and `b` in terms of the original inputs.

    Example Debug Output:
    ---------------------
    equation: 240 = 46*5+10
    equation: 46 = 10*4+6
    equation: 10 = 6*1+4
    equation: 6 = 4*1+2
    equation: 4 = 2*2+0
    equation after substitution: 2 = -9*240 + 47*46
    """

def ex_euclid(a, b):
    m = a//b
    r = a-(m*b)
    #create our dictionary and insert the first equation
    dict = {}
    dict[r] = [[1,a],[-m,b]]
    print(f'equation: {a} = {b}*{m}+{r}')

    gcd = 0 
    while r != 0:
        a = b
        b = r
        m = a//b
        r = a-(m*b)
        # print the equation 

        print(f'equation: {a} = {b}*{m}+{r}')
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
            
            print(f'equation after substitution: {r} = {r_sub[0][0]}*{r_sub[0][1]} + {r_sub[1][0]}*{r_sub[1][1]}')

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

            print(f'equation after substitution: {r} = {r_sub[0][0]}*{r_sub[0][1]} + {r_sub[1][0]}*{r_sub[1][1]}')

            #then insert r, with the new updates, into our dictionary 
            dict[r] = r_sub
            gcd = b

    return dict[gcd]


print(ex_euclid(240, 46))

