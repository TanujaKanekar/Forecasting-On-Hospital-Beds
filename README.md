# <center> Forecasting On  Availability Of Hospital Beds 

<img align="center" alt="hospitalbed"  width="700" src="https://github.com/TanujaKanekar/Forecasting-On-Hospital-Beds/blob/main/commission%2C%20Dao%20Dao.jpg">

## Objective/Problem Statement
  <p>Total Inpatient Beds have been recorded to understand the occupancy of the beds on a daily basis for a year.Objective is to forecast the data                                       available and find out estimated beds available for the period of next one month with least RMSE value.</p>

## Background
<p> The enormous impact of the COVID− 19 pandemic has surprised many hospitals beginning March 2020. It soon became apparent that the capacity of hospital beds was at the verge of coming under great pressure. Besides a shift of regular beds to specific COVID-19 beds with special hygiene measures, pressure on the number of beds arose primarily from the need to foresee sufficient capacity in the Intensive Care Unit (ICU).</p>
<p>Recently around March-April 2021 the second wave of COVID-19 in India has had severe consequences in the form of spiralling cases, reduced supplies of essential treatments, and increased deaths particularly in the young population that lead.In this condition the hospital beds were fully filled and many people took treatment on the streets too and also due to lack of oxygen.It was hard for everyone to know which hospital has available beds.So keeping this in mind we created a Time Series Forecasting to check the availabilty of Hospital beds.</p>
<p>Not only it is helpful for people to find the Hospital beds but its important for Hospital Management.The Hospital capacity planning is driven by complex dynamics between input, output and the number of available beds. In normal times, hospitals aim to achieve an optimal bed occupancy by maximizing bed occupancy while minimizing overflow, which often has a negative effect on patient outcomes. However, pandemics and natural disasters typically come with a sudden influx of unforeseen patients, which almost instantly pushes the boundaries of a hospital’s capacity. Frontline health care workers, directly engaged in the diagnosis, treatment, and care for patients with COVID-19, are susceptible to experience psychological burden in return, while also being at greater health risks. Lack of bed capacity, scarcity in supplies and high occupancy rates further increases that burden.</p>
<p>The ability to predict hospital bed capacity is essential for monitoring and planning purposes during epidemics, such as the ongoing COVID-19 pandemic</p>

 ## Project Flow
<p><b>Data Understanding:</b> Understanding the attribu>tes of the data, summarize the data by identifying key characteristics, such as data volume and total number of variables.In the data, missing values ,inaccuracies.</p>
<p><b>EDA(Exploratory Data Analysis):</b>Primarily used to see what data can reveal beyond the formal modeling or hypothesis testing task and provides a better understanding of dataset variables and the relationships between them, also uses various plots for checking normality, outliers etc.</p>
<p><b>Stationarity check:</b>Stationarity means that the statistical properties of a time series do not change over time. It is important because many useful analytical tools and statistical tests and models rely on it.</p>
<p><b>Model Building:</b>This process involves setting up ways of collection data, understanding and paying attention to what is important in the data, finding statistical, mathematical or a simulation model to gain understanding and make predictions.</p>
<p><b>Model Evaluation:</b>It aims to estimate the generalization accuracy of a model on future data. It is a phase  that is decided whether the model performs better.</p>
<p><b>Model Deployment:</b>It is a task of exposing the model into real use. It is used to integrate the model into an existing production environment to make practical decisions based on data.</p>
  
## Models Used
<p><b>1) AutoRegressive(AR):</b>This model predicts the future values based on the past values. The process is basically a linear regression of the data in the current series against one or more past values in the same series.</p>
<p><b>2) Moving Average(MA):</b>This model predicts the future values based on the past error values. The process is basically a linear regression of the data in the current series against one or more past values in the same series.</p>
<p><b>3) Autoregressive Moving Average(ARMA):</b>This model uses both the AR and MA model to forecast the data. In ARMA it is assumed that the time series is stationary and when it fluctuates, it does so uniformly around a particular time.</p>
<p><b>4)Autoregressive Integrated Moving Average(ARIMA):</b>This model combines both autoregressive and moving average with the differencing term I which helps to make time series data stationary.</p>
<p><b>5)Seasonal Autoregressive Integrated Moving Average(SARIMA):</b>This model is an extension of ARIMA that explicitly supports univariate time series data with a seasonal component. Also  this model uses differencing at a lag equal to the number of seasons to remove additional seasonal effect.</p> 
<p><b>6)Simple Exponential Smoothing(SES):</b>This model is used when the data is not supporting any trend or seasonal component and it works on weighted averages. The weight id determined by the smoothing parameter α.</p>
<p><b>7)Holts Trend:</b>This model is a valuable extension of exponential smoothing that helps deal with trending data. this model is used when Input data exhibits level and strong upward trend but no seasonality.</p>
<p><b>8)Holts Winter’s Exponential Smoothing(HWES):</b>This model is also called Triple Exponential Smoothing method that is suitable for univariate time series with trend and/or seasonal components.</p>
<p><b>9)Holts Winter’s Exponential Smoothing Additive Season and Trend:</b>This model has additive trend and seasonality. Here the components add together to make up the time series, the three components added here are –seasonality, trend and error. Thus they kind of exhibit linear pattern.</p>
<p><b>10)Holts Winter’s Exponential Smoothing Multiplicative Season and  Additive Trend:</b>This model uses Multiplicative seasonality and Additive trend so here the components are multiplied resulting in effect with percentage growth. This shows kind of exponential trend.</p>
<p><b>11)Prophet:</b>This model is developed by Facebook for univariate time series forecasting and it will automatically provide a good set of hyper parameters.</p> 










