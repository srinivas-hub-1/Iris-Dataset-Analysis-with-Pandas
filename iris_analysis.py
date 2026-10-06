import pandas as pd

# Load IRIS.csv from the same folder as this script.
iris_df = pd.read_csv(dataset_path)

# A. Inspect the dataset and calculate summary statistics.
print("\nFirst 10 rows:")
print(iris_df.head(10))

print("\nDataset information:")
iris_df.info()

print("\nShape:", iris_df.shape)
print("\nData types:")
print(iris_df.dtypes)

print("\nSummary statistics:")
summary_statistics = iris_df.describe().loc[["mean", "std", "min", "max"]]
print(summary_statistics)

# B. Filter rows using both conditions.
filtered_virginica_df = iris_df.query(
    'petal_length > 4.5 and species == "Iris-virginica"'
).copy()
print("\nIris-virginica rows with petal_length > 4.5:")
print(filtered_virginica_df)

# C. Group all species and calculate one required statistic per measurement.
species_summary = iris_df.groupby("species").agg(
    average_sepal_length=("sepal_length", "mean"),
    maximum_petal_width=("petal_width", "max"),
    standard_deviation_sepal_width=("sepal_width", "std"),
)
print("\nStatistics by species:")
print(species_summary)

# D. Create a petal ratio feature and preserve the original DataFrame.
iris_with_ratio_df = iris_df.assign(
    petal_ratio=iris_df["petal_length"] / iris_df["petal_width"]
)
print("\nFirst 10 rows with petal_ratio:")
print(iris_with_ratio_df.head(10))

# Calculate the average petal ratio for each species.
average_petal_ratio = (
    iris_with_ratio_df.groupby("species")["petal_ratio"]
    .mean()
    .rename("average_petal_ratio")
)
print("\nAverage petal ratio by species:")
print(average_petal_ratio)
