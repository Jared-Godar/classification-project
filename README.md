# classification-project
The repsitory contains the files for Jared Godar's first Codeup project on classification and modeling of telco churn.

## About the Project

### Project Goals

The main goal of this project is to be able to accurately predict the likelyhood that an existing customer whill terminate their services with Telco, Inc. 

This will be accomplished by using past customer data to create multiple prediction models, rating the effectiveness of each model, and testing the best model on new data is has never seen.

Having this new information will allow us to identify factors that cause customer turnover, which customers we are most at risk of using, and devise srtategies to retain these customers. 

### Project Description

This project provides the opportunity to create and evaluate multiple predictive models as well as implement other essential parts of the data science pipeline.

It will incolve pulling relavant data from a SQL database; cleaning that data; splitting the data into training, validation, and test sets; feature engineering; exploratory data analysis; modeling; model evaluation; model testing; and effectively communicating findings in written and oral formats.

Finding new customers is expensive in terms of both money and effort: advertising, onboarding promotions, new customer support and education, etc. 

One way to increase revenue and active customers, is to decrease the number of customers leaving. In order to accomplish this, it will be helpful to know which customers are leaving and why.

Once we have this information, we can devise new customer retention strategies.

### Initial Questions

- What are the main drivers of churn?
- What are the relative importances of the assorted drivers?
- Are there any other potentially useful features that can be engineered from the current data available?
- Are the relationships suggested by initial visualizations statistically significant?
- Is the data balanced or unbalanced?
- Are there null values or missing data that must be addressed?
- Are there any duplicates in the dataset?
- What are the specific business consequences for different prediction outcomes (false positive, false negative)?
- Which model feature is most important for this data and business case?
- Which model evaluation metrics are most sensitive to this primary feature?

### Data Dictionary

List each variable

### Steps to Reproduce

1. Acquire date from telco database
2. 

### The Plan

1. **Acquire, clean, prepare, and split the data:**
    - Pull from telco database.
    - Eliminate any unnecessary or redundant fields.
    - Engineer new, potentially informative features.
    - Search for null values and respond appropriately (delete, impute, etc.).
    - Make dummy variables and one-hot encode any categorical variable.
    - Divide the data in to training, validation, and testing sets.
2. **Exploratory data analysis:**
    - Visualize pairwaise relationships looking for correlation with churn in the main customer population as well as within relavant subgroups (age, gender, sercive type, etc.).
    - Note any interesting correlations or other findings.
    - Test presumptive relationships for statistical significance.
    -  Think of what modeling techniques would be appropriate or most useful given the unique features of data discovered.
    - Record any other interesng observations or findings.
    *NOTE: This data analysis will be limited to the training dataset*
3. **Model generation, assessment, and optimization:**
    - Generate multiple models to predict churn using a varity of classification techniques.
    - Calculate a baseline prediction for comparison.
    - Calculate evaluation metrics to assess quality of models (accuracy, NPV, recall, F1, etc.)
    - Generate multiple models for each technique by changing hyperparameters and evaluate each looking for the model with the highest accuracy on the training and validation sets with the least overfitting, observed as the difference between the training and validation predictions.
    - Determine which metric is most important for assessment based on specific business case.
    - Use that metric to select the highest performing model.
    - Test that model with the previously unused and unseen test data once and only once.
4. **Streamline presentation**
    - Take only the most relative information from the working along and create a succinct report that walks through the rationale, steps, code, and observations for the entire data science pipeline of acquiring, cleaning, preparing, modeling, evaluating, and testing our model.
    - Using this new-found information, devise strategies to retain customers.
    - Outline next steps for this project:
        - Potential specific changes designed to retain customers
        - Strategy to tests and evaluate implementation of those changes
        - Potential revenu and savings for success

#### Wrangle


##### Modules (acquire.py + prepare.py + split.py + wrangle.py)

##### Missing Values (report.ipynb)

- Communicate decisions and reasoning for handling of missing values.

##### Data Split (prepare.py (def function), report.ipynb (run function))

