#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints the elements of listint_t list
 * @h: pointer to head of list
 * Return: int number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int x;

    current = h;
    x = 0;
    while (current != NULL)
    {
        printf("%i\n", current->x);
        current = current->next;
        x++;
    }

    return (x);
}

/**
 * add_nodeint_end - adds a node at the end of a list
 * @head: pointer to first node of list
 * @n: integer value
 * Return: address of the new element 
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a list
 * @head: pointer to list
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
