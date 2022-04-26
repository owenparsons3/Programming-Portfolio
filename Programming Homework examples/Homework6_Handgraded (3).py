#!/usr/bin/env python
# coding: utf-8

# ## General instructions for filling in a nbgrader Jupyter Notebook
# 
# In each part of this Jupyter Notebook  a  text cell gives you the question that you are looking to answer. Below this you will find a code cell, with further instructions and code, followed by the lines: 
# ```python
# # YOUR CODE HERE
# raise NotImplementedError()
# ```
# 
# This is the place where your solution goes: **DELETE** the line 
# ```python
# raise NotImplementedError()
# ```
# and replace it with your solution. 
# 
# You should also bear in mind the following instructions. 
# 
# - This Notebook is automatically graded. This means that even slight variations in the names of variables will cause your solution to fail. For example, if in the instructions you are told to name your list `divisible` then make sure that you do this. If you name it `Divisible` or `divible` then the autograded tests will fail. Similarly if the instructions say that the time must have  name `t`, this is the name that you must use and **not** `x` or `time` (as again the autograded tests will fail). 
# 
# - The `True` and `False` Booleans start with a **capital** letter. Make sure to always write them in this way. 
# 
# - When you are working on this Notebook, make sure to execute every bit of code that you write and make sure that it works as intended!
# 
# - When you are done, from the menu bar you should run `Kernel`$\rightarrow$`Restart & Run All` to make sure all your code runs without errors before submitting.
# 
# You must also fill in your name and University of Bristol ID in the cell below:

# In[89]:


NAME = "Owen Parsons"
UoB_ID = "1930993"


# # Homework 6 Handgraded 
# 
# ## Marks, Content, and Marking Criteria 
# 
# **Submission.** You should submit this Homework by **12:00 Noon Wednesday 27th April**.
# 
# **Points vs. Marks.**  Below, you will find 5 programming questions, worth a total of 30 points. This Homeworks counts as 15 marks to your final grade. (Hence 2 points are equivalent to 1 mark.)  
# 
# **Content.** The content of this Homework covers material from weeks 8-10 of the course, including two questions on number theory, two questions on techniques used for encryption/cryptography and one question on Dynamic Programming.  
# 
# **Marking Criteria.** The grading of this homework is a two part process. Firstly it is processed by the autograder to check the **correctness** of your computations/results. The grading is then completed by hand. The criteria taken into account during handgrading are as follows. 
# 
# 1. **Structure and clarity.** Is the structure of your code well thought out (e.g. broken down clearly into separate tasks) and has it been written with clarity in mind?  For example  can one get a good idea of what you are doing by a brief look through your code? (One way of improving the clarity of your code is to always use meaningful names for variables.) 
# 2. **Documentation.** Does your code have suitable documentation in the form of comments and is this clearly set out (and in compliance with the indentation rules of Python)? Good documentation of code is informative, to the point and succcinct. 
# 3. **Efficiency.** Is your code computationally efficient?  For example your code should not  compute very large numbers unnecessarily or use very long loops unnecessarily, and should in general not perform a large quantity of  redundant computation (i.e. computing values that you do not need).  
# 4. **Compliance with instructions.** Does your code do what the instructions of the question say? When writing your code you should closely follow the instructions given. For example, if you are told that you may not used a particular python library function then you will lose marks if you do so. 
# 5. **Quality of plotting and print outs.** In some questions you are asked to plot a function or print out data. The result should clearly convey the properties of the function or data involved.  It should also be clearly set out according to the instructions given and admit all the standard embellishments such as labelling, titles and legends. 

# In[90]:


# RUN THIS CELL FIRST (IT WILL BE RUN FIRST DURING AUTOGRADING)
import numpy as np 
import matplotlib.pyplot as plt
import math

# YOU MAY USE FUNCTIONS FROM THE MODULE FROM TUTORIAL 8
from number_theory_lecture_functions import *


# ## Question 1.
# 
# In this question we will use the sum of cubes of divisors of an integer, $$s_3(n) =\sum_{d|n} {d^3}.$$ You may assume without proof that this is a multiplicative function.
# 
# ### Part 1: A function for $s_3$. (1 Pt)
# Write a function `sum_div_cubed(n)` that calculates $s_3(n)$.
# 
# **Note:** You may use functions from lectures and the `number_theory_lecture_functions` module.

# In[91]:


# THIS CODE IS AUTOGRADED AND CHECKED BY HAND FOR CORRECTNESS
# AND COMPLIANCE TO THE GIVEN INSTRUCTIONS

# YOUR CODE HERE
def sum_of_div_cubed_pp(p,e):
    return (p**(e*3+3)-1)//(p**3-1)
sum_div_cubed=make_mult_func(sum_of_div_cubed_pp)


# In[92]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
assert sum_div_cubed(3)==28
assert sum_div_cubed(12)==2044

# THERE ARE HIDDEN TESTS HERE


# ### Part 2: Average value of $s_3$: (2 Pts)
# 
# Let $a(n)$ be the average value of $s_3(k)$ for $k \leq n$, so $$a(n) = \dfrac{ \sum_{k=1}^n{s_3(k)}}{n}.$$
# 
# (a) Plot a graph of $a(n)$ against $n$ for $n$ in the range $[1,10 000]$.
# 
# (b) Plot a graph of $s_3(n)$ against $n$ for $n$ in the range $[1,10 000]$.
# 
# You should ensure your graphs have an appropriate size, line style, title and axis labels.

# In[93]:


# THIS CODE IS HANDGRADED FOR THE QUALITY OF THE GRAPHICAL OUTPUT PRODUCED
# IT IS ALSO CHECKED BY HAND FOR CORRECTNESS AND COMPLIANCE TO INSTRUCTIONS

# YOUR CODE HERE
#create a dictionary of the first 10000 sum(s3(n)) terms
MEMO = dict()
MEMO[1] = sum_div_cubed(1) 
for i in range(2,10001):
    MEMO[i] = MEMO[i-1] + sum_div_cubed(i) 
    
#define a(n)

def a(n):
    return MEMO[n] / n
    
x_values = [i for i in range(1,10001)]
y_values = [a(i) for i in range(1,10001)]

#plt.plot(x_values, y_values)
plt.title('Graph to show a(n) against n')
plt.xlabel('Natural numbers to 10000')
plt.ylabel('a(n)')
plt.plot(x_values, y_values)
plt.show()

#for part b

z_values = [sum_div_cubed(i) for i in range(1,10001)]
#plt.plot(x_values, z_values)
plt.figure(figsize = (6,6))

