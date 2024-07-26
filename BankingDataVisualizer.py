import pandas #Importing pandas for data manipulation and analysis
import matplotlib.pyplot as pyplot #Importing matplotlib for creating visualizations
import seaborn #Importing seaborn for statistical data visualization

def load_data(file_path):
    """
    Load data from a CSV file.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pandas.read_csv(file_path) #Read the CSV file into a variable
        return data
    
    except Exception as e:
        print(f"Error loading data: {e}") #Print error message if loading fails
        return None

def process_data(data):
    """
    Process data by identifying numeric and categorical columns, 
    handling missing values, and converting data types.
    Args:
        data (pd.DataFrame): Raw data.
    Returns:
        tuple: Processed data, numeric columns, and categorical columns.
    """
    #Automatically detect numeric and categorical columns
    numeric_columns = data.select_dtypes(include='number').columns
    categorical_columns = data.select_dtypes(include='object').columns

    if not numeric_columns.any(): #Check if there are any numeric columns
        print("Error: No numeric columns found in the data")
        return None
    
    if not categorical_columns.any(): #Check if there are any categorical columns
        print("Error: No categorical columns found in the data")
        return None
    
    data = data.dropna() #Delete rows with values that are = n/a or none

    #Convert numeric columns to float/decimals
    for column in numeric_columns:
        data[column] = data[column].astype(float)
    
    return data, numeric_columns, categorical_columns

def visualize_bar_chart(data, x_column, y_column, title, xlabel, ylabel):
    """
    Create a bar chart.
    Args:
        data (pd.DataFrame): Data to be visualized.
        x_column (str): Column name for x-axis.
        y_column (str): Column name for y-axis.
        title (str): Title of the chart.
        xlabel (str): Label for x-axis.
        ylabel (str): Label for y-axis.
    """
    pyplot.figure(figsize=(10, 6)) #Set the window size
    
    seaborn.barplot(x = x_column, y = y_column, data = data) #Create a bar plot
    
    pyplot.title(title) #Set the title of the chart
    
    pyplot.xlabel(xlabel) #Set the label for x-axis
    pyplot.ylabel(ylabel) #Set the label for y-axis
    
    pyplot.tick_params(axis = 'x', which = 'major', labelsize = 5) #Change the size of the dates on the x-axis so that they are seen clearly without clashing
    
    pyplot.show() #Display the chart

def visualize_pie_chart(data, column, title):
    """
    Create a pie chart.
    Args:
        data (pd.DataFrame): Data to be visualized.
        column (str): Column name for the pie slices.
        title (str): Title of the chart.
    """
    pyplot.figure(figsize = (8, 8)) #Set the window size
    
    data[column].value_counts().plot.pie(autopct = '%1.1f%%') #Create a pie chart
    
    pyplot.title(title) #Set the title of the chart
    
    pyplot.ylabel('') #Remove the y-label
    
    pyplot.show() #Display the chart

def main(file_path):
    """
    Main function to load, process, and visualize data.
    Args:
        file_path (str): Path to the CSV file.
    """
    data = load_data(file_path)
    
    if data is None: #Check if data loading was successful
        return

    processed_data = process_data(data)
    
    if processed_data is None: #Check if data processing was successful
        return

    data, numeric_columns, categorical_columns = processed_data

    for num_col in numeric_columns: #Loop over all numeric columns
        for cat_col in categorical_columns: #Loop over all categorical columns
            visualize_bar_chart(data, cat_col, num_col, f'Total {num_col} by {cat_col}', cat_col, f'Total {num_col}')
            visualize_pie_chart(data, cat_col, f'Transaction Distribution by {cat_col}')

if __name__ == "__main__":
    file_path = 'C:/Users/aliwa/Downloads/repayment_schedule.csv' #Path to the CSV file
    main(file_path) #Calling the main function