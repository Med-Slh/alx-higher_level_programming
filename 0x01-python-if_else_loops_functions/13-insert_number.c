#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - function that insert a number
 * @head: linked list
 * @number: number to insert
 * Return: address of the new node or NULL 
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list, *new_Node;

	list = *head;
	new_Node = malloc(sizeof(listint_t));
	if (new_Node == NULL)
		return (NULL);
	new_Node->n = number;
	if (list == NULL || list->n >= number)
	{
		new_Node->next = list;
		*head = new_Node;
		return (new_Node);
	}

	while (list && list->next && list->next->n < number)
		list = list->next;

	new_Node->next = list->next;
	list->next = new_Node;

	return (new_Node);
}
