from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from app.models.schemas import GenerateLayoutRequest
from app.services.layout_generator import generate_layout_html, get_available_templates

router = APIRouter()


@router.get("/templates", summary="List available templates")
async def list_templates():
    """
    Returns the available templates for document generation.
    """
    return get_available_templates()


@router.post(
    "/generate-layout", response_class=HTMLResponse, summary="Generate document layout"
)
async def generate_layout(request: GenerateLayoutRequest):
    """
    Generates HTML layout using the provided elements and template.
    """
    try:
        html = generate_layout_html(
            elements=[element.model_dump() for element in request.elements],
            template_id=request.template_id,
        )
        return HTMLResponse(content=html, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
