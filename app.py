import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Analyzer")
st.write("Analyze student performance using Python, Pandas, and Matplotlib.")

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

uploaded_file = st.file_uploader(
    "📂 Upload Student CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = load_data(uploaded_file)

    # ------------------------------
    # Data Processing
    # ------------------------------
    df["Total"] = df["math"] + df["science"] + df["english"]
    df["Average"] = df["Total"] / 3

    def grade(avg):
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "Fail"

    df["Grade"] = df["Average"].apply(grade)

    # ------------------------------
    # Sidebar Filter
    # ------------------------------
    st.sidebar.header("Filters")

    selected_class = st.sidebar.selectbox(
        "Select Class",
        ["All"] + sorted(df["class"].unique().tolist())
    )

    if selected_class != "All":
        filtered_df = df[df["class"] == selected_class]
    else:
        filtered_df = df

    # ------------------------------
    # Metrics
    # ------------------------------
    st.subheader("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Students", len(filtered_df))
    col2.metric("Average Marks", round(filtered_df["Average"].mean(), 2))
    col3.metric("Highest Score", filtered_df["Total"].max())
    col4.metric("Lowest Score", filtered_df["Total"].min())

    # ------------------------------
    # Student Table
    # ------------------------------
    st.subheader("📋 Student Records")
    st.dataframe(filtered_df, use_container_width=True)

    # ------------------------------
    # Top Students
    # ------------------------------
    st.subheader("🏆 Top 5 Students")

    top_students = filtered_df.sort_values(
        by="Total",
        ascending=False
    ).head(5)

    st.table(
        top_students[
            ["name", "class", "Total", "Average", "Grade"]
        ]
    )

    # ------------------------------
    # Failed Students
    # ------------------------------
    st.subheader("❌ Failed Students")

    failed = filtered_df[filtered_df["Grade"] == "Fail"]

    if len(failed) > 0:
        st.dataframe(failed)
    else:
        st.success("No failed students.")

    # ------------------------------
    # Subject Average
    # ------------------------------
    st.subheader("📚 Subject Average")

    subject_avg = filtered_df[
        ["math", "science", "english"]
    ].mean()

    fig1, ax1 = plt.subplots(figsize=(6, 4))

    ax1.bar(subject_avg.index, subject_avg.values)

    ax1.set_ylabel("Average Marks")
    ax1.set_title("Subject Wise Average")

    st.pyplot(fig1)

    # ------------------------------
    # Grade Distribution
    # ------------------------------
    st.subheader("🎯 Grade Distribution")

    grade_counts = filtered_df["Grade"].value_counts()

    fig2, ax2 = plt.subplots(figsize=(6, 6))

    ax2.pie(
        grade_counts,
        labels=grade_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax2.set_title("Grade Distribution")

    st.pyplot(fig2)

    # ------------------------------
    # Class Performance
    # ------------------------------
    st.subheader("🏫 Class-wise Average Performance")

    class_avg = df.groupby("class")["Average"].mean()

    fig3, ax3 = plt.subplots(figsize=(8, 4))

    ax3.bar(class_avg.index, class_avg.values)

    ax3.set_xlabel("Class")
    ax3.set_ylabel("Average Marks")
    ax3.set_title("Class Performance")

    st.pyplot(fig3)

    # ------------------------------
    # Download Processed Data
    # ------------------------------
    st.subheader("⬇ Download Processed Report")

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="student_report.csv",
        mime="text/csv"
    )

else:
    st.info("📂 Please upload a CSV file to begin analysis.")