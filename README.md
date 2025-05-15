![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=true)
# Capstone Project: Credit Score Classification Analysis

This project aims to perform ETL (Extract, Transform, Load) process on customer financial data, store it into a CSV file, and create interactive dashboards using Streamlit for visualising insights. The focus is on understanding customer behaviour and identifying financial risks.
This project follows a structured development workflow using GitHub Projects and Pull Requests:

- Tasks were organised and tracked using a Kanban-style Project Board. 
- All pull requests were clearly documented, linked to their respective issues, and included detailed descriptions.

## Use Case

This application is designed for use by financial advisors, business analysts, and risk officers to analyse personal and financial data of customers. Through visual dashboards, it provides deep insights into customer financial health, segment-based trends, and risk behaviours, facilitating data-driven decision-making.

## User Stories

```txt
As a requirement engineer,
I want to identify and select a suitable dataset for the capstone ETL project.

As a data engineer, 
I want to identify usable and relevant columns in the dataset
So that only meaningful data is extracted and displayed to the user in the final product.

As a product owner,
I want to define the user stories and tab-based requirements for the Streamlit app,
So that a Data Engineer can build a meaningful customer financial insights dashboard based on the processed dataset.

As a data engineer,
I want to extract the credit score CSV dataset
So that I can begin building the ETL pipeline.

As a data engineer,
I want to transform the raw data using Pandas
So that it is clean, structured, and analysis-ready.

As a data engineer,
I want to load the cleaned dataset into a CSV format
So that it is ready for analysis.

As a data engineer,
I want to build a Streamlit dashboard
So that the user can explore insights and use the app according to user requirements.

As a data engineer,
I want to unit test the functionalities in the capstone project,
So that I can ensure each component behaves as expected.

As a data engineer,
I want logging integrated into the ETL process,
So that I can monitor execution and diagnose failures.

As a data engineer,
I want documentation,
So that maintainers can efficiently understand the code architecture, setup and usage.

As a data engineer,
I want to deploy the Streamlit app
So that users can access it via a web browser.
```


## Key Components

### 1. Data Extraction

- Source: Raw CSV dataset with customer financial and behavioural data
- Method: Read using Pandas

### 2. Data Transformation

- Clean null values and standardise formats
- Feature engineering for debt-to-income ratio, credit scores, etc.

### 3. Data Loading

- Load processed data into a CSV file

### 4. Visualisation

- Tool: Streamlit
- Tabs:
  - Customer Financial Health
  - Segment Analysis & Trends
  - Risk & Behaviour Insights

## ETL Pipeline Architecture

```mermaid
flowchart TD
    A@{ shape: stadium, label: "Start: Raw Data"} --> B@{ shape: tri, label: "Extract Data"}
    B --> C[Transformations]
    C --> D[Load into CSV file]
    D --> E[Retrieve Data from CSV file]
    E --> F[Plots]
    F --> G([Streamlit Visualisation])

 ```
### Data Transformation Subprocesses
```mermaid
 flowchart LR
    A[Data Transformation*] --> B1[[Drop Unwanted Columns]]
    B1 --> B2[[Clean Data]]
    B2 --> B3[[Convert Data]]
    B3 --> B4[[Check Thresholds]]
    B4 --> B5[[Handle Null Values]]
    B5 --> B6@{ shape: lean-r, label: "Transformed Data" }
 ```
### Table Schema of Transformed Data (`processed_data.csv`)

