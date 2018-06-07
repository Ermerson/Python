
# coding: utf-8

# In[1]:


def fatorial(n):
    return 1 if n == 0 else n*fatorial(n-1)
fatorial(3)


# ### Outro modulo de calcular o tempo de uma função
# 

# In[7]:


import time

def timer(fnc):
    
    def inner(arg):
        
        t0 = time.time()
        fnc(arg)
        t1 = time.time()
        return t1-t0
    
    return inner

timed_fatorial = timer(fatorial)
timed_fatorial(900)


# ## Isso é um Decorator, mas há uma sintaxe mais elegante.

# In[9]:


@timer
def timed_fatorial(n):
    return 1 if n == 0 else n * fatorial(n-1)

timed_fatorial(900)

