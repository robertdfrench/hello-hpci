#include "mpi.h"
#include "stdio.h"


int get_rank_for_this_process() {
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    return rank;
}


void hello_world(int rank_id) {
    printf("Hello from Rank %d!\n", rank_id);
}


int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    
    int my_rank = get_rank_for_this_process();
    hello_world(my_rank);

    MPI_Finalize();
}
