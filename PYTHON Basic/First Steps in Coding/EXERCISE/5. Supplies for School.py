count_packet_pens = int ( input())
count_packet_markers = int ( input())
liters_preparation = int ( input())
discount_rate = int ( input())

price_pens = count_packet_pens * 5.80
price_markers = count_packet_markers * 7.20
price_preparation = liters_preparation * 1.20
sum_all = price_pens + price_markers + price_preparation

money = sum_all - (sum_all * discount_rate/100)
print(money)
