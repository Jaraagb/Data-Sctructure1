from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    Orders tickets by type and priority. (dudas, asesor, caja, otros)
    """
    # Si no se especifica prioridad y la persona es mayor de 60 años, se asigna prioridad automáticamente
    if ticket.priority_attention is None:
        ticket.priority_attention = ticket.age > 60

    # Agregar el ticket a la cola correcta
    ticketTypes[ticket.type].enqueue(ticket)
