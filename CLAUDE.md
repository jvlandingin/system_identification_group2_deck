# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains presentation decks for **Chapters 8 and 10** from "System Identification: Theory for the User" (2nd Edition) by Lennart Ljung.

**Scope:** This group project covers Chapters 8 and 10, with presentations separated into individual files for better manageability.

The project uses Quarto to generate reveal.js presentation slides from the textbook content, enabling collaborative editing without requiring R or specialized IDEs.

## Current Status

### Chapter 8: Convergence and Consistency
**File:** `presentation_deck_chapter8.qmd` (~41 slides)

**Completed:**
- Section 8.5: Frequency-Domain Description of the Limit Model
  - Motivation for understanding model misfit
  - Data from arbitrary systems (Wiener filter assumption)
  - The true system (Assumption S1)
  - Open-loop and closed-loop cases
  - Expression for V̄(θ) in frequency domain
  - Example 8.5: Fitting a first-order model to second-order system
  - Key insights on model structure selection

### Chapter 10: Computing the Estimate
**File:** `presentation_deck_chapter10.qmd` (97 KB)

**Completed Sections:**
- Chapter 10 Overview
- **Section 10.1: Linear Regressions and Least Squares**
  - Normal equations
  - QR factorization approach
  - Numerical stability discussion
  - Augmented matrix method
  - Initial conditions handling
  - Levinson algorithm with detailed computational complexity analysis

- **Section 10.2: Numerical Solution by Iterative Search Methods** ✅ Recently Enhanced
  - When analytical solutions fail
  - Newton's method and Hessian computation
  - Gradient formula and computational burden
  - Steepest descent method
  - Gauss-Newton method and Hessian approximation
  - Levenberg-Marquardt method with adaptive λ strategy
  - Solving correlation equations

- **Section 10.5: Local Solutions and Initial Values**
  - Local minima in iterative optimization
  - Multi-start strategies
  - Initialization procedures for different model types

**Content Quality Standards:**
- Comprehensive speaker notes with Greek letter pronunciations (θ, φ, κ, λ, etc.)
- Technical term explanations (condition number, quadratic norm, Hessian, etc.)
- Step-by-step mathematical derivations
- Intuitive analogies and visual explanations
- Concrete numerical examples with ASCII diagrams
- **Balance between slide content and speaker notes** - key information visible on slides, detailed explanations in notes

## Key Commands

### Rendering the Presentations

**Chapter 8:**
```bash
quarto render presentation_deck_chapter8.qmd
```

**Chapter 10:**
```bash
quarto render presentation_deck_chapter10.qmd
```

**Both chapters:**
```bash
quarto render presentation_deck_chapter8.qmd && quarto render presentation_deck_chapter10.qmd
```

### Preview with Auto-reload
```bash
quarto preview presentation_deck_chapter8.qmd
quarto preview presentation_deck_chapter10.qmd
```

### Export to PDF
```bash
quarto render presentation_deck_chapter8.qmd --to pdf
quarto render presentation_deck_chapter10.qmd --to pdf
```

## Project Structure

**Main Presentation Files:**
- `presentation_deck_chapter8.qmd` - Chapter 8 presentation (Section 8.5)
- `presentation_deck_chapter10.qmd` - Chapter 10 presentation (Sections 10.1, 10.2, 10.5)
- `presentation_deck.qmd` - Original combined presentation (archived, use separate files instead)

**Generated Output:**
- `presentation_deck_chapter8.html` - Chapter 8 HTML presentation
- `presentation_deck_chapter10.html` - Chapter 10 HTML presentation
- `presentation_deck_chapter*_files/` - Supporting files for reveal.js presentations

**Source Materials:**
- `System Identification_...pdf` - Source textbook (Ljung, 2nd Edition)

**Configuration:**
- `styles.css` - Custom CSS for presentation styling
- `CLAUDE.md` - This file

**Style Guidelines (in `.claude/prompts/`):**
- `speaker_prompt_v2.md` - Guidelines for writing speaker notes (natural speech, click indicators, formula descriptions)
- `slide_structure_v1.md` - Guidelines for slide content limits and overflow prevention (E/B/H/R audit method)

## Content Development Workflow

The typical workflow involves:
1. User provides screenshots from specific chapters/sub-chapters of the textbook
2. Claude explains the content to help user understand the concepts
3. Creating presentation slides in the appropriate chapter file (`presentation_deck_chapter8.qmd` or `presentation_deck_chapter10.qmd`) based on that understanding
4. User reviews slides and requests clarifications or improvements
5. Claude refines slides based on feedback

## Slide Audit Workflow

When auditing existing slides for compliance:
1. **Read slides in batches** (e.g., slides 1-20, then 21-40)
2. **Check each slide against the rules:**
   - Does it have a brief intro in speaker notes?
   - Do speaker notes echo slide content first?
   - Are click indicators present for `. . .` reveals?
   - Are formulas described (not read literally)?
   - Is bullet point spacing correct (blank lines)?
   - Does content fit without overflow?
3. **List all violations** with slide numbers
4. **Fix systematically** - address each violation one by one
5. **Re-render and verify** - check the HTML output visually

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

**IMPORTANT - BULLET POINT SPACING**: Always include a blank line after headers and between each bullet point—this applies to **both speaker notes AND slide content**. Without blank lines, Quarto renders all bullets on a single line.

```markdown
❌ Bad (renders on single line):
-   First bullet
-   Second bullet
-   Third bullet

✅ Good (renders correctly):
-   First bullet

-   Second bullet

-   Third bullet
```

## Presentation Style Guidelines

