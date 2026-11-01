"""Compare parsed JSON values, ignoring object-key order."""
import argparse
import json
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("left", type=Path)
p.add_argument("right", type=Path)
a = p.parse_args()

def reject_constant(value):
    raise ValueError(f"Nonstandard JSON constant: {value}")

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate object key: {key}")
        result[key] = value
    return result

def read(path):
    return json.loads(
        path.read_text(encoding="utf-8-sig"),
        parse_constant=reject_constant,
        object_pairs_hook=unique_object
    )

def equal(left, right):
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(
            equal(left[k], right[k]) for k in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            equal(x, y) for x, y in zip(left, right)
        )
    return left == right

try:
    same = equal(read(a.left), read(a.right))
except (OSError, UnicodeError, ValueError, RecursionError) as error:
    p.exit(2, f"Cannot compare JSON: {error}\n")

print("EQUAL" if same else "DIFFERENT")
raise SystemExit(0 if same else 1)