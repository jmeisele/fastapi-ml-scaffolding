from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_scaffolding.core import security
from fastapi_scaffolding.models.payload import HousePredictionPayload # Incoming payload data model
from fastapi_scaffolding.models.prediction import HousePredictionResult # Outbound prediction result data model
from fastapi_scaffolding.services.models import HousePriceModel # ML Model itself

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