1. **Mathematical Notation:**
   - Equations are styled with italics via custom CSS
   - Use MathJax for rendering (`html-math-method: mathjax` in YAML)
   - Greek letters should include pronunciation guides in speaker notes

2. **Content Distribution (IMPORTANT):**
   - **Slides should be self-contained and informative** - viewers should understand main points without speaker notes
   - Move key information, examples, and explanations from speaker notes to slides
   - Use incremental reveals (`. . .`) to control information flow on slides
   - Speaker notes should provide deeper context, not essential content
   - **Bad**: Formula on slide, all explanation in notes
   - **Good**: Formula with component breakdown on slide, additional context in notes

3. **Explanations:**
   - Break complex concepts into multiple slides
   - Include concrete numerical examples where helpful
   - Add visual intuition with tables, ASCII diagrams, or pseudocode blocks
   - Use comparison tables to show trade-offs between methods
   - Provide "why it matters" context on slides, not just in notes

4. **Speaker Notes (CRITICAL - Follow These Rules):**

   **Core Principle**: The audience should see and hear the same thing. Don't make them process two different phrasings simultaneously—this creates cognitive dissonance.

   **Rule 1: Echo the Slide Content FIRST, Then Expand**
   - **Read what they see, then explain.** Always echo the slide text before adding context.
   - Repeat key headings and bullet points from the slide exactly in the speaker notes
   - Only AFTER echoing can you add brief explanations (1-2 sentences max)
   - Never paraphrase slide content with different words—use the same words

   **❌ Bad (audience reads one thing, hears another):**
   > Slide says: "R(N) — Sample covariance matrix"
   > Notes say: "One over N times the sum of φ times φ-transpose..."

   **✅ Good (echo first, then expand):**
   > Slide says: "R(N) — Sample covariance matrix"
   > Notes say: "R(N) is the sample covariance matrix of regressors φ (fie). This measures how the regression vectors correlate with each other."

   **Rule 2: Start Each Slide with a Brief Intro**
   Begin speaker notes with a short transitional phrase (1 sentence):
   - "Now let's look at..."
   - "Here's the key insight..."
   - "Let me explain what this means..."

   **Rule 3: Add Click Indicators**
   - Use `[→ Click for...]` to mark where `. . .` (incremental reveals) appear on slide
   - Example: `[→ Click to reveal approach]`

   **Rule 4: Don't Read Formulas Literally**
   - Describe meaning, not symbols: "The formula shows we use transfer function G₀..."
   - Include pronunciation guides: θ (THAY-tah), φ (fie), ψ (sigh), ε (EP-sih-lon), κ (CAP-uh), λ (LAM-duh), ρ (row), μ (mew)
   - **Reference the slide instead of repeating**: Use phrases like "The proof is on the slide" or "As shown in the formula above" rather than re-explaining what's already visible

   **Rule 5: What NOT to Do**
   - ❌ Don't explain questions answered on the same slide
   - ❌ Don't add lengthy additional explanations
   - ❌ Don't invent "key insights" or content not on the slide
   - ❌ Don't read formulas symbol-by-symbol

5. **Slide Organization:**
   - Start with high-level overview
   - Progress from simple to complex
   - Use section headers with background colors for major transitions
   - End sections with summary slides
   - Split dense slides into multiple focused slides when needed

6. **Slide Overflow Prevention (CRITICAL):**
   - **Max 1 major equation per slide** - two equations almost always overflow
   - Use E/B/H/R audit: Equations, Bullets, Headers, Reveals
   - Overflow likely if: E ≥ 2, or E=1 AND B > 3, or H > 2
   - When in doubt, split the slide
   - See `.claude/prompts/slide_structure_v1.md` for full audit checklist

   **How to Split Overflowing Slides:**
   - Split by concept: Part 1 shows "what", Part 2 shows "why" or "how"
   - Split by equation: One equation per slide with its explanation
   - Split by comparison: One side per slide (e.g., "Before" slide, "After" slide)
   - Keep slide titles related: "Topic: Part 1" and "Topic: Part 2" or "Topic" and "Topic (continued)"
   - Ensure each split slide can stand alone—don't leave orphan bullets

## Common Pitfalls to Avoid

Based on audit experience, these issues frequently occur:

1. **Missing blank lines between bullets** - Most common issue. Always add blank lines.
2. **Speaker notes that read formulas literally** - Say "The formula shows..." not "y equals theta times phi..."
3. **Dense speaker notes** - If it's hard to read aloud, simplify. Reference the slide instead of repeating.
4. **Two equations on one slide** - Almost always overflows. Split into two slides.
5. **Callout boxes + equations** - Combination often overflows. Choose one or simplify.
6. **Missing click indicators** - Every `. . .` on a slide needs a corresponding `[→ Click...]` in notes.
7. **Invented content in notes** - Speaker notes should support slide content, not add new material.

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
- Levinson algorithm and reflection coefficients
- Lattice filters

**Section 10.2 Key Topics (Enhanced with better slide content):**
- When analytical solutions fail (examples on slides)
- Newton's method with Hessian structure visualized
- Gradient formula with component breakdown
- Nonlinear least-squares problem importance
- Steepest descent: pros/cons with visual intuition
- Gauss-Newton: Hessian approximation explained on slides
- Levenberg-Marquardt: adaptive λ strategy with pseudocode
- Comparison table of all three methods
- Correlation equations and Newton-Raphson

**Section 10.5 Key Topics:**
- Local vs. global minima
- Multi-start strategies
- Two sources of local minima (structural and sample-induced)
- Start-up procedures for black-box models
- IV method initialization
- Seeding strategy for nonlinear models
- Initial filter conditions