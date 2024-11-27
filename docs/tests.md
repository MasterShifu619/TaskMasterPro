# TaskMasterPro Test Documentation

## Test Categories

### Unit Tests
**Purpose**: Test individual components and functions in isolation

#### Model Tests
**Tests for List Model**:
- List creation
- List deletion 
- List updating
- List tag handling
- List item relationships

#### View Tests
**Tests for Core Views**:
- List creation/deletion
- Item management
- Template handling
- User authentication
- Analytics calculations

#### Form Tests
**Tests for Forms**:
- User registration validation
- Login validation
- List creation validation
- Template creation validation

### Integration Tests
**Purpose**: Test interaction between components

#### Template-List Integration
**Tests for**:
- Creating lists from templates
- Creating templates from lists
- Template item synchronization
- Template sharing

#### User-List Integration  
**Tests for**:
- User list ownership
- List sharing between users
- Permission handling
- Multi-user interactions

### End-to-End Tests
**Purpose**: Test complete user workflows

#### Core Workflows
**Tests for**:
- User registration to list creation
- Template usage workflow
- Analytics generation
- Focus view interactions

## /todo/tests/test_views.py
**Purpose**: Test core view functionality and request handling

### Setup
```
python:todo/tests/test_views.py
startLine: 14
endLine: 21
```

**Key Features**:
- Creates test client
- Sets up request factory
- Creates test user
- Handles authentication

### Authentication Tests
**Test Cases**:
1. `testLogin()`: Tests login view and authentication
   - Verifies login request handling
   - Checks response codes
   - Validates user session

2. `test_login_request()`: Tests login form submission
   - Validates credentials
   - Checks message handling
   - Verifies redirect behavior

### List Management Tests
**Test Cases**:
1. `test_delete_todo_list()`: Tests list deletion
   - Creates test list and items
   - Verifies deletion
   - Checks cascade deletion of items

2. `test_createNewTodoList()`: Tests list creation
   - Tests basic list creation
   - Validates tag handling
   - Checks user association

3. `test_createNewTodoList2()`: Tests list sharing
   - Tests shared list creation
   - Validates user permissions
   - Checks sharing status

### Item Management Tests
**Test Cases**:
1. `test_addNewListItem()`: Tests item creation
   - Validates item properties
   - Checks list association
   - Verifies timestamps

2. `test_removeListItem()`: Tests item deletion
   - Verifies item removal
   - Checks list updates
   - Validates response

3. `test_getListItemByName()`: Tests item retrieval
   - Checks item lookup
   - Validates data accuracy
   - Tests response format

### Template Tests
**Test Cases**:
1. `test_template_from_todo()`: Tests template creation
   - Validates template conversion
   - Checks item copying
   - Verifies associations

2. `test_todo_from_template()`: Tests list creation from template
   - Tests template application
   - Validates item creation
   - Checks property copying

## /todo/tests/test_frontend.py
**Purpose**: Test frontend functionality and user interactions

### Setup & Configuration
```
python:todo/tests/test_frontend.py
startLine: 11
endLine: 27
```
**Features**:
- Test client setup
- User creation and authentication
- Test list initialization

### Authentication Tests
1. `test_login_request()`
```
python:todo/tests/test_frontend.py
startLine: 29
endLine: 36
```
**Tests**:
- Login request handling
- Session management
- Message storage
- Response validation

### List Management Tests
1. `test_create_new_todo_list()`
```
python:todo/tests/test_frontend.py
startLine: 38
endLine: 52
```
**Tests**:
- List creation with tags
- Timestamp handling
- Shared user functionality
- JSON request formatting

2. `test_add_new_list_item()`
```
python:todo/tests/test_frontend.py
startLine: 54
endLine: 70
```
**Tests**:
- Item creation
- Due date handling
- Tag color assignment
- Completion status

3. `test_remove_list_item()`
```
python:todo/tests/test_frontend.py
startLine: 72
endLine: 85
```
**Tests**:
- Item deletion
- Response validation
- Database cleanup

### Template Tests
1. `test_todo_from_template()`
```
python:todo/tests/test_frontend.py
startLine: 87
endLine: 99
```
**Tests**:
- Template to list conversion
- Item copying
- User association
- Redirect validation

### Tag Management Tests
1. `test_get_list_tags()`
```
python:todo/tests/test_frontend.py
startLine: 101
endLine: 115
```
**Tests**:
- Tag retrieval
- User-specific tags
- Response validation

### Item Status Tests
1. `test_mark_list_item()`
```
python:todo/tests/test_frontend.py
startLine: 117
endLine: 137
```
**Tests**:
- Item completion
- Rating system
- Timestamp handling
- Status updates

