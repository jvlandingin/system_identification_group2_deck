# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a presentation deck for **Chapter 10: "Computing the Estimate"** from "System Identification: Theory for the User" (2nd Edition) by Lennart Ljung.

**Scope:** This group project covers Chapters 8 and 10. This repository is assigned to the subgroup working on **Chapter 10 only**.

The project uses Quarto to generate reveal.js presentation slides from the textbook content, enabling collaborative editing without requiring R or specialized IDEs.

## Current Status

**Completed Sections:**
- Chapter 10 Overview
- Section 10.1: Linear Regressions and Least Squares
  - Normal equations
  - QR factorization approach
  - Numerical stability discussion
  - Augmented matrix method
  - Initial conditions handling

**In Progress:**
- Section 10.2 (future work)

**Completed in Section 10.1:**
- All slides created for Section 10.1
- Comprehensive speaker notes including:
  - Greek letter pronunciations (θ, φ, κ, etc.)
  - Technical term explanations (condition number, quadratic norm, etc.)
  - Step-by-step mathematical derivations
  - Intuitive analogies and visual explanations
  - Concrete numerical examples with ASCII diagrams

## Key Commands

### Rendering the Presentation
```bash
quarto render presentation_deck.qmd
```

### Preview the Presentation (with auto-reload)
```bash
quarto preview presentation_deck.qmd
```

### Export to PDF
```bash
quarto render presentation_deck.qmd --to pdf
```

## Project Structure

- `presentation_deck.qmd` - Main Quarto document containing the reveal.js presentation slides
- `presentation_deck.html` - Generated HTML presentation output
- `presentation_deck_files/` - Supporting files for the reveal.js presentation (plugins, libraries)
- `System Identification_...pdf` - Source textbook (Ljung, 2nd Edition)

## Content Development Workflow

The typical workflow involves:
1. User provides screenshots from specific chapters/sub-chapters of the textbook
2. Claude explains the content to help user understand the concepts
3. Creating presentation slides in `presentation_deck.qmd` based on that understanding
4. User reviews slides and requests clarifications or improvements
5. Claude refines slides based on feedback

## Quarto Reveal.js Format Notes

The presentation uses Quarto's reveal.js format. Key syntax:
- Slides are separated by `##` headers (with `------------------------------------------------------------------------` dividers)
- Use `$$` for display math equations or `$...$` for inline math
- The YAML header configures the reveal.js output format and theme
- Slide-specific options can be set using `{.attribute}` syntax
- Use `. . .` for incremental reveals within a slide

### Speaker Notes Format

Speaker notes are added using the following format:

```markdown
::: notes
**Topic header:**

Brief explanation paragraph.

**Another header:**

- First bullet point

- Second bullet point (note: blank line between bullets)

- Third bullet point
:::
```

**IMPORTANT**: Always include a blank line after headers and between each bullet point in speaker notes for proper formatting.

## Presentation Style Guidelines

1. **Mathematical Notation:**
   - Equations are styled with italics via custom CSS
   - Use MathJax for rendering (`html-math-method: mathjax` in YAML)
   - Greek letters should include pronunciation guides in speaker notes

2. **Explanations:**
   - Break complex concepts into multiple slides
   - Use incremental reveals (`. . .`) to control information flow
   - Include concrete numerical examples where helpful
   - Add visual intuition with ASCII diagrams in code blocks

3. **Speaker Notes:**
   - Explain non-obvious terminology
   - Provide step-by-step derivations
   - Include pronunciation guides for Greek letters
   - Add context about why concepts matter
   - Suggest what to emphasize during presentation

4. **Slide Organization:**
   - Start with high-level overview
   - Progress from simple to complex
   - Use section headers with background colors for major transitions
   - End sections with summary slides

## Technical Concepts Covered

**Section 10.1 Key Topics:**
- Least Squares (LS) estimation
- Normal equations: R(N)θ = f(N)
- Ill-conditioning and numerical stability
- QR factorization/decomposition
- Condition number (κ) and why it matters
- Augmented matrix approach: [Φ Y]
- Orthonormal transformations
- Back-substitution for triangular systems
- Initial conditions (prewindowing vs. postwindowing)
- Yule-Walker equations