years_price_training_basket = int (input())

price_sneakers = years_price_training_basket - (years_price_training_basket*(40/100))
price_Kit = price_sneakers - (price_sneakers*20/100)
price_ball = price_Kit * 1/4
price_accesсories = price_ball * 1/5

total_sum = (years_price_training_basket + price_accesсories + price_ball + price_Kit + price_sneakers)
print(total_sum)
