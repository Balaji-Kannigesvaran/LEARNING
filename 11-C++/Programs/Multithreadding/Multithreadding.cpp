#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <algorithm>

int universalInitialization() {
    //Universal Initialisation
    //Works with all Data types
    int a{ 7 };
    float b{ 3.0f };
    std::string str1{ "Multithreading" };
    std::cout << "a: " << a << '\n';
    std::cout << "b: " << b << '\n';
    std::cout << "str1: " << str1 << '\n';

    //Narrowing Conversion Not allowed
    int x = 7.7;     //Legal. Results only in warning
    //int y{ 7.7 };    //Illegal. Results in compilation err

    //Can be used with compund types also
    std::vector<int> vec1{ 2,5,6,1,7 };

    std::cout << "vec1: ";
    for (std::vector<int>::iterator it = vec1.begin(); it != vec1.end(); ++it)
        std::cout << *it << " ";
    std::cout << '\n';

    return 0;
}

int func(int x) {
    std::cout << "func int called\n";
    return 0;
}

int func(int* x) {
    std::cout << "func int* called\n";
    return 0;
}

int nullPtr() {
    func(NULL);
    func(nullptr);
    
    return 0;
}

int chrono1() {
    namespace sc = std::chrono;
    sc::seconds;            //1 Second interval
    sc::milliseconds;       //1 millisecond = 1/1000 second interval
    sc::microseconds;       //1 microsecond = 1/1000000second interval

    sc::seconds(2);         //2 second interval
    sc::milliseconds(3);    //3 millisecond interval
    sc::microseconds(4);    //4 microsecond interval

    return 0;
}

int chrono2() {
    using namespace std::literals;
    2s;                     //2 second interval
    3ms;                    //3 millisecond interval
    4us;                    //4 microsecond interval

    return 0;
}

int rangedForLoop() {
    std::vector<int> vec = { 3,2,4,5,6 };
    //This will make a copy and loop through it
    for (int i : vec) {
        std::cout << i << " ";
    }
    std::cout << '\n';

    //Modifying elements across the loop
    for (int i : vec) {
        i++;
    }
    for (int i : vec) {
        std::cout << i << " ";
    }
    std::cout << '\n';

    //The above code creates a copy and modifies it
    //So, when we print, we could not see the modified values
    //To modify a value, we need to pass reference
    for (int& i : vec) {
        i++;
    }
    for (auto i : vec) {
        std::cout << i << " ";
    }
    std::cout << '\n';
    //Here auto is used simply so that it will also be covered
    //int will also work

    return 0;
}

int lambdaExpression() {
    
    [](int arg) {return 2 * arg; };
    //In C++11 for multiple satements inside function block
    //[](int arg) -> int {arg = 2 * arg; return arg; };

    //Passing arguements
    [](int arg) {return 2 * arg; }(3);

    //Assigning to a variable
    auto x = [](int arg) {return 2 * arg; }(6);
    std::cout << "x: " << x << '\n';

    //Capturing local variable
    int n = 5;
    //[n](int arg) { n++; std::cout << "n: " << n << '\n'; return n * arg; }(3);
    //This will give err saying n is not a modifyable value, if we pass by value
    //So we have to do pass by reference
    std::cout << "n: " << n << '\n';
    int y = [&n](int arg) { n++; std::cout << "n: " << n << '\n'; return n * arg; }(3);
    std::cout << "n: " << n << " y: " << y << '\n';

    //Lambda expressions as Predicates to algorithm
    std::vector<int> vec = { 2,5,7,4,6 };
    auto n_even = std::count_if(vec.begin(), vec.end(),
        [](int n) {
            return (n % 2 == 0);
        }
    );
    std::cout << "\nThe vector has " << n_even << " element(s) with even values";

    int radix = 3;
    auto n_rad = std::count_if(vec.begin(), vec.end(),
        [radix](int n) {
            return (n % radix == 0);
        }
    );
    std::cout << "\nThe vector has " << n_rad << " element(s) which are exact multiples of "<< n_rad << '\n';



    return 0;
}

int main()
{
    std::cout << "\n<---- Universal Initialisation ---->\n";
    universalInitialization();
    std::cout << "\n<---- NULL & nullptr ---->\n";
    nullPtr();
    std::cout << "\n<---- Chrono ---->";
    chrono1();
    chrono2();
    std::cout << "\n<---- Ranged For loop ---->\n";
    rangedForLoop();\
    std::cout << "\n<---- lambda Expression ---->\n";
    lambdaExpression();
}
