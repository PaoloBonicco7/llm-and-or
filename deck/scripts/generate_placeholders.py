#!/usr/bin/env python3
from __future__ import annotations

import struct
import zlib
from pathlib import Path


def _png_chunk(tag: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + tag
        + data
        + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    )


def write_placeholder_png(path: Path, width: int = 1280, height: int = 720) -> None:
    # Simple diagonal stripe pattern to make it visually obvious it's a placeholder.
    # RGB, 8-bit, no alpha.
    def pixel(x: int, y: int) -> tuple[int, int, int]:
        stripe = ((x + y) // 24) % 2
        base = 238 if stripe == 0 else 220
        return (base, base, base)

    raw_rows = []
    for y in range(height):
        row = bytearray()
        row.append(0)  # filter type 0
        for x in range(width):
            r, g, b = pixel(x, y)
            row.extend((r, g, b))
        raw_rows.append(bytes(row))

    raw = b"".join(raw_rows)
    compressed = zlib.compress(raw, level=9)

    signature = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = (
        signature
        + _png_chunk(b"IHDR", ihdr)
        + _png_chunk(b"IDAT", compressed)
        + _png_chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def main() -> None:
    out_dir = Path(__file__).resolve().parent.parent / "public" / "fig"
    out_dir.mkdir(parents=True, exist_ok=True)

    files = [
        "wangli_fig_closed_loop.png",
        "wangli_fig_assisted_optimization.png",
        "zhang_fig_architecture.png",
        "zhang_alg1_debug_loop.png",
        "jiang_fig1_framework.png",
        "jiang_tab_or_fig_results.png",
    ]

    for name in files:
        write_placeholder_png(out_dir / name)

    print(f"Generated {len(files)} placeholder images in: {out_dir}")


if __name__ == "__main__":
    main()

