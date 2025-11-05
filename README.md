# 🏦 ATB Banking Services — Streamlit App

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Active-success.svg)

> A fully interactive **banking simulation web app** built using **Streamlit**.  
> Create a virtual account, set a secure PIN, deposit and withdraw money, and check your balance — all with a friendly interface and real-time state management.

---

##  Features

 **User Registration** — Set your username and a secure 4-digit PIN.  
 **PIN Verification** — Secure login before accessing account functions.  
 **Deposit Money** — Add funds to your balance instantly.  
 **Withdraw Money** — Withdraw only if your balance allows.  
 **Check Balance** — Instantly view your current balance.  
 **Exit Option** — Safely exit with a thank-you message.  
 **Session Persistence** — User data stored in Streamlit’s `session_state`.

---

##  Tech Stack

| Component | Technology Used |
|------------|------------------|
|  Language | Python 3.8+ |
|  Framework | Streamlit |
|  Storage | Streamlit Session State |
|  UI | Streamlit Components (Buttons, Inputs, etc.) |

---

##  Project Structure

```
ATB_Banking_App/
│
├── app.py              # Main Streamlit app
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ATB_Banking_App.git
cd ATB_Banking_App
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install Streamlit:

```bash
pip install streamlit
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🖥️ How It Works

1. **Register** — Enter your username and set a 4-digit PIN.  
2. **Verify** — Re-enter your PIN for authentication.  
3. **Initial Deposit** — Deposit your first amount to open the account.  
4. **Access Menu** — Choose from available banking services:
   - Deposit money
   - Withdraw funds
   - Check balance
   - Exit the session

---

## 🔄 Code Flow Overview

```python
main() ➜
 ├── create_username()        # Register new user
 ├── verify_pin()             # PIN verification for security
 ├── initial_deposit()        # First deposit after account creation
 └── menu()                   # Banking operations (Deposit, Withdraw, etc.)
```

### 🧩 Streamlit Components Used

| Function | Purpose |
|-----------|----------|
| `st.title()` / `st.subheader()` | Display headers and titles |
| `st.text_input()` | Take username and PIN inputs |
| `st.number_input()` | Handle deposit and withdrawal inputs |
| `st.radio()` | Provide menu selection options |
| `st.button()` | Trigger actions |
| `st.success()` / `st.error()` / `st.warning()` / `st.info()` | Show status messages |
| `st.session_state` | Maintain user data across operations |

---

## 🔒 Security Notice

> ⚠️ This project is for **learning and demonstration purposes only**.  
It does **not** implement real-world authentication, encryption, or database storage.

---

## 🧑‍💻 Author

** Md Atheeb**  
 B.Tech CSE (AIML) Student  
 Passionate about **AI, Machine Learning, and Intelligent Systems**  
 [LinkedIn](https://www.linkedin.com/in/md-atheeb-0b9a77327) | [GitHub](https://github.com/mdatheeb)

---

## 🚀 Future Enhancements

-  Transaction History  
-  Multi-user Login System  
-  Database Integration (SQLite / Firebase)  
-  Responsive UI with custom themes  
-  Voice-based commands (via Streamlit Speech Components)

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use and modify it.

---

### ⭐ If you like this project, don’t forget to **star** the repo!
