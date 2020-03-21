# map(func, seqs) workalike with zip

def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

