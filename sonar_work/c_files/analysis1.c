#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
#include <time.h>
#define N 4096

// To run this code, cd into the folder c_files and run the following commands. 
// gcc analysis1.c -lfftw3 -lm
// ./a.out

int main(void) {

   clock_t start = clock();
/*Do something*/


  fftw_complex in[N], out[N], in2[N]; /* double [2] */
  fftw_plan p, q;
  int i;

  /* prepare a cosine wave */
  for (i = 0; i < N; i++) {
    in[i][0] = cos(3 * 2*M_PI*i/N);
    in[i][1] = 0;
  }

  /* forward Fourier transform, save the result in 'out' */
  p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
  fftw_execute(p);
  for (i = 0; i < N; i++)
    printf("freq: %3d %+9.5f %+9.5f I\n", i, out[i][0], out[i][1]);
  fftw_destroy_plan(p);

  /* backward Fourier transform, save the result in 'in2' */
  printf("\nInverse transform:\n");
  q = fftw_plan_dft_1d(N, out, in2, FFTW_BACKWARD, FFTW_ESTIMATE);
  fftw_execute(q);
  /* normalize */
  for (i = 0; i < N; i++) {
    in2[i][0] *= 1./N;
    in2[i][1] *= 1./N;
  }
  for (i = 0; i < N; i++)
    printf("recover: %3d %+9.5f %+9.5f I vs. %+9.5f %+9.5f I\n",
        i, in[i][0], in[i][1], in2[i][0], in2[i][1]);
  fftw_destroy_plan(q);

  fftw_cleanup();

   clock_t end = clock();
   float seconds = (float)(end - start) / CLOCKS_PER_SEC;

   printf("%f", seconds);
  return 0;
}