#Escreva um program que leia um valor em metros e o exiba convertido em centimetos e milimetros
m = float(input('Digite o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('O valor de {} em: \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(m, km, hm, dam, dm, cm, mm))
