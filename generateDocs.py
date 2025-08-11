import os
import yaml

def scan_dir(base_dir):
    nav_entries = []

    for root, dirs, files in os.walk(base_dir):
        dirs.sort()
        files.sort()

        md_files = [f for f in files if f.endswith(".md") or f.endswith(".ipynb")]
        if not md_files:
            continue

        rel_dir = os.path.relpath(root, ".")
        section_name = os.path.basename(root) if rel_dir != "." else "Home"

        if rel_dir == ".":
            # Top-level README.md
            for f in md_files:
                if f.lower() == "readme.md":
                    nav_entries.append({ "Home": f })
        else:
            pages = []
            for f in md_files:
                title = os.path.splitext(f)[0]
                pages.append({ title: os.path.join(rel_dir, f) })
            nav_entries.append({ section_name: pages })

    return nav_entries

def build_mkdocs(nav_entries):
    config = {
        "site_name": "My Repo Docs",
        "theme": {
            "name": "material",
            "features": [
                "navigation.expand",
                "navigation.sections",
                "search.highlight",
                "search.suggest"
            ]
        },
        "plugins": [
            "search",
            "mkdocs-jupyter",
            "awesome-pages"
        ],
        "nav": nav_entries
    }
    return config

if __name__ == "__main__":
    nav = scan_dir(".")
    config = build_mkdocs(nav)
    with open("mkdocs.yml", "w") as f:
        yaml.dump(config, f, sort_keys=False)
    print("✅ mkdocs.yml generated")
