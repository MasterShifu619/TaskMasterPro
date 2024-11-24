# TaskMasterPro Function Documentation

## /todo/views.py

### Authentication & User Management
#### index(request, list_id=0)
**Purpose**: Main view to render homepage with user's todo lists and calendar events.
**Parameters**:
- request: HttpRequest object
- list_id: Optional integer to filter specific list (default: 0)
**Returns**: Rendered template with todo lists context
**Code Reference**:
```python:todo/views.py
startLine: 31
endLine: 69
```

#### createNewTodoList(request)
**Purpose**: Creates new todo list with optional sharing capabilities
**Parameters**:
- request: POST request with JSON body containing:
  - list_name: string
  - create_on: timestamp
  - list_tag: string
  - shared_user: string (optional)
  - create_new_tag: boolean
**Returns**: HTTP 200 response on success
**Code Reference**:
```python:todo/views.py
startLine: 360
endLine: 439
```

### Template Management
#### todo_from_template(request)
**Purpose**: Creates new todo list from existing template
**Parameters**: 
- request: POST request with template_id
**Returns**: Redirect to /todo
**Code Reference**:
```python:todo/views.py
startLine: 71
endLine: 99
```

#### template_from_todo(request)
**Purpose**: Creates template from existing todo list
**Parameters**:
- request: POST request with todo_id
**Returns**: Redirect to /templates
**Code Reference**:
```python:todo/views.py
startLine: 102
endLine: 123
```

### List Management
#### delete_todo(request)
**Purpose**: Deletes specified todo list
**Parameters**:
- request: POST request with todo_id
**Returns**: Redirect to /todo
**Code Reference**:
```python:todo/views.py
startLine: 126
endLine: 133
```

### Analytics & Focus
#### user_analytics(request)
**Purpose**: Generates user analytics and task statistics
**Parameters**:
- request: HttpRequest object
**Returns**: Rendered analytics template with statistics
**Code Reference**:
```python:todo/views.py
startLine: 559
endLine: 657
```

#### focus(request, list_id=0)
**Purpose**: Shows daily themed tasks based on weekday
**Parameters**:
- request: HttpRequest object
- list_id: Optional integer
**Returns**: Rendered focus template with filtered tasks
**Code Reference**:
```python:todo/views.py
startLine: 686
endLine: 732
```
### List Management Functions

#### removeListItem(request)
**Purpose**: Removes a specific item from a todo list
**Parameters**:
- request: POST request with list_item_id in JSON body
**Returns**: Redirect to /todo
**Authentication**: Required
**Code Reference**:
```python:todo/views.py
startLine: 151
endLine: 169
```

#### addNewListItem(request)
**Purpose**: Adds new item to existing todo list
**Parameters**:
- request: POST request with JSON body containing:
  - list_id: string
  - list_item_name: string
  - create_on: timestamp
**Returns**: JsonResponse with item details
**Authentication**: Required
**Code Reference**:
```python:todo/views.py
startLine: 209
endLine: 326
```

### Analytics Functions

#### user_analytics(request)
**Purpose**: Generates user statistics and analytics
**Features**:
- Task completion rates
- Procrastination metrics
- Busy day analysis
- Calendar integration
**Returns**: Rendered analytics template
**Code Reference**:
```python:todo/views.py
startLine: 559
endLine: 657
```

#### focus(request, list_id=0)
**Purpose**: Daily themed task view
**Features**:
- Day-specific task filtering
- Calendar integration
- Theme-based task organization
**Returns**: Rendered focus template
**Code Reference**:
```python:todo/views.py
startLine: 686
endLine: 732
```
## /todo/models.py

