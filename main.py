from cafeteria.condimentos.leite import leite
from cafeteria.produtos_base.cafe import cafe

cafe_personalizado = cafe()

print(cafe_personalizado.descricao())
print(cafe_personalizado.custo())

cafe_personalizado = leite(cafe_personalizado)
cafe_personalizado = leite(cafe_personalizado)
cafe_personalizado = leite(cafe_personalizado)

print(cafe_personalizado.descricao())
print(cafe_personalizado.custo())