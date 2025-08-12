import os
import shutil
import yaml
import pathlib

SOURCE_DIR = "."
DOCS_DIR = ".github/docs"
OVERRIDES_DIR = "overrides"
ASSETS_DIR = os.path.join(DOCS_DIR, "assets")
CUSTOM_CSS = os.path.join(ASSETS_DIR, "extra.css")

ALLOWED_EXT = (
    ".md",
    ".ipynb",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".py",
    ".txt",
    ".cpp",
    ".c",
    ".h",
    ".hpp",
    ".css",
)

CODE_WRAP_EXTS = (".cpp", ".c", ".h", ".hpp", ".py")
IGNORE_FILES = {
"generateDocs.py",
"generateREADME.py",
}


def wrap_code_as_md(src_path, dest_path):
    lang = pathlib.Path(src_path).suffix.lstrip(".")
    with open(src_path, "r", encoding="utf-8", errors="ignore") as src, open(
        dest_path, "w", encoding="utf-8"
    ) as md:
        md.write(f"# {os.path.basename(src_path)}\n\n")
        md.write(f"```{lang}\n")
        md.write(src.read())
        md.write("\n```")


def copy_docs():
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)

    os.makedirs(DOCS_DIR)

    for root, _, files in os.walk(SOURCE_DIR):
        if any(
            skip in root
            for skip in [DOCS_DIR, ".git", ".github", ".vscode", "site", OVERRIDES_DIR]
        ):
            continue

        rel_path = os.path.relpath(root, SOURCE_DIR)
        dest_path = os.path.join(DOCS_DIR, rel_path)
        os.makedirs(dest_path, exist_ok=True)

        folder_name = os.path.basename(root) if rel_path != "." else "Home"
        folder_name_clean = folder_name.replace(" ", "_")

        for file in files:
            src_file = os.path.join(root, file)
            filename_lower = file.lower()

            if file.lower().endswith(ALLOWED_EXT):
                if filename_lower == "readme.md":
                    new_md_name = (
                        f"{folder_name}.md" if rel_path != "." else "README.md"
                    )
                    shutil.copy2(src_file, os.path.join(dest_path, new_md_name))
                else:
                    shutil.copy2(src_file, os.path.join(dest_path, file))

                if (
                    file.lower().endswith(CODE_WRAP_EXTS)
                    and filename_lower != "readme.md"
                ):
                    md_name = os.path.splitext(file)[0] + ".md"
                    wrap_code_as_md(src_file, os.path.join(dest_path, md_name))


def ensure_custom_css():
    os.makedirs(ASSETS_DIR, exist_ok=True)

    if not os.path.exists(CUSTOM_CSS):
        with open(CUSTOM_CSS, "w", encoding="utf-8") as f:
            f.write(
                """
.md-main__inner {
    max-width: 2000px;
    margin-left: auto !important;
    margin-right: auto !important;
}

.md-content {
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    border-left: 1px solid rgba(64, 81, 181, 0.5) !important;
    border-right: 1px solid rgba(64, 82, 181, 0.5) !important;
}
"""
            )


def ensure_mkdocs_extra_css():
    if not os.path.exists("mkdocs.yml"):
        print("⚠ mkdocs.yml Not Found! 404")
        return

    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    extra_css_list = config.get("extra_css", [])

    css_rel_path = f"assets/{os.path.basename(CUSTOM_CSS)}"
    if css_rel_path not in extra_css_list:
        extra_css_list.append(css_rel_path)
        config["extra_css"] = extra_css_list

        with open("mkdocs.yml", "w", encoding="utf-8") as f:
            yaml.dump(config, f, sort_keys=False)

        print(f"✅ Added {CUSTOM_CSS} TO mkdocs.yml")


def scan_dir(base_dir):
    nav_entries = {}
    md_exts = (".md", ".ipynb")

    for root, dirs, files in os.walk(base_dir):
        dirs.sort()
        files.sort()

        md_files = [f for f in files if f.lower().endswith(md_exts)]
        if not md_files:
            continue

        rel_dir = os.path.relpath(root, base_dir)
        section_name = os.path.basename(root) if rel_dir != "." else "Home"

        if rel_dir == ".":
            parent_name = "."
        else:
            parent_name = os.path.basename(os.path.dirname(root))
            if parent_name == os.path.basename(base_dir):
                parent_name = "."

        pages = []

        folder_readme = f"{section_name}.md" if rel_dir != "." else "README.md"

        if folder_readme in md_files:
            readme_path = (
                os.path.join(rel_dir, folder_readme)
                if rel_dir != "."
                else folder_readme
            )
            pages.append({section_name: readme_path})
            for f in sorted(md_files):
                if f == folder_readme:
                    continue
                title = os.path.splitext(f)[0].replace("-", " ")
                pages.append({title: os.path.join(rel_dir, f)})
        else:
            for f in sorted(md_files):
                title = os.path.splitext(f)[0].replace("-", " ")
                pages.append({title: os.path.join(rel_dir, f)})

        if parent_name != ".":
            nav_entries.setdefault(parent_name, []).append({section_name: pages})
        else:
            nav_entries.setdefault(section_name, pages)

    final_nav = [{key: value} for key, value in nav_entries.items()]
    return final_nav


def build_mkdocs(nav_entries):
    return {
        "site_name": "Python Programs",
        "docs_dir": ".github/docs",
        "theme": {
            "name": "material",
            "palette": [
                {
                    "scheme": "default",
                    "primary": "indigo",
                    "accent": "pink",
                    "toggle": {
                        "icon": "material/weather-night",
                        "name": "Switch to dark mode",
                    },
                },
                {
                    "scheme": "slate",
                    "primary": "indigo",
                    "accent": "pink",
                    "toggle": {
                        "icon": "material/weather-sunny",
                        "name": "Switch to light mode",
                    },
                },
            ],
            "features": [
                "navigation.instant",
                "navigation.expand",
                "navigation.sections",
                "navigation.path",
                "navigation.prune",
                "search.highlight",
                "search.suggest",
                "content.code.copy",
            ],
        },
        "markdown_extensions": [
            "admonition",
            "codehilite",
            "footnotes",
            "tables",
            "toc",
            {
                "pymdownx.highlight": {
                    "anchor_linenums": True,
                    "linenums": True,
                    "linenums_style": "table",
                    "use_pygments": True,
                }
            },
            "pymdownx.superfences",
        ],
        "extra_css": [f"assets/{os.path.basename(CUSTOM_CSS)}"],
        "plugins": ["search", "offline", "tags"],
        "repo_url": "https://github.com/SpreadSheets600/Python-Programs",
        "repo_name": "Python-Programs",
        "nav": nav_entries,
    }


if __name__ == "__main__":
    copy_docs()
    ensure_custom_css()
    ensure_mkdocs_extra_css()

    nav = scan_dir(DOCS_DIR)
    config = build_mkdocs(nav)

    with open("mkdocs.yml", "w") as f:
        yaml.dump(config, f, sort_keys=False)

    print("✅ mkdocs.yml generated and docs folder prepared with custom CSS support")
