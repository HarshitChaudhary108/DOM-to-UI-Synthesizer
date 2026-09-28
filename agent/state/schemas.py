from typing import Literal
from pydantic import BaseModel, Field


class Section(BaseModel):
    kind: Literal["navbar", "hero", "features", "pricing", "testimonials", "cta", "footer", "generic"]
    heading: str = ""
    subheading: str = ""
    items: list[str] = Field(default_factory=list)       # nav links / card titles / bullets
    cta_text: str = ""
    image_urls: list[str] = Field(default_factory=list)
    layout_notes: str = ""                                # e.g. "2 columns, image right, dark bg"


class DesignSpec(BaseModel):
    site_name: str
    primary_color: str        # hex
    secondary_color: str      # hex
    background_color: str     # hex
    text_color: str           # hex
    font_family: str
    sections: list[Section]


class CodeFile(BaseModel):
    path: str
    content: str


class CodeOutput(BaseModel):
    files: list[CodeFile]
    deleted: list[str] = Field(default_factory=list)