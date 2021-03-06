def test_multi_setter_test(get_contract_with_gas_estimation):
    multi_setter_test = """
dog: int128[3]
bar: int128[3][3]
@public
def foo() -> int128:
    self.dog = [1, 2, 3]
    return(self.dog[0] + self.dog[1] * 10 + self.dog[2] * 100)

@public
def fop() -> int128:
    self.bar[0] = [1, 2, 3]
    self.bar[1] = [4, 5, 6]
    return self.bar[0][0] + self.bar[0][1] * 10 + self.bar[0][2] * 100 + \
        self.bar[1][0] * 1000 + self.bar[1][1] * 10000 + self.bar[1][2] * 100000

@public
def goo() -> int128:
    goo: int128[3]
    goo = [1, 2, 3]
    return(goo[0] + goo[1] * 10 + goo[2] * 100)

@public
def gop() -> int128: # Following a standard naming scheme; nothing to do with the US republican party
    gar: int128[3][3]
    gar[0] = [1, 2, 3]
    gar[1] = [4, 5, 6]
    return gar[0][0] + gar[0][1] * 10 + gar[0][2] * 100 + \
        gar[1][0] * 1000 + gar[1][1] * 10000 + gar[1][2] * 100000

@public
def hoo() -> int128:
    clear(self.dog)
    return(self.dog[0] + self.dog[1] * 10 + self.dog[2] * 100)

@public
def hop() -> int128:
    clear(self.bar[1])
    return self.bar[0][0] + self.bar[0][1] * 10 + self.bar[0][2] * 100 + \
        self.bar[1][0] * 1000 + self.bar[1][1] * 10000 + self.bar[1][2] * 100000

@public
def joo() -> int128:
    goo: int128[3]
    goo = [1, 2, 3]
    clear(goo)
    return(goo[0] + goo[1] * 10 + goo[2] * 100)

@public
def jop() -> int128:
    gar: int128[3][3]
    gar[0] = [1, 2, 3]
    gar[1] = [4, 5, 6]
    clear(gar[1])
    return gar[0][0] + gar[0][1] * 10 + gar[0][2] * 100 + \
        gar[1][0] * 1000 + gar[1][1] * 10000 + gar[1][2] * 100000

    """

    c = get_contract_with_gas_estimation(multi_setter_test)
    assert c.foo() == 321
    c.foo(transact={})
    assert c.fop() == 654321
    c.fop(transact={})
    assert c.goo() == 321
    assert c.gop() == 654321
    assert c.hoo() == 0
    assert c.hop() == 321
    assert c.joo() == 0
    assert c.jop() == 321
    print('Passed multi-setter literal test')


