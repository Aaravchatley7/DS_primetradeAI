## Trader Performance vs Market Sentiment Analysis

## Objective

This project analyzes how market sentiment (Fear vs Greed) impacts trader behavior and performance on Hyperliquid.

The goal is to identify patterns that can help inform better trading strategies.


##  Dataset

* Bitcoin Market Sentiment (Fear/Greed Index)
* Historical Trader Data (Hyperliquid trades)


##  Methodology

* Cleaned and standardized both datasets (handled timestamps, column inconsistencies)
* Merged datasets on a daily level
* Created key metrics:

  * Daily PnL
  * Win rate
  * Trade frequency
  * Trade size
* Performed:

  * Performance analysis (PnL vs sentiment)
  * Behavioral analysis (trade patterns)
  * Trader segmentation (frequent vs infrequent, size-based)


##  Key Insights

* Trader performance varies across sentiment regimes, with noticeable differences in PnL distribution.
* Increased trading activity does not necessarily lead to higher profitability.
* Larger trade sizes do not consistently improve returns and may increase risk exposure.
* Trader behavior adapts to market sentiment, influencing positioning and activity levels.

##  Strategy Recommendations

1. Reduce trading aggressiveness during Fear periods due to higher volatility and inconsistent outcomes.
2. Align trades with market trends during Greed periods for better performance.
3. Avoid overtrading, as higher activity does not guarantee better returns.
4. Focus on consistency rather than aggressive trading strategies.


##  Bonus (Optional)

A simple predictive model was built to estimate next-day trader profitability using sentiment and behavioral features, achieving ~66% accuracy.


##  How to Run

1. Open the notebook (`.ipynb`) in Google Colab or Jupyter Notebook
2. Install required libraries:

   ```
   pip install pandas matplotlib seaborn scikit-learn
   ```
3. Run all cells sequentially
4. At the end install the data as a csv file and run the app.py code in terminl using the command streamlit run app.py to get the bonus part


##  Files Included

* `AaravChatley_DataScienceIntern.ipynb` → Main notebook
* `README.md` → Project documentation
*  charts/screenshots
*  `app.py` to run streamlit ui
*  `final_data.csv` for app.py to interpret the results

