from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import CombatSessionResponse, TurnResponse
from ..database import get_db
from ..models import HeroModel, CombatSessionModel
from src.game.hero import Warrior, Mystic, Assassin
from src.game.enemy import Goblin, Skeleton, DarkKnight
from src.game.combat import calculate_damage, is_critical_hit
import random

router = APIRouter(prefix="/combat", tags=["combat"])

def get_hero_object(hero_record):
    class_map = {"Warrior": Warrior, "Mystic": Mystic, "Assassin": Assassin}
    hero = class_map[hero_record.hero_class](hero_record.name)
    hero.hp = hero_record.hp
    hero.max_hp = hero_record.max_hp
    hero.attack = hero_record.attack
    hero.defense = hero_record.defense
    hero.crit_chance = hero_record.crit_chance
    hero.potions = hero_record.potions
    hero.gold = hero_record.gold
    hero.experience = hero_record.experience
    hero.level = hero_record.level
    hero.skill_cooldown = hero_record.skill_cooldown
    return hero

def get_enemy_object(enemy_type, enemy_hp=None):
    enemy_map = {"Goblin": Goblin, "Skeleton": Skeleton, "DarkKnight": DarkKnight}
    
    if enemy_type not in enemy_map:
        raise HTTPException(status_code=404, detail="Unkown enemy type")
    
    enemy = enemy_map[enemy_type]()
    if enemy_hp is not None:
        enemy.hp = enemy_hp

    return enemy

@router.post("/start/{hero_id}", response_model=CombatSessionResponse)
def start_combat(hero_id: int, enemy_type: str="Goblin", db: Session=Depends(get_db)):
    hero = db.query(HeroModel).filter(HeroModel.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    enemies = ["Goblin", "Skeleton", "DarkKnight"]

    if enemy_type not in enemies:
        raise HTTPException(status_code=404, detail="Uknown enemy type")
    else:
        enemy = get_enemy_object(enemy_type, enemy_hp=None)
    
    session = CombatSessionModel(
        hero_id = hero_id, 
        enemy_type = enemy_type, 
        enemy_hp = enemy.hp, 
        enemy_max_hp = enemy.max_hp, 
        is_active = True, 
        outcome = None
    )

    db.add(session)
    db.commit()
    db.refresh(session)
    
    return session

@router.get("/{session_id}", response_model=CombatSessionResponse)
def get_session(session_id: int, db: Session=Depends(get_db)):
    session = db.query(CombatSessionModel).filter(CombatSessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return session

@router.post("/{session_id}/turn", response_model=TurnResponse)
def take_turn(session_id: int, action: str, db: Session=Depends(get_db)):
    session = db.query(CombatSessionModel).filter(CombatSessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    if not bool(session.is_active):
        raise HTTPException(status_code=400, detail="Combat is already over.")
    
    hero_record = db.query(HeroModel).filter(HeroModel.id == session.hero_id).first()
    hero = get_hero_object(hero_record)
    enemy = get_enemy_object(session.enemy_type, enemy_hp=session.enemy_hp)

    # Action handler
    if action == "attack":
        hero_damage = calculate_damage(hero.attack, enemy.defense, hero.crit_chance)
        enemy.take_damage(hero_damage)
    elif action == "skill":
        pass
    elif action == "potion":
        pass
    else:
        raise HTTPException(status_code=400, detail="Invalid action")
    
    # Enemy attacks
    enemy_damage = 0
    if enemy.is_alive():
        enemy_damage = calculate_damage(enemy.attack, hero.defense, crit_chance=0) # Enemies don't crit
        hero.take_damage(enemy_damage)
    
    # Outcomes
    outcome = None
    if not enemy.is_alive():
        outcome = "Victory!"
        session.is_active = False # type: ignore
    elif not hero.is_alive():
        outcome = "Defeat!"
        session.is_active = False # type: ignore

    session.outcome = outcome # type: ignore

    # Updating values in database
    session.enemy_hp = enemy.hp
    hero_record.hp = hero.hp # type: ignore
    db.commit()

    return {
        "hero_hp": hero.hp,
        "enemy_hp": enemy.hp,
        "hero_damage": hero_damage, # type: ignore
        "enemy_damage": enemy_damage,
        "outcome": outcome,
       # "debug": {
       #     "enemy_attack": enemy.attack,
       #     "hero_defense": hero.defense,
       #     "raw_diff": enemy.attack - hero.defense
       # }
    }