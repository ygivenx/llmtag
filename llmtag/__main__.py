"""
Main entry point for the llmtag command line interface.
"""
import argparse
from pathlib import Path
import pandas as pd
from .llm_label import get_note_label
import csv


def main():
    """
    Command line args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file path for note text")
    parser.add_argument("--context-length", help="context length", default=512, type=int)
    parser.add_argument("--out-file", help="results", default="out.csv")
    args = parser.parse_args()
    fp = Path(args.file)

    res = []
    labels = []
    reasons = []
    if fp.exists():
        if fp.suffix == ".csv":
            df = pd.read_csv(fp)
            print(df.head())
            for i, row in df.iterrows():
                note = row["notes"]
                ser = get_note_label(note, n_ctx=args.context_length)
                labels.append(ser["label"])
                reasons.append(ser["reason"])
            df["llm_label"] = labels
            df["llm_reasons"] = reasons
            print(df.to_markdown())
            df.to_csv(args.out_file, index=False, quoting=csv.QUOTE_MINIMAL)
        
        else:
            with open(args.file, "r") as f:
                note = f.read()
                res.append(get_note_label(note, n_ctx=args.context_length))
                return res
    else:
        raise FileNotFoundError(f"File {args.file} not found")


if __name__ == "__main__":
    main()
