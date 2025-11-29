#!/usr/bin/env python3
"""
Script to add natural, conversational presentation scripts to all slides
in the Chapter 10 presentation deck that don't already have them.
"""

import re

# Define scripts for each slide by their heading
SLIDE_SCRIPTS = {
    "Least Squares Solution": """**SCRIPT:**

So what's the least squares solution? When we use the prediction-error approach with a quadratic norm - meaning we're minimizing the sum of squared errors - we get this LS estimate right here. It's theta hat N LS equals R inverse of N times f of N.

Now what are R and f? R of N is the sample covariance matrix of our regressors - it's capturing how our regression vectors correlate with each other. And f of N is the sample cross-covariance between our regressors and the outputs - it's capturing how our inputs relate to our outputs.

This is a beautiful result because it's analytical - we don't need to run any iterative optimization. We just compute these matrices from our data and we're done. The catch, as we'll see, is that computing this solution numerically can be tricky.""",

    "Understanding the LS Estimate": """**SCRIPT:**

Let's make sure we understand what this LS estimate actually is. We have our prediction equation here - y hat at time t is phi transpose times theta. So what is theta hat N LS? It's the parameter vector that minimizes the sum of squared errors between our predictions and the actual outputs.

The two components are R of N, which is the sample covariance matrix of the regressors phi of t, and f of N, which is the sample cross-covariance between phi of t and the outputs y of t.

This solution comes from solving a system of linear equations - which brings us to the normal equations.""",

    "The Normal Equations (Alternative View)": """**SCRIPT:**

Here's another way to look at this. The LS estimate theta hat N LS solves this equation: R of N times theta hat N LS equals f of N. These are called the normal equations - and if you've taken a linear algebra class, this should look familiar. It's just a system of linear equations.

The word "normal" here doesn't mean "typical" - it actually comes from geometry, referring to perpendicularity. The solution makes the error vector perpendicular, or normal, to the space of regressors. But that's just trivia - the key point is that this is a linear system we need to solve.""",

    "Numerical Challenge": """**SCRIPT:**

Now here's where things get interesting from a numerical standpoint. The problem is that this coefficient matrix R of N can be ill-conditioned. What does that mean? It means that small errors in the data can lead to huge errors in the solution. This is particularly bad when the dimension is high.

Why does this happen? Because computing R of N involves products of the original data - you're taking phi of t and multiplying it by phi transpose of t, then summing these up. This operation can amplify numerical errors.

So the solution is to use matrix factorization techniques. Instead of forming R of N directly and then inverting it, we'll construct a matrix R such that R times R transpose equals R of N. This turns out to be much more numerically stable. That's where QR factorization comes in.""",

    "QR Factorization Definition": """**SCRIPT:**

So what is QR factorization? For any matrix A with n rows and d columns, we can write it as A equals Q times R. Here, Q is an n by n orthogonal matrix - meaning Q times Q transpose equals the identity matrix. And R is n by d upper triangular - meaning it has zeros below the diagonal.

There are various ways to compute this factorization - Householder transformations, Gram-Schmidt procedure, or Cholesky decomposition. The specific algorithm doesn't matter so much for our purposes - what matters is understanding why this factorization is useful.""",
}

def add_script_to_slide(content, slide_heading, script_text):
    """Add script to a slide if it doesn't already have one."""
    # Pattern to match slide heading and check if it has a SCRIPT
    pattern = rf'(##\s+{re.escape(slide_heading)}.*?)(------------------------------------------------------------------------)'

    def replacement(match):
        slide_content = match.group(1)
        divider = match.group(2)

        # Check if already has SCRIPT
        if '**SCRIPT:**' in slide_content:
            return match.group(0)  # Return unchanged

        # Check if it has notes section
        if '::: notes' in slide_content:
            # Add SCRIPT at the beginning of notes
            slide_content = slide_content.replace('::: notes\n', f'::: notes\n**SCRIPT:**\n\n{script_text}\n\n')
        else:
            # Add new notes section before divider
            slide_content += f'\n\n::: notes\n**SCRIPT:**\n\n{script_text}\n:::\n\n'

        return slide_content + divider

    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def main():
    filepath = r"c:\Users\JV Landingin\Documents\20-29 Learning\23 University\23.11 UPD DS Program\DS 397 System Identification\system_identification_group2_deck\presentation_deck_chapter10.qmd"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add scripts to slides
    for heading, script in SLIDE_SCRIPTS.items():
        content = add_script_to_slide(content, heading, script)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Added scripts to {len(SLIDE_SCRIPTS)} slides")

if __name__ == "__main__":
    main()
