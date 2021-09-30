#include "lists.h"

/**
 * list_length - finds how many nodes are in a linked list
 * @head: the list
 * Return: number of nodes
 */

int list_length(listint_t *head)
{
	listint_t *seek = head;
	int length;

	for (length = 0; seek; length++)
		seek = seek->next;
	return (length);
}

/**
 * list_to_array - stores the values from a linked list in an array
 * @head: head of the linked list
 * @length: number of nodes in a linked list
 * Return: the created array
 */

int *list_to_array(listint_t *head, int length)
{
	listint_t *seek;
	int i, *arr;

	arr = malloc(sizeof(int) * length);
	if (!arr)
		return (NULL);
	for (i = 0, seek = head; seek; i++, seek = seek->next)
		arr[i] = seek->n;
	return (arr);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head of the linked list
 * Return: 1 if true 0 if false, -1 on error
 */

int is_palindrome(listint_t **head)
{
	int *arr = NULL, length, i;

	if (!head || !*head)
		return (1);
	length = list_length(*head);
	arr = list_to_array(*head, length);
	if (!arr)
		return (-1);
	for (i = 0, --length; i < length; i++, length--)
	{
		if (arr[i] != arr[length])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
