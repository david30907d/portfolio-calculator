total = 0
ETFs_string = input("please input your porfolio: ").split()
ETFs_int = [float(etf) for etf in ETFs_string]
total = sum(ETFs_int)
percentages = [round(etf/total, 2) for etf in ETFs_int]
print(percentages)