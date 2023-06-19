This repository contains Python code for analyzing a bank dataset. The dataset is stored in a CSV file and includes information about customers such as their age, marital status, education, and more. The code provides several functions to read and analyze the dataset.

# Functions
read_dataset(filename)
This function reads the dataset from a CSV file and returns it as a list of lists. Each inner list represents a row in the dataset, and the elements of the inner lists represent the values in each column.

# print_headers(dataset)
This function takes the dataset as input and prints the headers (column names) in the file.

# count_customers_by_marital(dataset)
This function counts the number of customers in each marital status category and prints the results.

# create_count_plot(dataset, column_name)
This function creates a count plot for a chosen column in the dataset. It counts the occurrences of each value in the chosen column and prints the results.

# age_histogram(dataset)
This function prepares a histogram for the age column in the dataset. It assumes that the age column is at index 0 in each row and prints a visual representation of the histogram using asterisks.

# Usage
To use these functions, follow the steps below:

Ensure you have a CSV file containing the bank dataset.

Set the filename variable in the code to the path of your CSV file.

Execute the code to perform the following actions:

Read the dataset from the file.
Print the headers in the file.
Count the customers in each marital category.
Prompt the user to enter a column name for a count plot.
Create a count plot for the chosen column.
Prepare and print a histogram for the age column.
Please note that this code assumes the dataset follows a specific structure, and any modifications to the dataset structure may require adjustments to the code.
![Alt text](<Output/Screenshot (181).png>)
![Alt text](<Output/Screenshot (182).png>)
Feel free to explore and modify the code as needed for your specific use case. Enjoy analyzing the bank dataset!




