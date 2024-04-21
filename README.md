# Secure Peer-to-Peer Messaging System

This repository contains a Python-based peer-to-peer (P2P) messaging system developed for a hackathon project. The system focuses on secure, distributed communication without central data storage, adhering to principles outlined in peer-to-peer network architectures.

## Features

- **Discovery**: Clients register to a discovery server to update and verify IP addresses for P2P communication.
- **Session Initiation**: Users can initiate sessions by sending messages, blocking, or muting other users.
- **Communication and Synchronization**: Allows users to send and receive messages in real-time. Messages intended for offline users are stored locally and synchronized when the recipient becomes available.
- **Security**: Optional hashing of messages to ensure data integrity and confidentiality.

## Getting Started

### Prerequisites

- Python 3.x
- SQLite3

### Running the Server

Navigate to the project directory and run:

```bash
python3 server.py
```
### Running a Client

Open another terminal window and run:

```bash
python3 client.py
```
### Thread Management

To handle periodic tasks such as sending heartbeat messages, run:

```bash
python3 thread.py
```
### Database Setup

To set up the database for storing messages and client details:
```bash
python3 database.py
```
## Project Structure

The system is composed of several key components:

- `server.py`: Manages connections and broadcasts messages to all connected clients.
- `client.py`: Handles user input, communicates with the server, and displays incoming messages.
- `thread.py`: Manages background tasks for connectivity checks and sends heartbeat messages.
- `database.py`: Handles all database operations for data persistence, ensuring data is stored securely on the client side.

