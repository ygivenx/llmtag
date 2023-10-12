"""
Main entry point for the llmtag command line interface.
"""
import argparse
from pathlib import Path
from .llm_label import get_note_label


def main():
    """
    Command line args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file path for note text")
    parser.add_argument("--context-length", help="context length", default=512, type=int)
    args = parser.parse_args()
    fp = Path(args.file)

    if fp.exists():
        with open(args.file, "r") as f:
            note = f.read()
    else:
        raise FileNotFoundError(f"File {args.file} not found")

    res = get_note_label(note, n_ctx=args.context_length)
    print(res)


if __name__ == "__main__":
    main()