| #  | Column Name              | Data Type           | SQL Type        | Description                                           | Valid Values / Notes                                                  |
|----|--------------------------|---------------------|------------------|-------------------------------------------------------|------------------------------------------------------------------------|
| 1  | Customer_ID              | String (ID)         | VARCHAR(50)      | Unique customer identifier                           | Alphanumeric (e.g. CUS_0x21b1)                                        |
| 2  | Month                    | String (Month)      | VARCHAR(20)      | Month of the transaction or record                   | January - December                                                    |
| 3  | Name                     | String              | VARCHAR          | Full name of the customer                            | Must contain alphabetic characters or spaces                          |
| 4  | Age                      | Float (years)       | DECIMAL(4,1)     | Age of the customer in years                         | Between 10 and 100                                                    |
| 5  | Occupation               | String (Job Title)  | VARCHAR(100)     | Customer's job or employment role                    | Cleaned and null values imputed using forward/backward fill, grouped by Customer_ID        |
| 6  | Annual_Income            | Float (USD)         | DECIMAL(12,2)    | Annual income in USD                                 | Must be non-negative                                                  |
| 7  | Monthly_Inhand_Salary    | Float (USD)         | DECIMAL(12,2)    | Monthly income after tax (derived from Annual_Income)| Cleaned and null values imputed using forward/backward fill, grouped by Customer_ID                    |
| 8  | Credit_Score             | Categorical         | VARCHAR(30)      | Customer's credit score quality                        | One of: 'Good', 'Standard', 'Bad'                                     |
| 9  | Outstanding_Debt         | Float (USD)         | DECIMAL(12,2)    | Total outstanding debt in USD                        | Must be ≥ 0                                                           |
| 10 | Credit_Utilization_Ratio | Float (%)           | DECIMAL(5,2)     | Ratio of credit used to available credit             | 0–100%, must be ≥ 0                                                   |
| 11 | Credit_History_Age       | Float (months)      | INT              | Age of credit history in months                      | Imputed with median. Original format: '23 Years and 5 Months'         |
| 12 | Payment_of_Min_Amount    | Categorical         | VARCHAR(30)      | Whether minimum payment was made                     | One of: 'Yes', 'No', 'N/A'                                            |
| 13 | Total_EMI_per_month      | Float (USD)         | DECIMAL(12,2)    | Sum of all loan EMIs per month                       | Must be ≥ 0                                                           |
| 14 | Amount_invested_monthly  | Float (USD)         | DECIMAL(12,2)    | Total monthly amount invested by the customer        | Must be ≥ 0 or filled with 0 or median                                |
| 15 | Payment_Behaviour        | Categorical         | VARCHAR(30)      | Spending and payment behavior classification         | '[High\|Low]_spent_[Small\|Medium\|Large]_value_payments'             |
| 16 | Monthly_Balance          | Float (USD)         | DECIMAL(12,2)    | Remaining balance after expenses and investments     | Cleaned and null values imputed using forward/backward fill, grouped by Customer_ID        |

## Streamlit Dashboard Overview

### Tab 1: Customer Financial Health

Explore individual customers’ metrics such as:

- Income vs. Debt ratio
- Monthly Balance trends
- EMI, Investment, Balance Bar Charts

### Tab 2: Segment Analysis & Trends

Group-wise insights such as:

- Monthly Balance by Occupation
- EMI trends by Age
- Credit Score distribution

### Tab 3: Risk & Behaviour Insights

Flag high-risk profiles:

- High debt and low salary
- Missed minimum payments
- Bar chart for red flag behaviour


## Get Started
### Prerequisites

Before running the project, ensure the following are in place:

- Python 3 is installed on your system
- Git is installed to clone the repository
- Clone this repository using:

```bash
git clone <repository_url>
cd <repository_directory>
```

Install all required dependencies using:

```bash
pip install -r requirements.txt
```

### Running the tests

To run tests on this repo execute the following command from the root directory:

```bash
python -m pytest -p no:pytest_postgresql
```

### Running the ETL Pipeline

To execute ETL pipeline and store processed data, run the following command from the root directory:

```bash
python -m scripts.run_etl
```

### Running the Streamlit App

To launch the visualisation dashboard on Streamlit:

```bash
streamlit run app/main.py
```

## Future Work

- Database Integration: Export the processed data to a PostgreSQL database would improve data integrity, support faster queries, and allow better system integration compared to using only CSV files.
- Data Normalisation: Decomposing the denormalised output table into smaller, relational tables reduces redundancy, improves storage efficiency, and enables more maintainable data structures through proper relational design.
- Enhanced Dashboard Interactivity: Expand dashboards by adding features like time sliders to make the Streamlit dashboard more engaging and insightful.
- Predictive Modelling: Incorporating machine learning models to predict credit risk or classify customer profiles based on behavioural patterns would add significant analytical value.
