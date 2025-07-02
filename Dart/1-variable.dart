void main() {
  var name = 'John';
  String city = 'New York';
  int age = 25;
  double height = 5.9;
  bool isStudent = true;
  
  greetUser('Hey');
  greetUser(name);
  
  int result = addNumbers(10, 5);
  print('Result: $result');
  
  print('City: $city');
  print('Age: $age');
  print('Height: $height');
  print('Is student: $isStudent');
}

void greetUser(String name) {
  print('Hello, $name');
}

int addNumbers(int a, int b) {
  return a + b;
}