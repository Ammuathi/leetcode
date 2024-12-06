def upper_fun(fun):
    def inner_fun(name):
        result=fun(name)
        return result.upper()
    return inner_fun
@upper_fun
def hello_name(name):
    return "hello" + name
print(hello_name('ammu'))


