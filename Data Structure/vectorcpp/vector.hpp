#ifndef VECTOR_H
#define VECTOR_H

const int DEFAULT_VECTOR_SIZE = 10;
const int DEFAULT_CAPACITY_EXTENSION = 2;

template <typename T>
class Vector{
    private:
        int size;       //current number of elements in vector 
        int capacity;   //full capacity of vector
        T* elements;    //create a pointer variable named elements, probably array of pointers

    public:
        //Construction
        Vector(){ //Vector<type> v;
            size = 0;
            capacity = DEFAULT_VECTOR_SIZE;
            elements = new T[capacity]; //create "new" array of "type T" of size 10. "new" is allocating and creating new object in heap.
        }  
        Vector(int n, const T& value){ //T& is real value as a reference (real value in stack) => Vector<type> v(n,value);
            size = n;
            capacity = n*DEFAULT_CAPACITY_EXTENSION;
            elements = new T[capacity];
            for (int i=0; i<size; i++){
                elements[i] = value;
            }
        }; 
        Vector(const Vector& rhs){      //copy of another Vector w => Vector<type> v(w);
            size = rhs.size;
            capacity = rhs.capacity;
            elements = new T[capacity];
            for (int i=0; i<size; i++){
                elements[i]=rhs.elements[i];
            }
        
        }

        //Destruction
        ~Vector(){
            delete[] elements;  //delete arrays. For more info, search delete keywords c++.
        }

        //Base functions
        int Size() const{ //const after functions mean the function is guarantee cannot change value of object
            return size;
        } 
        int Capacity() const{
            return capacity;
        }
        bool isEmpty() const{
            return size==0;
        }

        //define operation [],= of vector
        T& operator [](int index){  // v[i] = a;     (value inside v is changed)
            if (index>=size) {
                std::cout<<"IndexOutOfRange\n";
            }
            return elements[index];
        }    
        const T& operator [](int index) const{      // a = v[i];     (value inside v is not changed)
            if (index>=size) {
                std::cout<<"IndexOutOfRange\n";
            }
            return elements[index];
        }      
        Vector& operator =(const Vector& rhs);      // v = w



        //FUNCTIONS
        //TODO: emplace_back, pop_back, 
        //FUNCTIONS
        void printV(){
            std::cout<<"[";
            for (int i=0; i<size-1; i++){
                std::cout<<elements[i]<<",";
            }
            if (size!=0) std::cout<<elements[size-1];
            std::cout<<"]\n";
            std::cout<<"Size = "<<size<<'\n';
            std::cout<<"Capacity = "<<capacity;
        }

        void pushBack(const T& object){ //v.pushBack('hello');
            if (size>=capacity) {;
                //Create new array with double the capacity
                //Copy all of the elements to the new array
                capacity = capacity*DEFAULT_CAPACITY_EXTENSION;
                T* new_elements = new T[capacity];
                for (int i=0; i<size; i++){
                    new_elements[i] = elements[i];
                }
                delete[] elements;
                elements = new_elements; //pointer = pointer
            }

            elements[size] = object;    
            size++;
        }

        void popBack(){ //TODO: If size reduce by 80% of capacity. Reduce capacity.
            if (size>0){
                size--; //popBack does not really delete item in stack, just cannot iterate to them b/c size boundary.
                elements[size].~T();
            }
        }

        void clear(){
            for (int i=0; i<size; i++){
                elements[i].~T();
            }
            size=0;
        }
        //TODO: insert, erase, etc
};


#endif