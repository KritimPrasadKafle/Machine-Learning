class BankAccount{
  String _accountNumber;
  double _balance;

  BankAccount(this._accountNumber, this._balance);

  double get balance => _balance;
  String get accountNumber => _accountNumber;
  
  set balance(double newBalance){
    if(newBalance >= 0){
      _balance = newBalance;
    }else{
      print('Balance cannot be negative');
    }
  }

  void deposit(double amount){
    if(amount > 0){
      _balance += amount;
      print('Deposited: \$${amount}, New balance: \$${_balance}');
    }
  }
}

void main(){
BankAccount b1 = new BankAccount("sdfjjdsf", 123);
print(b1._accountNumber);
b1.deposit(25);

}