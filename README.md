# Diamond - Price - Prediction:

- [LinkedIn]([https://www.linkedin.com/in/om-kuman-25805a251/]))

## Tables of content:
* [Overview](#Overview)
* [About the data](#About-the-data)
* [Technologies Used](#Technologies-Used)
* [Installation Steps](#Installation-Steps)
* [Directory Structure](#Directory-Structure)
* [Visual Insights of Data](#Visual-Insights-of-Data)
* [Comaparing Data Models](#Comaparing-Data-Models)
	
	
   <img target="_blank" src="static\builtin\napkin-selection.png" width=900>




## Overview:

****The Diamond Price Prediction**** project is an end-to-end machine learning solution designed to forecast
diamond prices accurately. Diamonds, being highly valuable and sought-after gems, have prices that fluctuate 
based on various attributes, such as cut, carat, clarity, and color. The project follows a structured data ****science workflow****, 
starting with data sourced directly from a ****relational database****, ensuring high data integrity and scalability.

The process begins with data extraction and cleaning, ensuring the data is prepared for meaningful analysis. 
****Exploratory Data Analysis (EDA)****(#EDA and Modeling) is performed to uncover patterns, trends, and anomalies in the dataset. This step is complemented by interactive visualizations to provide in-depth insights into the key factors affecting diamond prices. The results of this analysis guide the feature engineering process, where the most relevant attributes are selected and transformed for modeling.

****Machine learning algorithms**** are employed for price prediction, with models tuned and evaluated using 
metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to ensure accuracy. 
These predictions are validated against test data to confirm the reliability of the system.

The project includes a ****Flask-based web application****, serving as an intuitive user interface where buyers 
and sellers can input diamond specifications and receive real-time price predictions. The application is 
integrated with a Continuous Integration/Continuous Deployment (CD) pipeline, ensuring smooth updates 
and maintenance of both the machine learning model and the web platform. This pipeline automates processes like testing, building, deploying  and ensuring consistent performance.


## About the Data:

The dataset The goal is to predict the price of a given diamond (Regression Analysis).

There are 10 independent variables (including id):

- ****carat****: Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.

- ****cut****: Quality of Diamond Cut

- ****color****: Color of Diamond

- ****clarity****: Diamond clarity is a measure of the purity and rarity of the stone, graded by the 
    visibility of these characteristics under 10-power magnification.

- ****depth****: The depth of the diamond is its height (in millimetres) measured from the culet (bottom tip) to the table (top surface)

- ****table****: A diamond's table is the facet which can be seen when the stone is viewed face up.

- ****x****: Diamond X dimension

- ****y****: Diamond Y dimension

- ****z****: Diamond Z dimension

## Target variable:

- ****price****: Price of the Diamond.


## Technologies Used:

1) Pandas:

	- A Python library for data manipulation and analysis.
	- Used for reading, cleaning, and transforming data into a structured format like DataFrames.
	- Provides powerful functions for data slicing, filtering, grouping, and aggregation.
		
2) NumPy:

	- A fundamental package for scientific computing in Python.
	- Used for numerical computations, handling large arrays, and performing matrix operations.
	- Offers high-performance tools for mathematical functions and linear algebra.

3) Scikit-learn:

	- A machine learning library in Python.
	- Provides tools for model building, evaluation, and selection.
	- Includes algorithms for classification, regression, clustering, and preprocessing.

4) Flask:

	- A lightweight web framework for Python.
	- Used to build the web interface for the Diamond Price Prediction project.
	- Serving as an intuitive user interface where buyers 
	   and sellers can input diamond specifications and receive real-time price predictions
	- Facilitates integration of the machine learning model into a web application for user interaction.

5) CD Pipelines:

	- Continuous Deployment pipelines automate software delivery.
	- Used to ensure seamless updates of the web app and ML model.
	- Includes processes like testing, building, and deploying code changes efficiently.

6) MLFlow:

	- An open-source platform for managing the ML lifecycle.
	- Used for tracking experiments, saving model artifacts, and versioning models.
	- Simplifies deployment and monitoring of machine learning workflows.

7) Seaborn:

	- A Python library for creating informative statistical graphics.
	- Built on Matplotlib, it simplifies the creation of aesthetically pleasing plots.
	- Used for EDA to visualize relationships between features.

8) Matplotlib:

	- A core library for creating static, animated, and interactive visualizations in Python.
	- Provides detailed control over graphing parameters.
	- Used for plotting data distributions, trends, and model performance metrics.




   <img target="_blank" src="static\builtin\napkin-selection (1).png" width=900>



# Getting Started

To set up a local copy, follow these simple steps. Significantly depends on a variety of circumstances. This research intends to use machine learning techniques to accurately estimate diamond values, providing significant information to both buyers and sellers in the diamond market.

## Installation Steps

### Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. ***Clone the Repository****

- Open your terminal or command prompt.

- Navigate to the directory where you want to install the project.

- Run the following command to clone the GitHub repository:

```

git clone https://github.com/OmMkuman1902/Diamond_Price_Prediction

```

2. ****Create a Virtual Environment**** (Optional but recommended)

- It's a good practice to create a virtual environment to manage project dependencies. Run the following command:

```

conda create -p <Environment_Name> python==<python version> -y

```

3. ****Activate the Virtual Environment**** (Optional)

- Activate the virtual environment based on your operating system:

```

conda activate <Environment_Name>/

```

4. ****Install Dependencies****

- Navigate to the project directory:

```

cd [project_directory]

```

- Run the following command to install project dependencies:

```

pip install -r requirements.txt

```

5. ****Run the Project****

- Start the project by running the appropriate command.

```

python app.py

```
## Directory Structure:
├── project_root/
    
    ├──src/
        ├── __init__.py/
        ├── components/
		├── __init__.py/
		├── data_ingesion.py/
		├── data_transformation.py/
                ├── data_modeler.py/     
        ├── pipeline/
		├── __init__.py/
		├── predict_pipeline.py/
		├── train_pipeline.py/		
        ├── logger.py/
        ├── exception.py/
        ├── utils.py/
	├── notebooks/
	├── app.py/
    ├── requirements.txt/
    ├── setup.py/



## Visual Insights of Data:
 ### 1) Preview of Data
   <img target="_blank" src="static\builtin\Top_5_data.png" width=400>

 ### 2) Statistical Information:
   <img target="_blank" src="static\builtin\Describe.png" width=600>
      
	  - Basic statistics about the numercal features of the dataset .

 ### 3) Visualization on categorical features and Observations :
        - Distribution of Output Feature( Price ) :
   <img target="_blank" src="static\builtin\log_dist.png" width=900>  

        - Cut of Diamond Feature :
   <img target="_blank" src="static\builtin\Cut_per.png" width=900>

	    
	- Color of Diamond Feature :
   <img target="_blank" src="static\builtin\color_per.png" width=900>
   

        - Clarity of Diamond Feature :
   <img target="_blank" src="static\builtin\Clarity_per.png" width=900>

    
	    - Clarity according to Price :
   <img target="_blank" src="static\builtin\Clarity_vs_price.png" width=900>


        - Cut according to all numeric features  :
   <img target="_blank" src="static\builtin\Cut_vs_numeric.png" width=900>


        - Cut according to Color  :
   <img target="_blank" src="static\builtin\Cut_vs_color.png" width=900>


        - Color according to Clarity  :
   <img target="_blank" src="static\builtin\Color_vs_clarity.png" width=900>


        - Summary of Color Vs Price  :
   <img target="_blank" src="static\builtin\Summary_Color.png" width=1100>

- There are also more indepth exploration, you can check my notebook folder for the same.

### Comaparing Data Models:
        - Model Accuracies :
   <img target="_blank" src="static\builtin\model_acc.png" width=400>

        - Regression Graph  :
   <img target="_blank" src="static\builtin\reg_graph.png" width=600>

        - Actual vs Predictions :
   <img target="_blank" src="static\builtin\predictions.png" width=600>
      





