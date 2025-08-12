import argparse
from pathlib import Path


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


def generate_readme_for_folder(folder_path, file_pattern="Program-*.py"):
    readme_path = folder_path / "README.md"

    if readme_path.exists():
        print(f"Skipping {folder_path.name}, README.md Already Exsist.")
        return

    folder_name_cap = " ".join(word.capitalize() for word in folder_path.name.split())

    md_lines = [f"# Programming Assignment : {folder_name_cap}", "", "---", ""]

    prog_files = sorted(folder_path.glob(file_pattern))
    if not prog_files:
        print(
            f"Warning : No Files Matching The Pattern '{file_pattern}' Found In {folder_path}"
        )
        return

    for prog_file in prog_files:
        print(f"Processing File : {prog_file.name}")
        title, code = extract_title_and_code(prog_file)

        md_lines.append(f"## {title}")
        md_lines.append("")
        md_lines.append("```python")
        md_lines.append(code)
        md_lines.append("```")
        md_lines.append("")
        md_lines.append("OUTPUT :")
        md_lines.append("")
        md_lines.append("```bash")
        md_lines.append("")
        md_lines.append("```")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"Generated {readme_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate README.md Files For Code Folders."
    )
    parser.add_argument(
        "base_dir", type=str, help="Base Directory To Scan For Code Folders"
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default="Program-*.py",
        help="File Glob Pattern to Match Program Files ( efault: 'Program-*.py' )",
    )
    parser.add_argument(
        "--filter",
        type=str,
        default=None,
        help="Optional : Only Process Folders Starting with This String",
    )
    args = parser.parse_args()

    base_path = Path(args.base_dir)
    if not base_path.exists() or not base_path.is_dir():
        print(
            f"Error : Base Directory '{base_path}' Does Not Exist or Is Not a Directory."
        )
        return

    for folder in sorted(base_path.iterdir()):
        if folder.is_dir():
            if args.filter:
                if not folder.name.lower().startswith(args.filter.lower()):
                    continue

            generate_readme_for_folder(folder, file_pattern=args.pattern)


if __name__ == "__main__":
    main()
