# AgenticAI-Project MCP

A comprehensive Model Context Protocol (MCP) server for Human Resource Management System (HRMS) operations, providing AI-powered automation for common HR tasks and employee management.

## Overview

The AgenticAI-Project MCP enables seamless integration of HR management capabilities into AI assistants, allowing for natural language interaction with employee data, leave management, ticketing systems, and communication workflows.

## Features

### 📊 Employee Management
- Add new employees to the system
- Retrieve employee details by name or ID
- Manager hierarchy support

### 📧 Communication
- Send emails with SMTP support
- Automated notifications and updates
- Multi-recipient support

### 🎫 Ticket Management
- Create support/request tickets for employees
- Track items and reasons for requests
- Employee-specific ticket assignment

### 📅 Meeting Scheduling
- Schedule meetings with employees
- DateTime-based scheduling
- Topic-based meeting organization

### 🏖️ Leave Management
- Apply for leave on behalf of employees
- Multi-date leave support
- Retrieve leave information and balances

## Available Functions

### Employee Operations

#### `add_employee`
Add a new employee to the HRMS system.

**Parameters:**
- `emp_name` (string, required): Employee's full name
- `manager_id` (string, required): ID of the employee's manager
- `email` (string, required): Employee's email address

**Returns:** Confirmation message

#### `get_employee_details_by_id_or_name`
Retrieve employee information by name or ID.

**Parameters:**
- `name` (string, required): Employee's name
- `id` (string, required): Employee's ID

**Returns:** Employee details including ID and manager information

### Communication

#### `send_email`
Send emails through the system.

**Parameters:**
- `to_emails` (array of strings, required): List of recipient email addresses
- `subject` (string, required): Email subject line
- `body` (string, required): Email content
- `html` (boolean, optional): Whether to send as HTML format (default: false)

### Support & Ticketing

#### `create_ticket`
Create a support or request ticket.

**Parameters:**
- `emp_id` (string, required): Employee ID creating the ticket
- `item` (string, required): Item or service being requested
- `reason` (string, required): Reason for the request

### Scheduling

#### `schedule_meeting`
Schedule a meeting with an employee.

**Parameters:**
- `emp_id` (string, required): Employee ID for the meeting
- `topic` (string, required): Meeting topic/agenda
- `date_time` (datetime, required): Meeting date and time (ISO format)

### Leave Management

#### `leave_apply`
Submit a leave application.

**Parameters:**
- `emp_id` (string, required): Employee ID applying for leave
- `leave_dates` (array of dates, required): List of leave dates in YYYY-MM-DD format

#### `get_leave_info`
Retrieve leave information for an employee.

**Parameters:**
- `emp_id` (string, required): Employee ID to query

**Returns:** Leave balance and history information

## Usage Examples

### Adding a New Employee
```python
# Add a new employee with manager assignment
add_employee(
    emp_name="John Doe",
    manager_id="MGR001",
    email="john.doe@company.com"
)
```

### Scheduling a Meeting
```python
# Schedule a performance review meeting
schedule_meeting(
    emp_id="EMP001",
    topic="Q3 Performance Review",
    date_time="2024-09-15T14:00:00"
)
```

### Applying for Leave
```python
# Apply for multi-day leave
leave_apply(
    emp_id="EMP001",
    leave_dates=["2024-08-20", "2024-08-21", "2024-08-22"]
)
```

### Creating a Support Ticket
```python
# Request new equipment
create_ticket(
    emp_id="EMP001",
    item="Laptop",
    reason="Current laptop is malfunctioning and needs replacement"
)
```

## Integration

This MCP server is designed to work with AI assistants that support the Model Context Protocol. It provides a natural language interface for HR operations, allowing users to:

- "Add a new employee named Sarah Johnson with manager ID MGR002"
- "Schedule a team meeting with employee EMP003 for next Friday at 2 PM"
- "Apply for leave for employee EMP001 from August 25th to 27th"
- "Send an email to the development team about the new project launch"

## Configuration

The MCP server requires proper configuration of:
- Employee database connectivity
- Email service integration
- Calendar system integration
- Ticketing system backend

## Security Considerations

- All employee data operations should be authenticated
- Email functionality should include spam protection
- Leave applications should follow company policies
- Meeting scheduling should respect calendar permissions

## Error Handling

The server provides comprehensive error handling for:
- Invalid employee IDs
- Malformed date/time formats
- Email delivery failures
- Database connectivity issues

## Support

For issues, feature requests, or integration support, please contact the AgenticAI-Project development team.

---

*This MCP server enables natural, conversational interaction with HR systems, making employee management more intuitive and efficient.*

add this to the claude_desktop_config.json
for uv:
```
    "AgenticAI-Project": {
      "command": "path to UV.exe",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "path_to_the_sever.py script"
      ],
      "env": {
        "G_EMAIL": "your_email_id",
        "G_EMAIL_PWD": "your_gmail_app_passcode"
      }
    }
```
For python interpeter:
```
    "AgenticAI-Project": {
      "command": "python",
      "args": [
        "path_to_the_sever.py script",
        "run",
        "--with"
        "mcp[cli]",
        "mcp",
        "run",
      ],
      "env": {
        "G_EMAIL": "your_email_id",
        "G_EMAIL_PWD": "your_gmail_app_passcode"
      }
    }
```