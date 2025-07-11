
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    task_id : int
    title : str
    description : Optional[str] = None
    done : bool = False