valores=[1,2,3]
valores.sort()
contador=1
flag=1

if(flag==1):
    for i in range(0,len(valores)):
    #print(valores[i])
        if valores[i]!=contador:
            print(contador)
            break
        elif valores[i]==len(valores):
            a=len(valores)+1
            print(a)
        else:
            contador=contador+1
