from pydantic import BaseModel, Field
from typing import List, Dict


class ActionIndexModels(BaseModel):
    category_key: str = Field(..., description="分类KEY")
    description: str = Field(..., description="描述")


class ActionCategoryModels(BaseModel):
    id: str = Field(..., description="动作ID")
    description: str = Field(..., description="描述")


class ActionDataFrameModels(BaseModel):
    time: float = Field(..., description="开始时间")
    joints: Dict = Field(..., description="关节配置")


class ActionDataModels(BaseModel):
    duration: float = Field(..., description="持续时间")
    frames: List[ActionDataFrameModels] = Field(..., description="动作配置")