### List
**Purpose**: Main model for todo lists
**Fields**:
- title_text: CharField(100)
- created_on: DateTimeField
- updated_on: DateTimeField
- list_tag: CharField(50)
- user_id: ForeignKey(User)
- is_shared: BooleanField
**Code Reference**:
```python:todo/models.py
startLine: 4
endLine: 15
```
### ListTags
**Purpose**: Manages user-specific tags for categorizing lists
**Fields**:
- user_id: ForeignKey(User)
- tag_name: CharField(50)
- created_on: DateTimeField
**Code Reference**:
```python:todo/models.py
startLine: 17
endLine: 25
```
### Template
**Purpose**: Stores reusable list templates
**Fields**:
- title_text: CharField(100)
- created_on: DateTimeField
- updated_on: DateTimeField
- user_id: ForeignKey(User)
**Code Reference**:
```python:todo/models.py
startLine: 48
endLine: 57
```

### TemplateItem
**Purpose**: Individual items within a template
**Fields**:
- item_text: CharField(100)
- created_on: DateTimeField
- template: ForeignKey(Template)
- finished_on: DateTimeField
- due_date: DateField
- tag_color: CharField(10)
**Code Reference**:
```python:todo/models.py
startLine: 60
endLine: 71
```

### SharedUsers
**Purpose**: Tracks users with whom a list is shared
**Fields**:
- list_id: ForeignKey(List)
- shared_user: CharField(200)
**Code Reference**:
```python:todo/models.py
startLine: 73
endLine: 80
```

### SharedList
**Purpose**: Tracks lists shared with a user
**Fields**:
- user: ForeignKey(User)
- shared_list_id: CharField(200)
**Code Reference**:
```python:todo/models.py
startLine: 82
endLine: 89
```
## /todo/task_suggester.py

### TaskSuggester
**Purpose**: Analyzes and prioritizes tasks based on due dates and other factors

#### __init__(self, user_lists)
**Purpose**: Initializes suggester with user's todo lists
**Parameters**:
- user_lists: QuerySet of List objects belonging to user

#### get_priority_level(self, days_until_due)
**Purpose**: Determines priority level based on days until due date
**Parameters**:
- days_until_due: Integer number of days until task is due
**Returns**: Tuple of (priority_level: str, reason: str)
- Priority levels: Critical, High, Medium, Normal, Low
- Reason: Human readable explanation

#### calculate_task_priority(self, task) 
**Purpose**: Calculates numerical priority score and level for a task
**Parameters**:
- task: ListItem object
**Returns**: Tuple of:
- priority_score: Integer 0-100
- priority_level: String priority category
- reason: String explanation
**Algorithm**:
- Overdue tasks: 100 + days overdue
- Due today: 90
- Due in 3 days: 80
- Due this week: 70
- Later: Decreasing score based on days

#### get_suggested_tasks(self, max_limit=6)
**Purpose**: Gets prioritized list of suggested tasks
**Parameters**: 
- max_limit: Maximum number of tasks to return (default 6)
**Returns**: List of tuples (task, priority_level, reason)
**Algorithm**:
1. Gets incomplete tasks
2. Calculates priority for each
3. Sorts by:
   - Priority score
   - Due date
   - Creation date
4. Returns urgent tasks or up to max_limit tasks

## /todo/urls.py

### URL Patterns
**Purpose**: Maps URLs to view functions

#### Todo List URLs:
- `/todo`: Main todo list view (index)
- `/todo/<list_id>`: Specific list view
- `/todo/new-from-template`: Create list from template
- `/delete-todo`: Delete list

#### Template URLs:  
- `/templates`: Template list view
- `/templates/<template_id>`: Specific template view
- `/templates/delete/<template_id>`: Delete template
- `/templates/new-from-todo`: Create template from list

#### List Item URLs:
- `/addNewListItem`: Create new item
- `/updateListItem/<item_id>`: Update item
- `/removeListItem`: Delete item
- `/markListItem`: Toggle completion
- `/getListItemByName`, `/getListItemById`: Item lookups

#### User Management URLs:
- `/register`: User registration
- `/login`: Login
- `/logout`: Logout
- `/password_reset`: Password reset

#### Analytics URLs:
- `/user_analytics`: User statistics
- `/focus`: Daily focus view

