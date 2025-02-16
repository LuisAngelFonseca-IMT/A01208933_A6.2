# A01208933_A6.2
# Hotel Reservation System

This module implements a simple hotel reservation system with persistent storage using JSON files. It provides functionalities to manage hotels, customers, and reservations.

## Steps to Run Tests

1. **Navigate to the Directory**
   ```bash
   cd /path/to/your/project
   ```

2. **Run Unit Tests**
   ```bash
   python -m unittest reservation_system.py
   ```

3. **Expected Outcome**
   - Tests will validate the creation, modification, display, and deletion of hotels, customers, and reservations.
   - Successful tests will display an `OK` message.

4. **Code Coverage**
   - To check coverage, install the `coverage` module:
     ```bash
     pip install coverage
     ```
   - Run the tests with coverage:
     ```bash
     coverage run -m unittest reservation_system.py
     coverage report -m
     ```

This ensures compliance with PEP8 standards and robust test coverage for critical functionalities.