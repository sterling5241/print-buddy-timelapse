import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "print-buddy-timelapse"


def build(out):
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{NAME}.tar.gz"
    with tarfile.open(path, "w:gz") as tar:
        tar.add(ROOT / "pb_timelapse", arcname=f"{NAME}/pb_timelapse", filter=lambda t: None if "__pycache__" in t.name else t)
    print(path)


if __name__ == "__main__":
    build(Path(sys.argv[1] if len(sys.argv) > 1 else "dist"))
