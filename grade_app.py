import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Grade Management",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main application */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Header */
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666666;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Section titles */
    .section-title {
        font-size: 25px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Form */
    div[data-testid="stForm"] {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0px 3px 12px rgba(0, 0, 0, 0.05);
    }

    /* Student card */
    .student-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
        box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.05);
    }

    .student-name {
        font-size: 23px;
        font-weight: 700;
    }

    .student-grade {
        font-size: 20px;
        font-weight: 700;
    }

    .student-average {
        font-size: 18px;
        font-weight: 600;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #888888;
        padding: 25px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# GRADE CALCULATION FUNCTION
# =========================================================

def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


# =========================================================
# SESSION STATE
# =========================================================

if "students" not in st.session_state:
    st.session_state.students = []


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">'
    '🎓 Student Grade Management System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Manage student marks, calculate grades and track performance'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SUMMARY CALCULATIONS
# =========================================================

total_students = len(
    st.session_state.students
)

if total_students > 0:

    averages = [
        student["Average"]
        for student in st.session_state.students
    ]

    overall_average = (
        sum(averages) / len(averages)
    )

    highest_average = max(averages)

else:

    overall_average = 0
    highest_average = 0


# =========================================================
# SUMMARY CARDS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="👨‍🎓 Total Students",
        value=total_students
    )

with col2:

    st.metric(
        label="📊 Overall Average",
        value=f"{overall_average:.2f}"
    )

with col3:

    st.metric(
        label="🏆 Highest Average",
        value=f"{highest_average:.2f}"
    )


st.write("")
st.write("")


# =========================================================
# ADD STUDENT
# =========================================================

st.markdown(
    '<div class="section-title">'
    '📝 Add Student'
    '</div>',
    unsafe_allow_html=True
)


with st.form(
    "student_form",
    clear_on_submit=True
):

    # -----------------------------------------------------
    # STUDENT NAME
    # -----------------------------------------------------

    name = st.text_input(
        "Student Name",
        placeholder="Enter student name"
    )


    # -----------------------------------------------------
    # SUBJECT MARKS
    # -----------------------------------------------------

    st.markdown("### 📚 Subject Marks")


    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:

        english = st.number_input(
            "🇬🇧 English",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )


    with col2:

        tamil = st.number_input(
            "தமிழ் Tamil",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )


    with col3:

        maths = st.number_input(
            "🔢 Maths",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )


    with col4:

        evs = st.number_input(
            "🌱 EVS",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )


    with col5:

        hindi = st.number_input(
            "🇮🇳 Hindi",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )


    st.write("")


    # -----------------------------------------------------
    # ADD BUTTON
    # -----------------------------------------------------

    submitted = st.form_submit_button(
        "➕ Add Student",
        use_container_width=True
    )


    # =====================================================
    # SUBMISSION
    # =====================================================

    if submitted:

        # -------------------------------------------------
        # NAME VALIDATION
        # -------------------------------------------------

        if name.strip() == "":

            st.error(
                "⚠️ Please enter the student name."
            )

        else:

            student_name = name.strip()


            # -------------------------------------------------
            # DUPLICATE CHECK
            # -------------------------------------------------

            existing_names = [
                student["Name"].lower()
                for student in st.session_state.students
            ]


            if student_name.lower() in existing_names:

                st.error(
                    f"⚠️ Student '{student_name}' "
                    "already exists."
                )


            else:

                # ---------------------------------------------
                # MARKS
                # ---------------------------------------------

                marks = [
                    english,
                    tamil,
                    maths,
                    evs,
                    hindi
                ]


                # ---------------------------------------------
                # TOTAL
                # ---------------------------------------------

                total = sum(marks)


                # ---------------------------------------------
                # AVERAGE
                # ---------------------------------------------

                average = total / len(marks)


                # ---------------------------------------------
                # GRADE
                # ---------------------------------------------

                grade = calculate_grade(
                    average
                )


                # ---------------------------------------------
                # STUDENT RECORD
                # ---------------------------------------------

                student = {

                    "Name": student_name,

                    "English": english,

                    "Tamil": tamil,

                    "Maths": maths,

                    "EVS": evs,

                    "Hindi": hindi,

                    "Total": total,

                    "Average": round(
                        average,
                        2
                    ),

                    "Grade": grade
                }


                # ---------------------------------------------
                # SAVE
                # ---------------------------------------------

                st.session_state.students.append(
                    student
                )


                # ---------------------------------------------
                # SUCCESS
                # ---------------------------------------------

                st.success(
                    f"✅ {student_name} "
                    "has been added successfully!"
                )


                # ---------------------------------------------
                # REFRESH
                # ---------------------------------------------

                st.rerun()


# =========================================================
# STUDENT RECORDS
# =========================================================

st.write("")


st.markdown(
    '<div class="section-title">'
    '📊 Student Records'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# NO STUDENTS
# =========================================================

if len(st.session_state.students) == 0:

    st.info(
        "📭 No students have been added yet. "
        "Use the form above to add a student."
    )


# =========================================================
# DISPLAY STUDENTS
# =========================================================

else:

    for index, student in enumerate(
        st.session_state.students,
        start=1
    ):

        # -------------------------------------------------
        # STUDENT CARD
        # -------------------------------------------------

        with st.container(border=True):

            # ---------------------------------------------
            # STUDENT HEADER
            # ---------------------------------------------

            col1, col2, col3 = st.columns(
                [2, 1, 1]
            )


            with col1:

                st.markdown(
                    f"### 👨‍🎓 {index}. {student['Name']}"
                )


            with col2:

                st.markdown(
                    f"**🏆 Grade:** {student['Grade']}"
                )


            with col3:

                st.markdown(
                    f"**📊 Average:** "
                    f"{student['Average']:.2f}"
                )


            # ---------------------------------------------
            # SUBJECT MARKS
            # ---------------------------------------------

            st.markdown(
                "##### 📚 Subject Marks"
            )


            c1, c2, c3, c4, c5 = st.columns(5)


            with c1:

                st.metric(
                    "🇬🇧 English",
                    student["English"]
                )


            with c2:

                st.metric(
                    "தமிழ் Tamil",
                    student["Tamil"]
                )


            with c3:

                st.metric(
                    "🔢 Maths",
                    student["Maths"]
                )


            with c4:

                st.metric(
                    "🌱 EVS",
                    student["EVS"]
                )


            with c5:

                st.metric(
                    "🇮🇳 Hindi",
                    student["Hindi"]
                )


            # ---------------------------------------------
            # TOTAL
            # ---------------------------------------------

            st.markdown(
                f"**📊 Total Marks:** "
                f"{student['Total']} / 500"
            )


# =========================================================
# CLEAR ALL STUDENTS
# =========================================================

if len(st.session_state.students) > 0:

    st.write("")
    st.write("")


    col1, col2, col3 = st.columns(
        [1, 1, 1]
    )


    with col2:

        clear_all = st.button(
            "🗑️ Clear All Students",
            use_container_width=True
        )


        if clear_all:

            st.session_state.students = []


            st.success(
                "✅ All student records "
                "have been cleared."
            )


            st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")


st.markdown(
    """
    <div class="footer">

        🎓 Student Grade Management System

        <br>

        Built with Python & Streamlit

    </div>
    """,
    unsafe_allow_html=True
)