
# coding: utf-8

# ## Fatorial - Abordagem procedural

# In[7]:


def p_fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(p_fatorial(0))
print(p_fatorial(2))
print(p_fatorial(4))
print(p_fatorial(101))
    


# ## Abordagem Funcional

# In[11]:


def f_fatorial(n):
    return 1 if n == 0 else n*f_fatorial(n-1)

print(p_fatorial(0))
print(p_fatorial(2))
print(p_fatorial(4))
print(p_fatorial(100000))

