# Bank Management System with Tkinter GUI

This is a simple Bank Management System / ATM (Automated Teller Machine) system implemented in Python, featuring a graphical user interface (GUI) built with Tkinter. The system allows users to perform basic banking operations such as cash withdrawal, cash deposit, checking account balance, and viewing transaction history.

## Features

- **User Authentication**: Users can authenticate themselves using a card number.
- **Cash Withdrawal**: Allows users to withdraw cash from their accounts.
- **Cash Deposit**: Provides the functionality to deposit cash into user accounts.
- **Account Balance**: Enables users to check their account balance.
- **Transaction History**: Users can view their transaction history.
- **Security Measures**: Implements basic security measures such as PIN validation and temporary account lockout.

## Requirements

- Python 3.x
- PostgreSQL database
- `tkinter` (for GUI)
- `psycopg2` (for database connection)
- `prettytable` (for displaying transaction history in tabular format)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sarcasticdhruv/Bank-Management-System.git
   ```

2. Set up the PostgreSQL database by executing the provided SQL script (`db.sql`).

    ```bash
    psql database.sql
    ```

3. Update the `db_config.py` file with your PostgreSQL database credentials.

## Usage

1. Run the Python script:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions to navigate through the ATM system.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please [open an issue](https://github.com/sarcasticdhruv/Bank-Management-System/issues) or submit a pull request.
