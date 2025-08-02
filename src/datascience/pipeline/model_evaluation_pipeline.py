from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            self.config = ConfigurationManager()
            self.model_evaluation_config = self.config.get_model_evaluation_config()
            self.model_evaluation = ModelEvaluation(self.model_evaluation_config)
        except Exception as e:
            logger.error(f"Error during model evaluation pipeline: {e}")
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(">>> Starting Model Evaluation Pipeline <<<")
        pipeline = ModelEvaluationPipeline()
        pipeline.initiate_model_evaluation()
        pipeline.model_evaluation.log_into_mlflow()
        logger.info(">>> Model Evaluation Pipeline Completed <<<")
    except Exception as e:
        logger.exception(e)
        raise e