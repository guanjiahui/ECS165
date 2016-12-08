#include <iostream> 
#include <pqxx/pqxx> 

#include <fstream>
#include <sstream> 
 
using namespace std; 
using namespace pqxx; 
 
int main(int argc, char* argv[]) { 
  string sql; 

  ifstream file("EIA_CO2_Electricity_2015.csv");
  string value;
  while (file.good())
  {
    getline (file, value, ',');
    cout<< string(value,1,value.length()-2);
  }




 
  return 0; 
} 

