# Built a Retail Sales & Profit Dashboard Using Python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -----------------------------
# Monthly Sales Data
# -----------------------------
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug'
])

sales = np.array([
    20000, 25000, 30000, 28000,
    35000, 40000, 42000, 45000
])

profit = np.array([
    5000, 7000, 9000, 6500,
    10000, 12000, 12500, 15000
])

customers = np.array([
    120, 150, 170, 160,
    200, 230, 250, 270
])

# -----------------------------
# Product Data
# -----------------------------

products = np.array([
    'Laptop',
    'Phone',
    'Headphones',
    'Keyboard',
    'Mouse'
])

product_profit = np.array([
    25000,
    18000,
    8000,
    6000,
    4000
])

# -----------------------------
# Creating DataFrame
# -----------------------------

df = pd.DataFrame({
    'Month': months,
    'Sales': sales,
    'Profit': profit,
    'Customers': customers
})

print(df)

# -----------------------------
# Extra Data for Histogram
# -----------------------------

daily_sales = np.array([
    2000, 2200, 2500, 2100, 2700,
    3000, 2800, 3500, 3300, 3600,
    4000, 4200, 3900, 4100, 4500
])



# Changing Background Color

plt.style.use('ggplot')

# Creating Figure

fig,ax = plt.subplots(3,2, figsize = (14,10),dpi = 100)



# Figure1 :- Line Plot

ax[0,0].plot(df["Month"],df["Sales"],color = 'green',marker = 'o',label = 'Monthly_Sales')
ax[0,0].set_title("Monthly Sales")
ax[0,0].set_xlabel("Months")
ax[0,0].set_ylabel("Sales")
ax[0,0].grid(True,color = 'white',alpha = 0.3,linestyle = '--')
ax[0,0].legend()


# Figure2:- Bar Plots
ax[0,1].bar(products,product_profit,color = 'darkblue',label = 'Product_Profits')
ax[0,1].set_title("Products & Profits")
ax[0,1].set_xlabel("Products")
ax[0,1].set_ylabel("Profits")
ax[0,1].grid(True,color = 'white',alpha = 0.3,linestyle = '--')
ax[0,1].legend()


# Figure3:- Scatter Plot
ax[1,0].scatter(df["Sales"],df["Profit"],color = 'purple',s = 100,label = 'Sales & Profits')
ax[1,0].set_title("Sales Vs Profits")
ax[1,0].set_xlabel("Sales")
ax[1,0].set_ylabel("Profits")
ax[1,0].grid(True,color = 'white',alpha = 0.3,linestyle = '--')
ax[1,0].legend()

# Figure4:- Histogram

ax[1,1].hist(daily_sales,bins = 'fd',color = 'skyblue',edgecolor = 'white',label = 'Each Day Sales')
ax[1,1].set_title("Daily Sales")
ax[1,1].set_xlabel("Sales Per Day")
ax[1,1].set_ylabel("Frequency")
ax[1,1].grid(True,color = 'white',alpha = 0.3,linestyle = '--')
ax[1,1].legend()

# Figure5:- Line Plot

ax[2,0].plot(df["Month"],df["Customers"],color = 'red',marker = 'o',label = 'Customers Trend')
ax[2,0].set_title("Each Month Customers Growth")
ax[2,0].set_xlabel("Months")
ax[2,0].set_ylabel("Customers Growth")
ax[2,0].grid(True,color = 'white',alpha = 0.3,linestyle = '--')
ax[2,0].legend()

ax[2,1].axis('off')

# Creating a One Headline To The Figure
fig.suptitle("Retail Sales & Profit Dashboard Using Python",fontsize = 16)
fig.tight_layout(rect = [0,0,1,0.95])

# Showing Graph
plt.show()