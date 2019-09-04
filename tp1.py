import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.genfromtxt('ENFR2013.txt', delimiter='|', skip_header=1)
a=data.shape
print("intro: Cargando datos...")
print(a)

#------------PUNTO UNO-------------->
enum=["Gran Buenos Aires","Pampeana","Noroeste","Noreste","Cuyo","Patagonia"]
print("EJ1: Calculando cantidad de entradas por región...")
regiones=data[:,2]
salida=[0,0,0,0,0,0]
for x in regiones:
	salida[x.astype(np.int64)-1]+=1

print("Resultados:")
entradas=pd.Series(salida,index=enum)
df=pd.DataFrame({'Entradas':entradas})
print(df)
print("  Total de entradas: "+str(sum(salida)))

#------------PUNTO DOS-------------->
print("EJ2: Graficando porcentajes para tipos de vivienda en el aglomerado de Gran Córdoba...")
tiposViv=["Casa","Casilla","Depto","Inquilinato","Hotel o\npension","Local","Otros"]
viviendas=data[:,5:7]
porcentaje=np.arange(max(data[:,6]))
total=1
for x in viviendas:
	if(x[0]==2 and x[1]!=9):
		i=x[1].astype(np.int64)
		porcentaje[i-1]+=1
		total+=1
for x in range(0,6):
	porcentaje[x]=(porcentaje[x]*100)/total
r=pd.Series(porcentaje,index=tiposViv)
r.sort_values(inplace=True)
plt.figure(figsize=(9,6))
plt.subplot(111)
plt.bar(r.index,r.values)
plt.suptitle("Porcentaje para cada tipo de vivienda en Gran Córdoba")
plt.show()

#-------------PUNTO TRES-------------->
print("EJ3: Calculando cantidad de viviendas con baño o letrina en el Chaco...")
banio=np.array([data[:,3],data[:,14]])
banio=banio.transpose()
c=0
n=0
for x in banio:
	if(x[0]==22 and x[1]==1):
		c+=1
	elif(x[0]==22 and x[1]==2):
		n+=1

print("  Cantidad con baño: "+str(c))
print("  Cantidad sin baño: "+str(n))

#-------------PUNTO CUATRO------------->
print("EJ4: Procesando datos sobre los jefes de hogar...")

N = max(data[:,29]).astype(np.int64)
CH=np.arange(N)
CM=np.arange(N)
i=0
for x in data[:,29]:
	val=x.astype(np.int64)
	if(data[i,27]==1):
		CH[val-1]+=1
	elif(data[i,27]==2):
		CM[val-1]+=1
	i+=1

ind = np.arange(N)
width = 0.35
p1 = plt.bar(ind, CH, width)
p2 = plt.bar(ind, CM, width, bottom=CH)
plt.ylabel('Cantidad por sexo')
plt.xlabel('Edades')
plt.title('Cantidad de jefes de hogar para todo el país, discriminado en sexo y edades')
plt.xticks(ind, ('0 a 17', '18 a 24', '25 a 34', '35 a 49', '50 a 64', '65 o +'))
plt.legend((p1[0], p2[0]), ('Hombres', 'Mujeres'))
plt.show()
t=1
for x in range(0,5,+1):
	t=CH+CM
	CH=(CH*100)/t
	CM=100-CH
p1=plt.bar(ind,CH,width)
p2=plt.bar(ind,CM,width,bottom=CH)
plt.ylabel('Porcentaje por sexo')
plt.xlabel('Edades')
plt.title('Porcentaje de jefes de hogar para todo el país,discriminado en sexo y edades')
plt.xticks(ind, ('0 a 17', '18 a 24', '25 a 34', '35 a 49', '50 a 64', '65 o +'))
plt.legend((p1[0],p2[0]),('Hombres','Mujeres'))
plt.show(block=True)

#------------PUNTO CINCO---------------->
N = len(data[:,28])
CH=np.arange(N)
CM=np.arange(N)
i=0
for x in data[:,28]:
	if(data[i,27]==1):
		CH[i]=x
	elif(data[i,27]==2):
		CM[i]=x
	i+=1
bini=max(data[:,28]).astype(np.int64)
bini=np.arange(bini)
plt.hist(CM,bins=bini)
plt.title("Histograma para las jefas de hogar discriminado en edades")
plt.show()

plt.hist(CH,bins=bini)
plt.title("Histograma para los jefes de hogar discriminado en edades")
plt.show()
