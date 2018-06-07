
# coding: utf-8

# ### Uma função procedural simples

# In[2]:


from math import sqrt

def p_pythagoras(x,y):
    return sqrt(x**2 + y**2)

p_pythagoras(1,1)


# ### Uma função lambda simples

# In[3]:


l_pythagoras = lambda x, y: sqrt(x**2 + y**2)
l_pythagoras(1,1)


# In[6]:


## funções lambda não precisa ter nomes
(lambda x, y: sqrt(x**2 + y**2))(1,1)


# ### Recursão requer que a Lambda tenha um nome.

# In[4]:


l_fatorial = lambda n: 1 if n == 0 else n * l_fatorial(n-1)
l_fatorial(3)


# ## O uso de lambdas é conveniente

# In[5]:


lista = [0,1,2,3,4]
list(map(lambda x: x*2, lista))

