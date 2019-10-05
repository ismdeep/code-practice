void* create_array(size_t size, size_t sizeof_item) {
    void * arr = malloc(sizeof_item * size);
    return arr;
}

void** create_matrix(size_t rows, size_t cols, size_t sizeof_item) {
    void ** arr = (void **)malloc(sizeof(size_t) * rows);
    for (size_t row_id = 0; row_id < rows; ++row_id) {
        arr[row_id] = malloc(sizeof_item * cols);
    }
    return arr;
}

void*** create_cube(size_t x, size_t y, size_t z, size_t sizeof_item) {
    void*** arr = (void ***) malloc(sizeof(void**) * x);
    for (size_t x_id = 0; x_id < x; ++x_id) {
        arr[x_id] = (void **) malloc(sizeof(void*) * y);
        for (size_t y_id = 0; y_id < y; ++y_id) {
            arr[x_id][y_id] = malloc(sizeof_item * z);
        }
    }
    return arr;
}
