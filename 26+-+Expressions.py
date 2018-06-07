
# coding: utf-8

# ### Desvio condivional: modo procedural

# In[3]:


def p_descricao_nota(nota):
    if nota > 7:
        return 'Bom'
    if nota > 5:
        return 'Suficiente'
    return 'Insuficiente'

p_descricao_nota(8)


# ## Desvio condicional: modo funcional
# 

# In[4]:


(lambda nota: 'bom' if nota > 7 else 'suficiente' if nota > 5 else 'insuficiente')(6)


#  ###  Código conciso é facil de ler
# 

# In[9]:


#0 e 1 valem como booleanos
gender_code = 1
gender = 'feminino' if gender_code else 'masculino'
print(gender)

