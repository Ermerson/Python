
# coding: utf-8

# In[1]:


def fatorial(n):
    return 1 if n == 0 else n*fatorial(n-1)
fatorial(3)


# 
# ## E se quisermos usar diferentes unidades de tempo?

# In[5]:


import time

def timer_with_args(units="s"):
    
    def timer(fnc):
        
        def inner(arg):
            
            t0 = time.time()
            fnc(arg)
            t1 = time.time()
            diff = t1-t0
            if units == 'ms':
                diff *= 1000
            return diff
        
        return inner
    return timer

timed_fatorial = timer_with_args(units="ms")(fatorial)
timed_fatorial(500)


# ## Decorator com Argumentos usando a notação @

# In[16]:


@timer_with_args(units='s')
def fatorial(n):
    return 1 if n == 0 else n*fatorial(n-1)

fatorial(400)

