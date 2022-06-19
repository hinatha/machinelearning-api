# machinelearning-api

## Features

### Routes

```bash
$ flask routes
Endpoint           Methods  Rule
-----------------  -------  -----------------------
api.check_schema   POST     /v1/check-schema
api.file_id        POST     /v1/file-id
api.health         GET      /v1/health
api.probabilities  POST     /v1/probabilities
static             GET      /static/<path:filename>
```

### User Story

- User can see result of number predict.
- User can check schema.
- User can check health status.

### Project structure

```bash
.
├── README.md
├── analysis.ipynb
├── api
│   ├── __init__.py
│   ├── calculation.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   └── config.cpython-39.pyc
│   │   ├── config.py
│   │   └── json-schemas
│   │       ├── __init__.py
│   │       ├── check_dir_name.json
│   │       ├── check_file_id.json
│   │       └── check_file_schema.json
│   ├── images.db
│   ├── json_validate.py
│   ├── migrations
│   ├── model.pickle
│   ├── models.py
│   ├── preparation.py
│   ├── preprocess.py
│   └── run.py
├── handwriting_pics
│   ├── 0.jpg
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   ├── 5.jpg
│   ├── 6.jpg
│   ├── 7.jpg
│   ├── 8.jpg
│   └── 9.jpg
├── images.db
├── model.pickle
├── requirements-test.txt
├── requirements.txt
└── test
    ├── __init__.py
    ├── conftest.py
    ├── test_calculation.py
    ├── test_preparation.py
    └── test_preprocess.py

```

## Usage

### venv

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
(.venv) $ python3 -m pip install -r requirements.txt
```

### Make learned MLapi

Execute below code in analysis.ipynb

```bash
import pickle
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

digits = load_digits()
X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

logreg = LogisticRegression(max_iter=2000)
model = logreg.fit(X_train, y_train)
with open('model.pickle', mode='wb') as fp:
    pickle.dump(model, fp)
```

### Flask run

```bash
(.venv)$ cd api
(.venv)$ export FLASK_APP=run.py
(.venv)$ Flask run
```

### Execute pytest

```bash
(.venv) $ python3 -m pip install -r requirements-test.txt
(.venv) $ pytest
=========================================================================================== test session starts ============================================================================================
platform darwin -- Python 3.9.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/H.Kondo/Desktop/work/machinelearning-api
plugins: anyio-3.6.1, cov-3.0.0
collected 7 items                                                                                                                                                                                          

test/test_calculation.py .                                                                                                                                                                           [ 14%]
test/test_preparation.py ...                                                                                                                                                                         [ 57%]
test/test_preprocess.py ...                                                                                                                                                                          [100%]

============================================================================================= warnings summary =============================================================================================
test/test_calculation.py::test_evaluate_probs
  /Users/H.Kondo/Desktop/work/machinelearning-api/.venv/lib/python3.9/site-packages/sklearn/base.py:329: UserWarning: Trying to unpickle estimator LogisticRegression from version 0.24.2 when using version 1.1.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
  https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
    warnings.warn(

test/test_preprocess.py::test_shrink_image
  /Users/H.Kondo/Desktop/work/machinelearning-api/api/preprocess.py:45: RuntimeWarning: invalid value encountered in true_divide
    img_data16 = (img_data256 - min_bright) / (max_bright - min_bright) * max_size

-- Docs: https://docs.pytest.org/en/stable/warnings.html
====================================================================================== 7 passed, 2 warnings in 1.38s =======================================================================================
```
