
# coding: utf-8

# In[2]:


l_fatorial = lambda n: 1 if n == 0 else n*l_fatorial(n-1)
l_fatorial(3)


# #### Encadeando funções e combinando valores de retorno
# 
# 

# In[4]:


def mult_em_cadeia(*oque):
    total =1
    for (fnc, arg) in oque:
        total *= fnc(arg)
    return total

mult_em_cadeia((l_fatorial, 2), (l_fatorial,3), (l_fatorial, 4))


# ## Operadores como funções regulares
# 

# In[6]:


import operator

def op_em_cadeia(como, *oque):
    total = 1
    for (fnc, arg) in oque:
        total = como(total, fnc(arg))
    return total

op_em_cadeia(operator.truediv, (l_fatorial,2),(l_fatorial,3))

