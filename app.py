
import streamlit as st
import joblib

# Page Configuration
st.set_page_config(
    page_title="Online Retail Analytics",
    page_icon="🛍️",
    layout="wide"
)

# Load Models
cluster_model = joblib.load("customer_segmentation_model.joblib")
recommendation_dict = joblib.load("recommendation_system_full_max.joblib")

# Recommendation Function
def recommend_products(product_name, top_n=5):

    try:
        return recommendation_dict[product_name][:top_n]

    except:
        return ["Product not found"]


# Title
st.title("🛍️ Customer Segmentation & Product Recommendation System")

st.markdown("---")

# Dashboard Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Customers", "4372")

with col2:
    st.metric("Products", "3896")

with col3:
    st.metric("Segments", "4")

st.markdown("---")

# Create Tabs
tab1, tab2 = st.tabs([
    "📊 Customer Segmentation",
    "🎁 Product Recommendation"
])

# ==================================================
# CUSTOMER SEGMENTATION
# ==================================================

with tab1:

    st.subheader("Predict Customer Segment")

    recency = st.number_input(
        "Recency (Days)",
        min_value=0,
        value=10
    )

    frequency = st.number_input(
        "Frequency",
        min_value=0,
        value=5
    )

    monetary = st.number_input(
        "Monetary Value",
        min_value=0.0,
        value=100.0
    )

    if st.button("Predict Segment"):

        prediction = cluster_model.predict(
            [[recency, frequency, monetary]]
        )[0]

        st.success(
            f"Predicted Customer Cluster: {prediction}"
        )

# ==================================================
# PRODUCT RECOMMENDATION
# ==================================================

with tab2:

    st.subheader("Product Recommendation System")

    product = st.text_input(
        "Enter Product Name",
        placeholder="Example: WHITE HANGING HEART T-LIGHT HOLDER"
    )

    if st.button("Recommend Products"):

        recommendations = recommend_products(product)

        if recommendations[0] == "Product not found":

            st.error(
                "Product not found. Please enter the exact product name."
            )

        else:

            st.success("Recommended Products")

            for item in recommendations:
                st.write("✅", item)

st.markdown("---")
st.markdown(
    "Developed using Machine Learning | RFM Analysis | K-Means Clustering | Recommendation System"
)
