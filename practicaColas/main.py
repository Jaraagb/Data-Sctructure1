from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

@app.post("/ticketCreate")
async def create_ticket(ticket: Ticket):
    add_queue(ticket, ticketTypes)
    return {"message": "Ticket added successfully"}

@app.get("/ticketNext/{ticket_type}")
async def get_next_ticket(ticket_type: str):
    if ticket_type in ticketTypes:
        next_ticket = ticketTypes[ticket_type].dequeue()
        if next_ticket:
            return next_ticket.dict()  # Convertimos el objeto en JSON
        return {"message": "No tickets in queue"}
    return {"error": "Invalid ticket type"}

@app.get("/ticketList/{ticket_type}")
async def get_ticket_list(ticket_type: str):
    if ticket_type in ticketTypes:
        queue_list = []
        current = ticketTypes[ticket_type].head
        while current:
            queue_list.append(current.data.dict())  # Convertimos cada ticket en JSON
            current = current.next
        return queue_list
    return {"error": "Invalid ticket type"}