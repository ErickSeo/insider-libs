from model_registry.application.gateways import IMlflowGateway

class MlflowService():
    def __init__(self, 
                 mlflow_gateway: IMlflowGateway):
        self._mlflow_gateway: IMlflowGateway = mlflow_gateway
    
    def set_experiment(self, 
                       experiment_name: str):
        self._mlflow_gateway.set_experiment(experiment_name=experiment_name)