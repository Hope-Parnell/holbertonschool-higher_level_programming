#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head of the linked list
 * Return: 1 if true 0 if false, -1 on error
 */

int is_palindrome(listint_t **head)
{
	listint_t *seek;
	int arr[500000], length, i;

	if (!head || !*head)
		return (1);
	for (length = 0, seek = *head; seek; length++)
	{
		arr[length] = seek->n;
		seek = seek->next;
	}
	for (i = 0, --length; i < length; i++, length--)
	{
		if (arr[i] != arr[length])
			return (0);
	}
	return (1);
}
