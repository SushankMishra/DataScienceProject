import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "datascience"

list_of_files = [
    ".gthub/workflows/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/research.ipynb",
    "README.md",
    "templates/index.html",
]
for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)
    if not os.path.exists(filedir) and filedir != '':
        logging.info(f"Creating directory: {filedir}")
        os.makedirs(filedir, exist_ok=True)
    if not os.path.exists(file_path) and file_path != '':
        logging.info(f"Creating file: {file_path}")
        with open(file_path, 'w') as f:
            pass  # Create an empty file
    else:
        logging.info(f"File already exists: {file_path}")
