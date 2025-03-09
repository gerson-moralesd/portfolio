# My Projects

### Adaptive Staffing Intelligence
Given a historical dataset from advertisers around the world, we were tasked with developing a dynamic month-by-month staffing plan that ensured that eligible businesses that advertise on Google could access support from Ads Experts. The unpredictable daily influx of new accounts and the dynamic nature of employee availability makes staffing optimization a challenge. 

EDA was performed using Tableau, leading to various visualizations to analyze trends. Two graphs were specially important: the first one, Budget Distribution per Country, showed that in general, all countries' forecasted budget follows a Lognormal distribution. On the other hand, the Sign-Up amount per Country map shows that the US is a premium market, as it has the higher number of advertisers as well as the highest agent salary. For more visualizations, please refer to the link below the poster.

We created a Semi-Markov Decision Process, which is a technique to model situations where you make decisions, but the time between decisions isn’t fixed. Our strategy was based on hiring and firing employees on the first of every month, following constraints given by the problem. We found out that, if following the model optimization recommendations, markets such as the US, India and China could have a higher net profit of up to two million dollars.

Finally, Although we wanted to compare the Semi-MDP with a Semi-MDP and Deep Q-Network model, we could not do it because of computation limitations. Further improvements to the model include comparing both approaches in order to select the best one. A recommendation for stakeholders is to integrate machine-learning based demand forecasting, as well as our model, to predict advertiser sign-ups and adjust hiring before demand spikes.

![Adaptive Staffing Intelligence poster](/assets/img/Adaptive Staffing Intelligence.png)
<a href="https://github.com/gerson-moralesd/portfolio/blob/main/assets/files/Poster%20-%20Adaptive%20Staffing%20Intelligence.pdf">View poster</a> | 
<a href="https://public.tableau.com/app/profile/gerson.morales.deras/viz/AnalyticsScience/Story1?publish=yes">Open Tableau Story</a> 
<br>

### Population Growth and Crime Trends in San Francisco
During the first part of my Machine Learning and Data Analytics class, we worked using real world data from the government to create models that motivate conversations about policy making addressing crime in San Francisco. We developed two logistic regression models, two random forests models, and one XGBoost model, each demonstrating varying levels of accuracy.

The first task was cleaning the data, which involved geospatial mapping and time feature engineering. We then performed other transformations, such as Label and One-Hot encoding. Finally, we mapped these categories into a lower dimensional space to create a target variable for classification. 

After cleaning the data, we perfomed Exploratory Data Analysis and addressed the dataset limitations. For example, we noticed that the most dangerous neighborhoods by crime count were Soma-Potrero-Mission Bay and Western Addition-Buena Vista-Eureka. However, neighborhood specific tagging, such as demographic information, were only available for the years 2020-2022.

Finally, we proposed some policy recommendations that could be implemented based on our findings. Implementing even a subset of those recommendations should, in the long run, lead to a reduction in crime rates and lead to a more efficient allocation of local government and law enforcement resources.

![Population Growth and Crime Trends poster](/assets/img/Population Growth and Crime Trends in San Francisco.png)
<br>

<a href="https://github.com/gerson-moralesd/portfolio/blob/main/assets/files/Population%20Growth%20and%20Crime%20Trends.pdf">View poster</a> | 
<a href="https://github.com/gerson-moralesd/portfolio/blob/main/assets/files/Population%20Growth%20and%20Crime%20Trends%20in%20San%20Francisco.pdf">Read the report</a> 

### SIMIO WAREHOUSE: Fall 2023 Simio Case Study
This project focuses on improving the operations of a warehouse that supports an e-commerce platform selling advanced video cards used in applications like AI and cryptocurrency mining. We used Simio simulations to figure out how many workers are needed and to create efficient inventory policies, aiming to boost efficiency, reduce costs, and keep customers happy.

First, we analyzed a year’s worth of order data, then modeled the warehouse in Simio to test different management scenarios. The main tasks included handling bulk shipments of three types of video cards, testing and packaging them, and managing automated machines that sometimes fail and slow down the process.

