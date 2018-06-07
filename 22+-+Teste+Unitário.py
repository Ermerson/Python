
# coding: utf-8

# In[6]:


import itertools

def smile(l):
    return list(itertools.chain(*[['☺']*i for i in l]))
print(smile([1,2]))


# ### Teste unitário

# In[9]:


print('Começando o teste')
assert(smile([]) == [])
assert(smile([1]) == ['☺'])
assert(smile([0]) == [])
assert(smile([1,0,2]) == ['☺','☺','☺'])
       
print('feito')


# ## Prova
# Analisando o resultado dos testes, notamos que 
# l*a + l*b + l*c +, onde l é o smile e a,b,c são a quantidade de smiles nas listas
# 
# Então podemos simplificar a função smile

# In[10]:


def smile(l):
    return['☺'] * sum(l)

print(smile([1,2]))

