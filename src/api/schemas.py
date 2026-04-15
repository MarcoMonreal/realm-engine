from pydantic import BaseModel
from typing import Optional

class HeroCreate(BaseModel):
    name: str
    hero_class: str

class HeroResponse(BaseModel):
    id: int
    name: str
    hero_class: str
    hp: int
    max_hp: int
    attack: int
    defense: int
    crit_chance: float
    potions: int
    gold: int
    experience: int
    level: int

    class Config:
        from_attributes = True

class HeroUpdate(BaseModel):
    hp: Optional[int]
    max_hp: Optional[int]
    attack: Optional[int]
    defense: Optional[int]
    crit_chance: Optional[float]
    potions: Optional[int]
    gold: Optional[int]
    experience: Optional[int]
    level: Optional[int]

class CombatSessionResponse(BaseModel):
    id: int
    hero_id: int
    enemy_type: str
    enemy_hp: int
    enemy_max_hp: int
    is_active: bool
    outcome: Optional[str]

    class Config:
        from_attributes = True

class TurnResponse(BaseModel):
    hero_hp: int
    enemy_hp: int
    hero_damage: int
    enemy_damage: int
    outcome: Optional[str]