We determined the best points to reorder stock and calculated optimal inventory levels for both unpackaged and packaged cards. Our simulation showed that having three workers per shift (totaling nine across three shifts) kept operations running smoothly without delays, meeting customer demand efficiently.

By fine-tuning our inventory policies and using the insights from the simulation, we were able to optimize the warehouse's performance, selling nearly 2 million cards monthly and maintaining reasonable costs. This project highlights the value of simulation tools like Simio in making informed decisions and improving warehouse management.

![Simio Warehouse poster](/assets/img/Simio Warehouse - Fall 2023 Simio Case Study.png)
<br>
<a href="https://github.com/gerson-moralesd/portfolio/blob/main/assets/files/SIMIO%20Warehouse.pdf">View poster</a> | 
<a href="https://github.com/gerson-moralesd/portfolio/blob/main/assets/files/SIMIO%20Warehouse%20file.spfx">Download the simulation</a> 

### Optimizing Distribution Networks for OptiCoffee
OptiCoffee aims to expand its operations in Bogotá and needs to select the best warehouses for storing and transporting coffee. The goal is to ensure a profitable expansion that can meet customer demand while maximizing warehouse capacity.

To accomplish this, we formulated a mathematical model to design the optimal logistics distribution network for OptiCoffee. We optimized cost-efficient coffee distribution across three national networks, considering cost and distance constraints. Our analysis included developing a Python simulation model to evaluate and refine the proposed network design.

We analyzed two scenarios: one with a Triangular distribution and another using the mode scenario. We found that estimating demand with the expected value kept costs low but also lowered the probability of meeting demand. Conversely, using the mode (the most frequently requested value) increased costs but significantly improved the likelihood of meeting demand.

This analysis helps OptiCoffee make informed decisions about warehouse selection, balancing cost with the ability to meet customer needs effectively.

![Optimizing Opticoffee poster](/assets/img/Optimizing Distributions Networks for Opticoffee.png)
<br>
<a href="https://github.com/gerson-moralesd/portfolio/blob/main/assets/files/OptiCoffee.pdf">View poster</a> | 
<a href="https://github.com/gerson-moralesd/portfolio/tree/main/assets/files/OptiCoffee">Open Python files</a> 

### Financial Analysis and Valuation for Mercado Libre - CFA Institute Research Challenge
Mercado Libre (MELI) is a leading e-commerce and fintech company operating across 18 countries in Latin America. The report offers an investment analysis of the company, emphasizing its market dominance, consistent revenue growth, and resilience amidst economic challenges. MELI's one-year price target is set at $1,236.88, which suggests a 12.64% upside, based on a Discounted Cash Flow (DCF) methodology. The company's ability to expand into various high-growth services and markets underpins the favorable growth projections.

The report highlights the evolution of MELI’s revenue streams, with the fintech sector's contribution significantly increasing in 2022, projected to surpass the commerce sector by 2024. This shift indicates a strategic move towards fintech, which is expected to drive more than half of the company's revenue in the coming years. Despite an expected adjustment in growth rates by 2023, the company is projected to maintain double-digit growth through 2025.

MELI's business model includes a comprehensive ecosystem of e-commerce and digital payment services, such as its marketplace, payment solutions, and logistics. The company is a regional leader in e-commerce, particularly in Brazil, Argentina, and Mexico, which collectively account for 94% of its revenues. The fintech sector, particularly in Brazil, has shown substantial growth, enhancing MELI's financial services portfolio and market presence.

The report also addresses the risks and challenges faced by MELI, including operational risks like technological disruptions and macroeconomic factors such as inflation and potential recession. Nonetheless, MELI's strong market positioning, strategic expansions, and robust financial performance underscore its potential for sustained growth and value creation in the Latin American market.

![CFA Challenge - MELI Document Preview](/assets/img/CFA Challenge - MELI.png)
<br>
<a href="https://github.com/gerson-moralesd/portfolio/blob/main/assets/files/CFA%20Challenge%20-%20MELI.pdf">Read the report</a>
