# Workplace project: Profit Scoring
Banks and other credit lending institutions have a large cutsomer base with varying behavioural characteristics in terms of spend behaviour, revolving behaviour, age, disposal income, etc. Most of the institutions focus predominantly on booking clients with a low probability of defaulting, rightfully so given the risk involved in borrowing money. 

However, the primary purpose of business lending money is to make a profit and there a few banks actively looking into whether the clients they are booking are likely to be profitable or not, rather than merely charging high rates to potentional defaulters. This project aims to indicate to stakeholders that a good balance of expected risk and expected profitability should be considered. Similar to scorecards that measure risk of defaulting, we develop a profit scoring method to determine profit scores and explore the use of machine learning models in predicting these profit scores.

**Project objective**: The main objective of this project is to build a profit scoring systems that helps to identify high value clients (high profitability with low to medium risk of defaulting). Profit score in this sense refers to the probability of generating high profitability.

## Important links
**1) Project planning**: Click [here](https://trello.com/b/xmYPabfb/workplace-project) for trello project progress board.

**2) Presentation slides**: Click [here](https://docs.google.com/presentation/d/1LY5Smb_PuqboQQasrJBPjQyH3A2vt6ji4ydF6Vteieg/edit#slide=id.gc6f980f91_0_0) for google slides presentation.

**3) PBI dashboard**: Clicke [here](https://app.powerbi.com/groups/me/reports/442ae843-7963-4a78-a942-023e1c6e6f03/5bfcac1093ef468c19e8?redirectedFromSignup=1&experience=power-bi) for Power BI dashboard with exploratory data analysis views.

**4) Streamlit app**: Click [here](https://workplaceprojec-o6csmnjcjysrr3j9sbn8cw.streamlit.app/) for Streamlit profit scoring app.

## Data dictionary
**Column** | **Description** | **Data type**
--- | --- | ---
Id | Unique identifier for each customer | Integer
Account_status  | Indicates the state of a customer's account | String
Salary | The customer's annual gross salary | Float
Internal PD | Probability of default computed internally | Float
External PD | Probability of default computed externally | Float
Loan_amount | Total loan amount granted | Float
Profit | Customer's profit at a point in time | Float
Banking_with_bank | Flag of wether they customer  banks with the bank | Integer
Months_on_book | How long customer has been on the books | Integer
Product | The type of credit product the customer has | String
External_utilisation | Ratio of outstanding balance to loan sizes with other banks | Float
Internal_utilisation | Ratio of outstanding balance to loan size with this bank | Float
Spend_percentage | Monthly amount spent to loan size | Float
Probability | Probaility of being profitable | Float
Profit_score | Probability of profitability converted to a scale of 1-10 | Integer