## /todo/templates/

### index.html
**Purpose**: Main todo list view template
#### Core Structure
- DOCTYPE and meta tags
- CSS variables and base styles
- Navigation bar
- Sidebar with list creation
- Main content area with lists
- Calendar integration
- JavaScript functionality
#### Style Definitions
**Location**:
```
html:todo/templates/todo/index.html
startLine: 11
endLine: 300
```
**Features**:
- CSS variables for consistent theming
- Responsive layout styles
- Component-specific styles
- Interactive elements styling
#### Navigation Section
**Location**: 
```
html:todo/templates/todo/index.html
startLine: 1008
endLine: 1014
```
**Features**:
- Lists navigation
- Templates link
- User Analytics link
- Daily Focus link

#### JavaScript Functions
**Location**:
```
html:todo/templates/todo/index.html
startLine: 1293
endLine: 1800
```
**Key Functions**:
- `newTodoList()`: Creates new todo list
- `toggleNewTagInput()`: Handles tag input visibility
- `removeListItem()`: Deletes list items
- `markListItemByName()`: Toggles item completion
- `applyTemplate()`: Applies selected template


#### User Authentication Section
**Location**:
```
html:todo/templates/todo/index.html
startLine: 1015
endLine: 1022
```
**Features**:
- Welcome message for authenticated users
- Login/Logout buttons
- Authentication state handling

#### Todo List Creation Form
**Location**:
```
html:todo/templates/todo/index.html
startLine: 1024
endLine: 1034
```
**Features**:
- New list creation form
- List name input
- Tag selection dropdown
- Dynamic tag input toggle

#### Calendar Integration
**Location**:
```
html:todo/templates/todo/index.html
startLine: 1090
endLine: 1102
```
**Features**:
- Monthly calendar view
- Navigation controls
- Task due date visualization

### template.html
**Purpose**: Template management view

#### Core Structure
- DOCTYPE and meta tags
- Shared styling with index.html
- Template-specific styles
- Template listing and management

#### Template Navigation
**Location**:
```
html:todo/templates/todo/template.html
startLine: 456
endLine: 460
```
**Features**:
- List of available templates
- Template selection links

#### Template Display
**Location**:
```
html:todo/templates/todo/template.html
startLine: 462
endLine: 472
```
**Features**:
- Template title display
- Template items list
- Create todo from template button
- Template management buttons

### focus.html
**Purpose**: Daily themed task view
**Features**:
- Day-specific task filtering:
  - Monday: Refreshing tasks
  - Tuesday: Learning tasks
  - Wednesday: Wellness tasks
  - Thursday: Meeting tasks
  - Friday: Fitness tasks
  - Saturday: Self Care tasks
  - Sunday: Planning tasks
- Calendar integration
- Task priority display

### login.html
**Purpose**: User authentication interface

#### Core Structure & Styling
**Location**:
```
html:todo/templates/todo/login.html
startLine: 1
endLine: 35
```
**Features**:
- CSS variables for consistent theming
- Responsive design
- Form styling
- Error message handling

#### Navigation Bar
**Location**:
```
html:todo/templates/todo/login.html
startLine: 36
endLine: 115
```
**Features**:
- Simplified navigation
- Logo link
- Responsive design for mobile
- Clean authentication UI

#### Login Form
**Location**:
```
html:todo/templates/todo/login.html
startLine: 250
endLine: 290
```
**Features**:
- Username input
- Password input
- CSRF protection
- Error message display
- Links to registration and password reset

## /todo/templates/user_analytics.html
**Purpose**: Displays user statistics and task analytics

#### Core Structure & Dependencies
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 1
endLine: 25
```
**Features**:
- FullCalendar integration
- Chart.js integration
- Responsive meta tags
- CSS variables

#### Analytics Dashboard
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 639
endLine: 682
```
**Features**:
- Calendar visualization
- Task completion charts
- Rating distribution
- Busy day analysis

