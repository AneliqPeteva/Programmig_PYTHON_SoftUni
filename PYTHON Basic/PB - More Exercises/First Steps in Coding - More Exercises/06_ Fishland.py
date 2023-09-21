price_mackerel = float(input()) #skumriq
price_sprat = float(input()) #caca
kg_bonito = float(input()) #kilograma palamud
kg_horsemackerel = float(input()) #kilograma сафрид Mussels
kg_mussels = int(input()) #kilograma midi

price_bohito = price_mackerel + (price_mackerel * 0.6)
price_horsemackerel = price_sprat + (price_sprat * 0.8)
sum_mussels = 7.50 * kg_mussels
sum_bohito = price_bohito * kg_bonito
sum_horsemackerel = price_horsemackerel * kg_horsemackerel

total_sum = sum_bohito + sum_horsemackerel + sum_mussels
print(f"{total_sum:.2f}")
