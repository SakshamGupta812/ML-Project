import os
import sys

import dill

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):

    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(
            dir_path,
            exist_ok=True
        )

        with open(
            file_path,
            "wb"
        ) as file_obj:

            dill.dump(
                obj,
                file_obj
            )

    except Exception as e:

        raise CustomException(
            e,
            sys
        )


def evaluate_models(
    X_train,
    y_train,
    X_test,
    y_test,
    models,
    params
):

    try:

        report = {}

        for model_name in models:

            model = models[model_name]

            # Get parameters for current model
            para = params[model_name]

            # GridSearch
            gs = GridSearchCV(
                estimator=model,
                param_grid=para,
                cv=3,
                error_score="raise"
            )

            gs.fit(
                X_train,
                y_train
            )

            # Set best parameters
            model.set_params(
                **gs.best_params_
            )

            # Train model
            model.fit(
                X_train,
                y_train
            )

            # Predictions
            y_train_pred = model.predict(
                X_train
            )

            y_test_pred = model.predict(
                X_test
            )

            # Scores
            train_model_score = r2_score(
                y_train,
                y_train_pred
            )

            test_model_score = r2_score(
                y_test,
                y_test_pred
            )

            report[model_name] = test_model_score

        return report

    except Exception as e:

        raise CustomException(
            e,
            sys
        )