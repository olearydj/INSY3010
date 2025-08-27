# INSY3010 Jupyter Notebooks

This folder contains the files used for INSY 3010 - Programming and Database Applications for ISE. They are provided in [Jupyter Notebook](https://docs.jupyter.org/en/latest/) format (`.ipynb` files) for use on [Google Colab](https://colab.google/).

## Working with Course Notebooks in Google Colab

For a crash course on the Colab interface that we will use in this class, watch the first 10 minutes of this YouTube video: [Colab 101: Your Ultimate Beginner's Guide](https://youtu.be/Ii6gs9zADEA?si=3t0t0Vv69m3MH3K-).

### Accessing Notebooks

1. Click on the Colab link provided for each notebook.
2. This opens a copy of the notebook in Google Colab.
3. You're now working on a temporary copy that doesn't affect the original.

Remember, the ability to access these notebooks from anywhere is a great advantage, but it comes with the responsibility of managing your own work carefully.

### Saving Your Work

- Your work is not automatically saved.
- To keep your changes:
  1. Go to `File > Save a copy in Drive`
  2. This creates a copy in your Google Drive.
- If you don't save, you'll lose your work when you close the tab.

### Managing Versions

- Each time you save, it creates a new copy in your Drive.
- To stay organized:
  1. Use consistent naming (e.g., "Assignment1_V1", "Assignment1_V2")
  2. Consider creating a specific folder for this course in your Drive.

### Updating to the Latest Version

- If the instructor updates the original notebook:
  1. Your saved copy won't automatically update.
  2. To get the latest version, click the original Colab link again.
  3. Save this new version in your Drive if needed.

### Collaboration and Sharing

- You can share your Colab notebook with others:
  1. Click the "Share" button at the top right.
  2. Adjust permissions as needed.
- Be mindful of privacy: don't share notebooks with sensitive information.

### Working Offline and Reconnecting

- Colab requires an internet connection.
- If disconnected:
  1. Click "Reconnect" at the top of the notebook.
  2. You might need to rerun some cells.

### Resource Limitations

- Colab may disconnect after periods of inactivity.
- For long computations, check periodically to ensure you're still connected.

### Submitting Your Work

- Unless otherwise notified, Notebooks are intended for in-class instruction and practice. They will not be submitted or graded.

### Best Practices

1. Save your work frequently.
2. Check for updates to the original notebooks regularly.
3. Keep your saved notebooks organized in your Google Drive.
4. Always run all cells before submitting to ensure all outputs are current.

## Understanding Cell Execution Order in Jupyter Notebooks

Jupyter notebooks are composed of cells that can be executed independently. However, running cells out of order can lead to unexpected results and errors. Here's what you need to know:

### Risks of Running Cells Out of Order

1. Dependency Issues 
    - Later cells often depend on variables or functions defined in earlier cells.
    - Running a later cell before its dependencies can cause NameError or undefined variable errors.

2. Inconsistent State 
    - The notebook's state (variables, functions, etc.) may not reflect what you see in the code if cells are run out of order.
    - This can lead to confusion and incorrect results.

3. Overwriting Variables 
    - Re-running earlier cells after modifying variables in later cells can overwrite your changes unexpectedly.

4. Import Conflicts 
    - Importing modules or changing import statements out of order can lead to conflicting definitions.

5. Resource Allocation 
    - Some cells might allocate resources (like opening files or database connections) that other cells expect to be available.

### Best Practices for Cell Execution

1. Run Cells in Order 
    - Start from the top and run cells sequentially.
    - Use "Run All" or "Run All Above" features when available.

2. Restart and Run All 
    - If you're unsure about the notebook's state, use "Restart Kernel and Run All Cells" to ensure a clean execution.

3. Pay Attention to Cell Numbers 
    - Colab shows the order in which cells were last executed. Use this to track your execution order.

4. Use Markdown Cells as Checkpoints 
    - Add markdown cells to create logical sections in your notebook. Run all cells up to these checkpoints to ensure consistency.

5. Be Cautious with Interactive Widgets 
    - If your notebook uses interactive widgets, be aware that their state might not match the cell execution order.

Remember, the goal is to maintain a consistent and predictable state throughout your notebook. When in doubt, restart the kernel and run all cells from the beginning.

## Attribution and Licensing

These notebooks are based on [*Think Python*, 3rd edition](https://greenteapress.com/wp/think-python-3rd-edition), by Allen B. Downey, the first edition of which was the original inspiration for Charles R. Severance's [*Python for Everybody* (aka PY4E)](https://py4e.com). Both are outstanding resources for people interested in learning Python, but neither are exactly what I was looking for in this course.

Both *Think Python*, 3rd Edition and *Python for Everybody* are licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). This allows them to be freely copied, distributed, and modified, for non-commercial purposes, with proper attribution. Any modifications must be shared under a compatible license.

### Links

- *Think Python*
    - [Publisher's Page with licensing information](https://greenteapress.com/wp/think-python-3rd-edition/)
    - [Online Version of the Book](https://allendowney.github.io/ThinkPython/)
    - [Supporting code and Jupyter Notebooks](https://github.com/AllenDowney/ThinkPython/tree/v3)
- *Python for Everybody*
    - [PY4E Homepage](https://py4e.com)
    - Versions of the book in [PDF](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf), and [HTML](https://www.py4e.com/html3)
    - [Course content and source code](https://github.com/csev/py4e)

### Licensing

Like those before it, this work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Original content and modifications by Danny J. O'Leary ([dan.oleary@auburn.edu](mailto:djo0008@auburn.edu)), building on the works mentioned above. You can find a copy of the full text of the license here: [LICENSE](LICENSE).

