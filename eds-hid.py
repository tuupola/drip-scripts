#!/usr/bin/env python3

import sys
from pathlib import Path


def raa_from_det(det: bytes) -> int:
    return ((det[3] & 0x0F) << 10) | (det[4] << 2) | ((det[5] >> 6) & 0x03)


def hda_from_det(det: bytes) -> int:
    return ((det[5] & 0x3F) << 8) | det[6]


def hid_from_det(det: bytes) -> int:
    return ((det[3] & 0x0F) << 24) | (det[4] << 16) | (det[5] << 8) | det[6]


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

    print(
        f"{'Entity':<24} {'RAA':>6} {'HDA':>6} {'HID':>12}  "
        f"{'Parent RAA':>10} {'Parent HDA':>10} {'Parent HID':>12}"
    )
    for path in files:
        try:
            data = parse_eds(path)
        except ValueError as err:
            print(err, file=sys.stderr)
            continue
        child = data[8:24]
        parent = data[56:72]
        print(
            f"{path.stem:<24} {raa_from_det(child):6d} {hda_from_det(child):6d} "
            f"0x{hid_from_det(child):08x}  {raa_from_det(parent):10d} {hda_from_det(parent):10d} "
            f"0x{hid_from_det(parent):08x}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
