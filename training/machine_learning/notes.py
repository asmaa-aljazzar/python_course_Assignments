
# region
#
#* Artificial Intelligence [AI].
#* Machine Learning [ML] -> is AI.
#* Deep Learning [DL] -> is AI and ML.
#* Generative AI [GAI] -> is AI and ML and DL.
#
# region
#
## AI at first work with posibilities [Rule base] - The Goal is #? to make the machine think and act like humans.
#
# region
#
#? Machine Learning: [Work with structure data]
#*  is a discipline o fcomputer science theat uses computer algorithms and analytics to build predictive models that can solve proplems.
#*  is  based on algorithms that can learn from data without relying on rule-based programming.
#       Data => Learns from past data => output.
#
# region
#
#? Deep learning: [Work with structure and unstructure data]
#*  is a subset of machine learning that deals with algorithms inspired by the structure and function of the human brain.
#*  Can work with and enormous amount of both structured and unstructured data.
#*  the major difference between DL and ML is the way data is presented to the machine.
#       input . . . . => angorithm . . . . => output . . . .
#       each dot in input is a data, each data will connect with each dot in algorithm, the same to output.
#*  work with alot of dataset.    
#
# region
#
# Data Input => Data Cleaning => Pre-processing => Model Training => Deployment
# Extarct    => Transform
#
# region
#
#? Machine Learning:
#*       Supervised Learning: 
#        I tell it the lable [survived or not], then it know the other and new data.
#           - Classification. [Not ordered numbers]
#               binary: tow things.
#               multi.
#               #! Lable: cat, dog.
#               #! Classification: cat, cats, dog, dogs ==> 0, 1, 2, 3. || cant't change the number, can't do any operation on them.
#           - Recognition. [Numbers]
#               #! continuos data => data extract from data ==> the weight of a cat, the wight of a dog || If i do an poereation between them it will mean something
#*       Unupervised Learning:
#        I don't thell it the lables the AI will lable it.
#*       Reinforcement Learning
#
# region
#
#? Supervised Learning:
#   when do the algorithm and learn then have a data from a data set ==> modle.
#? Unsupervised Learining
# Finds patterns or groups in unlabeled data, like clustering or dimensionality reducion.
# input raw data => Interpretation: unknown output => Algorithm => Processing => output
#? reinforcement Learning
# interacts with environment and learn from them based on #! rewards 
# Action => env => Reward.
#
# region
#
#? Dataset Splitting 
#? [file for each one]: example: 70% training, 15% validation, 15% testing: togather will be a full dataset.
#
#* Training Data
#!       It is the set of data that is used to train and make the model learn the hidden features/patterns in the data.
#       In each epoch, the same training data is fed to the neural network architecture repeatedly, 
#       and the model continues to learn the features of the data.
#       The training set should have a diversified set of inputs so that the model is trained in all scenarios 
#       and can predict any unseen data sample that may appear in the future.
#* Validation
#!       The validation set is a set of data, separate from the training set, that is used to validate our model performance during training.
#       This validation process gives information that helps us tune the model’s hyperparameters and configurations accordingly. 
#       It is like a critic telling us whether the training is moving in the right direction or not.
#       The model is trained on the training set, and, simultaneously, the model evaluation is performed on the validation set after every epoch.
#* Test Data
#!       The test set is a separate set of data used to test the model after completing the training.
#       It provides an unbiased final model performance metric in terms of accuracy, precision, etc.
#       To put it simply, it answers the question of "How well does the model perform?"
#
# region
#   
#? Evaluation Metrics
# ============================
#!              Predicted
#?              _______ _______
#?             |  Pos  |  Neg  |
#? ------------------------------
#* Actual  Pos |  TP   |  FN   |
#?              ---------------  
#*         Neg |  FP   |  TN   |
# ============================
#
# TP = True Positive  -> Test says Positive, and reality Positive.
# FN = False Negative -> Test says Nigative, and reality Positive.
# FP = False Positive -> Test says Positive, and reality Nigative.
# TN = True Negative  -> Test says Nigative, and reality Nigative.
#
# region
#
# =========================
#? Evaluation Metrics in ML
# =========================
#
#? Classification Metrics
# ----------------------
#* Accuracy       :
#   (TP + TN) / (TP + TN + FP + FN)
#* Precision      :
#   TP / (TP + FP)       -> How many predicted positives are actually positive
#* Recall (TPR)   : 
#! Important
#    TP / (TP + FN)       -> How many actual positives are correctly predicted
#* F1 Score       :
#    2 * (Precision * Recall) / (Precision + Recall)
#* ROC-AUC        :
#    Area under the ROC curve (TPR vs. FPR)
#* Confusion Matrix:
#    Matrix showing TP, FP, TN, FN
#* Log Loss       :
#    -log(predicted probability for true class), averaged

