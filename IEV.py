rates = [16935, 16128, 17885, 18564, 18155, 19017]
dom = 2 * (rates[0] + rates[1] + rates[2])
rec = 1.5 * rates[3] + rates[4]

print dom + rec