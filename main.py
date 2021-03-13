from fastapi import FastAPI

def on_build(app: FastAPI):
    """
    Can be triggered from CLI : ModularAPI modules build <moduleName>
    """
    pass

def on_load(app: FastAPI):
    """
    API Endpoints
    """
    pass