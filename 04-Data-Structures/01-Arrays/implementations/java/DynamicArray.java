/**
 * Custom Dynamic Array in Java (JDK 17+)
 * 
 * Key concepts to implement:
 * - Generic class using Object[] internal array
 * - Geometric resizing (1.5x or 2x)
 * - Boundary exception handling (IndexOutOfBoundsException)
 * - Iterable interface support for enhanced for-loops
 */

package implementations.java;

public class DynamicArray<T> {
    private Object[] data;
    private int size;
    private int capacity;

    public DynamicArray(int initialCapacity) {
        this.capacity = initialCapacity;
        this.size = 0;
        this.data = new Object[initialCapacity];
    }

    public DynamicArray() {
        this(4);
    }

    public void add(T element) {
        // TODO: Check if size == capacity -> resize(capacity * 2)
        // TODO: data[size++] = element
    }

    @SuppressWarnings("unchecked")
    public T get(int index) {
        // TODO: Check index bounds (0 <= index < size)
        // TODO: return (T) data[index]
        return null;
    }

    public int size() {
        return this.size;
    }

    private void resize(int newCapacity) {
        // TODO: Allocate new Object[newCapacity]
        // TODO: System.arraycopy(data, 0, newArray, 0, size)
        // TODO: Reassign data reference
    }
}
