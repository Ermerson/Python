
# coding: utf-8

# ### Retornando uma função  de outra função

# ### Quatro passos para assar um pãozinho

# In[2]:


preaquecer_forno = lambda: print('Preaquecendo o forno')
colocar_paozinho = lambda: print('Colocando o paozinho no forno')
esperar_cinco_minutos = lambda: print('Esperando cinco minutos')
tirar_paozinho = lambda: print('Retirando Paozinho do forno')


# In[4]:


preaquecer_forno()
colocar_paozinho()
esperar_cinco_minutos()
tirar_paozinho()


# ### Criando uma função launcher e passando todos os passos para ela.
# 

# In[9]:


def perform_steps(*functions):
    
    for function in functions:
        function()


# In[10]:


perform_steps(preaquecer_forno, 
              colocar_paozinho, 
              esperar_cinco_minutos, 
              tirar_paozinho)


# ## Empacotar todos os passo em uma unica função

# In[12]:


def criar_receita(*functions):
    
    def run_all():
        
        for function in functions:
            function()
            
    return run_all

receita = criar_receita(preaquecer_forno, 
              colocar_paozinho, 
              esperar_cinco_minutos, 
              tirar_paozinho)

receita()

