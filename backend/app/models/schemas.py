from pydantic import BaseModel
from typing import List, Optional


class LayoutElement(BaseModel):
    type: str
    content: Optional[str] = None
    src: Optional[str] = None
    caption: Optional[str] = None
    list_items: Optional[List[str]] = None


class GenerateLayoutRequest(BaseModel):
    elements: List[LayoutElement]
    template_id: str
