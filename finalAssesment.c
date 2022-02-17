#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Employee
{
    int id;
    int age;
    char name[20];
    char department[20];
};

void main()
{
    write();
    read();
}

void write()
{
     FILE *of;

   // opening file for write mode
   of= fopen ("finalAsss.txt", "w");
   if(of == NULL) {
      fprintf(stderr, "\nError to open the file\n");
      exit (1);
   }
   struct Employee inp1 = {1,24,"purushottam","IT"};

   fwrite (&inp1, sizeof(struct Employee ), 1, of);

    // checking condition
   if(fwrite != 0)
      printf("Contents to file written successfully !\n");
   else
      printf("Error writing file !\n");
   fclose (of);
}

void read()
{
     FILE *inf;
   struct Employee inp;
   inf = fopen ("finalAsss.txt", "r");
   if (inf == NULL) {
      fprintf(stderr, "\nError to open the file\n");
      exit (1);
   }
   while(fread(&inp, sizeof(struct Employee), 1, inf))
      printf ("id = %d\nname = %s\nage = %d \ndepartment = %d \n" , inp.id, inp.name,inp.age,inp.department);
   fclose (inf);
}


