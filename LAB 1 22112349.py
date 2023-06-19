#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


# Function to open and read the dataset
def read_dataset(filename):
    dataset = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line:  # Skip empty lines
                row = line.split(';')
                dataset.append(row)
    return dataset


# In[2]:


# Function to print the headers in the file
def print_headers(dataset):
    headers = dataset[0]
    print('Headers in the file:')
    for header in headers:
        print(header)


# In[ ]:




# Function to count customers in each category 'marital'
def count_customers_by_marital(dataset):
    marital_counts = {}
    for row in dataset[1:]:  
        marital_status = row[2]  
        if marital_status in marital_counts:
            marital_counts[marital_status] += 1
        else:
            marital_counts[marital_status] = 1
    print('Count of customers in each marital category:')
    for marital_status, count in marital_counts.items():
        print(f'{marital_status}: {count}')


# In[ ]:


# Function to create a count plot for a chosen column
def create_count_plot(dataset, column_name):
    column_index = dataset[0].index(column_name)
    values = [row[column_index] for row in dataset[1:]]
    value_counts = {}
    for value in values:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    print(f'Count plot for column "{column_name}":')
    for value, count in value_counts.items():
        print(f'{value}: {count}')


# In[ ]:



filename = r'C:\Users\91936\Downloads\bank (1).csv' 
dataset = read_dataset(filename)

print_headers(dataset)
print()
count_customers_by_marital(dataset)
print()


# Advanced Challenge: Create a count plot for a chosen column
column_choice = input('Enter the column name for the count plot: ')
create_count_plot(dataset, column_choice)


# In[ ]:


# Function to prepare a histogram for age using a print statement
def age_histogram(dataset):
    ages = [int(row[0]) for row in dataset[1:]]  # Assuming age column is at index 0
    print('Age Histogram:')
    for age in ages:
        print('*' * age)


# In[ ]:


age_histogram(dataset)
print()


# In[ ]:




