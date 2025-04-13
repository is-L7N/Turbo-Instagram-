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
