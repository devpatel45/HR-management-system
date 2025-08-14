import os
from mcp.server.fastmcp import FastMCP
from hrms import *
from datetime import date, datetime
from typing import List, Dict, Optional
from utils import seed_services
from dotenv import load_dotenv
from emails import EmailSender
_ = load_dotenv()

emailer = EmailSender(
    smtp_server="smtp.gmail.com",
    port=587,
    username=os.getenv("G_EMAIL"),
    password=os.getenv("G_EMAIL_PWD"),
    use_tls=True
)

mcp = FastMCP("AgenticAI-Project")

employee_manager = EmployeeManager()
leave_manager = LeaveManager()
ticket_manager = TicketManager()
meeting_manager = MeetingManager()

seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)

@mcp.tool()
def add_employee(emp_name: str, manager_id: str, email: str) -> str:
    """
    Add a new employee to the HRMS system.
    :param emp_name: Employee name
    :param manager_id: Manager ID (optional)
    :return: Confirmation message
    """
    emp = EmployeeCreate(
        emp_id = employee_manager.get_next_emp_id(),
        name=emp_name,
        manager_id=manager_id,
        email=email
    )
    employee_manager.add_employee(emp)

    return f"Employee {emp_name} added successfully"

@mcp.tool()
def get_employee_details_by_id_or_name(name: str, id:str) -> Dict[str, str]:
    """
    Get employee details by name.
    :param name: Name of the employee
    :param id: id of the employee
    :return: Employee ID and manager ID 
    :return: Employee name and manager ID
    """
    if name:
        matches = employee_manager.search_employee_by_name(name)
        if len(matches) == 0:
            raise ValueError(f"No employess found matches '{name}'.")
        emp_id = matches[0] 
        return employee_manager.get_employee_details(emp_id)
    
    matches = employee_manager.search_employee_by_id(id)
    emp_name, manager_id = matches['name'], matches['manager_id'] 
    return f"{id} is {emp_name} and the manager ID is {manager_id}"

@mcp.tool()
def send_email(to_emails: List[str], subject: str, body: str, html: bool = False) -> None:
    emailer.send_email(subject, body, to_emails, from_email=emailer.username, html=html)
    return "Email sent successfully."

@mcp.tool()
def create_ticket(emp_id: str, item: str, reason:str):
    ticket_req = TicketCreate(
        emp_id=emp_id,
        item=item,
        reason=reason
    )
    return ticket_manager.create_ticket(ticket_req)

@mcp.tool()
def schedule_meeting(emp_id: str, topic: str, date_time: datetime):
    meeting_req = MeetingCreate(
        emp_id=emp_id,
        meeting_dt=date_time,
        topic=topic
    )
    meeting_manager.schedule_meeting(meeting_req)
    return f"Meeting successfully scheduled on {date_time}"

@mcp.tool()
def leave_apply(emp_id: str, leave_dates: List[date]):
    leave_req = LeaveApplyRequest(
        emp_id=emp_id,
        leave_dates=leave_dates
    )
    leave_manager.apply_leave(leave_req)
    return f"Leave Application has been accepted for date of {leave_dates}"

@mcp.tool()
def get_leave_info(emp_id: str):
    leave_balance = leave_manager.get_leave_balance(employee_id=emp_id)
    leave_history = leave_manager.get_leave_history(employee_id=emp_id)

    return leave_balance, leave_history

@mcp.prompt("onboard_new_employee")
def onboard_new_employee(employee_name: str, manager_name: str):
    return f"""Onboard a new employee with the following details:
    - Name: {employee_name}
    - Manager Name: {manager_name}
    Steps to follow:
    - Add the employee to the HRMS system.
    - Send a welcome email to the employee with their login credentials. (Format: employee_name@atliq.com)
    - Notify the manager about the new employee's onboarding.
    - Raise tickets for a new laptop, id card, and other necessary equipment.
    - Schedule an introductory meeting between the employee and the manager and send the mail informing about the scheduled meeting with the new employee
    - Give the information on the leaves
    """



if __name__ == "__main__":
    mcp.run(transport="stdio")