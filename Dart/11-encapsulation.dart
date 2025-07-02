class GoodBankAccount {
  String _accountNumber;   // Private - protected
  double _balance;         // Private - controlled access
  String _pin;            // Private - secure
  List<String> _history;  // Private - transaction log
  
  GoodBankAccount(this._accountNumber, this._balance, this._pin) 
    : _history = [];
  
  // Safe getters - read-only access
  double get balance => _balance;
  String get accountNumber => _accountNumber;
  List<String> get transactionHistory => List.unmodifiable(_history);
  
  // Controlled methods with validation
  bool deposit(double amount) {
    if (amount <= 0) {
      print("❌ Deposit amount must be positive");
      return false;
    }
    _balance += amount;
    _history.add("Deposited: \$${amount}");
    print("✅ Deposited \$${amount}. New balance: \$${_balance}");
    return true;
  }
  
  bool withdraw(double amount, String enteredPin) {
    // Security check
    if (enteredPin != _pin) {
      print("❌ Invalid PIN!");
      return false;
    }
    
    // Validation
    if (amount <= 0) {
      print("❌ Withdrawal amount must be positive");
      return false;
    }
    
    if (amount > _balance) {
      print("❌ Insufficient funds! Balance: \$${_balance}");
      return false;
    }
    
    _balance -= amount;
    _history.add("Withdrew: \$${amount}");
    print("✅ Withdrew \$${amount}. New balance: \$${_balance}");
    return true;
  }
  
  bool transferTo(GoodBankAccount otherAccount, double amount, String pin) {
    if (withdraw(amount, pin)) {
      otherAccount.deposit(amount);
      _history.add("Transferred \$${amount} to ${otherAccount.accountNumber}");
      return true;
    }
    return false;
  }
}

void main() {
  GoodBankAccount account = GoodBankAccount("123456", 1000.0, "1234");
  GoodBankAccount friendAccount = GoodBankAccount("789012", 500.0, "5678");
  
  // ✅ Everything is controlled and safe:
  
  // 1. Can't directly steal money
  // account._balance = 0;  // ❌ Compile Error!
  
  // 2. All operations validated
  account.withdraw(200, "1234");    // ✅ Valid withdrawal
  account.withdraw(200, "wrong");   // ❌ Wrong PIN
  account.withdraw(2000, "1234");   // ❌ Insufficient funds
  account.withdraw(-50, "1234");    // ❌ Negative amount
  
  // 3. Safe deposits
  account.deposit(300);             // ✅ Valid deposit
  account.deposit(-100);            // ❌ Invalid amount
  
  // 4. Secure transfers
  account.transferTo(friendAccount, 100, "1234");  // ✅ Valid transfer
  
  // 5. Can only read safely
  print("Account: ${account.accountNumber}");
  print("Balance: \$${account.balance}");
  print("Transaction History:");
  for (String transaction in account.transactionHistory) {
    print("  $transaction");
  }
}