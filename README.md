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

## Installation

### Prerequisites
- Python 3.8+
- Gmail account with App Password (for email functionality)

### Option 1: Using UV (Recommended)
```bash
# Install dependencies
uv sync
```

### Option 2: Using Pip
```bash
# Install MCP dependencies
pip install mcp mcp[cli]
```

## Configuration

### Environment Variables
The following environment variables are required:
- `G_EMAIL`: Your Gmail email address
- `G_EMAIL_PWD`: Your Gmail App Password (not your regular password)

### Claude Desktop Configuration

Add the following configuration to your `claude_desktop_config.json` file:

#### For UV (Recommended):
```json
{
  "mcpServers": {
    "AgenticAI-Project": {
      "command": "path/to/uv.exe",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "path/to/server.py"
      ],
      "env": {
        "G_EMAIL": "your.email@gmail.com",
        "G_EMAIL_PWD": "your_gmail_app_password"
      }
    }
  }
}
```

#### For Python Interpreter:
```json
{
  "mcpServers": {
    "AgenticAI-Project": {
      "command": "python",
      "args": [
        "path/to/server.py"
      ],
      "env": {
        "G_EMAIL": "your.email@gmail.com",
        "G_EMAIL_PWD": "your_gmail_app_password"
      }
    }
  }
}
```

### Setting Up Gmail App Password

1. Enable 2-Factor Authentication on your Google account
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Generate a new App Password for "Mail"
4. Use this 16-character password as `G_EMAIL_PWD`

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
Send emails through the system using SMTP.

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
- `date_time` (datetime, required): Meeting date and time in ISO format (YYYY-MM-DDTHH:MM:SS)

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

### Natural Language Commands
Once integrated with Claude Desktop, you can use natural language commands:

- "Add a new employee named Sarah Johnson with manager ID MGR002 and email sarah.johnson@company.com"
- "Schedule a team meeting with employee EMP003 for next Friday at 2 PM about project planning"
- "Apply for leave for employee EMP001 from August 25th to 27th"
- "Send an email to john@company.com about the new project launch"
- "Get employee details for John Doe"
- "Create a ticket for employee EMP001 requesting a new laptop because current one is broken"

### Programmatic Usage

#### Adding a New Employee
```python
add_employee(
    emp_name="John Doe",
    manager_id="MGR001",
    email="john.doe@company.com"
)
```

#### Scheduling a Meeting
```python
schedule_meeting(
    emp_id="EMP001",
    topic="Q3 Performance Review",
    date_time="2024-09-15T14:00:00"
)
```

#### Applying for Leave
```python
leave_apply(
    emp_id="EMP001",
    leave_dates=["2024-08-20", "2024-08-21", "2024-08-22"]
)
```

#### Creating a Support Ticket
```python
create_ticket(
    emp_id="EMP001",
    item="Laptop",
    reason="Current laptop is malfunctioning and needs replacement"
)
```

#### Sending an Email
```python
send_email(
    to_emails=["team@company.com"],
    subject="Project Update",
    body="The new project has been launched successfully!",
    html=False
)
```

## Troubleshooting

### Common Issues

**Email not sending:**
- Verify Gmail App Password is correct
- Ensure 2FA is enabled on Gmail account
- Check if "Less secure app access" is enabled (if not using App Password)

**Employee operations failing:**
- Verify employee IDs exist in the system
- Check database connectivity
- Ensure proper permissions

**Meeting scheduling issues:**
- Verify date format is ISO 8601 (YYYY-MM-DDTHH:MM:SS)
- Check if employee ID exists
- Ensure calendar system is accessible

### Debug Mode
Set environment variable `DEBUG=1` to enable verbose logging:

```bash
export DEBUG=1
```

## Integration

This MCP server is designed to work with AI assistants that support the Model Context Protocol. It provides a natural language interface for HR operations, making complex HRMS tasks accessible through conversational commands.

### Supported AI Platforms
- Claude Desktop
- Any MCP-compatible AI assistant

## Security Considerations

- **Email Security**: Uses Gmail App Passwords for secure SMTP authentication
- **Data Protection**: All employee data operations should be authenticated
- **Access Control**: Leave applications follow company policies
- **Calendar Permissions**: Meeting scheduling respects calendar permissions
- **Environment Variables**: Sensitive credentials stored in environment variables

## Error Handling

The server provides comprehensive error handling for:
- Invalid employee IDs
- Malformed date/time formats
- Email delivery failures
- Database connectivity issues
- Authentication errors
- Network timeouts

## Requirements

### Python Dependencies
- `mcp`
- `mcp[cli]`
- Additional dependencies as specified in the server implementation

### System Requirements
- Network access for email functionality
- Database access for employee data
- Proper file system permissions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, feature requests, or integration support:
- Create an issue in the project repository
- Contact the AgenticAI-Project development team
- Check the documentation for common solutions

## Changelog

### Version 1.0.0
- Initial release with core HRMS functionality
- Employee management operations
- Email integration with SMTP
- Leave management system
- Meeting scheduling capabilities
- Ticket creation and management

---

*This MCP server enables natural, conversational interaction with HR systems, making employee management more intuitive and efficient. Transform your HR workflows with AI-powered automation.*