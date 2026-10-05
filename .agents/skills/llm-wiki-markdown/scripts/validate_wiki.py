# /// script
# requires-python = ">=3.12"
# dependencies = ["PyYAML==6.0.3"]
# ///
"""Report base OKF structure separately from workspace evidence and quality."""
import argparse
import json
import sys
from common import ContractError, validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiki-dir", required=True, help="Workspace; in bundle scope, may instead be bundle root")
    parser.add_argument("--scope", choices=["workspace", "bundle"], default="workspace")
    parser.add_argument("--no-indexes", action="store_true", help="Validate content before generating indexes")
    args = parser.parse_args()
    try:
        result = validate(args.wiki_dir, args.scope, not args.no_indexes)
        print(json.dumps(result, indent=2, default=str))
        return 0 if result["valid"] else 1
    except (ContractError, OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
