
# Instagram Username Transfer Script

👨‍💻 **Author**: [L7N 🇮🇶](https://github.com/is-L7N)  
📱 **Telegram**: [@PyL7N](https://t.me/PyL7N)  
🌐 **GitHub**: [https://github.com/is-L7N](https://github.com/is-L7N)

---

## 🚀 Description

This script is designed to perform a username transfer between two Instagram accounts in an automated and efficient manner. The script utilizes **multi-threading** to ensure fast execution while minimizing the risk of account blocks or username theft. This script is intended for developers and enthusiasts familiar with Instagram's private API endpoints.

---

## 🛠️ Features

- **Session Management**: Automatically handles session IDs or Bearer tokens.
- **Username Transfer**: Swaps usernames between two Instagram accounts.
- **Multi-threading**: Ensures the username change occurs on both accounts simultaneously.
- **Account Validation**: Checks whether the account is banned or has other issues.

---

## ⚙️ Requirements

- **Python 3.8+**
- Libraries:
  - `requests` for making HTTP requests.
  - `threading` for running operations concurrently.
  - `json` and `base64` for handling Instagram's private API requests and responses.
  - `random` for generating random user agent strings.

---

## 📝 Code Explanation

### 🧑‍💻 Instagram Class

This class contains methods for interacting with Instagram's private API to:
- **Generate a random user agent**: Mimics an actual Instagram app request.
- **Check account status**: Verifies if the account is active or banned.
- **Retrieve account information**: Fetches details like username, email, phone number, and biography.

```python
class Instagram:
    def user_agent(self):
        # Generates a random User-Agent for requests
        ...
    
    def Status(self) -> bool:
        # Checks if the account is active (not banned)
        ...
        
    def get_info(self, session):
        # Fetches account details using the session
        ...
```

---

### 👤 L7N Class

The `L7N` class manages the process of adding accounts and triggering the username transfer. It takes user input for session IDs and validates the session details before proceeding with the transfer.

```python
class L7N:
    def add_account(self, account_name):
        # Prompts for session ID and retrieves account info
        ...
    
    def add(self):
        # Initiates the process for both accounts
        ...
```

---

### 🔄 Trans Class

Handles the core functionality of changing usernames between two Instagram accounts. It uses threading to ensure both accounts' usernames are swapped simultaneously.

```python
class Trans:
    def __init__(self):
        # Initializes necessary details for username swap
        ...
    
    def change_username(self, session, info, new_username):
        # Sends the request to change the username
        ...
    
    def main(self):
        # Uses threading to change usernames on both accounts concurrently
        ...
```

---

### 🛠️ Fun Class

A utility class that provides functionality to convert between Instagram session IDs and Bearer tokens.

```python
class Fun:
    @staticmethod
    def trans_sessionid(ses):
        # Converts session ID to Bearer token and vice versa
        ...
```

---

## 📑 Example Usage

1. **Run the script**:
   ```bash
   python script.py
   ```

2. **Select your action**:
   - **[1]** Convert SessionID to Bearer Token or vice versa.
   - **[2]** Swap usernames between two Instagram accounts.
   - **[3]** Check if your account is banned.

3. **Follow the prompts** to input session details, and the script will handle the rest.

---

## ⚠️ Disclaimer

- Use this script responsibly. It's intended for educational purposes and personal use.
- **I am not responsible for any account bans or issues** caused by misuse of this tool.
- **Instagram may block or limit actions** performed by scripts like this.

---

## 👨‍💻 Contributing

If you have suggestions or improvements, feel free to create an issue or pull request on [GitHub](https://github.com/is-L7N).

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
