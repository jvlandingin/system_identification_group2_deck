# Slide Structure Guidelines for Quarto Reveal.js Presentations

## Core Principle
Slides must fit on screen without scrolling. Content should be visible at a glance—if it overflows, split it.

## Content Limits

### 1. Maximum Items Per Slide
- **Bullet points**: 4-5 max (fewer if bullets have sub-items)
- **Incremental reveals (`. . .`)**: 2-3 max per slide
- **Equations**: 1 major equation + 2-3 bullet explanations, OR 2 smaller equations
- **Tables**: Keep to 3-4 rows max; split larger tables across slides

### 2. Callout Boxes Take Space
Callouts (`::: {.warning}`, `::: {.key-insight}`) consume significant vertical space.

**Rules for callouts:**
- Only ONE callout per slide
- If callout + other content = overflow, split the slide
- Keep callout text to 1-2 sentences max
- Callouts work best as the final element (after a `. . .` reveal)

### 3. Images Need Room
- Use `width=70%` or smaller for images with accompanying text
- Image + 2-3 bullet points = safe limit
- Image + detailed explanation = split into two slides

## When to Split Slides

**Split when you have:**
- More than 3 incremental reveals
- A callout box AND more than 3 bullet points
- An equation AND a table
- Content that "explains the explanation" (nested concepts)

**Splitting pattern:**
```
Original dense slide → Slide A (setup/formula) + Slide B (interpretation/implications)
```

**Naming convention for split slides:**
- `## Topic Name` → `## Topic Name` + `## Topic Name (cont.)`
- Or use semantic names: `## Topic: Setup` + `## Topic: Key Insight`

## Content-First Principle

**Key explanations belong ON the slide, not hidden in speaker notes.**

❌ **Bad**: Slide shows formula, notes explain what it means
✅ **Good**: Slide shows formula + key interpretation, notes add conversational context

**Test**: If someone reads only the slides (no notes), can they understand the main points?

## Alignment Between Slides and Notes

Every `. . .` on a slide should have a matching `[→ Click for...]` in the notes.

**Example:**
```markdown
## My Slide

First point visible immediately

. . .

Second point after click

::: notes
First point explanation here.

[→ Click for second point]

Second point explanation here.
:::
```

## Slide Types and Their Limits

| Slide Type | Safe Content Limit |
|------------|-------------------|
| Title/Overview | Title + 3-4 bullets |
| Equation slide | 1 equation + 3 interpretation bullets |
| Comparison slide | 1 small table (3-4 rows) + 1-2 bullets |
| Image slide | 1 image (70%) + 2-3 bullets |
| Key insight slide | 1 callout + 2-3 supporting bullets |
| Summary slide | 4-5 takeaway bullets |

## Red Flags (Signs of Overflow)

Watch for these patterns that cause overflow:
- Multiple `. . .` reveals with content between each
- Callout box in the middle of a slide (not at end)
- Table + equation on same slide
- **TWO equations on one slide** (almost always overflows)
- More than 2 bold headers (e.g., **Step 1**: ... **Step 2**: ... **Step 3**: ...)
- Nested bullet points (bullets with sub-bullets)
- Equation + more than 2 bullet points below it

## Workflow for Dense Content

1. **Draft the slide** with all content you want to include
2. **Count elements**: bullets, reveals, callouts, equations
3. **Check against limits** from the table above
4. **Split if needed**: Find natural break point (setup vs. insight, formula vs. interpretation)
5. **Verify notes alignment**: Each `. . .` has matching `[→ Click...]`

## Proactive Content Audit (CRITICAL)

**Before finishing ANY editing session**, audit ALL slides for overflow risk:

**Quick audit method:**
For each slide, count:
- Number of equations (E)
- Number of bullet points (B)
- Number of bold headers (H)
- Number of `. . .` reveals (R)

**Overflow likely if:**
- E ≥ 2 (two equations = split)
- E = 1 AND B > 3 (equation with too many bullets)
- H > 2 (too many bold sections)
- R > 2 with substantial content between reveals

**When in doubt, split.** An extra slide is better than overflow.

## After Fixing Overflow Issues

**IMPORTANT**: When fixing overflow in a presentation, check ALL slides systematically—not just the ones explicitly pointed out.

**Verification checklist:**
- Render the presentation (`quarto render`)
- Click through every slide in the browser
- Check slide numbers match expected count
- Look for content cut off at bottom of any slide

## Examples

### Before (Overflow)
```markdown
## Complex Topic

**Definition**: ...

- Point 1
- Point 2

. . .

**Why it matters**:

- Implication 1
- Implication 2
- Implication 3

. . .

::: {.warning}
Important caveat that takes two lines of text
:::

**Summary**: Final thought here
```

### After (Split)
```markdown
## Complex Topic

**Definition**: ...

- Point 1
- Point 2

. . .

**Why it matters**:

- Implication 1
- Implication 2

---

## Complex Topic: Key Caveat

::: {.warning}
Important caveat that takes two lines of text
:::

. . .

**Summary**: Final thought here

- Additional context if needed
```