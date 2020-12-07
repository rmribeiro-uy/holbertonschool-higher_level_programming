#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head  of the list
 *
 * Return: 1 if the linked list has a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *future = list;

	if (list == NULL || list->next == NULL)
		return (0);

	if (list == future->next)
		return (1);

	while (list && future && future->next)
	{
		list = list->next;
		future = future->next->next;
		if (list == future || (list == future->next && future->next)
			return (1);
	}
	return (0);
}
