#!/usr/bin/env python3
"""Find slides in Chapter 10 that are missing SCRIPT sections."""

import re

def find_slides_without_scripts(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by slide markers
    slides = re.split(r'^## ', content, flags=re.MULTILINE)

    missing_scripts = []

    for i, slide in enumerate(slides):
        if i == 0:  # Skip YAML header
            continue

        # Get slide title (first line)
        lines = slide.split('\n', 1)
        title = lines[0].strip()

        # Check if slide has SCRIPT section
        if '**SCRIPT:**' not in slide:
            missing_scripts.append((i, title))

    return missing_scripts

if __name__ == '__main__':
    import sys
    import io

    # Force UTF-8 encoding for output
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    filename = r'c:\Users\JV Landingin\Documents\20-29 Learning\23 University\23.11 UPD DS Program\DS 397 System Identification\system_identification_group2_deck\presentation_deck_chapter10.qmd'

    missing = find_slides_without_scripts(filename)

    print(f"Total slides missing SCRIPT sections: {len(missing)}\n")
    print("Slides without scripts:")
    print("=" * 80)
    for idx, title in missing:
        print(f"{idx:2d}. {title}")
