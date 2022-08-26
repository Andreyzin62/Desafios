largura = float(input('largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura

print('A sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m2'.format(largura , altura , área))

tinta = área / 2

print('Para pintar essa parede vc precisa de {:.2f}l de tinta.'.format(tinta))
