from typing import Dict, Any, List, Optional, Protocol
from pydantic import BaseModel

class Predictor(Protocol):
    def predict(self, X: Dict[str, Any]) -> Any:
        ...

class Signature(BaseModel):
    inputs: str
    outputs: str

class ModelRegistrationDataEntity(BaseModel):
    model_name: str
    model_path: str
    description: str
    tags: Dict[str, str]
    version: str
    signatures: Optional[Signature] = None
    input_example: Optional[Dict[str, Any]] = None
    output_example: Optional[Dict[str, Any]] = None
    sample_input: Optional[Dict[str, Any]] = None
    model_instance: Optional[Predictor] = None

class ModelRegistrationResult(BaseModel):
    model_name: str
    version: str
    description: str

class MetricData(BaseModel):
    name: str
    value: float
