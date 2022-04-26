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

# In[ ]:


NAME = "Owen Parsons"
UoB_ID = "1930993"


# # Homework 1
# 
# ## Marks, Content, and Marking Criteria 
# 
# 
# **Points vs. Marks.**  Below, you will find 10 short programming questions, worth a total of 15 points. This Homeworks counts as 7.5 marks to your final grade. (Hence 2 points are equivalent to 1 mark.)  
# 
# **Content.** The content of this Homework covers introductory material on Python from weeks 1-2 of the course.
# 
# **Marking Criteria.** This homework is **automatically graded**. The autograder checks the **correctness** of your computations/results and attributes marks accordingly. 
# 
# **Compliance with Instructions.** When writing your code you should closely follow the instructions given. For example, if you are told that you may not use a particular python library function then you may lose several points if you do so.

# ## Question 1: swapping variables (1 Pt) 
# 
# We have three variables `a`, `b`  and `c` which we initialise to random numbers (using the function `random`). Write code to perform a permutation of the contents of the variables so  that after your code is implemented we will have the following state of affairs. 
# - `a` will  contain the original value of `c`, 
# - `b` will contain the original value of `a`,  
# - and `c` will contain the original value of `b`. 

# In[ ]:


# RUN THIS CELL TO DEFINE THE VARIABLES a, b, c (THIS CELL IS READ ONLY)
# NOTE: a0, b0 and c0 ARE USED FOR TESTING AND TO DEFINE THE INITIAL VALUES 
# OF a, b and c. DO NOT USE/REDEFINE THE VARIABLES a0, b0, c0 IN YOUR SOLUTION!! 
from random import *
a0 = random()
b0 = random()
c0 = random()
# WE NOW DEFINE VARIABLES a, b and c. 
a = a0
b = b0
c = c0


# In[ ]:


# THE VARIABLES a, b and c ARE NOW DEFINED SO YOU CAN PROCEED... 
# YOUR CODE HERE
c=b0
b=a0
a=c0

a,b,c


# In[ ]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# HERE'S A TYPICAL QUICK CHECK... 
print(a0,b0,c0)   
print(a,b,c)


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY


# ## Question 2: the trajectory of a football (1 Pt) 
# You kick a football at an (initial) velocity $v_0 = 15\,\mathrm{m}\mathrm{s}^{-1}$ (metres per second) at an angle of $\alpha = \pi/3$ radians. How long does it take to come down on the pitch again?
# 
# Recall that we have the two equations of motion in the $x$ (horizontal) and $y$ (vertical) directions:
# 
# \begin{align}
# x &= v_0 \cos(\alpha) t \\
# y &= v_0 \sin(\alpha) t - g t^2 
# \end{align}
# 
# where $g = 9.81\,\mathrm{m}\mathrm{s}^{-2}$ is the acceleration due to gravity. 
# 
# Your task is to solve this problem. To do this you should work out (by hand)  a formula $-$ in terms of $v_0$, $\alpha$ and $g$   $-$  for the time $t$ (in seconds) that the football takes to come down on the pitch again. In Python you should define a variable `t` for your solution using this formula. (So the value of `t` will be evaluated in the hidden test.) 
# 

# In[1]:


# THE FOLLOWING import STATEMENT MAKES THE FUNCTIONS cos, sin and sqrt AVAILABLE TO US
# ALSO THE CONSTANT pi (SEE TESTING AREA BELOW THIS CELL)
from math import *

# MANDATORY: ASSIGN YOUR SOLUTION TO A VARIABLE CALLED t 
# YOUR CODE HERE
v0 = 15
a = pi / 3
g = 9.81 
t = (v0*sin(a)) / g
t


# In[ ]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# WE CAN START BY CHECKING WHAT FUNCTIONS WE HAVE IMPORTED FROM THE math LIBRARY
# For example
print(pi)
print(sin(pi/6))
print(cos(pi/3))
print(cos(pi/4))
print(sqrt(2)/2)
# AND YOU CAN CHECK YOUR SOLUTION:  
print("\nThe solution is " + str(t))


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY 


