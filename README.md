# Student Grades Data Analysis with Pandas

This project is a small **data analysis exercise** using:

- **Pandas** for data manipulation  
- **NumPy** for numerical operations  
- **Matplotlib** for visualizations  
- Python’s built-in `random` module for basic randomness

It works on a simple dataset of students with **Name, Age, and Grade**, and demonstrates common data analysis tasks.

---

## 🔧 Main Features

### 📊 DataFrame creation and filtering
- Creates a `DataFrame` from a Python dictionary.
- Prints the first rows of the dataset.
- Filters rows where `Age > 22`.

### 🏙 Add and transform columns
- Adds a new column `City` with a default value.
- Sorts the DataFrame by `Age` in descending order.
- Computes the **mean age** of the students.

### 🔁 Concatenation and saving to CSV
- Creates a copy of the DataFrame.
- Concatenates the original and the copy into a larger DataFrame.
- Saves the resulting DataFrame into `data.csv`.

---

## 📈 Visualizations

### 📌 Histogram of Grades by Age
- For each unique age, plots a histogram of the corresponding grades.
- Helps visualize how grades are distributed per age group.

### 📌 Scatter Plot: Age vs Grade
- Plots a scatter plot of `Age` (x-axis) vs `Grade` (y-axis).
- Shows how grades vary across different ages.

---

## 🧹 Missing Values Handling

The script:
- Randomly selects several rows.
- Sets `Age` and `Grade` to `NaN` for those rows.
- Uses the `mis_val()` function to fill missing values with the **column mean**.

This demonstrates:
- Introducing missing data.
- Cleaning the data using simple imputation.

---

## 🔗 Joining DataFrames

Two small DataFrames are created:

- `data_1` with `ID`, `Name`, and `Age`
- `data_2` with `ID`, `Grade`, and `City`

The script performs:

- **Inner join** on `ID`
- **Outer join** on `ID`

This shows how to combine related information from different tables.

---

## 🎲 Random vs NumPy Random

The script compares:

- `random.random()` → random float between 0 and 1 (standard library)
- `np.random.rand()` → random float between 0 and 1 (NumPy)

It briefly highlights:
- `random` is fine for small/simple use cases.
- NumPy is faster and more suitable for large-scale or scientific computing.

---

## 📁 File Included

- `student_grades_analysis.py`

---

## ▶️ How to Run

Make sure you have the required packages installed:

```bash
pip install pandas matplotlib numpy
Then run:

python student_grades_analysis.py
```
You will see:

Console output with filtered views and joins.

Two plots: a histogram and a scatter plot.

🎓 What This Project Demonstrates
Basic data analysis with Pandas

Filtering, sorting, concatenation, and saving CSV files

Handling missing values with mean imputation

Merging DataFrames (inner/outer join)

Creating histograms and scatter plots with Matplotlib

Using both random and NumPy for random numbers
