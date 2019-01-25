#ifdef __linux__
# define ft_strlen _ft_strlen
# define ft_bzero _ft_bzero
# define ft_isalpha _ft_isalpha
# define ft_isdigit _ft_isdigit
# define ft_isalnum _ft_isalnum
# define ft_isascii _ft_isascii
# define ft_isprint _ft_isprint
#endif
#include <string.h>
#include <stdio.h>

#define buf 80

extern size_t ft_strlen(char *);
extern void ft_bzero(void*, size_t);
extern int ft_isalpha(int);
extern int ft_isdigit(int);
extern int ft_isalnum(int);
extern int ft_isascii(int);
extern int ft_isprint(int);

int		main(int ac, char **av)
{
	char b[buf];
	int c;

	memset(b, 'c', buf);
	ft_bzero(b, buf);
	for (int i = 0; i < buf; i++)
		printf("%-3.2hhx", b[i]);
	printf("\n%lu\n", ft_strlen(av[1]));
	c = av[1][0];
	printf("isalpha %d\n", ft_isalpha(c));
	printf("isdigit %d\n", ft_isdigit(c));
	printf("isalnum %d\n", ft_isalnum(c));
	printf("isascii %d %d\n", ft_isascii(c), c);
	printf("isprint %d\n", ft_isprint(c));
}
