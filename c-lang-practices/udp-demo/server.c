#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

int main(int argc, char* argv[]) {
    int sockfd;
    char buffer[1024];
    char *hello = "Hello message from server.";
    struct sockaddr_in server_addr, client_addr;

    /* Creating socket file descriptor */
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed.");
        exit(EXIT_FAILURE);
    }

    memset(&server_addr, 0, sizeof(server_addr));
    memset(&client_addr, 0, sizeof(client_addr));

    /* Filling server information */
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(8080);

    if ( (bind(sockfd, (const struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) ) {
        perror("bind failed.");
        exit(EXIT_FAILURE);
    }

    int len, n;
    n = recvfrom(sockfd, (char *)buffer, 1024, MSG_WAITALL, (struct sockaddr *) &client_addr, &len);
    buffer[n] = '\0';
    printf("Client: %s\n", buffer);
    sendto(sockfd, (const char *)hello, strlen(hello), 0, (const struct sockaddr *) &client_addr, len);
    printf("Hello message sent.\n");

    return 0;
}