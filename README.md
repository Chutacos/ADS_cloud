# ADS_cloud



---

### Table of Contents

- [Description](#description)
- [Setup&Reproducibility](#Setup&Reproducibility)
- [Deployment Process](#deployment)
- [Monitoring](#monitoring)
- [Technologies](#technologies)
- [License](#license)

---

## Description

### Summary of the Project

**JAD Healthcare Consulting**, contracted by the WHO, is developing a machine learning solution to predict regional COVID-19 outbreak risks using public geographic case data. This initiative aims to optimize resource allocation, such as PPE, clinical equipment, and medications, while providing insights into general COVID trends to inform global healthcare planning. The project focuses on predicting outbreaks rather than individual cases, medical recommendations, or policy decisions, ensuring a clear and manageable scope.

### Data Sources and Preparation

The data for this project comes from the AWS COVID-19 Data Lake, specifically the `jhu_csse_covid_19_timeseries_merged.csv` file, which contains global case data from 2020. While this dataset is valuable, it has limitations due to its incomplete timeline and potential biases in geographic representation. The data will be stored in an S3 bucket for preprocessing and feature engineering. Techniques such as handling missing values, normalizing case counts per capita, and balancing datasets geographically will improve data quality. Exploratory analysis will identify patterns like seasonality and trends to guide model development.



# Setup & Reproducibility 

This project is designed to be fully reproducible from the GitHub repository. Follow these steps to set up the pipeline locally:

## clone Repository

git clone https://github.com/Chutacos/ADS_cloud.git

## Set up Virtual Environment

pip install -r requirements.txt

# Deployment
### Model Development and Evaluation

The team plans to use decision tree-based classification models (e.g., Random Forest, XGBoost, LightGBM) deployed on AWS SageMaker using a "bring-your-own-script" approach for greater control over feature engineering and parameter tuning. These models will predict whether cases will increase or decrease in a given region during the subsequent period. Evaluation metrics include accuracy, precision, recall, F1 score, ROC/AUC analysis, and K-Fold Cross Validation. The chosen instance type (`ml.c5.4xlarge`) balances computational efficiency with memory requirements.


### Future Enhancements

Potential improvements include:
1. **Curating Additional Data**: Incorporating vaccination rates, strain-specific statistics, and traffic data to improve predictive accuracy.
2. **Testing Advanced Models**: Exploring LSTM models, DeepAR, or CNNs for time-series forecasting.
3. **Enhanced Feature Engineering**: Using clustering algorithms to prioritize high-risk areas for interventions like vaccinations or medical assistance.

This project represents a critical step in leveraging machine learning for public health planning and outbreak prevention while addressing privacy, bias, and ethical concerns effectively.



---

# Monitoring

### Security and Ethical Considerations

The project prioritizes privacy by ensuring Protected Health Information (PHI) and Personally Identifiable Information (PII) are de-identified before use. Biases in geographic representation and causality must be addressed to ensure fairness across populations. Ethical concerns include avoiding stigmatization of regions based on predictions and maintaining transparency about the model's limitations.


#### Technologies

- Python


[Back To The Top](#ADS-Cloud)

---

## License

MIT License


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#ADS-Cloud)

