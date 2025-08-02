from urllib.parse import urlparse
from sklearn.metrics import r2_score
from src.datascience.utils.common import save_json
import mlflow
from mlflow.models import infer_signature
import mlflow.sklearn
import numpy as np
import pandas as pd
import joblib
from pathlib import Path
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience import logger
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(np.mean((pred - actual) ** 2))
        mae = np.mean(np.abs(pred - actual))
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        X = test_data.drop(self.config.target_column.name, axis=1)
        y = test_data[self.config.target_column.name]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(self.config.mlflow_uri).scheme
        
        mlflow.set_experiment("model_evaluation_experiment")    
        with mlflow.start_run():
            y_pred = model.predict(X)
            rmse, mae, r2 = self.eval_metrics(y, y_pred)
            save_json(path = Path(self.config.metrics_file_name), data={
                "rmse": rmse,
                "mae": mae,
                "r2": r2
            })
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            mlflow.log_params(self.config.all_params)
            signature = infer_signature(X, y)
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", signature=signature, registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")

