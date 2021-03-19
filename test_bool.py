import subprocess


def test_to_text():
    args = '(false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testToText",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '("false")\n'

    args = '(true)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testToText",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '("true")\n'


def test_logand():
    args = '(false, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogand",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'

    args = '(true, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogand",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'

    args = '(true, true)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogand",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'


def test_logor():
    args = '(false, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogor",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'

    args = '(true, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogor",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'

    args = '(true, true)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogor",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'


def test_logxor():
    args = '(false, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogxor",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'

    args = '(true, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogxor",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'

    args = '(true, true)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLogxor",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'


def test_lognot():
    args = '(false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLognot",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'

    args = '(true)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testLognot",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'


def test_equal():
    args = '(false, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testEqual",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'

    args = '(true, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testEqual",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'

    args = '(true, true)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testEqual",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'


def test_not_equal():
    args = '(false, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testNotEqual",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'

    args = '(true, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testNotEqual",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(true)\n'

    args = '(true, true)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testNotEqual",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(false)\n'


def test_compare():
    args = '(false, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testCompare",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(variant { equal })\n'

    args = '(true, false)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testCompare",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(variant { greater })\n'

    args = '(false, true)'
    array_equal = subprocess.run(["dfx",
                                  "canister",
                                  "call",
                                  "bool",
                                  "testCompare",
                                  args],
                                 cwd="motoko/bool/",
                                 stdout=subprocess.PIPE,
                                 check=True)
    actual = array_equal.stdout.decode('utf-8')
    assert actual == '(variant { less })\n'
