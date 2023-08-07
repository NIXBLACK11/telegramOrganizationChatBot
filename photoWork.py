import os
import matplotlib.pyplot as plt
import telebot


def create_plot(expenditures):
    # Monthly expenditures data (replace with your actual data)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    expenditures = [1000, 1200, 800, 950, 1100, 750, 850, 900, 1000, 1150, 950, 1050]

    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.plot(months, expenditures, marker='o')  # Create the line plot with markers on data points
    plt.title('Monthly Expenditures')
    plt.xlabel('Months')
    plt.ylabel('Expenditure ($)')
    plt.grid(True)  # Add grid lines
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Ensure labels and titles are properly visible

    plt.savefig('monthly_expenditures.png')
