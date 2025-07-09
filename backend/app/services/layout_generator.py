import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATES_PATH = Path(__file__).resolve().parent.parent / "templates" / "layouts"
env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_PATH)),
    autoescape=select_autoescape(["html", "xml"]),
)

INDEX_PATH = TEMPLATES_PATH / "index.json"
with open(INDEX_PATH, encoding="utf-8") as f:
    REGISTERED_TEMPLATES = json.load(f)


def get_available_templates():
    """
    Returns a list of available templates with metadata for frontend selection.
    """
    return [
        {"id": template_id, **data}
        for template_id, data in REGISTERED_TEMPLATES.items()
    ]


def generate_layout_html(elements: list, template_id: str) -> str:
    """
    Generates HTML using the selected template and provided elements.

    Args:
        elements: List of structured content blocks.
        template_id: ID of the template as defined in index.json.

    Returns:
        Rendered HTML as a string.
    """
    if template_id not in REGISTERED_TEMPLATES:
        raise ValueError(f"Template '{template_id}' is not registered.")

    template_file = REGISTERED_TEMPLATES[template_id]["file"]
    template = env.get_template(template_file)
    html = template.render(elements=elements)
    return html
