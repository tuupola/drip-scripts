#!/usr/bin/env python3

import sys
from pathlib import Path


def parse_eds(path: Path) -> bytes:
    hex_text = path.read_text().strip()
    if len(hex_text) != 272:
        raise ValueError(f"{path.name}: expected 272 hex chars, got {len(hex_text)}")
    data = bytes.fromhex(hex_text)
    if len(data) != 136:
        raise ValueError(f"{path.name}: expected 136 bytes, got {len(data)}")
    return data


def main() -> int:
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    files = sorted(folder.glob("*.eds"))
    if not files:
        print(f"No .eds files in {folder}", file=sys.stderr)
        return 1

    print(f"{'Entity':<24} {'DET':<32}  {'Parent DET':<32}")
    for path in files:
        try:
            data = parse_eds(path)
        except ValueError as err:
            print(err, file=sys.stderr)
            continue
        child = data[8:24]
        parent = data[56:72]
        print(f"{path.stem:<24} {child.hex()}  {parent.hex()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
