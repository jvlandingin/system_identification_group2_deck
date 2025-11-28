# Speaker Notes Guidelines for Presentation Slides (v2)

## Core Principle
Speaker notes should support natural presentation flow—as if you're speaking to an audience while advancing through slides. The content should be split roughly 90% on slides, 100% in speaker notes (full coverage but mostly visible).

**CRITICAL: The audience should see and hear the same thing.** Don't make them process two different phrasings simultaneously—this creates cognitive dissonance.

## Structure & Content

### 1. Echo the Slide Content FIRST, Then Expand
- **Read what they see, then explain.** Always echo the slide text before adding context.
- Repeat key headings and bullet points from the slide exactly in the speaker notes
- Only AFTER echoing can you add brief explanations
- Never paraphrase slide content with different words—use the same words

**❌ Bad (audience reads one thing, hears another):**
> Slide says: "R(N) — Sample covariance matrix"
> Notes say: "One over N times the sum of φ times φ-transpose..."

**✅ Good (echo first, then expand):**
> Slide says: "R(N) — Sample covariance matrix"
> Notes say: "R(N) is the sample covariance matrix of regressors φ (fie). This measures how the regression vectors correlate with each other."

### 2. Add Minimal Explanations (1-2 sentences max per point)
- Only add explanations AFTER slide content that needs elaboration
- Keep expansions brief and conversational
- Imagine you're naturally elaborating on what you just read from the slide

### 3. Don't Explain Self-Evident Content
- Skip explanations for questions that are immediately answered on the slide
- Don't explain material that appears in the next animation/section
- Let the slide content speak for itself when appropriate

### 4. Add Click Indicators
- Use `[→ Click for...]` to mark where the presenter should advance to the next animation
- Place indicators where `. . .` (incremental reveals) appear on the slide
- Only mark actual slide transitions, not internal elaborations
- Example: `[→ Click to reveal approach]`

### 5. Match Slide Animation Structure
- Align speaker notes with the actual `. . .` dividers on the slide
- Don't create click points where none exist on the slide
- Follow the incremental reveal pattern exactly

### 6. Write for Natural Speech
- Use conversational language ("we're going to...", "let me explain...")
- Write as if speaking to an audience, not writing a textbook
- Avoid academic or overly formal tone
- Flow from one thought to the next naturally

### 7. Start Each Slide with a Brief Intro
Begin speaker notes with a short transitional phrase (1 sentence) to orient the audience:
- "Now let's look at..."
- "Here's the key insight..."
- "Let me explain what this means..."
- "Before we dive into the math..."

This helps the presenter transition smoothly between slides.

### 8. Never Invent Content
- Don't add "key insights," "warnings," or conceptual sections that aren't on the slide
- Stay true to what the slide actually contains
- If something needs explaining, put it on the slide, not just in notes

### 9. Don't Read Formulas Literally
When explaining equations in speaker notes, describe what they mean—don't transcribe them symbol by symbol.

**❌ Bad (awkward to read aloud):**
> "Then rewrite as: y(t) = G₀(q)u(t) + H₀(q)e₀(t). This is the standard form..."

**✅ Good (natural to speak):**
> "The formula shows we use a transfer function G₀ for the input-output relationship, and a noise model H₀ shaping the prediction error."

**✅ Also good (referencing symbols with pronunciation):**
> "We multiply φ (fie) by θ (THAY-tah) to get our prediction."

**Guidelines for formulas:**
- Describe the *meaning* or *structure*, not the symbols
- Use phrases like "the formula shows...", "this captures...", "notice that..."
- Focus on what the audience should understand, not what they can already see
- For complex equations, highlight the key insight or interpretation
- **Include pronunciation guides** for Greek letters: θ (THAY-tah), φ (fie), ψ (sigh), ε (EP-sih-lon), κ (CAP-uh), λ (LAM-duh), ρ (row), μ (mew)

## Workflow Example
1. **Read the slide structure** (headings, bullets, equations, animations)
2. **Identify where `. . .` animations occur** (these get click indicators)
3. **Write the script mirroring the slide** (repeat what's shown)
4. **Add 1-2 sentence explanations only** where helpful for elaboration
5. **For equations**: Describe meaning, don't transcribe symbols
6. **Insert `[→ Click...]` markers** at actual animation points
7. **Review**: Does it sound like natural speaking? Does it match the slide exactly?

## What NOT to Do
- ❌ Don't explain questions that are answered on the same slide
- ❌ Don't create separate scripts disconnected from slide content
- ❌ Don't add lengthy additional explanations
- ❌ Don't invent "key insights" or content not on the slide
- ❌ Don't add click indicators where slide animations don't exist
- ❌ Don't use overly technical or academic language
- ❌ Don't read formulas symbol-by-symbol (e.g., "y of t equals G zero of q times u of t...")

## Key Principle
The speaker notes guide presentation flow without duplicating content that's already visible, while providing just enough support for natural, confident delivery.