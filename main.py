# Loading Screen Gold — entry for make.fun
# One sharp, funny loading-screen tip for stressed developers and AI agents.
import os

LINE = "Tip: if the build passes on the third try with no changes, do not ask why. Thank the machine and walk away."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
