def test0(n):
    def test(fun):
        def wrapper(*args, **kwargs):
            print("执行前")
            for i in range(n):
                print(i)
                res = fun(*args, **kwargs)
                print("执行后")
            return res
        return wrapper
    return test


@test0(n=3)
def tets001(*args, **kwargs):
    print(args)
    print(1)


if __name__ == '__main__':
    tets001(1, 2)
