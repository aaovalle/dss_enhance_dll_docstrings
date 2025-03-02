import re

from documentation import Documentation, Section


def parse_docs(md_content: str) -> Documentation:
    sections: list[Section] = []
    stack = []

    pattern = re.compile(
        r"^(?P<indent>\s*)-\s+\[(?P<title>[^\]]+)\]\(<?(?P<file>[^)>]+)>?\)"
    )

    for line in md_content.splitlines():
        line = line.rstrip()
        if not line.strip().startswith("-"):
            continue

        match = pattern.match(line)
        if not match:
            continue

        indent = match.group("indent")
        level = len(indent) // 2
        title = match.group("title").strip()
        file = match.group("file").strip()

        section = Section(title=title, file=file)

        if level == 0:
            sections.append(section)
            stack = [section]
        else:
            while len(stack) > level:
                stack.pop()
            parent = stack[-1]
            parent.children.append(section)
            stack.append(section)

    return Documentation(sections=sections)


if __name__ == "__main__":
    import json
    from pathlib import Path

    data_path = Path("markdown")
    md_filename = "OpenDSS Documentation.md"
    json_filename = Path("docs.json")

    with (data_path / md_filename).open("r", encoding='utf-8') as f:
        md_content = f.read()
        documentation = parse_docs(md_content=md_content)

    og_md_files = {f.name for f in data_path.glob("*.md") if f.name != md_filename}
    md_files = documentation.get_unique_filenames()
    assert og_md_files == md_files, "Mismatched documentation sections"

    with json_filename.open("w") as f:
        json.dump(documentation.model_dump(), f, indent=4)