~50%-30%-20% split train-validate-test; Varies depending on observations, test can be as low as 10%

- Set random state of seed so split will be reproducable

- Always split before exploring variable relationships

##### Using modules

- After creating, want to import those into final report so you can use the functions ti acquire and prepare your data without clutter.

- Call functions and include a markdown cell describing steps.

#### Explore

##### Ask a clear question, [discover], provide a clear answer (report.ipynb)

- Share four questions in final report
    - >=2 supported by statistical test

- *You should call out questions of the data using natural language that speaks to the business stakeholders in markdown cells, ideally a header prior to the visualization or statistical test, that you then explore. This does not take the place of stating your null hypothesis/alternative hypothesis when doing a statistical test. But those hypotheses are generally for you. By writing questions that you intend to answer with visualizations and statistical tests in natural language, like ""Are office supplies leading to differences in profit in Texas?"", you are able to guide both yourself and your reader through the highlights of your analysis. You ask a question, create a visual, run a statistical test (if appropriate), and wrap it nicely with a markdown cell that contains a clear answer in layman's terms. You do all that before moving to the next question.*

##### Exploring through visualizations (report.ipynb)

- *At least 5 visualations are included in your final report.*

- *The ones included answer a question (remember, NO is an answer) or provide necessary context (such as the distribution of the target variable). All statistical tests included in the final report should be supported with an visualization of the interaction of the variables being tested. Charts in the final report should have titles and labels that are descriptive and useful for the end user/audience/consumer of the report.*

- *All visualizations in the final report are mentioned or discussed if a verbal presentation is given.*

##### Statistical tests (report.ipynb)

- *At least 2 statistical tests are included in your final report.*

- *The correct tests are run, given the data type and distribution, and the correct conclusions are drawn. For example (other tests may be used):*

  - *correlation: 2 continuous variables, normally distributed, testing for LINEAR correlation only (H_0: Not linearly dependent)*

  - *independent t-test: 1 continuous, somewhat normally distributed variable, one boolean variable, equal variance, independent (H_0: population mean of each group is equal)*
  
  - *chi-square test: 2 discrete variables. (H_0: the 2 variables are independent of each other).*

##### Summary (report.ipynb)

- *Following your exploration section, you summarize your analysis (in a **markdown** cell using natural language): what you found and how you will use it moving forward.*

- *This includes **key takeaways** from all the questions answered in explore, a **list of which features** will be used in modeling and **why**, and which features will not move forward and why. You may only call out a few of these features in the presentation, but having that there for reference is important in a report. A group of features may have the same reason why, and those can be mentioned together.*

##### Select Evaluation Metric (Report.ipynb)

- *Clear communication as to how you evaluated and compared models.*

- *What metric(s) did you use and why? For example, in one case, you may decide to use precision over accuracy. If so, why? If you use multiple metrics, how will you decide which to select if metric is better for model A but another is better for model B? Will you rank them? Find a way to aggregate them into a single metric you can use to rank?*

##### Evaluate Baseline (Report.ipynb)

- *Having a baseline tells you whether a model you build using the features you selected is any better than predicting by using only the target variable. One way a baseline is created in classification is by making predictions purely based on the most common outcome class, like predicting that all titanic passengers will die, becuase the majroity did die. By doing that, you end up with the highest accuracy without using extra information from features. The baseline is based on the training dataset. For a continuous target variable, the baseline  could be predicting that all salaries will be the median salary of our labeled train data. The predictions should be made on the training data using this information (like the predicted value, y_hat, for all passengers "survived" == 0) and then performance evaluated to measure your models against. If any model you build does not perform as well as a baseline that uses no features, then your features are not significant drivers of the outcome.*

##### Develop 3 Models (Report.ipynb)

- *The 3 models can differ based on the features used, the hyperparameters selected, and/or the algorithm used to fit the data.*

#### Evaluate on Train (Report.ipynb)

