# System Identification: Chapter 8 & Chapter 10 Presentation Deck

A collaborative presentation deck covering **Chapter 8: "Convergence and Consistency"** and **Chapter 10: "Computing the Estimate"** from "System Identification: Theory for the User" (2nd Edition) by Lennart Ljung.

**Sections covered in this deck:**

-   Section 10.1: Linear Regressions and Least Squares

-   QR Factorization approach for numerical stability

-   Initial conditions handling

## Quick Start

### Prerequisites

-   **Quarto** (free, no R required)
    -   Download: https://quarto.org/docs/get-started/
    -   Installation takes \~2 minutes

### Running the Presentation

**1. Preview with auto-reload (recommended for editing):**

``` bash
quarto preview presentation_deck.qmd
```

This opens the presentation in your browser and auto-refreshes as you edit.

**2. Render to HTML:**

``` bash
quarto render presentation_deck.qmd
```

Creates `presentation_deck.html`

**3. Render to PDF:**

``` bash
quarto render presentation_deck.qmd --to pdf
```

Creates `presentation_deck.pdf`

## File Structure

```         
├── presentation_deck.qmd      # Source file (EDIT THIS)
├── presentation_deck.html     # Generated HTML output
├── presentation_deck.pdf      # Generated PDF output
├── presentation_deck_files/   # Supporting files (auto-generated)
├── CLAUDE.md                  # Technical documentation for future development
├── README.md                  # This file
└── System Identification...pdf # Textbook reference
```

## Editing the Presentation

The presentation is written in **Quarto markdown** (`.qmd`). Edit `presentation_deck.qmd` with any text editor:

-   VS Code, Positron, Rstudio (recommended)

-   Sublime Text

-   Notepad

-   Any text editor

### Basic Syntax

**Slides are separated by:**

``` markdown
------------------------------------------------------------------------
```

**Slide headers:**

``` markdown
## Slide Title
```

**Math equations (LaTeX):**

``` markdown
Inline: $\theta$
Display: $$\hat{\theta}_N^{LS} = R^{-1}(N)f(N)$$
```

**Speaker notes (visible in presenter mode):**

``` markdown
::: notes
**Important concept:**

- First bullet point

- Second bullet point (note: blank line between bullets)
:::
```

**Incremental reveals (appear on click):**

``` markdown
. . .

Next content appears on next click
```

For full Quarto documentation: https://quarto.org/docs/presentations/revealjs/

## Collaboration Workflow

1.  **Edit** `presentation_deck.qmd`
2.  **Preview** with `quarto preview` to see changes
3.  **Commit** your changes: `git add presentation_deck.qmd && git commit -m "Your message"`
4.  **Push** to GitHub: `git push`

## Content Overview

### Section 10.1: Linear Regressions and Least Squares

**Topics covered:**

-   Normal equations: $R(N)\hat{\theta}_N^{LS} = f(N)$

-   Numerical stability challenges

-   QR factorization as a solution

-   Condition number and why matrix multiplication is problematic - Augmented matrix approach - Orthonormal transformations

-   Back-substitution on triangular systems

-   Initial conditions (prewindowing vs. postwindowing)

-   Yule-Walker equations

**Key insights:**

-   $\kappa(R_1) = \sqrt{\kappa(R(N))}$ → square root improvement in conditioning

-   Never compute $\mathbf{\Phi}^T\mathbf{\Phi}$ directly

-   Implement via $R_0$ only to avoid large matrix storage

## Viewing Presenter Notes

In the rendered HTML presentation: 1. Press **S** to open the speaker view 2. Notes appear in a separate window

## Questions?

Refer to:

-   `CLAUDE.md` for technical implementation details

-   Quarto docs: https://quarto.org/

-   Section 10 of "System Identification: Theory for the User" (Ljung, 2nd Edition)