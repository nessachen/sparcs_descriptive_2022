import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('sparcs-2022.csv')

# Data preparation

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_').str.replace('+', '')

pd.set_option('display.float_format', lambda x: '%.3f' % x)

df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')

df['total_charges'].isna().sum()
df['total_costs'].isna().sum()
df['length_of_stay'].isna().sum()

# Data analysis

## Basic descriptive statistics
columns_focus = ['age_group', 'gender', 'length_of_stay', 'type_of_admission', 'total_charges', 'total_costs']
df_focus = df[columns_focus]

df_focus['total_charges'].describe()
df_focus['total_charges'].mode()

df_focus['total_costs'].describe()
df_focus['total_costs'].mode()

df_focus['length_of_stay'].describe()
df_focus['length_of_stay'].mode()

## Exploring categorical variables
plt.figure(figsize=(10, 6))
age_count = df_focus['age_group'].value_counts()
sns.barplot(x=age_count.index, y=age_count.values)
plt.title('Distribution of Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.savefig('age_count.png')
plt.show()
plt.clf()

plt.figure(figsize=(10, 6))
gender_count = df_focus['gender'].value_counts()
sns.barplot(x=gender_count.index, y=gender_count.values)
plt.title('Distribution of Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.savefig('gender_count.png')
plt.show()
plt.clf()

plt.figure(figsize=(10, 6))
admission_count = df_focus['type_of_admission'].value_counts()
sns.barplot(x=admission_count.index, y=admission_count.values)
plt.title('Distribution of Admission Types')
plt.xlabel('Admission Type')
plt.ylabel('Count')
plt.savefig('admission_count.png')
plt.show()
plt.clf()

## Visualizations
plt.figure(figsize=(10, 6))
sns.histplot(data=df_focus['length_of_stay'], bins=10, kde=True)
plt.title('Histogram of Length of Stay')
plt.xlabel('Amount of Days')
plt.ylabel('Frequency')
plt.savefig('length_of_stay_histogram.png')
plt.show()
plt.clf()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_focus['total_charges'])
plt.title('Boxplot of Total Charges')
plt.ylabel('Total Charge')
plt.ylabel('Frequency')
plt.savefig('total_charges_boxplot.png')
plt.show()
plt.clf()

plt.figure(figsize=(8, 8))
plt.pie(data=admission_count, labels=admission_count.index, autopct='%1.1f%%', startangle=90)
plt.title('Admission Types')
plt.axis('equal')
plt.savefig('admission_piechart.png')
plt.show()
plt.clf()

plt.figure(figsize=(10, 6))
sns.barplot(data=df_focus, x='age_group', y='total_costs', estimator=sum, ci=None)
plt.title('Total Costs by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Cost')
plt.savefig('age_cost_barplot.png')
plt.show()
plt.clf()


plt.figure(figsize=(10, 6))
sns.barplot(data=df_focus, x='type_of_admission', y='total_costs', estimator=sum, ci=None)
plt.title('Total Costs by Type of Admission')
plt.xlabel('Type of Admission')
plt.ylabel('Total Cost')
plt.savefig('admission_cost_barplot.png')
plt.show()
plt.clf()

plt.figure(figsize=(10, 6))
sns.barplot(data=df_focus, x='type_of_admission', y='length_of_stay', estimator=sum, ci=None)
plt.title('Length of Stay by Type of Admission')
plt.xlabel('Type of Admission')
plt.ylabel('Length of Stay in Days')
plt.savefig('admission_stay_barplot.png')
plt.show()
plt.clf()


# Summary report
## What is the average length of stay? The average length of stay is 5.716 days which is determined from df_focus['length_of_stay'].describe()
## How does the total cost vary by age group or type of admission? To answer this question, I created the visualizations titled 'Total Costs by Age Group' and 'Total Costs by Type of Admission'. Based on the bar plots, the age group of 0-17 and the admission type of newborn have the greatest total costs by far.
## Any noticeable trends in admissions or charges? Based on the visualizations representing the count of admissions and total costs by type of admission, emergency admissions occur the most in the data, but newborn admissions accumulate the most total costs and I wonder why that is so. I thought there was the possibility that the length of stay for newborns is greater, which could lead to the high total costs. However, emergency admissions were the leading category in length of stay as well. Perhaps the inpatient individuals that are admitted as emergency do not need expensive medical services, whereas newborn admissions might require specialized and costly medical services.

## *Note*: Most of the visualizations have flaws in their layout. I tried troubleshooting with the documentation and other online resources. I am still not sure how to edit the python code to fix the problem or whether it would even be possible to due to the immense size and variation of the data. For example, the y-axis of most visualizations is measured in exponential notation which leads to some categories that have lower values not appearing in the visualization or appear as if it is zero or close to zero. Next, for the pie chart, some sections are very small and the display of the percentages ends up overlapping and blocking each other. Additionally, for the box plot, the visualization looks weird, which I believe may be possibly due to the data values because you can basically only see the outliers and not the actual main sections of the box plot.