- *All models should be evaluated on train: the training smaple is our largest sample, and it is a sample of data we have to both fit the model AND see how the model performs. We should never skip straight to validate. We would be missing out on valuable observations.*

##### Evaluate on Validate (Report.ipynb)

- *The top models should be evaluated with the validation sample dataset. It is important to use the validate sample for checking for any overfitting that may have occurred when fitting the model on train. If you are creating 10's of models, it is also important to only validate a handful of your top models with the Validate dataset. Otherwise, your data will have seen validate as much as train and you could accidentally introduce some implicit bias based on data and results you see while validating on so many models.*

#### Evaluate Top Model on Test (Report.ipynb)

- *Your top performing model, and only your top performing model should be evaluated on your test dataset. The purpose of having a test dataset to evaluate only the final model on is to have an estimate of how the model will perform in the future on data it has never seen.*

## Report (Final Notebook) 

#### code commenting (Report.ipynb)

- *Your code contains code comments that are helpful to the reader in understanding what each blocks/lines of code are doing.*

#### markdown (Report.ipynb)

- *Notebook contains adequate markdown that documents your thought process, decision making, and navigation through the pipeline. This should be present throughout the notebook consistently, wtih not just headers, but plenty of content that guides the reader and leaves no questions or doubt as to why you did something, e.g.*

#### Written Conclusion Summary (Report.ipynb)

- *Your conclusion summary should addresses the questions you raised in the opening of the project, which we would want to see at the end of every final notebook. Ideally, when the deliverable is a report, the summary should tie together your analysis, the drivers of the outcome, and how you would expect your ML model to perform in the future on unseen data, in layman's terms.*

#### conclusion recommendations (Report.ipynb)

- *Your notebook should ends with a conclusion that contains  actionable recommendations based on your insights and analysis to the business stakeholder(s), your simulated audience, or someone who would find this information valuable (if there is no stakeholder). Your recommendations should not be not about what to do differently with the data, but instead should be based on the business or domain you are studying.*

#### conclusion next steps (Report.ipynb)

- *Your conclusion should include next steps from a data science perspective that will assist in improving your research. Ideally, if you talk about trying more algorithms to improve performance, think about why you need to improve performance. And if the business calls for it, remember the best way to improve performance is to have better predictors/features. If you talk about gathering more data, being specific about what data you think will help you understand the problem better and why is the way to go!*

#### no errors (Report.ipynb)

- *Your final notebook should run without error. One error in a notebook can lead to the rest of it erroring out. If you have a reader who doesn't know python, they will then not be able to consume your report.*

## Live Presentation

### intro (live)

- *Speaker kicks of the presentation by introducing themselves and their project through a one-liner of what it's about.*

### audience & setting  (live)

- *Always be aware of the audience and setting for your presentation.  What is the appropriate level of technicality? What is the appropriate depth given audience, setting and medium in which its delivered. The way you communicate should be appropriate for the audience: volume, speed of talk, flow, professionalism. (Codeup Data Science Instructor Team, virtually delivered via jupyter notebook).*

### content (live)

- *Notebook talked through step-by-step, in an understandable and meaningful way. Extraneous content in the notebook is not present.*

### Verbal Conclusion (findings, next steps, recommendations)  (live) 

- *Presentation is concluded with a summary of what was found, recommendations, and next steps. The presentation does not just drop off after modeling, but the entire project is nicely tied up and summarized.*

### time (live) 

- *Time limit of 5 minutes is adhered to. The time is managed well, in that there is appropriate time spent on each section. The time of 5 minutes should not be met by talking quickly but by reducing the amount or depth of information conveyed, and by finding easier and more simplified methods to convey the more complex information. The speech should be natural, and take the time needed for the audience to consume the information. So the time is well spent when you have practiced and you have taken the extra time it takes to reduce the content in your notebook and presentation. Time should not be spent scrolling through 10's of visualizations or hundreds of lines of code.*

## Deliver Predictions

### Deliver predictions (.csv) 

*A csv with predictions made from the top model developed should be submitted, as per instructions in the project spec.*
