"""Compile src/*.txt TI-BASIC sources into bin/*.8xp files (requires `pip install tivars`)."""
from pathlib import Path

from tivars import TIProgram

root = Path(__file__).parent
out = root / "bin"
out.mkdir(exist_ok=True)

for src in sorted((root / "src").glob("*.txt")):
    name = src.stem.upper()
    prog = TIProgram(name=name)
    prog.load_string(src.read_text().rstrip("\n"))
    prog.save(str(out / f"{name}.8xp"))
    print(f"{name}: {len(prog.bytes())} bytes")
