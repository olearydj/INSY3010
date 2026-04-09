# INSY 3010 Final Project

**Spring 2026**

This assignment is different. The focus is on learning and understanding how tools, methods, Python, and SQL work together to create solutions. The assignment description is detailed to assist you in this process. Read it carefully and refer to it often.

You are free to collaborate in any way you choose. AI assistants like ChatGPT or Claude are allowed and even encouraged. Everyone will submit their own work, which will come in the form of a reflection with code snippets and other evidence as required. The code itself will not be graded, but well-written reflections will clearly demonstrate a command of the material. Some questions on the final exam will be designed to assess your understanding of this material.

## Main Objectives and Deliverables

1. Explore a warehouse distribution database
2. Implement functions using both SQL and Python data processing
3. Write query results to a file using Python file I/O
4. Reflect on the experience

There is only one deliverable: the written reflection. Complete the first three objectives in sequence. You may wish to work on the reflection in parallel.

## Part 1 - Warehouse Distribution Database

### The Database

This project uses a warehouse distribution tracking system. This section describes the database structure.

#### Business Scenario

*A logistics company operates a network of distribution centers across the southeastern United States. Each warehouse handles a variety of products across categories including electronics, hardware, safety equipment, and packaging materials. Shipments flow both inbound (from suppliers to warehouses) and outbound (from warehouses to customers) via multiple carriers that operate by ground, air, or rail. The system tracks every shipment, recording its origin warehouse, product, carrier, quantity, and delivery status to support operational analysis and logistics optimization.*

#### Entities

There are three primary entities and one junction table.

1. *Warehouse*
   - warehouse_id (PK) - e.g., "W001"
   - name - Distribution center name
   - city, state - Location
   - capacity_sqft - Storage capacity in square feet

2. *Product*
   - product_id (PK) - e.g., "P0001"
   - product_name - Product description
   - category - Electronics, Hardware, Safety, or Packaging
   - unit_weight - Weight per unit in pounds
   - unit_cost - Cost per unit in dollars

3. *Carrier*
   - carrier_id (PK) - e.g., "C001"
   - name - Carrier company name
   - mode - Ground, Air, or Rail
   - base_rate - Shipping rate per pound-unit in dollars

4. *Shipment* (junction table)
   - shipment_id (PK)
   - warehouse_id (FK to Warehouse)
   - product_id (FK to Product)
   - carrier_id (FK to Carrier)
   - ship_date - Date of shipment
   - quantity - Number of units
   - shipment_type - Inbound or Outbound
   - status - Delivered, In Transit, or Delayed

#### Relationships

1. *Warehouse* <-> *Product* (many-to-many): A warehouse handles many products, and a product can be stored at many warehouses.
2. *Warehouse* <-> *Carrier* (many-to-many): A warehouse uses many carriers, and a carrier serves many warehouses.
3. *Product* <-> *Carrier* (many-to-many): A product can be shipped by many carriers, and a carrier ships many products.

All three M:N relationships are implemented through the *Shipment* table, which has foreign keys to all three entities and stores additional data about each shipment event (date, quantity, type, status).

### Working with the Notebook

Open `project_notebook.ipynb` in Colab and work through it from top to bottom. The notebook is organized into three parts:

1. *Explore the Database* - Run each cell to see the tables, their columns, and sample data. Pay attention to the relationships between tables; understanding the schema is essential for the tasks that follow.

2. *Study the Examples* - Two complete examples show different approaches to the same kind of problem:
   - Example 1 uses **SQL** to filter and sort data inside the query
   - Example 2 uses **Python** to filter and sort data after fetching it  

   Both approaches use SQL to retrieve data from the database. The difference is where the *processing* happens. In the SQL approach, grouping, filtering, and sorting are all in the query. In the Python approach, raw data is loaded with SQL, then Python handles the rest. Understanding this distinction is key to the tasks that follow.

3. *Implement Your Functions* - For each task, read the provided implementation, write your version in the **YOUR CODE HERE** cell, and run the test cell that follows.

#### Secure Query Construction

When incorporating user-provided values into SQL queries, **never use f-strings or string concatenation**. This creates a security vulnerability called *SQL injection*. Instead, use *parameterized queries* with `?` placeholders:

```python
# Bad (vulnerable)
query = f"SELECT * FROM Product WHERE category = {category}"

# Good (secure)
query = "SELECT * FROM Product WHERE category = ?"
cursor.execute(query, (category,))
```

#### Task 1 - Implement SQL Version

Provided: `get_warehouse_totals_python(conn)` - calculates total quantity handled by each warehouse using Python dictionaries for grouping and sorting.

Your job: Implement `get_warehouse_totals_sql(conn)` using SQL to do the same thing.

Hints:

