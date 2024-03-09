# VK ML Engineer Internship Assignment
This repository includes:
- research and model fitting Jupyter Notebook pipeline, [also available here](https://colab.research.google.com/drive/1nxwdATTjjhaTaOw9Vg95kXA7S4bWZuSs?usp=sharing)
- Gradio web application
## Model
Final model configuration: MLP Classifier with 50 hidden layers and sigmoid activation function.  
Trained with LBFGS optimizer, L2 regularization and early_stopping.
### Metrics
```
              precision    recall  f1-score   support

           0       0.99      0.64      0.77      1495
           1       0.04      0.71      0.08        34

    accuracy                           0.64      1529
   macro avg       0.52      0.67      0.43      1529
weighted avg       0.97      0.64      0.76      1529


Accuracy Train Score: 0.6909937888198758
Accuracy Test Score: 0.6370176586003924
NDCG score: 0.43214574227842023
```
