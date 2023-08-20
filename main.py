import csv


def read_data():
    # required task: read data from the spreadsheet function
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data


def calculate_average(list_of_sales):
    # extension task: function 'calculate_average' takes input 'list_of_sales' and calculates the average of the sales
    total_items = len(list_of_sales)
    average = sum(list_of_sales) // total_items  # two slashes to return integer

    return average


def calculate_percentage_differences(sales):
    # extension task: function to calculate the percentage difference between months
    percentage_differences = []

    for index, sale in enumerate(list_of_sales):  # adds an index to keep track of position (0, 6226)
        if index == 0:  # If on first item in list, set to 0 because no previous data - working backwards
            percentage_differences.append(0.00)
        else:
            previous_month = list_of_sales[index - 1]  # store sale value of previous month
            current_month = list_of_sales[index]  # store sale value of current month
            percentage_diff = (float(current_month) - previous_month) / previous_month * 100
            percentage_differences.append(percentage_diff)

    return percentage_differences


sales = read_data()  # reading the data from the spreadsheet

list_of_sales = []
for each_sale in sales:
    sale_as_int = int(each_sale['sales'])  # required task: collect all sales from each month into a single list
    list_of_sales.append(sale_as_int)

print(f'Total sales in 2018 was {sum(list_of_sales)}')  # required task: output the total sales across all months

average_of_sales = calculate_average(list_of_sales)  # extension task: calculate the average
print(f'The average of all sales in 2018 was {average_of_sales}')


# extension task: calculate months with the highest and lowest sales
highest_sale = max(list_of_sales)
lowest_sale = min(list_of_sales)

print(f'The highest sale in 2018 was {highest_sale}')
print(f'The lowest sale in 2018 was {lowest_sale}')


# extension task: calculate monthly changes as a percentage
percentage_differences = calculate_percentage_differences(sales)
print(percentage_differences)


# extension task: output a summary of the results to a spreadsheet

report = {  # create a dictionary of what needs to be output
    'total_sales': sum(list_of_sales),
    'average_of_sales': average_of_sales,
    'lowest_sale': lowest_sale,
    'highest_sale': highest_sale,
}

with open('output.csv', 'w') as output_csv:  # creating a new file called output.csv
    fieldnames = ['total_sales', 'average_of_sales', 'lowest_sale', 'highest_sale']
    spreadsheet = csv.DictWriter(output_csv, fieldnames=fieldnames)

    spreadsheet.writeheader()  # write the fieldnames to the file
    spreadsheet.writerow(report)  # write the values to the file
