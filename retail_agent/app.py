import streamlit as st
from nl_sql import generate_sql
from sql_executor import run_sql

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Retail NL-SQL Agent",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.title("📊 Retail NL-SQL Agent")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Supported Queries",
        "7"
    )

with col2:
    st.metric(
        "Dataset Records",
        "7.9K"
    )

with col3:
    st.metric(
        "Agent Type",
        "NL → SQL"
    )

st.markdown(
    """
Ask business questions in natural language and automatically generate SQL,
execute it on the retail database, and visualize the results.
"""
)

st.markdown("---")

# ==========================================
# QUESTION INPUT
# ==========================================

question = st.text_input(
    "Ask a Business Question",
    placeholder="Example: Revenue by City"
)

# ==========================================
# GENERATE INSIGHT
# ==========================================

if st.button("Generate Insight"):

    if question.strip() == "":

        st.warning(
            "Please enter a business question."
        )

    else:

        sql_query = generate_sql(question)

        if sql_query is None:

            st.error(
                "Unsupported question. Please use one of the supported query patterns."
            )

        else:

            # ==========================================
            # GENERATED SQL
            # ==========================================

            st.subheader("Generated SQL")

            st.code(
                sql_query,
                language="sql"
            )

            result = run_sql(sql_query)

            # ==========================================
            # KPI SECTION
            # ==========================================

            st.subheader("Key Insights")

            kpi1, kpi2, kpi3 = st.columns(3)

            with kpi1:

                st.metric(
                    "Records Returned",
                    len(result)
                )

            with kpi2:

                try:

                    top_value = result.iloc[0, 1]

                    st.metric(
                        "Top Revenue",
                        f"₹{top_value/10000000:.2f} Cr"
                    )

                except:
                    pass

            with kpi3:

                try:

                    top_item = result.iloc[0, 0]

                    st.metric(
                        "Top Performer",
                        str(top_item)
                    )

                except:
                    pass

            # ==========================================
            # RESULTS TABLE
            # ==========================================

            display_result = result.copy()

            try:

                if len(display_result.columns) >= 2:

                    numeric_col = display_result.columns[1]

                    display_result[numeric_col] = (
                        display_result[numeric_col] / 10000000
                    ).round(2)

            except:
                pass

            st.subheader("Results")

            st.dataframe(
                display_result,
                use_container_width=True
            )

            # ==========================================
            # CHART
            # ==========================================

            try:

                if len(display_result.columns) >= 2:

                    chart_data = display_result.copy()

                    chart_data = chart_data.set_index(
                        chart_data.columns[0]
                    )

                    st.subheader("Business Visualization")

                    st.caption(
                        "Revenue values displayed in Crores"
                    )

                    st.bar_chart(chart_data)

            except:
                pass

            # ==========================================
            # BUSINESS INSIGHT
            # ==========================================

            try:

                if len(display_result) > 0:

                    first_col = display_result.columns[0]

                    top_item = display_result.iloc[0][first_col]

                    top_value = display_result.iloc[0][display_result.columns[1]]

                    st.subheader("Business Insight")

                    st.success(
                        f"""
🏆 Top Performing {first_col.title()}

📌 Name: {top_item}

💰 Revenue: ₹{top_value:.2f} Crore

This is currently the highest performing entry based on revenue generated.
"""
                    )

            except:
                pass

# ==========================================
# SUPPORTED QUESTIONS
# ==========================================

st.markdown("---")

st.subheader("Supported Questions")

st.write("• Revenue by City")
st.write("• Revenue by Category")
st.write("• Top Customers")
st.write("• Top Products")
st.write("• Revenue by Payment Method")
st.write("• Monthly Revenue")
st.write("• Pending Payments")

st.info(
    """
This agent converts Natural Language into SQL,
executes the query on SQLite,
and returns business insights with visualizations.
"""
)