- Use JOIN to connect Warehouse and Shipment tables
- Use GROUP BY to aggregate by warehouse
- Use SUM to total the quantity
- Use ORDER BY for sorting

#### Task 2 - Implement Python Version

Provided: `get_delayed_by_carrier_sql(conn)` - finds delayed shipments grouped by carrier, returning each carrier's delay count and total delayed quantity, all in SQL.

Your job: Implement `get_delayed_by_carrier_python(conn)` using Python for the filtering, grouping, and sorting.

Hints:

- Fetch shipment data with carrier names (you still need a JOIN to get carrier names)
- Filter for delayed shipments using an `if` statement
- Use a dictionary to group by carrier, tracking both count and quantity
- Convert to list of tuples and sort by count descending, then name ascending

#### Task 3 - Write Results to CSV

Implement `export_to_csv(data, headers, filename)` to write query results to a CSV file.

Your implementation should:

1. Use a context manager (`with` statement) to open the file safely
2. Write the header row first (comma-separated column names)
3. Write each data row (comma-separated values)
4. Use `try/except` to handle errors gracefully (e.g., invalid path, permission denied)
5. Return `True` on success, `False` on failure

#### Task 4 - Bonus Challenge

Implement `get_shipping_cost_by_mode(conn)` using SQL, Python, or a combination. This function estimates total shipping cost by carrier mode (Ground, Air, Rail) using the formula:

```text
cost = quantity * unit_weight * base_rate
```

This requires data from *three* tables: Shipment (quantity), Product (unit_weight), and Carrier (base_rate). Think about which approach makes the most sense.

#### Testing Your Code

Each task has a test cell immediately below it. Run the test cell after implementing your function. Success looks like:

```text
TASK 1 PASSED!
  Both implementations found 8 warehouses
```

If a test fails, read the error message carefully. It will tell you what's wrong (e.g., "SQL returned 5 warehouses but Python returned 3" means your query logic differs from the reference).

## Part 2 - Reflection

Document your experience with this assignment in a written reflection. Address each part below. Use screenshots of your code to support descriptions of your implementations, and include additional code snippets where they strengthen your analysis.

### Part 1: Database Schema

Consider the structure of the warehouse database:

1. Why does the Shipment table have three foreign keys instead of one or two? What would be lost if the `carrier_id` column were removed from Shipment and carrier information were stored differently?
2. Compare this schema to the flight database from the SQL exercises. What structural similarities and differences do you notice? How do the junction tables in each database serve similar purposes?
3. If you were asked to add a new feature to this system - tracking which warehouse *employees* processed each shipment - what table(s) would you add and how would they connect to the existing schema?

### Part 2: SQL vs Python - Specific Task Analysis

Pick either Task 1 or Task 2. For your chosen task:

1. Describe both implementations (the provided version and your version) and how they work.
2. Which was easier to write? Why?
3. Which is more readable or understandable?

### Part 3: SQL vs Python - General Principles

Based on your implementations:

1. What types of operations does SQL handle better than Python? Give specific examples from your tasks.
2. What types of operations does Python handle better than SQL? Give specific examples.
3. How would you decide which approach to use for a new data analysis task?

### Part 4: Error Handling

Consider the role of error handling in your code:

1. What specific errors were you catching with `try/except` in Task 3 and why?
2. Compare two approaches to handling potential errors: checking conditions before acting (e.g., "if the file exists, open it") versus trying the action and handling the failure (e.g., "try to open it; if it fails, handle the error"). Which did you use in Task 3? When might the other approach be better?
3. What would happen if `export_to_csv` did *not* use `try/except` and the file path was invalid? How would that affect the program?

### Part 5: File I/O

Reflect on writing data to files:

1. Explain what a context manager (`with` statement) does and why it matters when working with files. What could go wrong without one?
2. Describe the pattern you used to write each row to the CSV file. How did you convert the tuple values to a comma-separated string?
3. If you were writing a very large dataset (millions of rows), would your approach still work? Why or why not?

### Part 6: Learning and Collaboration

1. How did you approach learning the unfamiliar parts of this project (reading provided code, understanding the database structure, figuring out how SQL and Python work together)?
2. Did you collaborate with other students or use AI tools (ChatGPT, Claude, etc.)? How did that help or hinder your understanding?
3. Describe at least one "aha moment" where something clicked for you during this project. What were you struggling with, and what helped you understand it?

### Bonus: Task 4

If you completed Task 4:

1. Describe your approach (SQL, Python, or both) and explain why you chose it.
2. Discuss the three-table join involved. How does it differ from the two-table joins in Tasks 1 and 2?

## Grading

Your grade for this project is based entirely on the reflection. Each part is worth 15 points (5 for correctness, 10 for insights / understanding / depth).

| Part | Points |
|------|--------|
| Parts 1-6 | 90 |
| Bonus (Task 4) | 15 |
| Total available | 105 |
