import mlflow
import pandas as pd
from typing import Any, Optional
from model_registry.application.gateways.abstractions.mlflow_gateway import IMLflowGateway

from mlflow.models.signature import ModelSignature
from mlflow.pyfunc import PythonModel

class MLflowClientGateway(IMLflowGateway):
    def start_run(self, run_name: Optional[str] = None) -> None:
        mlflow.start_run(run_name=run_name)
    
    def log_param(self, key: str, value: Any) -> None:
        mlflow.log_param(key, value)
    
    def log_metric(self, key: str, value: float) -> None:
        mlflow.log_metric(key, value)
    
    def log_artifact(self, local_path: str) -> None:
        mlflow.log_artifact(local_path)
    
    def log_model(
        self,
        model: Any,
        artifact_path: str,
        signature: Optional[ModelSignature] = None,
        input_example: Optional[pd.DataFrame] = None
    ) -> None:
        if isinstance(model, PythonModel):
            mlflow.pyfunc.log_model(
                artifact_path=artifact_path,
                python_model=model,
                signature=signature,
                input_example=input_example
            )
        else:
            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path=artifact_path,
                signature=signature,
                input_example=input_example
            )
    
    def register_model(
        self,
        model_uri: str,
        name: str,
        stage: str = "Staging"
    ) -> None:
        mlflow.register_model(model_uri, name)
        client = mlflow.MlflowClient()
        latest_version = client.get_latest_versions(name, stages=[stage])[0].version
        client.transition_model_version_stage(
            name=name,
            version=latest_version,
            stage=stage
        )
    
    def end_run(self) -> None:
        mlflow.end_run()