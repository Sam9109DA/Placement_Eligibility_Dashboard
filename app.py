import streamlit as st
import pandas as pd
from repository import StudentRepository
from database import DatabaseConnection

# connect to DB
db = DatabaseConnection()
db.connect()

repo = StudentRepository(db.conn, db.cursor)

st.title("Placement Eligibility Dashboard")
if "students" not in st.session_state:
    st.session_state.students = None

if "filters" not in st.session_state:
    st.session_state.filters = None

# show total students
total = repo.total_students()
st.write(f"Total Students: {total}")

# inputs
codekata = st.slider("Minimum CodeKata Score", 0, 100, 50)
ct = st.slider("Minimum Career Track Score", 0, 100, 50)
# show filters
current_filters = (codekata,ct)

if st.session_state.filters != current_filters:
    st.session_state.students = None  # reset old data
    st.session_state.filters = current_filters

# button
if st.button("Find Eligible Students"):
    with st.spinner("Fetching eligible students..."):
        st.session_state.students = repo.get_eligible_students(codekata, ct)

students = st.session_state.students

# display
if students is not None:
    st.markdown("---")

    if len(students) > 0:
        df = pd.DataFrame(students, columns=[
            "ID", "Name", "CodeKata", "Career Track"
        ])

        st.success(f"Eligible Students: {len(df)}")

        search = st.text_input("Search Student by Name")

        if search:
            df = df[df["Name"].str.contains(search, case=False)]

        st.dataframe(df)
#chart
       
        # Top performers
        top_df = df.sort_values(by="CodeKata", ascending=False).head(10)

        st.subheader("Top 10 CodeKata Performers")
        st.bar_chart(top_df.set_index("Name")["CodeKata"])

# insights(sql queries)

        st.markdown("---")
        st.header("📊 Insights Dashboard")

# session state
        if "selected_insight" not in st.session_state:
          st.session_state.selected_insight = None

# buttons
        col1, col2, col3 = st.columns(3)

        if col1.button("Eligibility %"):
         st.session_state.selected_insight = "eligibility"

        if col2.button("Avg CodeKata"):
         st.session_state.selected_insight = "avg"

        if col3.button("Top Students"):
          st.session_state.selected_insight = "top"

        if st.button("Placement Status"):
          st.session_state.selected_insight = "placement"

        if st.button("Performance vs Placement"):
          st.session_state.selected_insight = "performance"  

        if st.button("Soft Skills Impact"):
          st.session_state.selected_insight = "softskills"  

# display
        if st.session_state.selected_insight == "eligibility":
          value = repo.get_eligibility_percentage()
          st.metric("Eligibility %", f"{value}%")

        elif st.session_state.selected_insight == "avg":
            value = repo.get_avg_codekata()
            st.metric("Avg CodeKata", value)

        elif st.session_state.selected_insight == "top":
            data = repo.get_top_students()
            df_top = pd.DataFrame(data, columns=["Name", "Total Score"])
            st.subheader("🏆 Top 5 Students")
            st.dataframe(df_top)

        elif st.session_state.selected_insight == "placement":
             data = repo.get_placement_distribution()
             df_place = pd.DataFrame(data, columns=["Status", "Count"])

             st.subheader("📊 Placement Status Distribution")
             st.bar_chart(df_place.set_index("Status"))

        elif st.session_state.selected_insight == "performance":
             data = repo.get_performance_vs_placement()
             df_perf = pd.DataFrame(data, columns=["Status", "Avg CodeKata", "Avg CT"])
             df_perf = df_perf.round(2) 

             st.subheader("📊 Performance vs Placement")
             st.dataframe(df_perf)

             st.caption(
             "Insight: Higher CodeKata scores alone do not guarantee placement. "
             "Other factors like Career Track or soft skills may influence outcomes."
             )
        elif st.session_state.selected_insight == "softskills":
            data = repo.get_softskills_vs_placement()
            df_soft = pd.DataFrame(data, columns=["Status", "Communication_Score", "Teamwork_Score"])

    # convert to numeric for calculations
            df_soft["Communication_Score"] = pd.to_numeric(df_soft["Communication_Score"])
            df_soft["Teamwork_Score"] = pd.to_numeric(df_soft["Teamwork_Score"])

            df_soft = df_soft.round(2)

            st.subheader("🧠 Soft Skills vs Placement")
            st.dataframe(df_soft)

    #  DYNAMIC INSIGHT LOGIC STARTS HERE

            placed = df_soft[df_soft["Status"] == "Placed"].iloc[0]
            not_placed = df_soft[df_soft["Status"] == "Not Placed"].iloc[0]

            comm_diff = placed["Communication_Score"] - not_placed["Communication_Score"]
            team_diff = placed["Teamwork_Score"] - not_placed["Teamwork_Score"]

            if comm_diff > 2 or team_diff > 2:
              insight = (
            "Insight: Placed students show noticeably higher soft skill scores, "
            "suggesting soft skills play a role in placement."
        )

            elif comm_diff < -2 or team_diff < -2:
               insight = (
            "Insight: Surprisingly, not placed students have similar or higher soft skill scores, "
            "indicating other factors influence placement."
        )

            else:
             insight = (
            "Insight: Soft skill scores are similar across groups, suggesting limited impact "
            "on placement in this dataset."
        )

             st.caption(insight)
       


# Distribution
        st.subheader("Score Distribution")
        st.bar_chart(df["CodeKata"].value_counts().sort_index())
# download
        st.download_button(
            "Download as CSV",
            df.to_csv(index=False),
            "eligible_students.csv",
            "text/csv"
        )
    else:
        st.warning("No students meet the selected criteria")

else:
    st.info("Click 'Find Eligible Students' to load data")