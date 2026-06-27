# Fazenda 3x1
while True:
	if can_harvest():
		harvest()
	move(North)


# Fazenda de qualquer tamanho 
while True:
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Grass)
		move(North)
	move(East)