import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Mengonversi path relatif menjadi absolut
base_path = os.path.dirname(__file__)
csv_products_path = os.path.join(base_path, 'product_orders.csv')
csv_combined_path = os.path.join(base_path, 'shipping_cost_and_sales.csv')

# Load data
df_products_order = pd.read_csv(csv_products_path)  
data_combined = pd.read_csv(csv_combined_path)

# Define Streamlit app
def main():
    # Set page title
    st.title('E-commerce Public Visualization')
    st.write("Welcome to the E-commerce Public Visualization Dashboard. This dashboard visualizes the relationship between shipping cost and sales amount, as well as the top 10 most popular product categories.")
    st.markdown('---')

    # Display scatter plot
    st.subheader('Visualize the relationship between shipping cost and sales amount')
    st.write("From the visualization results it can be seen that the lower the shipping costs, the higher the goods sold, as for the items with the highest total sales with low shipping costs are beleza_saude")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data_combined, x='freight_value', y='total_penjualan', hue='product_category_name')
    plt.title('Relationship between Shipping Cost and Sales Amount (Top 5 Items 2018)')
    plt.xlabel('Biaya Pengiriman (Freight Value)')
    plt.ylabel('Sales Total')
    plt.grid(True)
    plt.legend(title='Product Name')
    st.pyplot(plt)  
    st.markdown('---')

    # Calculate the frequency of each product category
    category_counts = df_products_order['product_category_name'].value_counts().head(10)
    # Display bar plot
    st.subheader('Top 10 Most Popular Product Categories')
    st.write("From the visualization results above, it can be concluded that mapping the 10 highest selling products is one solution to see consumer interest in products so that companies pay attention to producing products with the highest sales, besides that it is a consideration in the future to produce these goods.")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_counts.values, y=category_counts.index, palette='viridis')
    plt.title('Top 10 Most Popular Product Categories')
    plt.xlabel('Number of Orders')
    plt.ylabel('Product Category')
    plt.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(plt)  

# Run Streamlit app
if __name__ == '__main__':
    main()