plt.title('Graph to show s3(n) against n')
plt.xlabel('Natural numbers to 10000')
plt.ylabel('s3(n)')
plt.plot(x_values, z_values)
plt.show()


# ### Part 3: Estimate the limit of $a(n)$. (3 Pts)
# 
# Experimentally show that $\lim_{n\to\infty} \dfrac{a(n)}{n^3}$ exists by demonstrating this graphically. Estimate the value of this limit to $3$ decimal places. Present appropriate graphical and numerical evidence for this estimate.
# 
# Store your estimate in the variable `estimated_limit` in the cell two below.
# 
# **Note 1:** It should be enough to consider values of $n$ up to $10000$.
# 
# **Note 2:** You must explain your reasoning for your estimate. You may do this either using comments in the code cell or by adding a text answer in the markdown cell below.

# In[94]:


# THIS CODE IS HANDGRADED FOR THE QUALITY OF THE GRAPHICAL OUTPUT PRODUCED
# IT IS ALSO CHECKED BY HAND FOR CORRECTNESS AND COMPLIANCE TO INSTRUCTIONS
 
# YOUR CODE HERE


x_values = [i for i in range(1,10001)]
y_values = [a(i)/i**3 for i in range(1,10001)]
plt.title('Graph to show a(n)/n^3 against n')
plt.xlabel('Natural numbers to 10000')
plt.ylabel('a(n)/n^3')
plt.plot(x_values, y_values)
plt.show()


#This graph indicates that a(n)/n^3 does converge, and very quickly to just below 0.3.


# In[95]:


#Numerical evidence: let's look at the last 10 data points
for i in range(9990, 10000):
    print(a(i)/i**3)
# They do all seem close together (around 0.27), however it is not clear if they are converging


#Therefore to check for convergence we will look at the differnce between the n+1 th term, and nth term.
# As if lim as n tends to infinity of (n+1 th term - nth term) = 0, we know we have convergence
#We'll look at the last 4000 data points and plot the differnec of n+1th - nth term

last_4000 = [ a(i)/i**3 for i in range(6000, 10000)]
difference = []
for i in range(3999):
    d = last_4000[i+1] - last_4000[i]
    difference.append(d)
x_values = [i for i in range(3999)]
plt.plot(x_values, difference)
    
#Looking at this graoh it becomes clear that the differnce between consectutive terms is decreasing
#which indicates that a(n)/n^3 is convergent


# To put **your explanation** in the markdown cell below you must double click on it (and replace YOUR ANSWER HERE by your explanation).  

# YOUR ANSWER HERE

# In[96]:


## Fill in your estimate below
estimated_limit = 0.2706390522900406
# YOUR CODE HERE

estimated_limit =round(estimated_limit,3)


# In[97]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# This checks that the value is to three decimal places so we can check the value exactly.
assert estimated_limit == round(estimated_limit,3)

# THERE IS A HIDDEN TEST HERE


# ## Question 2.
# 
# 
# In this question, you will use techniques from computational number theory to demonstrate the flaw in a poorly designed version of the RSA protocol.
# 
# ### Part 1: Testing a function. (2 Pts)
# 
# The **Chinese remainder theorem** states that if two integers $n_1$ and $n_2$ are coprime then for any integers $x_1$ and $x_2$, the pair of congruences:
# 
# $a \equiv x_1 \mod n_1$ and $a \equiv x_2 \mod n_2$,
# 
# have integer solutions for $a$, and all of these solutions are congruent modulo $n_1n_2$. This means that there is a unique solution $x \in [0 , n_1 n_2)$. More generally, if $\{ n_1, n_2, \ldots n_m\}$ is a set of integers where $\gcd(n_i,n_j) = 1$ whenever $i \neq j$ it can be shown that the set of $m$ simultaneuous congruences:
# 
# $a \equiv x_1 \mod n_1$, $a \equiv x_2 \mod n_2$, $\ldots$, $a \equiv x_m \mod n_m$
# 
# has a unique solution in $[0, n_1n_2 \ldots n_m)$.
# 
# It is claimed that the function `many_cases_CRT(remainders,moduli)` in the cell below finds this integer $a$, given input list of the numbers $x_i$ and $n_i$. Design some tests to check that this function does what it is supposed to.
# 
# **Note 1:** You should not rewrite the function. This question is about testing, so we're looking for you to come up with reasonable tests.
# 
# **Note 2:** Your tests should be comprehensive enough to give you confidence that the function works. They should be clearly explained to convince someone reviewing them that the function is good. You may include this explanation either in your code comments or as text in the markdown cell below.
# 
# **Note 3:** You may assume that the function gives `None` on bad input. In marking, we will be looking at how throughly the function was tested on valid inputs.

# In[98]:


