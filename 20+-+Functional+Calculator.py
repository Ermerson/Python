
# coding: utf-8

# ### Paradigma Funcional 
# ##### Abordagem Procedural

# In[4]:


OPERATORS  = '+', '-', '*', '/'

def p_main():
    print('Esta é uma calculadora procedural')
    number1 = p_get_number()
    operator = p_get_operator()
    number2 = p_get_number()
    result = p_calculate(number1, operator, number2)
    print('o resultador é: %s ' %result)
    
def p_get_number():
    while True:
        s= input('Digite um numero inteiro: ')
        try:
            return int(s)
        except ValueError:
            print('isto não é um numero inteiro: ')
            
            
def p_get_operator():
    while True:
        s = input('Digite um operador (+, -, *, /): ')
        if s in OPERATORS:
            return s
        print('Isto não é um operador.')
    
def p_calculate(number1, operator, number2):
   
    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '/':
        return number1 / number2
    raise Exception('Operador inválido')

p_main()


# ### Abordagem Funcional

# In[10]:


OPERATORS  = '+', '-', '*', '/'

def f_get_number():
    return int(input('Digite um número inteiro.'))

def f_get_operator():
    return input('Digite um operador (+, _, *, /): ')

def f_calculate(number1, operator, number2):
    return number1 + number2 if operator == '+'         else number1 - number2 if operator =='-'         else number1 * number2 if operator =='*'         else number1 / number2 if operator =='/'         else None
        
def f_main():
    return f_calculate(f_get_number(), f_get_operator(), f_get_number())

print('O resultado é: %d' %f_main())

