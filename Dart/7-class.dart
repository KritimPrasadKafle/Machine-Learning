class Person{
  String name;
  int age;
  String city;

  Person(this.name, this.age, this.city);

  void introduce(){
    print('Hi, I\'m $name, $age years old, from $city');
  }

  void birthday(){
    age++;
    print('Happy birthday! Now I\'m $age years old');
  }

  bool isAdult(){
    return age >= 18;
  }

}

void main(){
  Person person1 = new Person('Alice', 25, 'New York');
  Person person2 = new Person('Kritim', 18, 'Hetauda');

  person1.introduce();
  person2.birthday();
}