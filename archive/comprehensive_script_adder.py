#!/usr/bin/env python3
"""
Comprehensive script to add natural, conversational presentation scripts
to ALL slides in Chapter 10 that don't already have **SCRIPT:** sections.
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def find_slides_without_scripts(content):
    """Find all slide headings that don't have SCRIPT sections."""
    # Split content into sections by ##
    pattern = r'##\s+([^\n{]+?)(?:\s+\{[^}]+\})?\s*\n'
    slides = []

    for match in re.finditer(pattern, content):
        heading = match.group(1).strip()
        start_pos = match.end()

        # Find the next ## or end of file
        next_match = re.search(r'\n##\s+', content[start_pos:])
        if next_match:
            end_pos = start_pos + next_match.start()
        else:
            end_pos = len(content)

        slide_content = content[start_pos:end_pos]

        # Check if it has SCRIPT
        if '**SCRIPT:**' not in slide_content:
            slides.append((heading, start_pos, end_pos, slide_content))

    return slides

def generate_script(heading, slide_content):
    """Generate a natural, conversational script based on slide heading and content."""

    #Extract key points from slide
    has_equation = bool(re.search(r'\$\$[^$]+\$\$', slide_content))
    has_bullets = bool(re.search(r'^\s*[-*]\s+', slide_content, re.MULTILINE))
    has_incremental = '. . .' in slide_content

    # Generate script based on heading keywords
    script_lines = []

    # Opening
    if "Summary" in heading:
        script_lines.append(f"Let's summarize what we've covered here. ")
    elif "Overview" in heading:
        script_lines.append(f"Let me give you an overview of {heading.lower()}. ")
    elif "Example" in heading:
        script_lines.append(f"Now let's look at a concrete example. ")
    elif "Why" in heading:
        script_lines.append(f"So you might be wondering - why does this matter? ")
    elif "Understanding" in heading:
        script_lines.append(f"Let's make sure we really understand this. ")
    else:
        script_lines.append(f"Now let's talk about {heading.lower()}. ")

    # Reference equations if present
    if has_equation:
        script_lines.append("So this equation here shows us the key relationship. ")

    # Reference bullets if present
    if has_bullets:
        script_lines.append("There are a few important points to note. ")

    # Add transition if incremental
    if has_incremental:
        script_lines.append("Let me walk you through this step by step. ")

    # Closing
    script_lines.append("This is going to be important for what comes next.")

    return "".join(script_lines)

def add_script_after_notes_header(notes_section, script):
    """Add script right after ::: notes header."""
    return notes_section.replace('::: notes\n', f'::: notes\n**SCRIPT:**\n\n{script}\n\n')

def add_script_to_slide_content(slide_content, script):
    """Add script to slide content, creating notes section if needed."""
    # Check if notes section exists
    if '::: notes' in slide_content:
        # Add script at the beginning of existing notes
        return add_script_after_notes_header(slide_content, script)
    else:
        # Find the last divider line before next slide
        # Add notes section before the divider
        lines = slide_content.split('\n')

        # Find last non-empty line
        insert_pos = len(lines)
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip() and not lines[i].startswith('---'):
                insert_pos = i + 1
                break

        # Insert notes section
        notes = [
            '',
            '::: notes',
            '**SCRIPT:**',
            '',
            script,
            ':::',
            ''
        ]

        lines[insert_pos:insert_pos] = notes
        return '\n'.join(lines)

def main():
    filepath = r"c:\Users\JV Landingin\Documents\20-29 Learning\23 University\23.11 UPD DS Program\DS 397 System Identification\system_identification_group2_deck\presentation_deck_chapter10.qmd"

    print("Reading file...")
    content = read_file(filepath)

    print("Finding slides without scripts...")
    slides_without_scripts = find_slides_without_scripts(content)

    print(f"Found {len(slides_without_scripts)} slides without scripts")

    if not slides_without_scripts:
        print("All slides already have scripts!")
        return

    print("\nAdding scripts...")
    # Process from end to beginning to maintain positions
    for heading, start_pos, end_pos, slide_content in reversed(slides_without_scripts):
        script = generate_script(heading, slide_content)
        new_slide_content = add_script_to_slide_content(slide_content, script)
        content = content[:start_pos] + new_slide_content + content[end_pos:]
        print(f"  + Added script to: {heading}")

    print("\nWriting updated file...")
    write_file(filepath, content)

    print(f"\nSuccessfully added scripts to {len(slides_without_scripts)} slides!")

if __name__ == "__main__":
    main()
