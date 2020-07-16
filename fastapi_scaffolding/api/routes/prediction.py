from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_scaffolding.core import security

# Incoming payload data model
from fastapi_scaffolding.data_models.payload import HousePredictionPayload

# Outbound prediction result data model
from fastapi_scaffolding.data_models.prediction import HousePredictionResult

# ML Model object itself
from fastapi_scaffolding.services.models import HousePriceModel

router = APIRouter()


@router.post("/predict", response_model=HousePredictionResult, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: HousePredictionPayload = None
) -> HousePredictionResult:

    model: HousePriceModel = request.app.state.model
    prediction: HousePredictionResult = model.predict(block_data)

    return prediction