## /todo/tests/test_task_suggester.py
**Purpose**: Test the task suggestion and prioritization system

### Setup & Configuration
```
python:todo/tests/test_task_suggester.py
startLine: 9
endLine: 31
```
**Features**:
- Test user creation
- Test list initialization
- TaskSuggester class setup

### Priority Level Tests
1. `test_priority_level_calculation()`
```
python:todo/tests/test_task_suggester.py
startLine: 32
endLine: 51
```
**Tests**:
- Overdue tasks (negative days)
- Same-day tasks (0 days)
- Near-future tasks (2 days)
- Weekly tasks (5 days)
- Future tasks (10+ days)

2. `test_task_priority_across_multiple_lists()`
```
python:todo/tests/test_task_suggester.py
startLine: 216
endLine: 254
```
**Tests**:
- Multi-list priority handling
- Cross-list task comparison
- Priority ordering verification
- List independence validation

3. `test_priority_score_gradual_decrease()`
```
python:todo/tests/test_task_suggester.py
startLine: 256
endLine: 284
```
**Tests**:
- Time-based priority decay
- Score calculation accuracy
- Minimum score boundaries
- Score progression logic

### Edge Case Tests
1. `test_empty_list_suggestions()`
```
python:todo/tests/test_task_suggester.py
startLine: 286
endLine: 309
```
**Tests**:
- Empty list handling
- Null suggestion handling
- Error prevention
- Empty state validation

## /todo/tests/test_user_analytics.py
**Purpose**: Test analytics calculations and data presentation

### Setup & Data Generation
```
python:todo/tests/test_user_analytics.py
startLine: 10
endLine: 62
```

### Core Analytics Tests
1. Task Counting Tests
```
python:todo/tests/test_user_analytics.py
startLine: 64
endLine: 74
```

2. Due Date Tests
```
python:todo/tests/test_user_analytics.py
startLine: 76
endLine: 82
```

3. Procrastination Analysis
```
python:todo/tests/test_user_analytics.py
startLine: 130
endLine: 203
```

4. Busy Days Classification
```
python:todo/tests/test_user_analytics.py
startLine: 217
endLine: 269
```

5. Calendar Event Tests
```
python:todo/tests/test_user_analytics.py
startLine: 271
endLine: 318
```

6. Ratings chart tests
```
python:todo/tests/test_user_analytics.py
startLine: 356
endLine: 420
```

7. Task suggestion tests
```
python:todo/tests/test_user_analytics.py
startLine: 422
endLine: 483
```

## /todo/tests/test_urls.py
**Purpose**: Test URL routing and resolution

### Core URL Tests
**Location**:
```python:todo/tests/test_urls.py
startLine: 1
endLine: 25
```
**Tests**:
- Index URL resolution
- Todo list URL resolution 
- Todo list with ID resolution
- Template URL resolution

### List Management URLs
**Location**:
```python:todo/tests/test_urls.py
startLine: 26
endLine: 50
```
**Tests**:
- Create new list URL
- Delete list URL
- Update list URL
- List item management URLs

### Template URLs
**Location**:
```python:todo/tests/test_urls.py
startLine: 51
endLine: 70
```
**Tests**:
- Template creation URL
- Template from todo URL
- Template with ID URL

### Authentication URLs
**Location**:
```python:todo/tests/test_urls.py
startLine: 71
endLine: 90
```
**Tests**:
- Login URL
- Register URL
- Logout URL
- Password reset URL

## /todo/tests/test_send_due_tasks_email.py
**Purpose**: Test email notification system

### Setup & Configuration
**Location**:
```python:todo/tests/test_send_due_tasks_email.py
startLine: 1
endLine: 30
```
**Features**:
- Test user creation
- Test list creation
- Due task setup

### Email Tests
**Location**:
```python:todo/tests/test_send_due_tasks_email.py
startLine: 31
endLine: 55
```
**Tests**:
- Email content verification
- Recipient validation
- Subject line checking
- Empty task list handling

## /todo/tests/test_models.py
**Purpose**: Test database models and relationships

### List Model Tests
**Tests**:
- List creation
- List updating
- List deletion
- List-user relationship

### ListItem Model Tests  
**Tests**:
- Item creation
- Item status updates
- Due date handling
- List association

## /todo/tests/test_forms.py
**Purpose**: Test form validation and processing

### User Forms
**Tests**:
- Registration form validation
- Login form validation
- Password reset form validation

### List Forms
**Tests**:
- List creation form
- List item form
- Template creation form









