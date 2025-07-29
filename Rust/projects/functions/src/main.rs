// fn main() {
//     println!("Hello, world! - main.rs:2");
//     another_function();
//     pass_value(40);

// }

// fn another_function(){
//     println!("Another function. - main.rs:9")
// }

// fn pass_value(value : i32){
//     println!("The value of x is: {value} - main.rs:13")

// }


// fn main(){
//     print_labeled_measurement(5, 'h');
// }

// fn print_labeled_measurement(value: i32, unit_label: char){
//     println!("The measurement is: {value}{unit_label} - main.rs:23")
// }


// fn main(){
//     let y = {
//         let x = 3;
//         x + 1
//     };

//     println!("The value of y is : {y} - main.rs:33")
// }

// fn five() -> i32{
//     5
// }

// fn main(){
//     let x = five();
//     println!("The value of x is: {x} - main.rs:42")
// }

// fn main(){
//     let x = plus_one(5);
//     println!("The value of x is: {x} - main.rs:47")
// }

// fn plus_one(x: i32) -> i32 {
//     x + 1
// }


fn main(){
    let y = minus_five(56.6);
    println!("The value of y is: {y} - main.rs:57")
}

fn minus_five(y: f64) -> f64{
    y - 5.4
}