"""make.fun judged-artifact entry for irvan-excuse: writes the one-line artifact to /output/entry.txt."""
import os

TEXT = "I lost the bounty because I optimized for excellence; I'd like the excellence credited against next time's entry fee."

def write_artifact() -> None:
    out = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")
    assert 1 <= len(TEXT) <= 200, "entry text must be 1-200 characters"
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    write_artifact()
