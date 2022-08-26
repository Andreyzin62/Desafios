medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida * 10000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm e {:.0f}km'.format(medida ,cm ,mm , km))
