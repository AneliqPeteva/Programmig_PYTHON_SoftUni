deposit_sum = float(input())
months = int(input())
yearly_rate = float(input())

total_sum = deposit_sum + months * ((deposit_sum * yearly_rate /100 ) / 12)
print(total_sum)