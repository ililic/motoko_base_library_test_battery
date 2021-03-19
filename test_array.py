import subprocess


def test_array_equals_true():
    args = '(vec { "New York" }, vec { "New York" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testEqual",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'


def test_array_equals_false():
    args = '(vec { "New York" }, vec { "Toronto" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testEqual",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'


def test_array_append():
    args = '(vec { "New York" }, vec { "Toronto" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testAppend",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(vec { "New York"; "Toronto" })\n'


def test_chain():
    args = '(vec { "New York" }, vec { "Seattle" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testChain",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(vec { 10_128; 98_109 })\n'


def test_filter():
    args = '(vec { "New York"; "Seattle"; "Toronto" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testFilter",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(vec { "New York" })\n'


def test_map_filter():
    args = '(vec { "New York"; "Seattle"; "Toronto" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testMapFilter",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(vec { 1; 1; 1 })\n'


def test_find_empty():
    args = '(vec { "Lisbon"; "Seoul"; "Tokyo" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testFind",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(null)\n'


def test_find_not_empty():
    args = '(vec { "Lisbon"; "Seoul"; "Tokyo"; \
        "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testFind",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(opt "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch")\n'


def test_flatten():
    args = '(vec { vec { "New York"; "Seattle"; "Toronto" } })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testFlatten",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(vec { "New York"; "Seattle"; "Toronto" })\n'


def test_map():
    args = '(vec { "New York"; "Seattle"; "Toronto"; \
        "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch" })'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "array",
                                  "testMap",
                                  args],
                                 cwd="motoko/array/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(vec { 8; 7; 7; 58 })\n'


def test_array_make():
    array_make = subprocess.run(["dfx",
                                 "canister",
                                 "call",
                                 "array",
                                 "testMake",
                                 "\'(\"New York\")\'"],
                                cwd="motoko/array/",
                                stdout=subprocess.PIPE,
                                check=True)
    actual = array_make.stdout.decode('utf-8')
    assert actual == '(vec { "\'("New York")\'" })\n'
