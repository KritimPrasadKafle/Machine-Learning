void main(){
  List<int> age = [12,32,42,76,56,90,86,111];
  int max = -1;
  for (int i = 0; i<age.length; i++){
    if (max<age[i]){
      max = age[i];
    }
  }
print('maximum number: $max');
}

