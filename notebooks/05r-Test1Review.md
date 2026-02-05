---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
---

+++ {"tags": ["remove-cell"]}

# Test 1 Review Workshop

+++

## Student Grade Calculator

+++

This workshop reviews the concepts covered on Test 1 by building a student grade calculator step-by-step. Each step focuses on specific syntax you need to know.

Test 1 Philosophy: "Apply the syntax" — you'll be told what to do and how to do it. This workshop practices exactly that.

Problem Context: A professor needs a simple tool to calculate a student's final grade. The grade is based on three scores: homework (20%), midterm (35%), and final exam (45%). Given these scores, calculate the weighted average and determine the letter grade.

+++

### Step 1 — Variables and Expressions

+++

Create variables for the three weights (as decimals) and three sample scores. Then calculate the weighted average using a single expression.

- `hw_weight = 0.20`, `mid_weight = 0.35`, `final_weight = 0.45`
- `hw_score = 85`, `mid_score = 78`, `final_score = 92`
- Calculate `weighted_avg` using the formula: (score × weight) + (score × weight) + ...

```{code-cell} ipython3
# create variables and calculate weighted average
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
hw_weight = 0.20
mid_weight = 0.35
final_weight = 0.45

hw_score = 85
mid_score = 78
final_score = 92

weighted_avg = hw_score * hw_weight + mid_score * mid_weight + final_score * final_weight
weighted_avg
```

### Step 2 — Type Conversion and Input

+++

Now get the scores from user input instead of hardcoding them. Remember: `input()` returns a string, so you must convert to the appropriate numeric type.

Get three scores from the user with these prompts:
- `"Enter homework score: "`
- `"Enter midterm score: "`
- `"Enter final exam score: "`

```{code-cell} ipython3
# get scores from user input
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
hw_score = float(input("Enter homework score: "))
mid_score = float(input("Enter midterm score: "))
final_score = float(input("Enter final exam score: "))

weighted_avg = hw_score * hw_weight + mid_score * mid_weight + final_score * final_weight
weighted_avg
```

### Step 3 — String Formatting

+++

Format the output nicely using an f-string. Display the weighted average rounded to one decimal place:

```text
Weighted Average: 86.3
```

```{code-cell} ipython3
# format and print the result
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
print(f"Weighted Average: {weighted_avg:.1f}")
```

### Step 4 — Conditionals

+++

Determine the letter grade based on the weighted average using this scale:
- A: 90 and above
- B: 80-89
- C: 70-79
- D: 60-69
- F: below 60

Store the result in a variable called `letter_grade`, then print it.

```{code-cell} ipython3
# determine letter grade
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
if weighted_avg >= 90:
    letter_grade = 'A'
elif weighted_avg >= 80:
    letter_grade = 'B'
elif weighted_avg >= 70:
    letter_grade = 'C'
elif weighted_avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Letter Grade: {letter_grade}")
```

### Step 5 — Functions (Calculate Average)

+++

Wrap the weighted average calculation in a function.

Write a function `calc_weighted_avg(hw, mid, final)` that takes three scores and returns the weighted average. Use the same weights as before (0.20, 0.35, 0.45).

```{code-cell} ipython3
def calc_weighted_avg(hw, mid, final):
    # your code here
    pass
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
def calc_weighted_avg(hw, mid, final):
    hw_weight = 0.20
    mid_weight = 0.35
    final_weight = 0.45
    return hw * hw_weight + mid * mid_weight + final * final_weight
```

```{code-cell} ipython3
# Test it
assert calc_weighted_avg(100, 100, 100) == 100.0
assert calc_weighted_avg(0, 0, 0) == 0.0
assert calc_weighted_avg(85, 78, 92) == 86.3
print("All tests passed!")
```

### Step 6 — Functions (Letter Grade)

+++

Write a function `get_letter_grade(avg)` that takes a numeric average and returns the letter grade as a string.

```{code-cell} ipython3
def get_letter_grade(avg):
    # your code here
    pass
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
def get_letter_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
```

```{code-cell} ipython3
# Test it
assert get_letter_grade(95) == 'A'
assert get_letter_grade(90) == 'A'
assert get_letter_grade(89) == 'B'
assert get_letter_grade(70) == 'C'
assert get_letter_grade(59) == 'F'
print("All tests passed!")
```

### Step 7 — String Methods

+++

Get the student's name from the user and format it properly. The user might enter the name in any case (e.g., "jOHN sMITH").

