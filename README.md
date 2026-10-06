# Analyse the Iris Dataset with Python and Pandas

I use Python and Pandas to inspect flower measurements, filter records, compare species, and create a petal ratio feature.

## My objective

I explore the Iris dataset through four practical analysis tasks. I turn each question into readable Python code and choose Pandas operations that match the required output.

## Skills I demonstrate

| Skill | How I apply it |
|---|---|
| Python and Pandas | I load a CSV file and analyse its data using DataFrames. |
| Exploratory data analysis | I inspect rows, dataset dimensions, column types, and summary statistics. |
| Conditional filtering | I combine numeric and category conditions with `query()`. |
| Grouped aggregation | I use `groupby()` and named aggregations to compare species. |
| Feature engineering | I create a petal ratio with `assign()` and calculate its average for each species. |
| Readable code | I choose descriptive variable names and explain each task through comments. |
| Data handling | I keep filtered records separate and preserve the original DataFrame when I create a feature. |

## How I approach the analysis

### A. Inspect the dataset

I display the first 10 rows, check the shape and data types, and calculate the mean, standard deviation, minimum, and maximum for numeric columns.

### B. Filter flower records

I select rows that satisfy both conditions:

- `petal_length > 4.5`
- `species == "Iris-virginica"`

I store these rows in `filtered_virginica_df` so that I can use the complete dataset for the remaining tasks.

### C. Compare all species

I group the complete dataset by `species` and calculate:

- Average `sepal_length`.
- Maximum `petal_width`.
- Standard deviation of `sepal_width`.

I use named aggregations to give each output column a clear name and calculate exactly the statistic that each question requires.

### D. Create a petal ratio feature

I divide `petal_length` by `petal_width` and store the result in a new `petal_ratio` column. I use `assign()` to create a new DataFrame, then calculate the average ratio for each species.

## How I improve my initial approach

My initial code used short variable names and applied every aggregation to every selected measurement column. I now use descriptive names and select one required statistic for each measurement.

I also group the complete dataset for species comparisons. This step includes every species instead of limiting the summaries to the filtered Iris-virginica records.

## Run the project

Use Python and Pandas, which are free and open source.

1. Download `iris_analysis.py` and `requirements.txt` into one folder.
2. Place your assignment dataset in the same folder and name it `IRIS.csv`.
3. Install Pandas and run the script:

```bash
python -m pip install -r requirements.txt
python iris_analysis.py
```

Provide these dataset columns:

```text
sepal_length, sepal_width, petal_length, petal_width, species
```

Use numeric values in the measurement columns. The filter matches the label `Iris-virginica` exactly. Use non-zero petal widths to calculate meaningful ratios.

To run the code in a notebook, replace the `dataset_path` assignment with your dataset path:

```python
dataset_path = "/content/IRIS.csv"
```

## Dataset and outputs

Use the Iris CSV from the assignment. Download it separately; this project package contains the code, README, and dependency file.

Add the original dataset source link here before publishing.

The script prints the first 10 rows, dataset information, summary statistics, matching flower records, species statistics, and average petal ratios. Run the script on your assignment dataset before adding numerical findings to this README.

## My learning focus

I am building practical Python and Pandas skills for data analysis. I connect data inspection, filtering, and grouped statistics with feature creation as I progress from data preparation towards machine learning.

This project demonstrates my data analysis foundations. I create a feature in this project; I have not trained or evaluated a machine learning model here.
