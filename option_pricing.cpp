#include <iostream>
#include <math.h>
#include "parisi_generator.h"           // Parisi-Rapuano random number generator
#define  PI 2*asin(1)
#define PRINT_DATA 1
#define TIPO 1  // 1-opcion call europea, 2-up and out call 
using namespace std;

double box_muller(double U1, double U2){
    return sqrt(-2*log(U1))*cos(2*PI*U2);
}

double normal(double mu, double sigma){
    return box_muller(Random(),Random())*sigma+mu;
}

double log_price_bs(double S0, double t, double W, double r, double vol){  
    return log(S0)+(r-0.5*vol*vol)*t+vol*W;
}

double price_bs(double S0, double t, double W, double r, double vol){ 
    return S0*exp((r-0.5*vol*vol)*t+vol*W);
}


int main(){

    double num=0.0;
    double t=0.0;
    double W=0.0;
    double S0=1.0;
    double S=S0;
    double sim_time=1;
    #if TIPO==1
        double N=1;
        double N_sims=10000000;
    #elif TIPO==2
        double N=10000;
        double N_sims=100000;
    #endif
    
    double dt=sim_time/N;
    double r=0.03;
    double vol=0.15;
    double K=1.0;
    double aux=0.0;
    double barrier=1.2;
    bool cond =1;

    double V=0.0;

    srand(time(NULL));
    ini_ran(rand());


    FILE *f = fopen("final_time_price.txt", "w");
    if (f==NULL) {
        printf("ERROR: no se ha abierto el fichero \n");
    }else{
        for(int j=0;j<N_sims;j++){
            S=S0;
            t=0.0;
            W=0.0;
            cond=1;
           for(int i=0; i<N && cond; i++){
                W+=normal(0,sqrt(dt));
                t+=dt;
                S=price_bs(S0,t,W,r,vol);

                #if TIPO==2  //opciones barrera
                    if(S>=barrier){
                        S=-1;
                        cond=0;
                    }
                #endif
            }
        if(S-K<0){
            aux=0;
        }else{
            aux=S-K;
        }
        #if PRINT_DATA==1
            fprintf(f,"%lf\t %lf\t %lf\n",S,aux,W); 
        #endif
        V+=aux;
        }
        printf("Precio: %lf", exp(-r*sim_time)*V/N_sims);
        
        fclose(f);
    }
    
return 0;
}