#? Regression Metrics
# ------------------
#* MSE (Mean Squared Error)     :
#    mean((y_true - y_pred)^2)
#* RMSE (Root Mean Squared Error):
#    sqrt(MSE)
#* MAE (Mean Absolute Error)    :
#    mean(abs(y_true - y_pred))
#* R² Score (Coefficient of Determination):
#    1 - (SS_res / SS_tot)

#? Clustering Metrics
# ------------------
#* Silhouette Score : 
# Measures cohesion and separation of clusters
#* ARI (Adjusted Rand Index):
#  Similarity between clustering and ground truth
#* NMI (Normalized Mutual Info):
#  Shared information between labels and clusters

#? Ranking Metrics (Information Retrieval / Recommenders)
# -------------------------------------------------------
#* Precision@k     :
#  Precision calculated at top-k predictions
#* Recall@k       
#* region\
#
#? Regression:
#  Weather forecasting, the model is trained on the past data,
#  and once the training is completed, 
#  it can easily predict the weather for future days.
#*  X: independent variables - (features) are the inputs used to predict a dependent variable (target).
#*  Y: dependent variables -  the outcome the model aims to predict.
# region
#? Simple Linear Regression
#   Statistical method that is used for predictive analysis. 
#   if a single independent var is used to predict the value of a numerical dependent variable then such a Linear Regression algorithm is called SLR.
#   if more than one independent var is used to predict te valure of a numerical dependent var, then its called Multiple Linear Regression.
#! 2 colomns
#   X with one independent variable حجم البيت
#   Y with one dependent variable سعر البيت
#? تقاطع حجم البيت مع النقطه يعطيني السعرالحقيقي
# The line should be near as posibile from all points in the chart. 
# Strong relationship when points are near to eachother.
#* Y is all actual values
#* Y^ what is predict
#
# region 
#
#? Linear Regression Line
# A linear line showing the relationship between the dependent and independent variables, Can show two types of relationship.
#TODO: Positive Linear Relationship:
#   If the dependent variable increases on the Y-axis and independent variable increases on x-axis.
#TODO: Nigative Linear Relationship:
#   If the dependent variable decreases on the Y-axis and independent variable decreases on x-axis.
# 
# region 
# 
#? MSE: Mean Square Error 
#*  to measure the average squared difference between actual (true) values and predicted values in regression problems.
#   - Always non-negative: Values closer to 0 are better (indicating a smaller error).
#   - Units: The same as the square of the original data’s units.
#   - Sensitive to outliers: Squaring the errors magnifies large deviations.
#!  MSE = (1⁄n) × Σ(yᵢ − ŷᵢ)²
# Smaller MSE = better modle
# 
# region 
# 
#? R-squared (R²) — Coefficient of Determination
#* R² is a statistical metric that measures how well a regression model explains the variance in the dependent variable.
#* It tells you the proportion of the variance in the target variable that is predictable from the independent variables.
#! R² = 1 - (SS_res / SS_tot)
# where: => SS_res = sum((y_i - y_hat_i)^2)
#        => SS_tot = sum((y_i - mean(y))^2)
# 
#.
# region
# #