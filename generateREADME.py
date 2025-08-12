from pathlib import Path

BASE_DIR = Path(r"Homework")

def extract_title_and_code(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    title = None
    code_lines = []
    for line in lines:
        stripped = line.strip()
        if title is None and stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
        else:
            code_lines.append(line)

    if title is None:
        title = filepath.stem.replace("-", " ").title()

    return title, "".join(code_lines).strip()


def generate_readme_for_homework(homework_path):
    homework_name = homework_path.name
    readme_path = homework_path / "README.md"

    md_lines = [f"# Programming Assignment: {homework_name}", "", "---", ""]

    for prog_file in sorted(homework_path.glob("Program-*.py")):
        title, code = extract_title_and_code(prog_file)

        md_lines.append(f"## {title}")
        md_lines.append("")
        md_lines.append("```python")
        md_lines.append(code)
        md_lines.append("```")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"Generated {readme_path}")


def main():
    print("Generating README files for Homework folders...")
    for folder in sorted(BASE_DIR.iterdir()):
        if folder.is_dir() and folder.name.lower().startswith("homework"):
            generate_readme_for_homework(folder)

            print(f"Processed {folder.name}")
if __name__ == "__main__":
    main()
