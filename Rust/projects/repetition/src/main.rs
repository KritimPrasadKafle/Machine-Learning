// fn main(){
//     loop{
//         println!("again - main.rs:3")
//     }
// }

// fn main(){

//     let mut counter = 0;

//     let result = loop{
//         counter += 1;
//         if counter == 10{
//             break counter * 2;
//         }
//     };

//     println!("The result is {result} - main.rs:18")
// }



// fn main() {
//     let mut count = 0;
//     'counting_up: loop {
//         println!("count = {count} - main.rs:26");
//         let mut remaining = 10;

//         loop {
//             println!("remaining = {remaining} - main.rs:30");
//             if remaining == 9 {
//                 break;
//             }
//             if count == 2 {
//                 break 'counting_up;
//             }
//             remaining -= 1;
//         }

//         count += 1;
//     }
//     println!("End count = {count} - main.rs:42");
// }

// fn main() {
//     let mut number = 3;

//     while number != 0 {
//         println!("{number}! - main.rs:49");

//         number -= 1;
//     }

//     println!("LIFTOFF!!! - main.rs:54");
// }

// fn main(){
//     let a = [10,20,30,40,50];
//     let mut index = 0;
//     while index < 5{
//         println!("the value is: {} - main.rs:61",a[index]);
//         index += 1;
//     }
// }

// fn main(){
//     let a = [1,2,3,4,5,5,6,6,7,8];
//     for element in a {
//         println!("The values are: {element} - main.rs:69");
//     }
// }

fn main(){
    for number in (1..4).rev(){
        println!("{number} - main.rs:75")
    }

    println!("LISTOFF!!! - main.rs:78")
}