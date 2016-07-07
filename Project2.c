/* Joshua Cutolo */
/* CSC 431 Project2.c */

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#define BUFFER_SIZE 5
#define TRUE 1
#define SLEEP_TIME 1

/* Create buffer */
int buffer[BUFFER_SIZE];

/* Create mutex */
pthread_mutex_t mutex;

/* Create empty and full semaphores for each type of ingredient */
sem_t pattySem;
sem_t cheeseSem;
sem_t bunSem;
sem_t pattyFullSem;
sem_t cheeseFullSem;
sem_t bunFullSem;

/* Function prototypes */
void *assemblyRobot(void *param);
void *bunSupplyRobot(void *param);
void *pattySupplyRobot(void *param);
void *cheeseSupplyRobot(void *param);

int main(int argc, char *argv[])
{
	/* User specified sleep time */
	int sleepTime = atoi(argv[1]);
	
	/* Usage must be 2 arguments! */
	if(argc != 2)
	{
		fprintf(stderr, "Usage: ./a.out <sleep time>\n");
	}
	
	printf("------------SIMULATION STARTING FOR %d SECONDS------------\n\n", sleepTime);
	
	/* Create thread ids */
	pthread_t tid1, tid2, tid3, tid4;
	
	/* Initialize the semaphores */
	sem_init(&bunSem, 0, 5);
	sem_init(&pattySem, 0, 5);
	sem_init(&cheeseSem, 0, 5);
	sem_init(&bunFullSem, 0, 0);
	sem_init(&pattyFullSem, 0, 0);
	sem_init(&cheeseFullSem, 0, 0);

	/* Initialize the mutex */
	pthread_mutex_init(&mutex, NULL);
	
	/* Create the 4 threads */
	pthread_create(&tid1, NULL, bunSupplyRobot, NULL);
	pthread_create(&tid2, NULL, pattySupplyRobot, NULL);
	pthread_create(&tid3, NULL, cheeseSupplyRobot, NULL);
	pthread_create(&tid4, NULL, assemblyRobot, NULL);
	
	/* Sleep for user specified time */
	sleep(sleepTime);

	/* Unlock the mutex */
	pthread_mutex_lock(&mutex);
	
	printf("\n------------SIMULATION ENDING------------\n");
	return 0;
}


/* Function to simulate the assembly robot thread */
void *assemblyRobot(void *param)
{
	int random;
	while(TRUE) {
		random = rand() % 5;
		sleep(random);
		sem_wait(&bunFullSem);
		sem_wait(&pattyFullSem);
		sem_wait(&cheeseFullSem);
		pthread_mutex_lock(&mutex);
		printf("Assembly robot made one burger\n");
		sleep(SLEEP_TIME);
		pthread_mutex_unlock(&mutex);
		sem_post(&bunSem);
		sem_post(&pattySem);
		sem_post(&cheeseSem);
	}
}

/* Function to simulate the bun supply robot thread */
void *bunSupplyRobot(void *param)
{
	int random;
	while (TRUE) {
		random = rand() % 5;
		sleep(random);
		sem_wait(&bunSem);
		pthread_mutex_lock(&mutex);
		printf("Bun supply robot put a bun on table\n");
		sleep(SLEEP_TIME);
		pthread_mutex_unlock(&mutex);
		sem_post(&bunFullSem);
	}
}

/* Function to simulate the cheese supply robot thread */
void *cheeseSupplyRobot(void *param)
{
	int random;
	while (TRUE) {
		random = rand() % 5;
		sleep(random);
		sem_wait(&cheeseSem);
		pthread_mutex_lock(&mutex);
		printf("Cheese slice supply robot put a slice on table\n");
		sleep(SLEEP_TIME);
		pthread_mutex_unlock(&mutex);
		sem_post(&cheeseFullSem);
	}
}

/* Function to simulate the patty supply robot thread */
void *pattySupplyRobot(void *param)
{
	int random;
	while (TRUE) {
		random = rand() % 5;
		sleep(random);
		sem_wait(&pattySem);
		pthread_mutex_lock(&mutex);
		printf("Patty supply robot put a patty on table\n");
		sleep(SLEEP_TIME);
		pthread_mutex_unlock(&mutex);
		sem_post(&pattyFullSem);
	}
}