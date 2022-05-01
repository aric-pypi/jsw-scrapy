import jsw_nx as nx


def test_base_filter():
    assert nx.filter([1, 2, 3], lambda v, i: v > 1) == [2, 3]
    assert nx.filter([1, 2, 3, None], lambda v, i: bool(v)) == [1, 2, 3]


def test_base_index():
    assert nx.index([1, 2, 3], 2) == 1
    assert nx.index([1, 2, 3], 5) == -1


def test_base_includes():
    assert nx.includes([1, 2, 3], 2) == True
    assert nx.includes([1, 2, 3], 5) == False


def test_base_map():
    assert nx.map([1, 2, 3], lambda v, i: v + 1) == [2, 3, 4]


def test_base_reduce():
    assert nx.reduce([1, 2, 3], lambda res, v, i: res + v) == 6


def test_base_mix():
    res = nx.mix(None, {"a": 123, "b": "234"}, {"c": 'AAA'})
    assert res == {"a": 123, "b": '234', "c": "AAA"}


def test_base_get():
    test_data = {
        'name': 'wonder',
        'contact': {
            'phone': 110,
            'sns': {
                'qq': {
                    'code': 112,
                }
            }
        },
    }

    assert nx.get(test_data, 'name') == 'wonder'
    assert nx.get(test_data, 'english_name') == None
    assert nx.get(test_data, 'contact.phone') == 110
    assert nx.get(test_data, 'contact.phone.mobile') == None
    assert nx.get(test_data, 'contact.sns.qq.code') == 112
    assert nx.get(test_data, 'other1.other2.other3') == None
    assert nx.get(None, 'name') == None
    assert nx.get(100, 'name') == None
    assert nx.get('some', 'name') == None
    assert nx.get('some', 'name', 'wonder') == 'wonder'


def test_every():
    arr = [1, 2, 3, 4, 5]
    res1 = nx.every(arr, lambda v, i: v > 0)
    res2 = nx.every(arr, lambda v, i: v > 3)
    assert res1 == True
    assert res2 == False


def test_some():
    arr = [-1, -2, -3, 4, -5]
    res1 = nx.some(arr, lambda v, i: v > 0)
    res2 = nx.some(arr, lambda v, i: v > 5)
    assert res1 == True
    assert res2 == False


def test_parse_int():
    assert nx.parse_int('123') == 123
    assert nx.parse_int('123.456') == None
    assert nx.parse_int('s233') == None