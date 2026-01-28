# This file will handle routing operations such as creating, updating,and deleting event
from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(tags=["events"])
events = []


@event_router.get("/", response_model=List[Event])
async def retrive_all_events() -> Event:
    return events


@event_router.get("/{id}", response_model=Event)
async def retrive_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found")


@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {"message": "data added!"}


@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)

            return {"message": "data hass benn deleted"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found")
