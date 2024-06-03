from concurrent.futures import ThreadPoolExecutor

def calculate(x):
    if len(x) > 1000:
        output_list = []
        with ThreadPoolExecutor(max_workers=6) as pool:
            output_list.extend(pool.map(sum_lists, x))
    else:
        return sum_lists(x)

def sum_lists(x):
    result = []
    for i in x:
        if len(i) > 2 or len(i) < 2:
            raise('List with more/less than two values')
        result.append(sum(i))
    return result