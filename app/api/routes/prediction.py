from fastapi import APIRouter
from starlette.requests import Request

# Incoming payload data model
from app.data_models.payload import HousePredictionPayload

# Outbound prediction result data model
from app.data_models.prediction import HousePredictionResult

# ML Model object itself
from app.services.models import HousePriceModel

router = APIRouter()


@router.post("/predict", response_model=HousePredictionResult, name="predict")
def post_predict(
    request: Request,
    block_data: HousePredictionPayload = None,
) -> HousePredictionResult:
    model: HousePriceModel = request.app.state.model
    prediction: HousePredictionResult = model.predict(block_data)
    return prediction
