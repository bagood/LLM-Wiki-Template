# /// script
# requires-python = ">=3.12"
# dependencies = ["PyYAML==6.0.3"]
# ///
"""Count distinct accepted source IDs that substantively engage with each topic."""
import argparse
import json
import sys
from common import ContractError, collect_mentions, load_manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiki-dir", required=True)
    args = parser.parse_args()
    try:
        result = collect_mentions(args.wiki_dir)
        result["threshold"] = load_manifest(args.wiki_dir)["threshold"]
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (ContractError, OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
