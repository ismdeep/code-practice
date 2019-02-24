//
// Created by ismdeep on 2019-02-24.
//

#include <iostream>
using namespace std;


class Foo{
public:
    // Default Constructor
    Foo() {
        cout << "Default constructor was called!" << endl;
    }

    // Copy Constructor
    Foo(const Foo&) {
        cout << "Copy constructor was called!" << endl;
    }

    // Assignment operator
    Foo& operator=(const Foo&) {
        cout << "Assignment operator was called!" << endl;
    }

};

int main(int argc, char *argv[]) {
    // #1
    // Just a declaration. f1 will be initialized
    // with whatever the default c'tor was
    // designed  to do
    //
    cout << "Trying init method #1: ";
    Foo f1;

    // #2
    // Direct initialization. The copy c'tor
    // will be called to initialize f2 with f1
    //
    cout << "Trying init method #2: ";
    Foo f2(f1);

    // #3
    // Although the '=' sign is used, this is the
    // same as before, f3 is initialized with f1
    // by the copy c'tor (note, the assignment
    // operator isn't invoked)
    //
    cout << "Trying init method #3: ";
    Foo f3 = f1;

    // #4
    // Does it look like a declaration? It sure
    // does... and it is a declaration allright,
    // but not of Foo object! This is tricky...
    // What is declared is a function called f4,
    // which takes no parameters and returns
    // a Foo
    //
    cout << "Trying init method #4: ";
    Foo f4();
    return 0;
}