import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Create Employee Data
data = {
    'Emp_ID': range(101, 121),
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Vikram', 'Neha', 'Arjun', 'Kavita', 'Rohan', 'Meena',
             'Sameer', 'Pooja', 'Karan', 'Divya', 'Manish', 'Ritika', 'Anil', 'Tina', 'Suresh', 'Jyoti'],
    'Department': ['HR', 'IT', 'Sales', 'Finance', 'IT', 'HR', 'Sales', 'Finance', 'IT', 'Sales',
                   'HR', 'Finance', 'Sales', 'IT', 'Finance', 'HR', 'IT', 'Sales', 'Finance', 'HR'],
    'Experience': [2, 5, 3, 7, 6, 4, 2, 8, 9, 5, 4, 6, 3, 7, 10, 5, 8, 2, 9, 3],
    'Salary': [35000, 65000, 42000, 80000, 75000, 50000, 39000, 85000, 90000, 62000,
               54000, 78000, 41000, 83000, 95000, 57000, 88000, 40000, 92000, 46000],
    'Performance': [8, 9, 7, 8, 9, 6, 7, 10, 9, 8, 6, 9, 7, 9, 10, 8, 9, 6, 10, 7]
}

df = pd.DataFrame(data)

# 2️⃣ Create Dashboard
plt.figure(figsize=(18, 10))
plt.suptitle('Employee Dashboard', fontsize=16, fontweight='bold', color='navy')


# --- Graph 1: Average Salary by Department ---
plt.subplot(2, 3, 1)
df.groupby('Department')['Salary'].mean().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Avg Salary by Department', fontsize=10)
plt.ylabel('Salary', fontsize=9)
plt.xticks(rotation=0, fontsize=8)
plt.yticks(fontsize=8)

# --- Graph 2: Employee Count by Department ---
plt.subplot(2, 3, 2)
df['Department'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90,
                                    colors=['lightcoral','lightblue','lightgreen','orange'], textprops={'fontsize':8})
plt.title('Employee Count by Department', fontsize=10)
plt.ylabel('')

# --- Graph 3: Salary vs Experience ---
plt.subplot(2, 3, 3)
plt.scatter(df['Experience'], df['Salary'], color='orange', edgecolor='black', s=80)
plt.title('Salary vs Experience', fontsize=10)
plt.xlabel('Experience (Years)', fontsize=9)
plt.ylabel('Salary', fontsize=9)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# --- Graph 4: Top 5 Highest Paid Employees ---
plt.subplot(2, 3, 4)
top5 = df.nlargest(5, 'Salary')
plt.bar(top5['Name'], top5['Salary'], color='lightgreen', edgecolor='black')
plt.title('Top 5 Paid Employees', fontsize=10)
plt.xticks(rotation=30, fontsize=8)
plt.yticks(fontsize=8)

# --- Graph 5: Average Performance by Department ---
plt.subplot(2, 3, 5)
df.groupby('Department')['Performance'].mean().plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('Avg Performance by Dept', fontsize=10)
plt.ylabel('Performance', fontsize=9)
plt.xticks(rotation=0, fontsize=8)
plt.yticks(fontsize=8)

# --- Graph 6: Experience Distribution ---
plt.subplot(2, 3, 6)
plt.hist(df['Experience'], bins=8, color='plum', edgecolor='black')
plt.title('Experience Distribution', fontsize=10)
plt.xlabel('Years of Experience', fontsize=9)
plt.ylabel('No. of Employees', fontsize=9)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)




# --- Adjust layout ---
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()