class Student {
  String name;
  int age;
  String? email; // Nullable
  double gpa;
  
  // Named constructor with optional parameters
  Student({
    required this.name,
    required this.age,
    this.email,
    this.gpa = 0.0, // Default value
  });
  
  // Named constructor
  Student.withEmail(this.name, this.age, this.email) : gpa = 0.0;
  Student.withName(this.age, this.email, this.name) : gpa = 2.3;
  
  void displayInfo() {
    print('Name: $name, Age: $age, GPA: $gpa');
    if (email != null) {
      print('Email: $email');
    }
  }
}

void main(){
Student s1 = new Student(name: 'Kritim', age: 19);
Student s2 = new Student.withEmail('Hello', 19, 'kritim@gmail.com');
Student s3 = new Student.withName(23, 'her@mail.com', 'sdfjkjkdsf');

s1.displayInfo();
s2.displayInfo();
s3.displayInfo();

}