# ## Question 3: creating lists of integers  (1 Pt) 
# 
# Create a list called `divisible` containing all the  integers $0 < n < 5000$ - i.e. in the closed interval $[1,4999]$ - that are divisible by both $11$ and $17$. 

# In[2]:


# MANDATORY: YOU MUST STORE YOUR RESULTS IN THE FOLLOWING LIST
divisible = []

# YOUR CODE HERE
numbers = range(1, 5000)
for i in numbers:
    if i % 11 == 0 and i % 17 == 0:
        divisible.append(i)
        
print(divisible)


# In[ ]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# FOR EXAMPLE PRINT OUT YOUR RESULT: 
print(divisible)


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY
# HERE ARE A FEW INITIAL TESTS THAT YOUR LIST SHOULD PASS
assert (187 in divisible) and (1496 in divisible) and (4114 in divisible)
assert (176 not in divisible) and (2056 not in divisible) and (3171 not in divisible)
# THERE ARE HIDDEN TESTS HERE


# ## Question  4: creating lists of integers (2 Pts)
# 
# Create a list called `part_divisible` containing the first 50 positive (i.e. $> 0$) integers that are divisible by **either** $7$ **or** by $13$ but **not by both**.  

# In[35]:


# MANDATORY: YOU MUST STORE YOUR RESULTS IN THE FOLLOWING LIST

# YOUR CODE HERE
part_divisible = []

numbers = range(1, 2000)

alpha = []
for i in numbers:
    if i % 7 == 0 and i % 13 == 0:
        alpha.append(i)
for j in numbers:
    if j % 7 == 0 or j % 13 == 0:
       
        if j not in alpha:
             part_divisible.append(j)
            

first50 = part_divisible[0:50]
print(first50)
 
        
        



# In[ ]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# FOR EXAMPLE PRINT OUT THE LENGTH OF YOUR RESULT AND THE LIST ITSELF:
print(len(part_divisible))
print(part_divisible)


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY
# HERE ARE A FEW INITIAL TESTS THAT YOUR LIST SHOULD PASS
assert (7 in part_divisible) and (13 in part_divisible) and (104 in part_divisible)
assert (217 in part_divisible) and (245 in part_divisible)
assert (12 not in part_divisible) and (33 not in part_divisible) and (205 not in part_divisible)
# THERE ARE HIDDEN TESTS HERE


# ## Question 5: handling basic statistics - rainfall per month
# Let's do a little bit of mathematics and statistics using lists. In the next cell is the amount of rainfall per month (in units of mm) for Bristol.

# In[9]:


rainfall = [82.3,53.8,58.6,49.3,62.3,55.2,54.6,64.2,68.0,85.4,82.6,85.9]


# ### Part 1: mean and total rainfall (1 Pt)
# 
# Compute: 
# - The mean rainfall per month in Bristol,
# - The total amount of rain per year in Bristol.
# 
# **Important.** You must use the variables `mean` and `total` to store your answers (in order to pass the hidden tests).

# In[5]:


# MANDATORY: USE THE VARIABLES mean AND total TO STORE YOUR ANSWER
# YOUR CODE HERE
import statistics
rainfall = [82.3,53.8,58.6,49.3,62.3,55.2,54.6,64.2,68.0,85.4,82.6,85.9]
mean = statistics.mean(rainfall)
total = sum(rainfall)
print(mean, total)


# In[6]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# HERE'S SOME TYPICAL CODE TO HELP YOU INSPECT YOUR RESULTS
print('We have a mean of ' + str(mean) + ' mm of rain per month in Bristol,', end = " " )
print('giving a total of ' + str(total) + ' mm.')


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY


# ### Part 2: the standard deviation (1 Pt)
# 
# Compute the sample standard deviation of the monthly rainfall and assign the result to the variable `std`. 
# 
# (The sample variance of $n$ values $x_1,x_2,\ldots,x_n$ is given by $\frac1n \sum_{i=1}^n (x_i - \overline{x})^2$, where $\overline{x}$ is their mean.  The sample standard deviation is the square-root of the sample variance.)

