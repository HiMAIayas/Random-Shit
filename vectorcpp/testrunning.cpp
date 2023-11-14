#include <iostream>
#include "./vector.hpp"

using namespace std;
int main(){
    Vector<std::string> v;
    v.pushBack("h");
    v.pushBack("e");
    v.pushBack("l");
    v.pushBack("l");
    v.pushBack("o");
    v.clear();

    v.printV();
}