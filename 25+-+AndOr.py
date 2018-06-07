
# coding: utf-8

# ## Entendendo melhor o *and e o *or

# In[7]:


ANIMAIS = 'mamífero', 'réptil', 'anfíbio', 'ave'
ANIMAIS_QUE_BOTAM_OVOS = 'réptil', 'ave', 'anfíbio'

is_animal = lambda animal: animal in ANIMAIS
animal_que_bota_ovos = lambda animal: print('x') or animal in ANIMAIS_QUE_BOTAM_OVOS

bota_ovos = lambda coisa: is_animal(coisa) and animal_que_bota_ovos(coisa)
bota_ovos('lucas')