# In[13]:


# MANDATORY: STORE YOUR SOLUTION IN THE VARIABLE std

# YOUR CODE HERE
import statistics
xis = []
rainfall = [82.3,53.8,58.6,49.3,62.3,55.2,54.6,64.2,68.0,85.4,82.6,85.9]
mean = statistics.mean(rainfall)
for i in rainfall:
    d = i - mean
    d = d**2
    xis.append(d)
sigma = sum(xis)
n = len(xis)
sample_variance = sigma * (1/n)
std = (sample_variance)**0.5
std


# In[14]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# HERE'S SOME TYPICAL CODE TO HELP YOU INSPECT YOUR RESULTS
print("We have a standard deviation in rainfall of " + str(std)+ ' mm.')


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY


# ## Question 6: list manipulation 
# Here is a short question on list manipulation. 
# 
# ### Part 1: modifying a list of characters  (1 Pt)
# 
# Convert the string `'The Fry Building'` into a list of characters (in the same order) which you should assign to the variable `fry_list`.  Then modify `fry_list` as follows. 
# 
# 1. Replace the first occurrence of the character `'i'` by the character `'l'`. (This is the letter `'l'` **not** the number `'1'`.)  
# 2. Replace the (first) occurrence of the character `'d'` by the character `'r'`. 

# In[16]:


# MANDATORY: USE THE VARIABLE fry_list TO STORE (AND MODIFY) YOUR LIST
fry_list = []

# YOUR CODE HERE
word = 'The Fry Building'
fry_list = []
for i in word:
    fry_list.append(i)
fry_list[10] = 'l'
fry_list[12] = 'r'
print(fry_list)


# In[17]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# FOR EXAMPLE PRINT OUT YOUR MODIFIED LIST: 
print(fry_list)


# In[18]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY


# ### Part 2: creating new lists of characters (1 Pt) 
# Convert the string `'The Ada Lovelace Building'` into a list which you should assign to the variable `ada_list`. From this list create another list - which you should assign to the variable `half_ada_list` -  containing only every second character of the string `'The Ada Lovelace Building'`, starting from the beginning. (I.e. the first character of `half_ada_list` will be `'T'`, the second character will be `'e'` etc.) 
# 
# **Remember.** The space character `' '` should be treated just like any other character. 

# In[19]:


# MANDATORY: USE THE VARIABLES ada_list AND half_ada_list TO STORE YOUR LISTS
ada_list = []
half_ada_list = []
word = 'The Ada Lovelace Building'
for i in word:
    ada_list.append(i)
for i in range(0,len(ada_list)):
    if i % 2 == 0:
        half_ada_list.append(ada_list[i])
print(half_ada_list)



# YOUR CODE HERE


# In[ ]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# FOR EXAMPLE PRINT OUT THE TWO LISTS: 
print(ada_list)
print(half_ada_list)


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY


# ## Question 7: list comprehension (1 Pt) 
# 
# Let's do a bit of  list comprehension. 
# 
# Create a list containing the values of $\displaystyle\left(\frac{x}{a}\right)^{\frac{1}{4}}$ for $a=5$ and integer values $2 \le x \le 12$. 
# 
# **Note.** You should assign your list to the variable `root_list`. 
# 
# **Remark.** Your list should contain $11$ values. 

# In[20]:


# MANDATORY: STORE YOUR ANSWER IN THE LIST WITH NAME root_list
# YOUR CODE HERE
root_list = []
for i in range(2,13):
    d = (i/5)**0.25
    root_list.append(d)
print(root_list)


# In[21]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# FOR EXAMPLE PRINT OUT YOUR RESULT: 
print(root_list)


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY


