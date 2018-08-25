from footest.supercar import foo

import sys
with open('/tmp/supercar', 'w') as f:
    f.write(",".join(sys.path))

def test_foo():
    assert foo() == "BAR"
