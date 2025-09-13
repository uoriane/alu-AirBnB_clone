# AirBnB Clone Project

A command-line interpreter for managing AirBnB objects, built with Python. This is the first step in creating a full AirBnB clone web application.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Available Commands](#available-commands)
- [Examples](#examples)
- [Data Models](#data-models)
- [Testing](#testing)
- [Project Architecture](#project-architecture)
- [Future Development](#future-development)

## Description

This project implements a command-line interpreter (console) that allows you to manage AirBnB objects like users, places, cities, and more. It's built using Python's Object-Oriented Programming principles and includes:

- Data Models: User, State, City, Amenity, Place, Review
- File Storage: JSON-based persistence system
- Command Interface: Interactive console for object management
- Unit Testing: Comprehensive test suite

## Features

- Object-Oriented Design: Clean class hierarchy with BaseModel
- Data Persistence: Automatic saving/loading to JSON files
- Interactive Console: User-friendly command interface
- Unit Testing: 19+ tests ensuring code quality
- Data Management: Create, read, update, delete operations
- Serialization: Convert objects to/from JSON format

## Project Structure

```
alu-AirBnB_clone/
├── console.py              # Main command interpreter
├── file.json               # Data storage file
├── models/                 # Data models package
│   ├── __init__.py         # Package initialization
│   ├── base_model.py       # Base class for all models
│   ├── user.py             # User model
│   ├── state.py            # State model
│   ├── city.py             # City model
│   ├── amenity.py          # Amenity model
│   ├── place.py            # Place model
│   ├── review.py           # Review model
│   └── engine/             # Storage engine
│       ├── __init__.py
│       └── file_storage.py # JSON file storage
├── tests/                  # Unit tests
│   ├── test_models/
│   └── test_engine/
├── README.md               # This file
└── AUTHORS                 # Contributors
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/uoriane/alu-AirBnB_clone.git
   cd alu-AirBnB_clone
   ```

2. Ensure Python 3+ is installed:
   ```bash
   python --version
   ```

3. No additional dependencies required! The project uses only Python standard library.

## Usage

### Starting the Console

```bash
python console.py
```

You'll see the prompt:
```
(hbnb) 
```

### Exiting the Console

```bash
(hbnb) quit
# or
(hbnb) EOF  # (Ctrl+D on Unix/Mac, Ctrl+Z on Windows)
```

## Available Commands

| Command | Syntax | Description | Example |
|---------|--------|-------------|---------|
| `create` | `create <class_name>` | Create a new object | `create User` |
| `show` | `show <class_name> <id>` | Display an object | `show User 123` |
| `all` | `all [class_name]` | List all objects | `all User` |
| `destroy` | `destroy <class_name> <id>` | Delete an object | `destroy User 123` |
| `update` | `update <class_name> <id> <attr> <value>` | Update object attribute | `update User 123 name "John"` |
| `help` | `help [command]` | Show help | `help create` |
| `quit` | `quit` | Exit console | `quit` |

## Examples

### Creating Objects

```bash
(hbnb) create User
f47ac10b-58cc-4372-a567-0e02b2c3d479

(hbnb) create State
550e8400-e29b-41d4-a716-446655440000

(hbnb) create Place
6ba7b810-9dad-11d1-80b4-00c04fd430c8
```

### Viewing Objects

```bash
(hbnb) show User f47ac10b-58cc-4372-a567-0e02b2c3d479
[User] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 'created_at': datetime.datetime(2025, 9, 13, 15, 34, 44, 870030), 'updated_at': datetime.datetime(2025, 9, 13, 15, 34, 44, 870057)}

(hbnb) all User
["[User] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 'created_at': datetime.datetime(2025, 9, 13, 15, 34, 44, 870030), 'updated_at': datetime.datetime(2025, 9, 13, 15, 34, 44, 870057)}"]
```

### Updating Objects

```bash
(hbnb) update User f47ac10b-58cc-4372-a567-0e02b2c3d479 first_name "John"
(hbnb) update User f47ac10b-58cc-4372-a567-0e02b2c3d479 email "john@example.com"
(hbnb) show User f47ac10b-58cc-4372-a567-0e02b2c3d479
[User] (f47ac10b-58cc-4372-a567-0e02b2c3d479) {'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 'first_name': 'John', 'email': 'john@example.com', 'created_at': datetime.datetime(2025, 9, 13, 15, 34, 44, 870030), 'updated_at': datetime.datetime(2025, 9, 13, 15, 34, 44, 870057)}
```

### Error Handling

```bash
(hbnb) create InvalidClass
** class doesn't exist **

(hbnb) show User
** instance id missing **

(hbnb) show User invalid-id
** no instance found **

(hbnb) update User 123
** attribute name missing **
```

## Data Models

### BaseModel
All models inherit from BaseModel, which provides:
- id: Unique identifier (UUID)
- created_at: Creation timestamp
- updated_at: Last modification timestamp
- save(): Save object to storage
- to_dict(): Convert to dictionary

### Available Models

| Model | Attributes | Description |
|-------|------------|-------------|
| **User** | `email`, `password`, `first_name`, `last_name` | AirBnB users |
| **State** | `name` | States/Provinces |
| **City** | `state_id`, `name` | Cities within states |
| **Amenity** | `name` | Property amenities (WiFi, Pool, etc.) |
| **Place** | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids` | Rental properties |
| **Review** | `place_id`, `user_id`, `text` | User reviews for places |

## Testing

Run the complete test suite:

```bash
python -m unittest discover tests
```

Expected output:
```
...................
----------------------------------------------------------------------
Ran 19 tests in 0.004s

OK
```

Run specific test files:
```bash
python -m unittest tests.test_models.test_user
python -m unittest tests.test_models.test_base_model
```

## Project Architecture

### Data Flow
```
Console Input → Command Processing → Model Operations → FileStorage → JSON File
     ↑                                                                    ↓
User Interface ← Object Display ← Model Retrieval ← FileStorage ← JSON File
```

### Key Components

1. **Console (console.py)**: Command-line interface using Python's cmd module
2. **Models**: Data classes inheriting from BaseModel
3. **FileStorage**: JSON-based persistence layer
4. **BaseModel**: Foundation class with common functionality

### Design Patterns Used

- **Command Pattern**: Console commands as methods
- **Template Method**: BaseModel defines common behavior
- **Serialization**: Object ↔ Dictionary ↔ JSON conversion
- **Factory Pattern**: Dynamic object creation from JSON

## Future Development

This is Phase 1 of the AirBnB clone. Future phases will include:

- **Phase 2**: Web interface (HTML/CSS)
- **Phase 3**: Database integration (MySQL)
- **Phase 4**: REST API
- **Phase 5**: User authentication
- **Phase 6**: Image uploads
- **Phase 7**: Advanced features

## Contributors

- **Oriane Uwineza** - <o.uwineza@alustudent.com>
- **Jabes Ruranga** - <n.ruranga@alustudent.com>

## Learning Objectives

This project teaches:
- Object-Oriented Programming in Python
- Class inheritance and method overriding
- File I/O and data persistence
- Command-line interfaces
- Unit testing with unittest
- Serialization/Deserialization
- Error handling and validation
- Python packages and imports

## Troubleshooting

### Common Issues

1. **"class doesn't exist"**: Make sure you're using the correct class name (User, State, City, etc.)
2. **"instance id missing"**: Provide the object ID when using show/destroy/update commands
3. **"no instance found"**: The object with that ID doesn't exist
4. **Import errors**: Ensure you're running from the project root directory

### Getting Help

- Use `help` command in the console
- Check the test files for usage examples
- Review the model files for available attributes