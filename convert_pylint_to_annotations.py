import json

with open("pylint.json") as f:
    issues = json.load(f)

for issue in issues:
    print(f"::error file={issue['path']},line={issue['line']}::{issue['message']}")

