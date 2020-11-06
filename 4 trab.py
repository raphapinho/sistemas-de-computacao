#!/usr/bin/env python
# coding: utf-8

# In[32]:


niv=float(input('coloque o número de níveis:'))
bit=niv**2
print('para {}de bits, tem-se {}niveis'.format(bit,niv))


# In[31]:


def binToDec(binaryString):
    sum=0
    base=1
    for i in reversed(binaryString):
        sum = sum = (base * int(i))
        base = base * 2
        print(sum)


# In[38]:


num=int(input('Digite um número inteiro:'))
print('''Escolha uma das base para converção:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção=int(input('sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')


# In[26]:


octal = 25
dec = 0

remain=octal
i=0
while remain > 0:
    dec+= int(remain % 10)*8**i
    remain = int(remain / 10)
    i+=i

print(f"octal({octal})=>Decimal({dec})")


# In[42]:


#coverter bin=dec#
b=110010
dec= int(str(b),2)
print(dec)


# In[1]:


https://github.com/raphapinho/SISTEMAS_NUMERA-O.git


# In[ ]:




