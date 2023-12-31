#include "nbody.h"
#include <iostream>
#include <fstream> 
#include <sstream>
#include <chrono>
#include <time.h>
#include <unistd.h>
#include<random>

using namespace std::chrono;
using namespace std;

int main(int argc, char* argv[]) {
		int n=0;
		
		
		// decode arguments
		if(argc < 2) {
			printf("You must provide at least one argument\n");
			exit(0);
		}
	    std::istringstream ss(argv[1]);

		if (!(ss >> n)) {
				std::cerr << "Invalid number: " << argv[1] << '\n';
		} else if (!ss.eof()) {
			std::cerr << "Trailing characters after number: " << argv[1] << '\n';
		}
		//std::cout<< "parameter n="<<n<<std::endl;
		
		// Get starting timepoint
		auto start = high_resolution_clock::now();
		//calling faunction
		Nbody nbody(n, 0.0001, 10);
		// Get stopping timepoint
		auto stop = high_resolution_clock::now();	
		
		auto duration = duration_cast<microseconds>(stop - start);

	
  
    //cout << "Time: "
      //   << duration.count() << " ms" << endl;
	    string file_name = "b.csv";
		ofstream results;
		results.open(file_name,std::ofstream::app);

		results<<duration.count()<<"\n";
    
        results.close();

		
		
	    //Disable output
		//nbody.timeIntegration();
		return 0;
}

