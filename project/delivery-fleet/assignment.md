---
title: "Project: Autonomous Delivery Fleet"
assignment_id: 20610398
assignment_group_id: 3513505
points_possible: 100
grading_type: points
submission_types: online_upload
allowed_extensions:
  - pdf
  - docx
  - ipynb
unlock_at: 2026-11-12T13:19:04-06:00
due_at: 2026-12-04T23:59:00-06:00
lock_at: 2026-12-04T23:59:00-06:00
published: true
---

# INSY 3010 Final Project: Autonomous Delivery Fleet

**Fall 2026**

**Due:** Friday, December 4, 2026, at 11:59 p.m. Auburn time. **Course weight:** 10%. **Project score:** 100 points.

## Your Assignment

A delivery company wants to understand its robot fleet's workload, failed deliveries, and energy use. Analyze the supplied `data/fleet.db`, produce the four reports below, and explain your findings and methods in a written reflection.

Begin by investigating the database. Establish how its records fit together and what the measurements mean before building your reports.

You may collaborate and use AI assistants. Submit your own work and acknowledge assistance. Questions about this assignment will account for **10–15% of your final exam score**. Be prepared to explain the database, your implementations, and your analysis.

## Deliverables

Submit these two files in Canvas:

1. **Reflection:** PDF or DOCX, organized under the six headings below. Support your explanations with selected code excerpts, query results, and verification evidence.
2. **Completed notebook:** `.ipynb`, with all four tasks implemented and relevant outputs retained. Restart the runtime and run all cells before saving your submission.

The reflection is the primary source for grading. The notebook supports your account of the work.

## Getting Started

[Open the project notebook in Colab](https://colab.research.google.com/github/olearydj/INSY3010/blob/main/project/delivery-fleet/project-notebook.ipynb). Use SQL and Python's standard library for the project.

The setup opens a database connection named `conn`. Task functions receive that connection and leave it open for subsequent work. The cleanup cell closes it. Use query parameters for variable values.

Distance, energy, and duration record actual activity. `PayloadKg` records the assigned load. A robot's depot assignment is fixed for the period represented in the database.

## Task 1: Completed Deliveries by Depot

Implement `completed_by_depot_sql(conn)` to produce the same report as the supplied `completed_by_depot_python(conn)`. Perform filtering, grouping, aggregation, and sorting in SQL.

Return a list of `(depot_name, completed_count, total_distance_km)` tuples for Completed missions. Include depots with at least one completed mission. Round total distance to two decimal places. Order by completed count descending, then depot name ascending.

## Task 2: Failed Missions by Zone

Implement `failed_by_zone_python(conn)` to produce the same report as the supplied `failed_by_zone_sql(conn)`. Use SQL to retrieve raw joined records. Perform filtering, grouping, aggregation, and sorting in Python.

Return a list of `(zone_name, failed_count, failed_distance_km)` tuples for Failed missions. Include zones with at least one failure. Count every failed mission, including failures with zero distance. Round total distance to two decimal places. Order by failure count descending, then zone name ascending. Return `[]` when there are no matching records.

## Task 3: Export a Report to CSV

Implement `export_to_csv(data, headers, filename)` using Python's `csv` module and a file context manager. Write the header followed by the data rows, using UTF-8 encoding and `newline=""`. Return `True` on success. Complete the supplied `try` block and retain its file-error handling.

Export your Task 1 report with the headers `Depot`, `Completed Count`, and `Total Distance Km`. Verify the exported contents and document how your function handles empty data, punctuation in text fields, and file-access errors. Include the evidence in your notebook and reflection.

## Task 4: Energy Use by Depot and Terrain

Implement `energy_by_depot_terrain(conn)` using SQL, Python, or a combination. For each depot and terrain type, report the completed mission count, distance traveled, energy consumed, and energy consumed per kilometer.

Return tuples in this order:

```text
(depot_name, terrain_type, completed_count,
 total_distance_km, total_energy_wh, wh_per_km)
```

Include groups with at least one Completed mission. Calculate Wh/km from each group's total energy and total distance. Round the three measurements to two decimal places after calculating the results. Sort by depot name ascending, then terrain type ascending.

## Reflection

Use the following six headings. Place evidence beside the explanation it supports and label values with their units.

### 1. Database Structure: 15 points

Describe the entities, attributes, keys, and relationships you discovered. Include an ER diagram with cardinalities and explain how the tables represent a delivery operation. Use specific records to illustrate the relationships. Identify a feature of the data that matters when interpreting your reports.

### 2. SQL and Python Implementations: 25 points

Explain how both versions of Tasks 1 and 2 produce their results. Trace one depot total and one zone summary through the underlying records. Show that the implementations agree, and discuss the consequences of doing the processing in SQL or Python.

### 3. Energy Analysis: 20 points

Explain and justify your Task 4 implementation. Interpret two result groups and verify one group's calculation. What can management conclude from the comparison? What else would you want to know before recommending an operational change?

### 4. Verification and Debugging: 15 points

Present at least three checks you designed beyond the supplied comparisons. Include a small independently calculated result, an empty or boundary case, and a check aimed at a plausible implementation error. Give the inputs, expected results, actual results, and your conclusions. Discuss a bug you encountered or deliberately introduced and how you diagnosed it.

### 5. File Output and Error Handling: 15 points

Explain the CSV implementation, file context manager, and error handling. Present evidence that the export preserves the report's contents and handles the cases specified in Task 3. Assess what your verification establishes and where it falls short.

### 6. Learning, Decisions, and Assistance: 10 points

Describe a specific change in your understanding and an implementation decision you made. Support both with examples from your work. Identify collaborators and AI tools used, describe their contributions, and explain how you checked the work they helped produce.

## Grading

The reflection is graded on technical correctness, evidence from your submitted work, and the reasoning behind your conclusions. All four tasks contribute to these sections.

| Reflection section | Correctness | Specific evidence | Reasoning and interpretation | Total |
|---|---:|---:|---:|---:|
| Database structure | 8 | 4 | 3 | 15 |
| SQL and Python implementations | 10 | 8 | 7 | 25 |
| Energy analysis | 8 | 6 | 6 | 20 |
| Verification and debugging | 5 | 6 | 4 | 15 |
| File output and error handling | 6 | 5 | 4 | 15 |
| Learning, decisions, and assistance | 2 | 4 | 4 | 10 |
| **Total** | **39** | **33** | **28** | **100** |

Full credit requires accurate explanations, reproducible evidence, and justified decisions. Incomplete explanations and weak evidence receive partial credit. Unsupported claims and generic discussion earn little credit. Your notebook and reflection should tell a consistent account of the work.