1. Get input with prompt `"Enter student name: "`
2. Use a string method to convert to title case
3. Store in variable `student_name`

```{code-cell} ipython3
# get and format student name
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
student_name = input("Enter student name: ").title()
student_name
```

### Step 8 — Lists

+++

Instead of separate variables, store the three scores in a list. Then use list indexing and built-in functions.

1. Create a list `scores = [85, 78, 92]` (hw, mid, final in order)
2. Use indexing to get each score
3. Use `min()` and `max()` to find the lowest and highest scores

```{code-cell} ipython3
# work with scores as a list
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
scores = [85, 78, 92]

hw_score = scores[0]
mid_score = scores[1]
final_score = scores[2]

lowest = min(scores)
highest = max(scores)

print(f"Scores: {scores}")
print(f"Lowest: {lowest}, Highest: {highest}")
```

### Step 9 — Combine Everything

+++

Put it all together into a complete grade report. Your program should:

1. Get the student's name (format with title case)
2. Get three scores from the user
3. Calculate the weighted average using your function
4. Determine the letter grade using your function
5. Print a formatted report like this:

```text
Grade Report for John Smith
---------------------------
Homework:     85.0
Midterm:      78.0
Final Exam:   92.0
---------------------------
Weighted Avg: 86.3
Letter Grade: B
```

```{code-cell} ipython3
# complete grade calculator
```

+++ {"jp-MarkdownHeadingCollapsed": true}

#### Solution

```{code-cell} ipython3
# Get student info
student_name = input("Enter student name: ").title()
hw_score = float(input("Enter homework score: "))
mid_score = float(input("Enter midterm score: "))
final_score = float(input("Enter final exam score: "))

# Calculate results
avg = calc_weighted_avg(hw_score, mid_score, final_score)
grade = get_letter_grade(avg)

# Print report
print(f"\nGrade Report for {student_name}")
print("---------------------------")
print(f"Homework:     {hw_score:.1f}")
print(f"Midterm:      {mid_score:.1f}")
print(f"Final Exam:   {final_score:.1f}")
print("---------------------------")
print(f"Weighted Avg: {avg:.1f}")
print(f"Letter Grade: {grade}")
```

### Step 10 — Fix the Bugs

+++

The following code has several errors. Find and fix them.

```{code-cell} ipython3
# This code has bugs - find and fix them

def calculate_average(score1, score2, score3)
    total = score1 + score2 + score3
    average = total / 3

name = input("Enter name: ")
s1 = input("Enter score 1: ")
s2 = input("Enter score 2: ")
s3 = input("Enter score 3: ")

result = calculate_average(s1, s2, s3)

if result > 90
    print(name + " earned an A")
elif result >= 80:
    print(name " earned a B")
else
    print(name + " needs improvement")
```

```{code-cell} ipython3
# Write your corrected version here
```

#### Solution

+++

The bugs were:
1. Missing colon after `def` line
2. Missing `return` statement
3. Scores not converted from string to float
4. Missing colon after `if result > 90`
5. Missing `+` in string concatenation (or use f-string)
6. Missing colon after `else`
7. Should be `>=` not `>` for the A grade (90 is an A)

```{code-cell} ipython3
def calculate_average(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return average

name = input("Enter name: ")
s1 = float(input("Enter score 1: "))
s2 = float(input("Enter score 2: "))
s3 = float(input("Enter score 3: "))

result = calculate_average(s1, s2, s3)

if result >= 90:
    print(name + " earned an A")
elif result >= 80:
    print(name + " earned a B")
else:
    print(name + " needs improvement")
```

## Additional Practice

+++

If you finish early, try these extensions:

**1. Add plus/minus grades:**
Modify `get_letter_grade()` to return grades like "A-", "B+", "B", "B-", etc. Use these boundaries: 97+ = A+, 93+ = A, 90+ = A-, 87+ = B+, etc.

**2. Validate input:**
What happens if the user enters a negative score or a score over 100? Add conditionals to check for valid input (0-100) and print an error message if invalid.

**3. Parse a name:**
Write a function `get_initials(full_name)` that takes a name like "John Smith" and returns "J.S." using string methods and indexing.

```{code-cell} ipython3
# Additional practice space
```

---

Auburn University / Industrial and Systems Engineering  
INSY 3010 / Programming and Databases for ISE  
© Copyright Danny J. O'Leary.
