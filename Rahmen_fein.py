length = 0.55
width = 0.83
depth = 0.035
waste = 0.2
price = 14.50
build = 5.71
clip = 4.3
tax = 0.19


def get_usage(length: float, width: float, depth: float, waste: float) -> float:
    usage = (2 * length + 2 * width + 8 * depth) * (1 + waste)
    return usage


def get_cost(price: float, build: float, usage: float, clip: float, tax: float) -> float:
    cost = (usage * price + build + clip) * (1 + tax)
    return cost


usage = round(get_usage(length, width, depth, waste), ndigits=2)

cost = round(get_cost(price, build, usage, clip, tax), ndigits=2)

print(f'cost: {cost} €')

print(f'usage: {usage} m')