def many_cases_CRT(remainders,moduli):
    """Given lists of integers [x1,x2,..xm] and [n1,n2,...nm] (with the latter list pairwise coprime) this return a
    such that a is congruent to x_i modulo n_i for all i. Bad inputs will return None."""
    
    ## Return None if the inputs lists have different lengths:
    if not len(remainders) == len(moduli):
        return None
    ## Return None if non-integers appear:
    for i in remainders+moduli:
        if not isinstance(i,int):
            return None
        
    ## The easiest case is list of length 1:
    if len(moduli) == 1:
        return remainders[0] % moduli[0]
    
    ## Check if the moduli are not coprime and return None if it fails:
    N = 1
    for n in moduli:
        N *= n
    for n in moduli:
        if not gcd(N//n,n) == 1:
            return None
        
    ## If all the input is OK, we can solve this recursively.
    nm = moduli[-1]
    xn = remainders[-1]
    (g,a,b) = gcd_ext(nm,N//nm)
    return ( xn*b*N//nm + nm*a*many_cases_CRT(remainders[:-1],moduli[:-1]) ) % N


# In[99]:


# THIS CODE IS HANDGRADED ACCORDING TO THE DESIGN OF YOUR TESTS - WOULD THEY CONVINCE 
# SOMEONE THAT THE FUNCTION IS GOOD? - AND THE EXPLANATION THAT YOU PROVIDE

## DESIGN AND RUN YOUR TESTS IN THIS CELL. YOU MAY USE THE CELLS BELOW IF MORE SPACE IS NEEDED.

# MY APPROACH TO THIS QUESTION:
# In order to test if this function works I first devise a test which tells me is a is congruent to x mod n
# Then using this test, I test the many_cases_CRT function on randomly generated inputs

#to test if a is congruent to xi mod ni for all i, we define a test function:
from random import randint

def test(a,remainders, moduli):
    #check a is less than n1n2...nm:
    product = 1
    for n in moduli:
        product *= n
    if a >= product:
        print('Test failed')
        
    else:      
        length = len(remainders)
        for i in range(length):
            if a % moduli[i] - remainders[i] % moduli[i] != 0: 
                #which tests if a is congruent to xi mod ni
                print('Test failed')
                break
            else:
                return None
        
# so if our test function returns nothing, we know a is the correct solution

# Now use this function to test the many_cases_CRT function with an example
# choose 3 moduli which are coprime- 7,11,15
#choose 3 remianders -40 , 5, 34
# attain a from many_cases_CRT:
a = many_cases_CRT([40, 5, 34], [7,11,15])
print(a)
#use our test function to see if a is right:
test(a, [40, 5, 34], [7,11,15])

#after running this, we have 544 as a, and no problems running the test function. So
# many_cases_CRT works for this example

# However this is just 1 example. Better to check multiple and randomly



# In[100]:


# So we define a test2 which tests the function on many more imputs
import random
def test2():
    # x is a list of prime numbers from 1-100, which will be the basis for our moduli list
    x= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    #our list moduli will comprise a random number of  r  values 
    r = randint(1,len(x))
    moduli_list = []
     # randomly chosen y value
    while len(moduli_list)  <= r:
        p = random.choice(x)
        if p not in moduli_list:
            moduli_list.append(p)
    # so we have our randomly generated moduli list
    # create a random remainders list of same length
    remainders_list = []
    for i in range(len(moduli_list)):
        p = randint(-1000,1000)
        remainders_list.append(p)
    #use many_cases_CRT to find a
    a = many_cases_CRT(remainders_list, moduli_list)
    
    print('a is equal to ' + str(a))
    print('Given remainder input ' , remainders_list)
    print('And moduli input ', moduli_list)
    
    #now check a satisfies our tests:
    if test(a, remainders_list, moduli_list) == None:
        print('Test passed for this try')
    else:
        print('Test failed')
    
#now we run test2 for a few iterations and see what we get
n = 3
for i in range(n):
    test2()
    
# After running this test (and we can change our value of n), we see that all the tests have been passed
#Given random (enough) entries of moduli and remainders
#So I conclude many_cases_CRT is an effective function for finding a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# To put **your explanation** in the markdown cell below you must double click on it (and replace YOUR ANSWER HERE by your explanation).  

# YOUR ANSWER HERE

# ### Part 2: Finding a power of a message in a broadcast attack: (2 Pts)
# 
# 
# In this question, you will use ideas from number theory to break a poor attempt at encryption. Assume that an adversary has sent a message to multiple, independent agents. To try to make it secure, each agent has their own RSA public key. To make encyption computationally easier, they all use the same public exponents but each has generated different 1024-bit primes. This means we can make the following assumptions:
# 
# 1. The same message has been sent to multiple agents;
# 2. Each of those agents has chosen the same small public exponent $e_i=5$ (but generated different primes);
# 3. The message is a large integer (with between 300 and 600 digits) We will call this $m$.
# 
# We suppose that we have intercepted 8 messages. Therefore the information we have is a list of 8 packets of data of the form `( (N_i,e_i) , ciphertext_i )`. In each tuple, the first element is another tuple containing the public key and the second element is the ciphered message sent to that agent. We now retrieve this  data from the file `data_packets_saved`.
# 
# Thus, for example, `ciphertext_1` is the message $m$ after encryption using the key `(N_1,e_1)`.
# 
# Run the cells below to import this data from the `data_packets_saved` module.

# In[101]:


# The function peek_at_file is in fact already imported in the import cell above
from number_theory_lecture_functions import peek_at_file
# Look at first 32 lines of data_packets_saved.py of there are that many... 
peek_at_file("data_packets_saved.py", 32) 


# We now import this data.

# In[102]:


from data_packets_saved import N, e, ciphertext
data_packets = [ ((N[i], e[i]), ciphertext[i]) for i in range(8)]


# We can also look at each data packet individually.

# In[103]:


# One of them:
agent = 6
print("For agent {}...\n".format(agent))
print("N =")
print(data_packets[agent][0][0],"\n")
print("e =", data_packets[agent][0][1],"\n")
print("ciphertext = ")
print(data_packets[agent][1])


# **Step 1: Find $m^5$.** If the message is a large integer $m$, then the cipher sent to the agent with public key $(N_1,5)$ is $m^5 \bmod N_1$. Reusing the same small public exponents means we know $m^5$ modulo each encryption modulus. Recall that $m < N_1$ but of course, $m^5$ is probably larger than $N_1$. Use a suitable combination of the ciphertexts to find $m^5$ modulo $L$ for some large number $L > m^5$.
# 
# Store the value for $m^5$ in the variable `m_5`.

# In[104]:


# THIS CODE IS BOTH AUTOGRADED AND HANDGRADED ACCORDING TO MARKING CRITERIA 1-4

# YOUR CODE HERE
list_of_remainders = []
list_of_moduli = []
for i in range(8):
    list_of_remainders.append(data_packets[i][1])
    list_of_moduli.append(data_packets[i][0][0])

m_5 = many_cases_CRT(list_of_remainders, list_of_moduli)
print(m_5)


# **Step 2:** Explain why this number must be the integer $m^5$.
# 
# **Note.** You should put **your explanation** in the markdown cell below. To do this you must double click on it and replace YOUR ANSWER HERE by your explanation.  

# YOUR ANSWER HERE

# In[79]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# We check the value of m_5
assert m_5 >0
# THERE IS A HIDDEN TEST HERE


# ### Part 3: Recovering the message. (2 Pts)
# In theory, we can recover the message by taking the fifth root. However, this number is so large you'll get an overflow error if you try to convert it to a float, so you will not be able to just use `m_5**0.2`. Instead, use the Newton-Raphson method to recover the original message. For convenience, the code from week 4's lecture is copied below but you will have to adapt it and decide what the correct inputs to use are.
# 
# Store the message (as a large integer, with between 300 and 600 digits) in the variable `message`.
# 
# **Note 1:** Remember that we know the answer is an integer. This means it is safe to use a fairly large tolerance (such as simply $1$) in Newton-Raphson.
# 
# **Note 2:** You will need to adapt the code for Newton-Raphson to avoid problems with overflow. The overflow will occur when python attempts to convert into a floating point number, for example during division.

# In[80]:


## This is the code from week 4 for the Newton-Raphson method. 
## This cell is read-only - you can copy and paste code from here. 

def Newton_Raphson(input_fun, input_deriv, xguess, tolerance, verbose=False):

    # The starting point for xsol is our initial guess 
    xsol = xguess
    # Ensure that delta is large enough for our while loop to start correctly
    delta = 10 * tolerance

    # Loop to repeatedly update xsol until we reach the tolerance
    while abs(delta) > tolerance:
        # Compute the estimate of delta using the tangent
        delta = - input_fun(xsol)/input_deriv(xsol)
        # Now update our approximation to the root xsol 
        xsol = xsol + delta
        # When verbose == True we print the value of our approximation
        # during every iteration of the while loop
        if verbose == True: 
            print(xsol)

    # Our function returns our final approximation 
    return xsol  


# In[83]:


# THIS CODE IS BOTH AUTOGRADED AND HANDGRADED ACCORDING TO MARKING CRITERIA 1-4
#same code as above except we cchange / to // to avoid an overflow error
def Newton_Raphson(input_fun, input_deriv, xguess, tolerance, verbose=False):

     
    xsol = xguess
    
    delta = 10 * tolerance

    
    while abs(delta) > tolerance:
        
       
        delta = - input_fun(xsol)//input_deriv(xsol)
        
        xsol = xsol + delta
        
        if verbose == True: 
            print(xsol)

    # Our function returns our final approximation 
    return xsol  

guess_sol = 10**int(len(str(m_5))/5)

def input_fun(x):
    return x**5 - m_5
def input_deriv(x):
    return 5*x**4

#call  Newton_Raphson
Newton_Raphson(input_fun, input_deriv, guess_sol, 1, verbose=False)


# In[84]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE


# In[85]:


# THERE IS A HIDDEN TEST HERE


# ## Question 3: Coding and Decoding Techniques 
# 
# The purpose of this question is to define coding and decoding functions in precisely the same way as in Lecture 9.2 BUT using ternary representation instead of binary representation. You will work with characters whose ASCII number is in the range $0$ to $255$ (generated by `range(0,256)`). In the lecture notes we work with the $8$-bit binary representation of the ASCII number of a character. Here you will work with the $6$-digit ternary representation of the ASCII number using the zero character `'0'` to pad out numbers of less than $6$ digits. (Accordingly `'000100'`, `'001101'`, `'002210'` and `'100012'` are the ternary string representations of the characters `'\t'` (the tab character) `'%'`, `'K'` and `'ø'` respectively.) 
# 
# ### Part 1: coding characters as ternary strings of fixed length (1 Pt) 
# 
# Design a function `char_to_ternary` that, given character `c` (whose ASCII number is in the specified range) as input, outputs the $6$-digit ternary (string) representation of `c`.
# 
# **Note 1.** You should use the function `base_repr` from the `numpy` library to convert an integer (in decimal) into ternary string representation and the function `int` to convert such a string back to an integer (in decimal). For example `np.base_repr(50,base=3)` returns the string `'1212'` whereas `int('1212',3)` returns `50`. (By hand $1 \cdot 3^3 + 2 \cdot 3^2 + 1 \cdot 3^1 + 2 \cdot 3^0 = 27 + 18 + 3 + 2 = 50$.) Note that for  Part 1 you only need `np.base_repr`, however in Part 4 you will need both `np.base_repr` and `int`. 
# 
# **Note.** You can assume that the input is a character whose ASCII number is in the range $0$ to $255$. I.e. no need to handle incorrect input.

# In[7]:


# THIS CODE IS AUTOGRADED AND CHECKED BY HAND FOR CORRECTNESS
# AND COMPLIANCE TO INSTRUCTIONS
def char_to_ternary(c): 
    x = ord(c)
    tern_string = np.base_repr(x,base=3)    # c as a ternary string
    num_zeros = 6 - len(tern_string)     # The number of zeros needed to pad out tern-string
    for i in range(num_zeros):           # Now pad out tern_string with num_zeros many zeros
        tern_string = '0' + tern_string  # to obtain the 6-bit ternary representation
    return tern_string  


# In[8]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE


# In[9]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# In each of the tests (including 5hidden tests) the inputs are characters whose 
# ASCII number is in the interval [0,255]
assert char_to_ternary('\t') == '000100'
assert char_to_ternary(' ') == '001012'
assert char_to_ternary('#') == '001022'
assert char_to_ternary('@') == '002101'
assert char_to_ternary('K') == '002210'
assert char_to_ternary('Ä') == '021021'
assert char_to_ternary('à') == '022022'
assert char_to_ternary('ý') == '100101'
# THERE ARE HIDDEN TESTS HERE


# ### Part 2: formatting a table of results (1 Pt)
# 
# Design a function `make_ternay_table` that, given integer inputs `lower` $\le$ `upper` in the interval $[0,255]$ (i.e. including both 0 and 255) prints out a table whose first column consists of integers $n$ in the interval `[lower,upper]`, whose second column consists of the characters (as strings) whose ASCII numbers are the integers in the first column, and whose third column consists of the 6-digit ternary representations of the characters of the second column as computed by your function `char_to_ternary`. The table should have a header and be formatted so that each column is (left) aligned. (There are a number of bizarre characters which mess up the alignment. The function calls `make_ternary_table(32,126)` and `make_ternary_table(174,255)` should however create perfectly aligned tables.) For example the function call 
# ```python
# make_ternary_table(40,50) 
# ```
# should print out the following (or a very similar) table. 
# ```
# ASCII    Character    Ternary Code
# =====    =========    ============
# 40       (            001111 
# 41       )            001112 
# 42       *            001120 
# 43       +            001121 
# 44       ,            001122 
# 45       -            001200 
# 46       .            001201 
# 47       /            001202 
# 48       0            001210 
# 49       1            001211 
# 50       2            001212 
# ``` 
# Your function should return the object `None`. 
# 
# **Note.** You can assume that the input consists of integers `lower` $\le$ `upper` belonging to the interval $[0,255]$. I.e. there is no need to handle incorrect input. 

# In[10]:


# THIS CODE IS HANDGRADED FOR THE QUALITY OF THE PRINTOUT PRODUCED
# IT IS ALSO CHECKED BY HAND FOR CORRECTNESS AND COMPLIANCE TO INSTRUCTIONS
def make_ternary_table(lower,upper): 
    print("ASCII   Character   Ternary Code  ")
    print("=====   =========   ============   ")

    for n in range(lower, upper +1):
        n_char = chr(n)
        n_tern = char_to_ternary(n_char)
        
        print("{:7s} {:11s} {:11s} ".format(str(n),n_char,n_tern))


# In[11]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE


# In[12]:


# THIS CELL CONTAINS TWO HIDDEN TESTS OF YOUR FUNCTION
# PRODUCING THE PRINTOUTS THAT WILL BE HAND GRADED. 


# ### Part 3: coding text using ternary representation (1 Pt)
# 
# Design a function `ternary_convert_to_integer` that behaves like `convert_to_integer` from Lecture 9.2 but uses `char_to_ternary` instead of `char_to_byte`. I.e. `ternary_convert_to_integer` takes as input a string `a_text` and outputs a unique (decimal) integer encoding of this string, using for the encoding  the ternary representation from above (instead of the binary representation used in the lecture).
# 
# **In more detail...**  Your function `ternary_convert_to_integer` should encode the string `a_text`  using the $6$ digit ternary string representation of each symbol in the message. To do this it should simply concatenate the ternary string representations with a leading '1'. It should then  convert this ternary string into a (decimal) integer and return this integer.  
# 
# **Note.** You can assume that the input is a string containing characters with ASCII numbers in the range $[0,255]$. I.e. there is no need to handle incorrect input. 

# In[13]:


# THIS CODE IS AUTOGRADED AND CHECKED BY HAND FOR CORRECTNESS
# AND COMPLIANCE TO INSTRUCTIONS
def ternary_convert_to_integer(a_text): 
 
    tern_string = '1' #create our tern string which starts with a 1 since we don't want to start with a 0
    for letter in a_text:   # for each character in the text, convert the character into a ternary string and add to tern_string
        tern_string = tern_string + char_to_ternary(letter)
    return int(tern_string,3)  #convert this tern_string to an integer


# In[14]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE


# In[15]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# In each of the tests (including 2 hidden tests) the input is a string comprising 
# a message written in a European language.(So  all characters used have ASCII number
# in the interval [0,255])
message_one = "The cloud of electrons provides the outward face of the atom."
message_two = "Nous avons réussi à communiquer en secret.\n"
message_two += "Mais faites attention: il y a des espions dans les environs."
print("Message one")
print("===========")
print(message_one,"\n")
print("Message two (in French)")
print("=======================")
print(message_two,"\n")
print("Now testing whether your function encodes these ") 
print("messages correctly...\n",)
# The integers corresponding to each of the above messages
ternary_code_one = int('''
47186584973596411277435264150735389413015012
13394743702063128360294178236140716955910733
61287682742240940535744150831217061307097989
2096296549982729635774824628336863767118044
'''.replace('\n',''))
ternary_code_two = int('''
803828640295490765398510740790275500778736138
778897190685944020041029984097010749512889845
259823286944535407380069606649472559954749879
999324695779488765398653019764558183607100303
821597720793473586800869829424002302619805055
090947006039244379128311273488957029351595818
4898038659496061634116088
'''.replace('\n',''))
# Testing your output
assert ternary_convert_to_integer(message_one) == ternary_code_one
assert ternary_convert_to_integer(message_two) == ternary_code_two
print("Visible tests successfully passed.")
# THERE ARE HIDDEN TESTS HERE


# ### Part 4: decoding integers to text (1 Pt)
# 
# Design a function `ternary_convert_to_text` which takes as input a positive integer and returns the string (i.e. a piece of text)  that this number is a code for under the method implemented by your function `ternary_convert_to_integer`. 
# 
# **Note.** You can assume that the input is a positive integer which is the encoding of a string generated by `ternary_convert_to_integer`. I.e. there is no need to handle incorrect input. 

# In[16]:


# THIS CODE IS AUTOGRADED AND CHECKED BY HAND FOR CORRECTNESS
# AND COMPLIANCE TO INSTRUCTIONS
def ternary_convert_to_text(n): 
    tern_string = np.base_repr(n,base=3)  #convert integer into a tern_string
    text = '' 
    length = len(tern_string)
    for i in range(1,length,6):  # start from 1, so we miss the dummy 1 we added before
        ternary_string = tern_string[i:i+6]    # then divide the string into blocks of 6, each block conatins a letter
        text += chr(int(ternary_string,3))    #add to text, each letter we find
    return text


# In[17]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE


# In[18]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# In each of the tests (including 2 hidden tests) the input is a 
# positive integer. Note that we use message_one and message_two 
# from the testing area of Part 3 above. We start with the definition 
# of these messages (repeated from above) and their decimal encodings 
message_one = "The cloud of electrons provides the outward face of the atom."
message_two = "Nous avons réussi à communiquer en secret.\n"
message_two += "Mais faites attention: il y a des espions dans les environs."
ternary_code_one = int('''
47186584973596411277435264150735389413015012
13394743702063128360294178236140716955910733
61287682742240940535744150831217061307097989
2096296549982729635774824628336863767118044
'''.replace('\n',''))
ternary_code_two = int('''
803828640295490765398510740790275500778736138
778897190685944020041029984097010749512889845
259823286944535407380069606649472559954749879
999324695779488765398653019764558183607100303
821597720793473586800869829424002302619805055
090947006039244379128311273488957029351595818
4898038659496061634116088
'''.replace('\n',''))
print("Message one after coding and successful decoding should be...")
print("===========================================================")
print(message_one,"\n")
print("Message two after coding and successful decoding should be...")
print("===========================================================")
print(message_two,"\n")
print("Now testing whether your function does the decoding part") 
print("of this correctly...\n",)
# Now we test that your function does this for (i.e. decodes correctly) the 
# integers dec_code_one and dec_code_two from the testing area of part (b)
assert ternary_convert_to_text(ternary_code_one) == message_one
assert ternary_convert_to_text(ternary_code_two) == message_two
# Note also that the functions ternary_convert_to_integer and ternay_convert_to_string
# are inverses of one another. Here is a quick test of that...
print("And that your two functions are inverses of one another...\n")
assert ternary_convert_to_text(ternary_convert_to_integer(message_one)) == message_one
assert ternary_convert_to_integer(ternary_convert_to_text(ternary_code_one)) == ternary_code_one
print("Visible tests successfully passed.")
# THERE ARE HIDDEN TESTS HERE


# ## Question 4: Cryptography - the Affine Cipher
# 
# Suppose that $m$ is a positive integer, $\mathit{alph}$ is an ordered alphabet of $m$ characters, and
# $\iota : \mathit{alph} \rightarrow \{0,\dots,m-1\}$ is a bijection mapping each letter to its position
# (i.e$.$ ranging from $0$ to $m-1$) in $\mathit{alph}$. Then, given integers $u \in \{1,\dots,m-1\}$ and
# $v \ge 0$ the **affine encipher** map $c_f: \mathit{alph} \rightarrow \mathit{alph}$ induced by the function
# 
# $$                      
# f(x) \,=\, ux + v \;(\mbox{mod}\; m)
# $$
# 
# is defined by $c_f(w) = \iota^{-1}\big(f(\iota(w)) \big)$. In other words $c_f(w)$ is the character whose position
# is the image of the position of the character $w$ under the map $f$. Now, provided that $u$ and $m$ are coprime
# it is easy to see that $f$ is a bijection on the set $\{0,\dots,m-1\}$ with inverse 
# 
# $$                      
# f^{-1}(x) \,=\, u^{-1}(x - v) \;(\mbox{mod}\;m) 
# $$
# 
# where $u^{-1}$ is the multiplicative inverse of $u$ modulo $m$ (i.e$.$ $u^{-1}u = 1 \;(\mbox{mod}\; m)$). In this case
# the **affine decipher** map $d_f: \mathit{alph} \rightarrow \mathit{alph}$ induced by $f$
# is defined by $d_f(w) = \iota^{-1}\big(f^{-1}(\iota(w)) \big)$.
# 
# Your **task in this question** is to develop a function which is able to perform both the process of enciphering and the process of deciphering a text/string using the affine cipher. To do this you will first develop your own functions to generate dictionaries to represent the enciphering and deciphering maps.   
# 
# **Note 1.** A good way to represent an alphabet in python is to use a string containing the characters of the alphabet $\mathit{alph}$. This means that we can implement $\iota: \mathit{alph} \rightarrow \{0,\dots,m-1\}$ 
# as the function that maps a character to its index in the string.  
# 
# **Note 2.** For simplicity we will assume that the length of our alphabet $m$ is a **prime number** (since this implies that, however we choose $u \in \{1,\dots,m-1\}$, the function $f$ is a bijection so  that $f^{-1}$ is defined). 
# 
# **Note 3.** We will use the two alphabet strings `ALPH_1` and `ALPH_2` (and a further alphabet `ALPH_3` of length 97 in the hidden tests) defined below of lengths 29 and 59 respectively. To see these alphabets you should run each of the cells below. Notice also that we are using `ALPH_1` and `ALPH_2` as global variables to be used in your work below. (Therefore these cells need to be run before the testing implemented below.) 
# 

# In[19]:


# DEFINITION OF THE FIRST ALPHABET 
import string
ALPH_1 = string.ascii_lowercase + ",. "
print("ALPH_1 is of length: m = {}".format(len(ALPH_1)))
print("It is defined to be the string below.")
print("Note that the last character is the space character.")
ALPH_1


# In[20]:


# DEFINITION OF THE SECOND ALPHABET 
ALPH_2 = string.ascii_letters + ",.;:?! " 
print("ALPH_2 is of length: m = {}".format(len(ALPH_2)))
print("It is defined to be the string below.")
print("Note that the last character is the space character.")
ALPH_2


# **Note 4.** As mentioned above we will represent encipher and decipher maps using dictionaries. Accordingly, for a given alphabet $\mathit{alph}$ of length $m$ we define the **encipher dictionary** induced by integers $u \in \{1,\dots,m-1\}$ and $v \ge 0$ to be the dictionary consisting of the $m$ many key, value pairs (`w`,$c_f$(`w`)). For example, using alphabet `ALPH_1` (so that $m = 29$) , and $u = 2$, $v = 3$ the encipher dictionary is of the form 
# 
# ```Python
# {'a': 'd', 'b': 'f', 'c': 'h', ... , 'z': 'y', ',': ',', '.': ' ', ' ': 'b'} .
# ```
# 
# Likewise we define the corresponding **decipher dictionary** induced by $u$, $v$ to be the dictionary consisting of the $m$ many key, value pairs $(w,d_f(w))$.
# 
# **Remark.** Remember that the encipher map is $f(x) \,=\, ux + v \;(\mbox{mod}\; m)$. Thus, using `ALPH_1` and  $u = 2$, $v = 3$ we have the following. 
# - $f(0) = 2 \times 0 + 3 \;(\mbox{mod}\; m) = 3$. Thus $c_f$(`'a'`) $= \iota^{-1}\big(f(\iota$(`'a'`)$) \big) = \iota^{-1}\big(f(0) \big) = \iota^{-1}\big(3) \big) =$ `'d'`. 
# - $f(1) = 2 \times 1 + 3 \;(\mbox{mod}\; m) = 5$. Thus $c_f$(`'b'`) $= \iota^{-1}\big(f(\iota$(`'b'`)$) \big) = \iota^{-1}\big(f(1) \big) = \iota^{-1}\big(5) \big) =$ `'f'`.
# 
# This corresponds to the fact that for `w` = `'a'` we have (`w`,$c_f$(`w`)) = (`'a'`,`'d'`) and when `w` = `'b'` we have (`w`,$c_f$(`w`)) = (`'b'`,`'f'`) in the encipher dictionary above. (And so on for the other characters in 
# `ALPH_1`.) 

# **Note 5.** One of the ways of generating a decipher dictionary in Part 2 requires a function to compute the modular inverse, i.e. a function that takes as input the pair $u$, $m$ with $m$ a prime and $u$ an integer in the set $\{1,\dots,m-1\}$ and returns the inverse of $u$ modulo $m$ (i.e$.$ $u^{-1}$ (mod $m$)). Luckily the function `modular_inverse` defined in lectures will do the job for us. So let's import it.

# In[21]:


# Function modular_inverse for use in Part 2. 
from number_theory_lecture_functions import modular_inverse
help(modular_inverse)


# OK. That's precisely what we need. Let's run a few checks. 

# In[22]:


assert modular_inverse(3,7) == 5
assert modular_inverse(12,37) == 34
assert modular_inverse(32,59) == 24
assert modular_inverse(14,29) == 27
assert modular_inverse(10,43) == 13
print("The checks were successful")
# To persuade yourself run a few more checks or test the above assertions. E.g. 
34 * 12 % 37 


# ### Part 1: generating an encipher dictionary (2 Pts)
# 
# Design a function `affine_encipher` that takes as inputs a string `alph` of length $m$ representing an alphabet, and integers `u` $\in \{1,\dots,m-1\}$ and  `v` $\ge 0$ and returns the encipher dictionary corresponding to `alph`, induced by `u` and `v`.
# 
# **Note.** In this and the following parts of the present question you can assume that the inputs to the function are as described. **In other words, in each of Parts 1-3 of this Question (i.e. Question 4) you do not  need to handle incorrect input.** 

# In[23]:


# THIS CODE IS BOTH AUTOGRADED AND HANDGRADED ACCORDING TO MARKING CRITERIA 1-4

def affine_encipher(alph,u,v):
    MEMO = dict()
    m = len(alph)
    for i in range(m):
        i_gets_sent_to  = (i *u + v) % m  # applying f(i)
        
        MEMO[alph[i]] = alph[i_gets_sent_to]  #store the new character for i in MEMO
    return MEMO


# In[24]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE
# For example some randomised checking... 


# In[25]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# In each of the tests (including the hidden tests) the first input is an
# alphabet of length m (say) where m is prime, the second input is an 
# integer in {1,...,m-1} and the third input is a non-negative integer. 
ALPH_1 = string.ascii_lowercase + ",. "
ALPH_2 = string.ascii_letters + ",.;:?! "
assert affine_encipher(ALPH_1,1,0)[' '] == ' '
assert affine_encipher(ALPH_1,22,8)['c'] == 'x'
assert affine_encipher(ALPH_2,42,63)[','] == 'f'
assert affine_encipher(ALPH_2,54,9)['H'] == 'v'
# THERE ARE HIDDEN TESTS HERE


# ### Part 2: generating a decipher dictionary (2 Pts) 
# 
# Write a function `affine_decipher` that takes as inputs a string `alph` of length $m$ representing an alphabet, and integers `u` $\in \{1,\dots,m-1\}$ and  `v` $\ge 0$  and returns the decipher dictionary corresponding to `alph`, induced by by `u` and `v`. 
# 
# **Note.** This function can be defined in at least two different ways. (You only have to come up with one correct definition.) One of these definitions needs the function `modular_inverse`. So, to make sure that it is 
# available we import it below (in case you have not run the other import cell above). 

# In[26]:



# THIS CODE IS BOTH AUTOGRADED AND HANDGRADED ACCORDING TO MARKING CRITERIA 1-4
from number_theory_lecture_functions import modular_inverse

def affine_decipher(alph,u,v):
    dict1 = {}
    m = len(alph)
    u_inverse = modular_inverse(u,m) # find the modular inverse of u
    for c in alph:
        i = alph.index(c)  
        f_inverse = (u_inverse*(i-v))%m  #apply the inverse map f
        i_inverse = alph[f_inverse]  
        dict1[c] = i_inverse   #replace c with i_inverse
    return dict1


# In[27]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE
        
        


# In[28]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# In each of the tests (including the hidden tests) the first input is an
# alphabet of length m (say) where m is prime, the second input is an 
# integer in {1,...,m-1} and the third input is a non-negative integer. 
ALPH_1 = string.ascii_lowercase + ",. "
ALPH_2 = string.ascii_letters + ",.;:?! "
assert affine_decipher(ALPH_1,1,0)['r'] == 'r'
assert affine_decipher(ALPH_1,18,3)['.'] == 'l'
assert affine_decipher(ALPH_2,12,90)['n'] == 'C'
# THERE ARE HIDDEN TESTS HERE


# ### Part 3: enciphering and deciphering (2 Pts) 
# 
# Design a function `affine_translate` that takes as inputs a string `alph` of length $m$ representing an alphabet, integers  `u` $\in \{1,\dots,m-1\}$ and `v` $\ge 0$, a string `message`, and a boolean variable `decrypt`. 
# 
# - If `decrypt` is  `False` your function should implement `affine_encipher(alph,u,v)` and use the resulting dictionary to encrypt the string `message` according to the map $c_f$ described above. (I.e$.$ each character `w` in `message` is mappped to $c_f$(`w`) to form the encrypted message.) Your function should return the encrypted message. 
# - If `decrypt` is  `True` your function should implement `affine_decipher(alph,u,v)` and use the resulting dictionary to decrypt the string `message` according to the map $d_f$ described above. (I.e$.$ each character `w` in `message` is mappped to $d_f$(`w`) to form the decrypted message.) Your function should return the decrypted message. 

# In[29]:


# THIS CODE IS BOTH AUTOGRADED AND HANDGRADED ACCORDING TO MARKING CRITERIA 1-4
def affine_translate(alph,u,v,message,decrypt):
    if decrypt == False:
        dicte = affine_encipher(alph,u,v)
        
        #turn message into a list so we can operate on it
        listy = []
        for i in message:
            listy.append(i)
            # change the characters to message to what they are assigned by affine_encipher
        for i in range(len(listy)):
            listy[i] = dicte[str(listy[i])]
        # turn listy back into a string
        message = ''
        for i in listy:
            message = message + i
        #print(listy, message)
        return message
    if decrypt == True:
        dictd = affine_decipher(alph,u,v)
        listy = []
        for i in message:
            listy.append(i)
            # change the characters to message to what they are assigned by affine_encipher
        for i in range(len(listy)):
            listy[i] = dictd[str(listy[i])]
        # turn listy back into a string
        message = ''
        for i in listy:
            message = message + i
        #print(listy, message)
        return message
        


# In[30]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE
message = 'lets creat my own test'
#lets encipher it
ALPH_1 = string.ascii_lowercase + ",. "
message2 = affine_translate(ALPH_1,34,68, message,False)
#now decrypt it
affine_translate(ALPH_1,34,68, message2,True)


# In[31]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# In each of the tests (including the hidden tests) the first input is an 
# alphabet of length m (say) where m is prime, the second input is an integer 
# in {1,...,m-1}, the third input is a non-negative integer, the fourth
# input is a string with letters belonging to the alphabet (i.e. the 
# first input) and the last input is either True or False
ALPH_1 = string.ascii_lowercase + ",. "
ALPH_2 = string.ascii_letters + ",.;:?! "
message1 = '''as will be seen later on, pygmalion needs, not a preface, but a sequel,
which i have supplied in its due place. the english have no respect for
their language, and will not teach their children to speak it.'''.replace('\n',' ')
enc_message1 = '''xhl,dkklgnlhnnflkxtnylrfqlaviwxkdrflfnnbhqlfrtlxlaynzxsnqlgctlxlhnmcnkql,u
dsuldluxonlhcaakdnbldfldthlbcnlakxsn ltunlnfikdhuluxonlfrlynhanstlzryltundylk
xficxinqlxfbl,dkklfrtltnxsultundylsudkbynfltrlhanx.ldt '''.replace('\n','')
print("The message is: \n'{}'".format(message1),"\n")
print("The encrypted message should be: \n'{}'".format(enc_message1),"\n")
print("The decrypted message should be: \n'{}'".format(message1))
assert affine_translate(ALPH_1,12,23,message1,False) == enc_message1
assert affine_translate(ALPH_1,12,23,enc_message1,True) == message1
# THERE ARE HIDDEN TESTS HERE


# # Question 5: Stamps
# 
# Stamps are available in various denominations (in pence), for example
# 
# 1,5,66,85,100.
# 
# Suppose that we have an unlimited number of stamps of each denomination available, and we want to make a given amount, say 138, with the minimum possible number of stamps.  E.g. we could use 
# 
# 138 = 100+5+5+5+5+5+5+5+1+1+1      (11 stamps)
# 
# but it would be better to use
# 
# 138 = 66+66+5+1      (4 stamps).
# 
# (As this example shows, it is not always best to greedily make up the amount starting with the biggest stamp denominations.)

# ### Part 1 (3 Pts)
# 
# Write a function `min_stamps(x,den)` that returns the minimum number of stamps needed to make the amount `x`, where `den` is a tuple of the available denominations of stamps.  Assume that all amounts are postive integers, and that `den` includes `1`, which guarantees that it is possible to make every amount.  
# 
# Your function should not take more than a fraction of a second to run on examples like the ones below.
# 
# Suggested approach: use dynamic programming.  For each denomination less than or equal to `x`, try using one stamp of that denomination, and consider the remaining amount.  You might want to store the results for the resulting subproblems in a list.  Use memoization to make it fast.  
# 
# In your final answer, make sure you initialize any required global variables (such as the memoization dictionary) before defining the function, so that they are ready to be used.  Your function needs to be able to work for different choices of the denominations `den` without re-initializing.  This means that both `x` and `den` should be incorporated into the dictionary keys.

# In[32]:


# THIS CODE IS BOTH AUTOGRADED AND HANDGRADED ACCORDING TO MARKING CRITERIA 1-4

MEMO=dict()             # suggested initialization

def min_stamps(x,den):  # minimum stamps needed to make amount x using denominations den    
    global MEMO
    #we create a dictionary of 'large' numbers and with first entry 0. Large numbers so we can 
    #update the dictionary later
    for n in range(x+1):
        MEMO[n] = float('inf')
    MEMO[0]=0  # as we need 0 stamps to make 0
    
    #for each denomication we traverse our dictionary up to d <= i and for each i, we see if d
    # if the preferable denomination to use which gives us the least stamps. If it is, we update 
    #the dictionary by MEMO[i-d] + 1, since MEMO[i-d] is already known, and +1 because we use
    #one stamp with d
    for d in den:
        for i in range(x+1):
            if d <= i:
                MEMO[i] = min(MEMO[i], MEMO[i -d] +1)
    return MEMO[x]


# In[33]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE
x = 138
den = [1,5,66,85,100]
min_stamps(x,den)


# In[34]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# you should do your own further testing in the cell above 

for i in range(1,11):
    print('Minimum stamps to make',i,'using',(1,3,4),':',min_stamps(i,(1,3,4)))

assert min_stamps(138,(1,5,66,85,100))==4

print('Minimum stamps to make 999 using (1,5,66,85,100):',min_stamps(999,(1,5,66,85,100)))

# HIDDEN TESTS BELOW


# ### Part 2 (2 Pts) 
# Write an additional function `sol(x,den)` that returns a solution: a combination of stamps of the minimum size, in the form of a list or tuple of the required stamp denominations, such as `(1,5,66,66)`. 

# In[35]:


# THIS CODE IS BOTH AUTOGRADED AND HANDGRADED ACCORDING TO MARKING CRITERIA 1-4
def sol(x,den):
    global MEMO
    for i in range(x+1):
        MEMO[i] = float('inf')  #create an array of length x with big numbers
    MEMO[0] = 0  
    
    min_num_stamps = [[] for i in range(x+1)]  #create a list of x empty lists
    
    for d in den:
        for j in range(x+1):
            if d<=j and MEMO[j-d] + 1 < MEMO[j]:
                MEMO[j] = MEMO[j-d] +1
                min_num_stamps[j] = min_num_stamps[j-d] + [d]
    return min_num_stamps[x]


# In[36]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE


# In[37]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# add your own further tests in the cell above

print(sol(6,(1,3,4)))
print(sol(138,(1,5,66,85,100)))
assert sum(sol(999,(1,5,66,85,100))) == 999

# HIDDEN TESTS BELOW


# ### Part 3 (3 Pts)
# Modify your functions so that they work even if `den` does not necessarily include `1`.  In this case, it may be impossible to make the amount given, in which case both functions should return `None`.  For example, with denominations 3,5 it is possible to make 6 (=3+3) and 8 (=3+5), but not 2 or 7.
# 
# Your new functions should be named `min_stamps_ext(x,den)` and `sol_ext(x,den)`. As before, your code should initialize any global variables, and your functions need to be able to work for different choices of the denominations `den` without re-initializing.
# 
# Hints: the basic structure of the functions can be the same as before, but you need to determine what to do if some or all of the recursive function calls return None, or if there are no denominations less than or equal to `x`.  It is advisable to use a different variable name for the memoization dictionary, to avoid conflict with the previous parts of the question. 

# In[86]:


# THIS CODE IS BOTH AUTOGRADED AND HANDGRADED ACCORDING TO MARKING CRITERIA 1-4

def min_stamps_ext(x, den):
    #if x is one of the denominations they we only need 1 stamp
    if x in den:
        return 1
    else:
        listy = []
        for i in den:
            if i<=x: #since if x < i, then we can't use stamp i
                if (x-i, den) in MEMO:
                    listy.append(MEMO[(x-i, den)])
                else:
                    if min_stamps_ext(x-i, den) != None:
                        MEMO[(x-i, den)] = min_stamps_ext(x-i, den) + 1
                        listy.append(MEMO[(x-i, den)])
        if len(listy) == 0: #which means we couldn't find any solutions
            return None
        return min(listy) #else we pick the minimum option
                        
def sol_ext(x,den):
    if min_stamps_ext(x, den) == None:
        return None  #since if we couldn't find a solution for min_stamps_ext
                     #then we won't find one here
        
        #else we return the sol function adding (1,) to the end to avoid errors
    else:
        return sol(x, den + (1,))
                


# In[87]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR CODE


# In[88]:


# AUTOGRADED TEST CELL INCLUDING HIDDEN TESTS
# add your own tests in the cell above

for i in range(1,14):
    print('Solution for making',i,'using',(3,5),':',sol_ext(i,(3,5)))
    
print('Minimum for 138 using (5,66,85,100):',min_stamps_ext(138,(5,66,85,100)))
print('Minimum for 999 using (5,66,85,100):',min_stamps_ext(999,(5,66,85,100)))

# HIDDEN TESTS BELOW


# ### BONUS Question for enthusiasts (not graded)
# 
# If you have completed this homework and would like a further challenge, please see the additional file `homework6_bonus_Q_not_graded.ipynb` (on the blackboard page) for a follow-on to the last question.

# In[ ]:





# In[ ]:




