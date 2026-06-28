#!/usr/bin/env python3
"""Validate repository skills without third-party dependencies."""

from __future__ import annotations

import ast
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_FRONTMATTER = {"name", "description"}
REQUIRED_INTERFACE = {"display_name", "short_description", "default_prompt"}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_simple_yaml_block(text: str, path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            fail(f"{path}: unsupported metadata line: {line!r}")
        key, value = stripped.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path}: unterminated YAML frontmatter")
    return parse_simple_yaml_block(text[4:end], path)


def parse_openai_yaml(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "interface:":
        fail(f"{path}: expected top-level interface mapping")
    body = "\n".join(line[2:] for line in lines[1:] if line.startswith("  "))
    return parse_simple_yaml_block(body, path)


def validate_skill(skill_dir: Path) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        fail(f"{skill_dir}: missing SKILL.md")

    metadata = parse_frontmatter(skill_file)
    missing = REQUIRED_FRONTMATTER - metadata.keys()
    if missing:
        fail(f"{skill_file}: missing metadata keys: {', '.join(sorted(missing))}")
    if metadata["name"] != skill_dir.name:
        fail(f"{skill_file}: name must match directory name {skill_dir.name!r}")
    if len(metadata["description"].split()) < 12:
        fail(f"{skill_file}: description is too short to trigger reliably")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if openai_yaml.exists():
        interface = parse_openai_yaml(openai_yaml)
        missing_interface = REQUIRED_INTERFACE - interface.keys()
        if missing_interface:
            fail(f"{openai_yaml}: missing interface keys: {', '.join(sorted(missing_interface))}")

    scripts_dir = skill_dir / "scripts"
    if scripts_dir.exists():
        for script in scripts_dir.glob("*.py"):
            ast.parse(script.read_text(encoding="utf-8"), filename=str(script))


def main() -> None:
    if not SKILLS_DIR.exists():
        fail("missing skills directory")
    skill_files = sorted(SKILLS_DIR.glob("**/SKILL.md"))
    if not skill_files:
        fail("no skills found")
    for skill_file in skill_files:
        validate_skill(skill_file.parent)
    print(f"validated {len(skill_files)} skill(s)")


if __name__ == "__main__":
    main()
