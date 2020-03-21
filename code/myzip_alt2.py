def myzip(*args):
    iters = list(map(iter, args))
    while iters:
        try:
            res = [next(i) for i in iters]
        except:
            break
        yield tuple(res)

