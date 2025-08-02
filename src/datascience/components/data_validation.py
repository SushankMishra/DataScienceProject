import os
import pandas as pd
from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import DataValidationConfig
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        logger.info(f"Data Validation Config Accepted")
    def validate_all_columns(self):
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    logger.error(f"Column {col} is not in the schema.")
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}\n")
                    break
            if validation_status:
                for col in all_schema:
                    if((self.config.all_schema[col] !=  data[col].dtype.name)):
                        validation_status = False
                        logger.error(f"Column {col} has incorrect data type.")
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation Status: {validation_status}\n")
                        break
            if validation_status:
                logger.info("All columns are valid and match the schema.")
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation Status: {validation_status}\n")
            return validation_status
        except Exception as e:
            logger.error(f"Error in data validation: {e}")
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: False\n")
            return False    
    
