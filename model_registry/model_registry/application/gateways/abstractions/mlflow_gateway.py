from abc import ABC, abstractmethod
from typing import Any, Optional
import pandas as pd

class IMLflowGateway(ABC):
    @abstractmethod
    def start_run(self, run_name: Optional[str] = None) -> None:
        raise NotImplementedError("Method not implemented")
    
    @abstractmethod
    def log_param(self, key: str, value: Any) -> None:
        raise NotImplementedError("Method not implemented")
    
    @abstractmethod
    def log_metric(self, key: str, value: float) -> None:
        raise NotImplementedError("Method not implemented")
    
    @abstractmethod
    def log_artifact(self, local_path: str) -> None:
        raise NotImplementedError("Method not implemented")
    
    @abstractmethod
    def log_model(
        self,
        model: Any,
        artifact_path: str,
        signature: Optional[Any] = None,
        input_example: Optional[pd.DataFrame] = None
    ) -> None:
        raise NotImplementedError("Method not implemented")
    
    @abstractmethod
    def register_model(
        self,
        model_uri: str,
        name: str,
        stage: str = "Staging"
    ) -> None:
        raise NotImplementedError("Method not implemented")
    
    @abstractmethod
    def end_run(self) -> None:
        raise NotImplementedError("Method not implemented")