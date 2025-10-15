# Content-Monetization-Modeler

**Goal:** Build a Linear Regression model that accurately estimates YouTube ad revenue for individual videos based on performance and contextual features, and deploy it using a simple Streamlit web application.

 Tech Stack
- **Programming Language:** Python 3.13.5  
- **Libraries:** pandas, numpy, scikit-learn, streamlit, matplotlib, seaborn  
- **Machine Learning Algorithms:** Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting  
- **Deployment:** Streamlit Web App  

 Approach

# 1. **Data Understanding**
- Dataset includes metrics such as *views, likes, comments, watch time, category, country, and ad revenue (USD)*.  
- Target variable: `ad_revenue_usd`  
- Preprocessing involved handling missing values, removing duplicates, and encoding categorical data.

 2. **Feature Engineering**
- Categorical variables encoded using **OneHotEncoder**
- Numerical variables scaled with **StandardScaler**
- Train-test split applied for robust evaluation

 3. **Model Building**
- Built multiple regression models for comparison:
  - Linear Regression  
  - Ridge Regression  
  - Lasso Regression  
  - Decision Tree  
  - Random Forest  
  - Gradient Boosting

- Evaluation Metrics:**
  - R² Score
  - Mean Squared Error (MSE)
  - Root Mean Squared Error(RMSE)
  - Mean Absolute Error(MAE)

### 4. **Model Performance**
| Model | R² | MSE |
|--------|----|----|
| Linear Regression | 0.9526 | 181.69 |
| Ridge Regression | 0.9526 | 181.69 |
| Lasso Regression | **0.9526** | **181.67** |
| Decision Tree | 0.9420 | 222.37 |
| Random Forest | 0.9498 | 192.34 |
| Gradient Boosting | 0.9523 | 182.85 |

**Result:** Lasso Regression performed the best, offering strong predictive accuracy.

---

 Streamlit Web App
The Streamlit app allows users to:
- Input video metrics (views, likes, comments, etc.)  
- Instantly predict estimated YouTube ad revenue  
- Visualize model performance and feature importance  


Results & Insights
- Strong correlation between views, watch time, and ad revenue.  
- Engagement metrics like likes and comments moderately influence earnings.  
- Lasso Regression achieved high accuracy (R² ≈ 0.95).  
- The model generalizes well and can guide content monetization strategy.

Conclusion
The **Content Monetization Modeler** demonstrates the power of data-driven insights in optimizing YouTube revenue generation.  
By combining **machine learning** with an interactive **Streamlit interface**, this project provides creators and analysts
 practical tool for strategic decision-making in the digital content ecosystem.
