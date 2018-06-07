
# coding: utf-8

# ### Passando funções como parameters

# ### Começando pelo fatorial
# 
# Higher other function

# In[1]:


l_fatorial = lambda n: 1 if n == 0 else n * l_fatorial(n-1)


# #### Calsulando o tempo de Execução
# 

# ##### Modo Procedural

# In[6]:


import time

t0 = time.time()
l_fatorial(900)
t1 = time.time()
print('Demorou: %.5f s'  %(t1-t0))


# In[17]:


def timer(fnc, arg):
    t0 = time.time()
    fnc(arg)
    t1 = time.time()
    return t1-t0

print('Demorou: %.5f s'  % timer(l_fatorial, 900))


# ###  Modo funcional com funções lambda

# In[18]:


l_timestamp = lambda fnc, arg: (time.time(), fnc(arg), time.time())
l_diff = lambda t0, retval, t1: t1-t0
l_timer = lambda fnc, arg: l_diff(*l_timestamp(fnc, arg))

print('Demorou: %.5f s'  % l_timer(l_fatorial, 900))

