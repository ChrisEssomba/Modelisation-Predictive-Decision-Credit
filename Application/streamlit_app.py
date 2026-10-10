import streamlit as st
import pickle
import numpy as np
from PIL import Image

# Configure page
st.set_page_config(
    page_title="Credit Approval Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def load_css():
    st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stSelectbox>div>div>select, .stNumberInput>div>div>input {
            background-color: #ffffff;
            border: 1px solid #ced4da;
        }
        .stButton>button {
            background-color: #4a6fa5;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
        }
        .binary-option {
            font-size: 0.9rem;
            color: #666;
            margin-top: -10px;
            margin-bottom: 15px;
        }
        .result-box {
            padding: 1.5rem;
            border-radius: 8px;
            margin-top: 1.5rem;
            font-size: 1.2rem;
            text-align: center;
        }
        .approved {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .rejected {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Load model
@st.cache_resource
def load_model():
    try:
        return pickle.load(open('./Model/model.pkl', 'rb'))
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

model = load_model()

# App header
st.title("💳 Credit Approval Predictor")
st.markdown("""
    This AI-powered tool predicts credit approval based on the applicant's financial information.
    **Please provide accurate information for best results.**
""")

# Main form
with st.form("credit_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Primary Applicant")
        
        applicant_income = st.number_input(
            "Applicant Income (USD)",
            min_value=0,
            value=5000,
            help="Gross monthly income of the primary applicant"
        )
        
        loan_amount = st.number_input(
            "Loan Amount (USD)",
            min_value=100,
            value=10000,
            help="Total amount of credit requested"
        )
        
        married = st.selectbox(
            "Married?",
            options=[("No", 0), ("Yes", 1)],
            format_func=lambda x: x[0],
            help="Marital status of the applicant"
        )
      
        
        dependents = st.selectbox(
            "Has Dependents?",
            options=[("No", 0), ("Yes", 1)],
            format_func=lambda x: x[0],
            help="Whether the applicant has financial dependents"
        )
       
    with col2:
        st.subheader("Additional Information")
        
        coapplicant_income = st.number_input(
            "Co-applicant Income (USD)",
            min_value=0,
            value=0,
            help="Gross monthly income of co-applicant (if any)"
        )
        
        self_employed = st.selectbox(
            "Self-Employed?",
            options=[("No", 0), ("Yes", 1)],
            format_func=lambda x: x[0],
            help="Whether the applicant is self-employed"
        )
       
        
        credit_history = st.selectbox(
            "Good Credit History?",
            options=[("No", 0), ("Yes", 1)],
            format_func=lambda x: x[0],
            help="Whether the applicant has a good credit history"
        )

    submitted = st.form_submit_button("Predict Approval", type="primary")

# Prediction logic
if submitted and model:
    with st.spinner("Analyzing application..."):
        try:
            # Extract numeric values from selectbox tuples
            married_val = married[1]
            dependents_val = dependents[1]
            self_employed_val = self_employed[1]
            credit_history_val = credit_history[1]
            
            features = np.array([[
                loan_amount,
                applicant_income,
                dependents_val,
                self_employed_val,
                credit_history_val,
                married_val,
                coapplicant_income
            ]])
            
            prediction = model.predict(features)
            
            if prediction[0] == 1:
                st.markdown(
                    f"""
                    <div class="result-box approved">
                        <h3>🎉 Credit Approved</h3>
                        <p>This application meets our credit criteria.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div class="result-box rejected">
                        <h3>❌ Credit Denied</h3>
                        <p>This application does not meet our current lending standards.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Sidebar with info
with st.sidebar:
    st.title("Field Information")
    st.markdown("""
    **Primary Application**
    - **Annual Income (USD):**
        Your net annual income, excluding taxes and deductions.
        
    - **Has Dependents:**
        Do you financially support any dependents (e.g., children, elderly family members)?
  
    **Other Fields:**
    - **Co-applicant Income (USD):** 
        If you're applying for the loan with someone else, enter their total annual income contribution. Otherwise, enter 0.
    
    - **Credit_History:** 
        Have you previously taken out and repaid a loan or credit successfully?
    
    """)
    
    st.markdown("---")
    st.markdown("""
    **Data Privacy Notice:**
    All information entered is processed securely and not stored.
    """)

# Footer
st.markdown("---")
st.caption("Credit Approval Prediction System v1.0 | For demonstration purposes only")