def test_multi_setter_struct_test(get_contract_with_gas_estimation):
    multi_setter_struct_test = """
struct Dog:
    foo: int128
    bar: int128
struct Bar:
    a: int128
    b: int128
struct Z:
    foo: int128[3]
    bar: Bar[2]
struct Goo:
    foo: int128
    bar: int128
struct Zed:
    foo: int128[3]
    bar: Bar[2]
dog: Dog[3]
z: Z[2]

@public
def foo() -> int128:
    foo0: int128 = 1
    self.dog[0] = Dog({foo: foo0, bar: 2})
    self.dog[1] = Dog({foo: 3, bar: 4})
    self.dog[2] = Dog({foo: 5, bar: 6})
    return self.dog[0].foo + self.dog[0].bar * 10 + self.dog[1].foo * 100 + \
        self.dog[1].bar * 1000 + self.dog[2].foo * 10000 + self.dog[2].bar * 100000

@public
def fop() -> int128:
    self.z = [Z({foo: [1, 2, 3], bar: [Bar({a: 4, b: 5}), Bar({a: 2, b: 3})]}),
              Z({foo: [6, 7, 8], bar: [Bar({a: 9, b: 1}), Bar({a: 7, b: 8})]})]
    return self.z[0].foo[0] + self.z[0].foo[1] * 10 + self.z[0].foo[2] * 100 + \
        self.z[0].bar[0].a * 1000 + self.z[0].bar[0].b * 10000 + self.z[0].bar[1].a * 100000 + self.z[0].bar[1].b * 1000000 + \
        self.z[1].foo[0] * 10000000 + self.z[1].foo[1] * 100000000 + self.z[1].foo[2] * 1000000000 + \
        self.z[1].bar[0].a * 10000000000 + self.z[1].bar[0].b * 100000000000 + \
        self.z[1].bar[1].a * 1000000000000 + self.z[1].bar[1].b * 10000000000000

@public
def goo() -> int128:
    goo: Goo[3]
    goo[0] = Goo({foo: 1, bar: 2})
    goo[1] = Goo({foo: 3, bar: 4})
    goo[2] = Goo({foo: 5, bar: 6})
    return goo[0].foo + goo[0].bar * 10 + goo[1].foo * 100 + \
        goo[1].bar * 1000 + goo[2].foo * 10000 + goo[2].bar * 100000

@public
def gop() -> int128:
    zed: Zed[2] = [
        Zed({foo: [1, 2, 3], bar: [Bar({a: 4, b: 5}), Bar({a: 2, b: 3})]}),
        Zed({foo: [6, 7, 8], bar: [Bar({a: 9, b: 1}), Bar({a: 7, b: 8})]})
    ]
    return zed[0].foo[0] + zed[0].foo[1] * 10 + zed[0].foo[2] * 100 + \
        zed[0].bar[0].a * 1000 + zed[0].bar[0].b * 10000 + zed[0].bar[1].a * 100000 + zed[0].bar[1].b * 1000000 + \
        zed[1].foo[0] * 10000000 + zed[1].foo[1] * 100000000 + zed[1].foo[2] * 1000000000 + \
        zed[1].bar[0].a * 10000000000 + zed[1].bar[0].b * 100000000000 + \
        zed[1].bar[1].a * 1000000000000 + zed[1].bar[1].b * 10000000000000
    """

    c = get_contract_with_gas_estimation(multi_setter_struct_test)
    assert c.foo() == 654321
    assert c.fop() == 87198763254321
    assert c.goo() == 654321
    assert c.gop() == 87198763254321

    print('Passed multi-setter struct test')


def test_type_converter_setter_test(get_contract_with_gas_estimation):
    type_converter_setter_test = """
pap: decimal[2][2]

@public
def goo() -> int128:
    self.pap = [[1, 2], [3, 4]]
    return floor(self.pap[0][0] + self.pap[0][1] * 10.0 + self.pap[1][0] * 100.0 + self.pap[1][1] * 1000.0)
    """

    c = get_contract_with_gas_estimation(type_converter_setter_test)
    assert c.goo() == 4321
    print('Passed type-conversion struct test')


def test_composite_setter_test(get_contract_with_gas_estimation):
    composite_setter_test = """
struct C:
    c: int128
struct Mom:
    a: C[3]
    b: int128
mom: Mom
qoq: C

@public
def foo() -> int128:
    self.mom = Mom({a: [C({c: 1}), C({c: 2}), C({c: 3})], b: 4})
    non: C = C({c: 5})
    self.mom.a[0] = non
    non = C({c: 6})
    self.mom.a[2] = non
    return self.mom.a[0].c + self.mom.a[1].c * 10 + self.mom.a[2].c * 100 + self.mom.b * 1000

@public
def fop() -> int128:
    popp: Mom = Mom({a: [C({c: 1}), C({c: 2}), C({c: 3})], b: 4})
    self.qoq = C({c: 5})
    popp.a[0] = self.qoq
    self.qoq = C({c: 6})
    popp.a[2] = self.qoq
    return popp.a[0].c + popp.a[1].c * 10 + popp.a[2].c * 100 + popp.b * 1000

@public
def foq() -> int128:
    popp: Mom = Mom({a: [C({c: 1}), C({c: 2}), C({c: 3})], b: 4})
    clear(popp.a[0])
    clear(popp.a[2])
    return popp.a[0].c + popp.a[1].c * 10 + popp.a[2].c * 100 + popp.b * 1000
    """

    c = get_contract_with_gas_estimation(composite_setter_test)
    assert c.foo() == 4625
    assert c.fop() == 4625
    assert c.foq() == 4020
    print('Passed composite struct test')
