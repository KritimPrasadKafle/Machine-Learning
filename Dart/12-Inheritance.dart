class Animal {
  String name;
  int age;
  
  Animal(this.name, this.age);
  
  void eat() {
    print('$name is eating');
  }
  
  void sleep() {
    print('$name is sleeping');
  }
}

class Dog extends Animal {
  String breed;
  
  Dog(String name, int age, this.breed) : super(name, age);
  
  void bark() {
    print('$name is barking! Woof!');
  }
  
  @override
  void eat() {
    print('$name the $breed is eating dog food');
  }
}

void main() {
  Dog mydog = Dog('Buddy', 3, 'Golden Retriever');
  mydog.eat();    // Uses overridden method
  mydog.bark();   // Dog-specific method
  mydog.sleep();  // Inherited from Animal
}