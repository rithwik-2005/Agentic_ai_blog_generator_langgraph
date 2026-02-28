from typing import TypedDict, Optional
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: Optional[str] = Field(default=None, description="Blog title")
    content: Optional[str] = Field(default=None, description="Blog content")

class BlogState(TypedDict):
    topic: str
    blog: Blog
    current_language: str