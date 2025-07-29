// fn main() {
//     let number = 4;
//     if number < 5{
//         println!("condition was true - main.rs:4");
//     }else{
//         println!("condition was false - main.rs:6")
//     }
// }




// fn main(){
//     let number = 3;
//     if number != 0{
//         println!("number was something other than zero - main.rs:16")
//     }
// }

// fn main() {
//     let number = 6;

//     if number % 4 == 0 {
//         println!("number is divisible by 4 - main.rs:24");
//     } else if number % 3 == 0 {
//         println!("number is divisible by 3 - main.rs:26");
//     } else if number % 2 == 0 {
//         println!("number is divisible by 2 - main.rs:28");
//     } else {
//         println!("number is not divisible by 4, 3, or 2 - main.rs:30");
//     }
// }

fn main(){
    let condition = true;
    let number = if condition {5} else {6};

    println!("The value of number is: {number} - main.rs:38")
}