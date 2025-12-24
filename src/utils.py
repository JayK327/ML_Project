import os,sys
import dill
from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f'Object saved successfully at {file_path}')
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models,params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model_name = list(models.keys())[i]
            logging.info(f'Training model: {model_name}')

            params_model = params[model_name]

            gs= GridSearchCV(model, params_model, cv=5, n_jobs=-1, verbose=1)
            gs.fit(X_train, y_train)

            params_model = gs.best_params_
            model.set_params(**params_model)
            model.fit(X_train, y_train)


            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_r2_score = r2_score(y_train, y_train_pred)
            test_r2_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_r2_score
            logging.info(f'{model_name} - Train R2 Score: {train_r2_score}, Test R2 Score: {test_r2_score}, Best Params: {params_model}')

        return report
    except Exception as e:
        raise CustomException(e, sys)