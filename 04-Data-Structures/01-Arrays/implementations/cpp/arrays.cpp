/**
 * Custom Dynamic Array (Vector) in C++ (C++17)
 * 
 * Key concepts to implement:
 * - Template class for generic typing
 * - Heap allocation with raw pointers or std::allocator
 * - Copy constructor and Rule of Five (Destructor, Copy/Move constructors & assignments)
 * - Amortized O(1) push_back with 2x capacity doubling
 */

#include <iostream>
#include <stdexcept>

template <typename T>
class DynamicArray {
private:
    T* data;
    size_t size_;
    size_t capacity_;

    void resize(size_t new_capacity) {
        // TODO: Allocate new buffer of new_capacity
        // TODO: Move/copy elements from old buffer
        // TODO: Delete old buffer and update pointer
    }

public:
    DynamicArray(size_t initial_capacity = 4)
        : size_(0), capacity_(initial_capacity) {
        data = new T[capacity_];
    }

    ~DynamicArray() {
        delete[] data;
    }

    void push_back(const T& value) {
        // TODO: Check if size_ == capacity_, call resize(2 * capacity_)
        // TODO: Insert value at size_ and increment size_
    }

    T& get(size_t index) {
        // TODO: Check index bounds (index < size_), return data[index]
        throw std::out_of_range("Index out of bounds");
    }

    size_t size() const { return size_; }
    size_t capacity() const { return capacity_; }
};
