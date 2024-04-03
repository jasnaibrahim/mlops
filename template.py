import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_files= [

    f"src/{project_name}/__init__.py",  
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/Data_ingestion.py",
    f"src/{project_name}/components/Data_Transformation.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/Data_Transformation.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename =os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"create a directory :{filedir} for the file {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")

    else:
        logging.info(f"{filename} is already exists")









    
