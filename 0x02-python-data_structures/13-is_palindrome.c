#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head of the linked list
 * Return: 1 if true 0 if false, -1 on error
 */

int is_palindrome(listint_t **head)
{
	listint_t *seek;
	int *arr, length, i;

	if (!head || !*head)
		return (1);
	seek = *head;
	for (length = 0; seek; length++)
		seek = seek->next;
	arr = malloc(sizeof(int) * length);
	if (!arr)
		return (-1);
	for (i = 0, seek = *head; seek; i++, seek = seek->next)
		arr[i] = seek->n;
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
