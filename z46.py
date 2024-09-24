from decimal import Decimal
E = Decimal("2.7182818284590452353602875")
input_data = open('input.txt', 'r')
round_data = int(input_data.read())
out = round(E, round_data)
output_data = open ('output.txt','w')
output_data.write(str(out))
input_data.close()
output_data.close()