# ## Question 8: string creation (2 Pts)
# 
# In the cell below (which you should run) the variable `paragraph` has been assigned to a string containing some of the text of the book "A Tale of Two Cities" by Charles Dickens. Note that this string contains exclusively characters which are (upper or lower case) letters $-$ such as `'A'`, `'a'` $-$  from our usual Roman alphabet or characters belonging to the set `{' ', ',', '.', ':'}` (so no tabs, newlines etc.). 
# 
# Iterate over the string `paragraph` using a for loop to create a new string which is the same as `paragraph` except that every space is replaced by the plus character '+', and assign this string to the variable `new_paragraph`.
# (So your string should look like: 
# ```
# 'France,+less+favoured+...+atheistical+and+traitorous.'
# ```
# where `...` represents everything in between!)

# In[24]:


# RUN THIS CELL FIRST TO DEFINE paragraph
paragraph = """France, less favoured on the whole as to matters spiritual than her
sister of the shield and trident, rolled with exceeding smoothness down
hill, making paper money and spending it. Under the guidance of her
Christian pastors, she entertained herself, besides, with such humane
achievements as sentencing a youth to have his hands cut off, his tongue
torn out with pincers, and his body burned alive, because he had not
kneeled down in the rain to do honour to a dirty procession of monks
which passed within his view, at a distance of some fifty or sixty
yards. It is likely enough that, rooted in the woods of France and
Norway, there were growing trees, when that sufferer was put to death,
already marked by the Woodman, Fate, to come down and be sawn into
boards, to make a certain movable framework with a sack and a knife in
it, terrible in history. It is likely enough that in the rough outhouses
of some tillers of the heavy lands adjacent to Paris, there were
sheltered from the weather that very day, rude carts, bespattered with
rustic mire, snuffed about by pigs, and roosted in by poultry, which
the Farmer, Death, had already set apart to be his tumbrils of
the Revolution. But that Woodman and that Farmer, though they work
unceasingly, work silently, and no one heard them as they went about
with muffled tread: the rather, forasmuch as to entertain any suspicion
that they were awake, was to be atheistical and traitorous.""".replace("\n"," ")


# In[27]:


# MANDATORY: STORE YOUR ANSWER IN THE STRING WITH NAME new_paragraph
new_paragraph = ""
# YOUR CODE HERE
for i in range(len(paragraph)):
    if paragraph[i] == ' ':
        new_paragraph = new_paragraph + '+'
    else:
        new_paragraph = new_paragraph + paragraph[i]
new_paragraph


# In[12]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS


# In[13]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY


# ## Question 9: specialised string creation (2 Pts)
# 
# Create a string of the form `'((...))'`containing (in the place of `...`)  the squares of the integers $1,2,\dots,100$ in ascending order and assign this string to the variable `super_tuple`. (So your string should look like
# ```
# '((1,4,9,16,25,...,9216,9409,9604,9801,10000))'
# ```
# where `...` represents everything in between!)
# 
# **Note.** There are NO spaces in the string `super_tuple`, just the external brackets, numeric characters and commas. 
# 
# **Hint.** Use list comprehension to create a list of squares and then iterate over this list using a for loop to create your string `super_tuple`. (Use either the function `str` or the method `format` inside your for loop. Note that you will need to combine your for loop with a couple of lines of code to deal with the beginning and end of the string.)

# In[29]:


# MANDATORY: STORE YOUR ANSWER IN THE STRING WITH NAME super_tuple
# YOUR CODE HERE
super_tuple = '(('
for i in range(99):
    super_tuple = super_tuple + str((i + 1)**2) + ','
super_tuple = super_tuple + str((100)**2) + '))'


# In[30]:


# TESTING AREA (NOT GRADED): USE THIS CELL TO CHECK OR TEST YOUR RESULTS
# FOR EXAMPLE INSPECT YOUR RESULT AS OUTPUT OF THIS CELL: 
super_tuple


# In[31]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY


# ## Question 10: interpreted languages? (1 Pt) 
# 
# Lisp, Python and Matlab are all interpreted languages: `True` or `False`?

# In[ ]:


# MANDATORY: WRITE YOUR ANSWER AS interpreted = True OR interpreted = False

# YOUR CODE HERE
interpreted = True


# In[ ]:


# THIS CELL CONTAINS HIDDEN TESTS AND IS READ-ONLY

