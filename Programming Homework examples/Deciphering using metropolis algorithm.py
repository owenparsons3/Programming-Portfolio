#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In this project, I was given several ciphers to decrypt such as :

# ciphertexts[3]="TULOMREMAEKBLRSWCTMWBIHB BTN KKUT NBTULOMRB DWBKSYMBYSWMRDBTULOMRKBJUNNBRMQM NBKE EUKEUT NBUDPSRY EUSDB ISCEBEOMBLN UDEMAEB DWBEO EBUDPSRY EUSDBT DBSPEMDBIMBCKMWBESBIRM XBEOMBTULOMRB PEMRBEOMBWUKTSQMRHBSPBPRMVCMDTHB D NHKUKBIHBEOMB R IBY EOMY EUTU DB DWBLSNHY EOB NBXUDWUB NKSBXDSJDB KB NXUDWCKBUDBEOMBDUDEOBTMDECRHBDM RNHB NNBKCTOBTULOMRKBTSCNWBIMBIRSXMDBIHB DBUDPSRYMWB EE TXMRBKCTOBTN KKUT NBTULOMRKBKEUNNBMDGSHBLSLCN RUEHBESW HBEOSCFOBYSKENHB KBLCZZNMKB NBXUDWUBJRSEMB BISSXBSDBTRHLESFR LOHBMDEUENMWBRUK N OBPUBUKEUXOR GB NBYC YY BY DCKTRULEBPSRBEOMBWMTULOMRUDFBTRHLESFR LOUTBYMKK FMKBJOUTOBWMKTRUIMWBEOMBPURKEBXDSJDBCKMBSPBPRMVCMDTHB D NHKUKB DWBTRHLE D NHKUKBEMTODUVCMKB DBUYLSRE DEBTSDERUICEUSDBSPBUIDB WN DBJ KBSDBK YLNMBKUZMBPSRBCKMBSPBPRMVCMDTHB D NHKUK"

#ciphertexts[4]="RJLHXTNERXWZEWZSXLESNIFWX TEKJAAS NYSVEWZSECYWKZEKJTVYAW TWVERSLSELYTTXTNETYPDSLVEDJVH AXVVELJASER VED VXK AAIEWJECJEWZSEK AKYA WXJTVEWZSEVYPVEDSLCJRVHXEV XCEVJERZSTEWZSEVWSLTEK PSEULSSEJTEPJTC IEPJLTXTNERSEK AKYA WSCEWZ WERSEVZJYACEASWEWJTTSVEJUER WSLED AA VWEXTE WEWZSELS LEJUEWZSEOSVVSAEWJEFYVZEWZSEVWSLTECJRTE TCEAXUWEWZSEDJR"

#ciphertexts[5]="IZWLXSZF QEFLZTQUVLSZMIHZCIVLUZEDDZIUPZXLYAHLPZCQZLICZECZMIHZC QAO CZ QMLWLXZC ICZECHZIBBLCECLZTEO CZKLZHCETADICLPZKSZIZBEULIBBDL"

# And I had to come up with different methods to solve the ciphers.

# For the large ciphers such as these one, I used a metropolis algorithm: advised by this instruction:

#  In the sample text, record the frequency (i.e. number of occurrences) of each of the 272 bigrams, i.e.
# pairs of consecutive characters such as SH, as well as the 27 characters. For each pair of
# characters i, j compute
# p(i, j) := frequency(ij) + 1 / frequency(i)

#This represents the probability that i is followed by j; the +1 is a ‘fudge factor’ to avoid
#zeros. To any potential decoded message m = i1i2 . . . in we assign a score

# which measures how plausible m is as a piece of English text (it represents the logarithm
# of the probability of seeing m under a certain “Markov model”). Write a function that
# computes S(m) for any message m.


# In[ ]:


#To start with I needed to print off a large body of text- first 10000 words from Moby dick


# In[ ]:


import string
import requests
url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
moby_text = requests.get(url).text

with open('moby_text.txt', 'w', errors = 'ignore') as f:
    f.write(moby_text)
with open('moby_text.txt', 'r', errors = 'ignore') as f:
    moby_text = f.read()
    
ALPH_lower = string.ascii_lowercase
ALPH_upper = string.ascii_uppercase

MEMO = dict()
for i in range(len(ALPH_lower)):
    MEMO[ALPH_lower[i]] = ALPH_upper[i] 
for i in range(len(ALPH_lower)):
    MEMO[ALPH_upper[i]] = ALPH_upper[i] 


def make_uppercase(text):
    l = len(text)
    new_text = ""
    for i in range(l):
        if text[i] == ' ':
            new_text += ' '
        elif text[i] in MEMO:
            new_text += MEMO[text[i]]
        else:
            new_text += ' '
            
        new_text = new_text.replace('  ', ' ')
        
    return new_text
moby_new_text = make_uppercase(moby_text[:100000])
upper_moby = moby_new_text[:10000]
print(moby_new_text[:10000])


# In[ ]:


#Now follow the instructions to create a score function for how likely a body of text is


# In[ ]:


PAIR_FREQ = dict()
for i in ALPH_upper:
    for j in ALPH_upper:
        PAIR_FREQ[str(i)+str(j)] = 0 
        
SINGLE_FREQ = dict()
for i in ALPH_upper:
    SINGLE_FREQ[i] = 0
    
def freq_count_pairs(text):
    global PAIR_FREQ
    for i in PAIR_FREQ:
        freq = text.count(i)
        PAIR_FREQ[i] = freq
    return PAIR_FREQ

def freq_count_single(text):
    global SINGLE_FREQ
    for i in SINGLE_FREQ:
        freq = text.count(i)
        SINGLE_FREQ[i] = freq
    return SINGLE_FREQ




def prob_ij(text,i,j):
    freq_count_pairs(text)
    freq_count_single(text)
    numerator = PAIR_FREQ[str(i)+str(j)] +1
    denominator = SINGLE_FREQ[i]
    return numerator/denominator

PROB_IJ = dict()
def dict_prob_ij(text):
    global PROB_IJ
    for i in ALPH_upper:
        for j in ALPH_upper:
            PROB_IJ[str(i)+str(j)] = prob_ij(upper_moby,i,j)
    return PROB_IJ

dict_prob_ij(upper_moby)



def score(message):
    n = len(message)
    s = 0
    for i in range(n-1):
        s += np.log(PROB_IJ[str(message[i])+str(message[i+1])])
    return s


# In[ ]:


# Use the metropolis algorithm to decipher text


# In[ ]:


from random import randint
import numpy as np
def metropolis(m,n,T,show_text_every):
    current_m = m
    iteration = 0
    while iteration < n:
        if iteration%show_text_every == 0:
            print('!' + current_m)
        iteration += 1
        r_l1 = ALPH_upper[randint(0,26)]
        r_l2 = ALPH_upper[randint(0,26)]
        mprime = letter_swap(current_m,r_l1,r_l2)
        smprime_less_sm = score(mprime) - score(current_m)
        if smprime_less_sm > 0:
            current_m = mprime
        elif random()<= np.exp(smprime_less_sm/T):
            current_m = mprime
        else:
            current_m = current_m
    return current_m

