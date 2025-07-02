class Car{
  String brand;
  int model;
  int year;
  double price;

  Car(this.brand, this.model, this.year, this.price);

  void displayInfo(){
    print('It provides the details of the car $brand, $model, $year, $price');
  }

  bool isVintage(){
    return year >= 25;
  }

  double applyDiscount(double percentage){
    double total = (percentage / price) * 100;
    return total;
  }
}

void main(){

Car c1 = new Car("Volvo", 2019, 15, 20000.00);
Car c2 = new Car("Prado", 2020, 30, 324899832432);
c1.displayInfo();
print(c2.isVintage());
print(c1.applyDiscount(30));
}