#### Task Status Sections
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 862
endLine: 879
```
**Features**:
- Due Soon tasks
- Overdue tasks
- Completed tasks
- Task details:
  - Creation date
  - Due date
  - Status
  - Completion time

#### Data Visualization
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 700
endLine: 780
```
**Features**:
- Monthly completion bar chart
- Task rating pie chart
- Busy days calendar
- Interactive charts with tooltips
- Responsive design

### Task Status Visualization
**Purpose**: Displays task status and analytics in an organized layout

#### Task Summary Section
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 663
endLine: 670
```
**Features**:
- Due soon count
- Overdue count
- Average procrastination time
- Completion statistics
- Percentage calculations

#### Task Suggestions Section
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 672
endLine: 706
```
**Features**:
- Priority-based task suggestions
- Visual priority indicators
- Due date display
- Empty state handling

#### Charts & Analytics
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 708
endLine: 718
```
**Features**:
- Daily completion chart
- Weekly completion chart
- Monthly completion chart
- Interactive data visualization

#### Busy Days Analysis
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 812
endLine: 829
```
**Features**:
- Color-coded status indicators:
  - Very Busy (Red)
  - Busy (Orange)
  - Moderately Busy (Yellow)
  - Not Busy (Green)
- Date-wise task load display
- Visual status bars

#### Task Status Lists
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 831
endLine: 879
```
**Features**:
- Due Soon tasks section
- Overdue tasks section
- Completed tasks section
- Per-task details:
  - Creation date
  - Due date
  - Status
  - Completion tracking

### Styling Components
**Location**:
```
html:todo/templates/todo/user_analytics.html
startLine: 189
endLine: 269
```
**Features**:
- Responsive grid layout
- Card-based design
- Status-based color coding
- Hover animations
- Shadow effects
- Accent bars for visual hierarchy

## /todo/templates/register.html
**Purpose**: User registration interface

#### Core Structure & Styling
**Location**:
```
html:todo/templates/todo/register.html
startLine: 1
endLine: 150
```
**Features**:
- Responsive design
- Form validation styling
- Error message handling
- Registration form layout

#### Registration Form
**Location**:
```
html:todo/templates/todo/register.html
startLine: 151
endLine: 190
```
**Features**:
- Username input
- Email input
- Password fields
- CSRF protection
- Form validation
- Login link for existing users

## /todo/templates/list_items.html
**Purpose**: Individual list item management

#### Core Structure
**Location**:
```
html:todo/templates/todo/list_items.html
startLine: 1
endLine: 100
```
**Features**:
- List item styling
- Navigation components
- Sidebar layout
- Responsive design

#### JavaScript Functions
**Location**:
```
html:todo/templates/todo/list_items.html
startLine: 400
endLine: 500
```
**Key Functions**:
- `newElement()`: Creates new list items
- `newTodoList()`: Creates new todo lists
- `showTodoList()`: Displays specific todo list
- AJAX handlers for database operations

## /todo/templates/focus.html
**Purpose**: Daily themed task focus view

#### Theme Definitions
**Location**:
```
html:todo/templates/todo/focus.html
startLine: 8
endLine: 50
```
**Features**:
- Day-specific color schemes:
  - Monday: Refreshing (Blue theme)
  - Tuesday: Learning (Green theme)
  - Wednesday: Wellness (Yellow theme)
  - Thursday: Collaborative (Orange theme)
  - Friday: Fitness (Purple theme)
  - Saturday: Self-Care (Light Yellow theme)
  - Sunday: Planning (Light Gold theme)

#### Calendar Integration
**Location**:
```
html:todo/templates/todo/focus.html
startLine: 200
endLine: 250
```
**Features**:
- FullCalendar implementation
- Event handling
- Dynamic theme application
- Daily message display

#### Task Display
**Location**:
```
html:todo/templates/todo/focus.html
startLine: 300
endLine: 350
```
**Features**:
- Daily task filtering
- Theme-based task organization
- Empty state handling
- Responsive layout



