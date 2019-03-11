#ifdef __linux__
# define ft_strlen _ft_strlen
# define ft_bzero _ft_bzero
# define ft_isalpha _ft_isalpha
# define ft_isdigit _ft_isdigit
# define ft_isalnum _ft_isalnum
# define ft_isascii _ft_isascii
# define ft_isprint _ft_isprint
# define ft_memcpy _ft_memcpy
# define ft_memset _ft_memset
# define ft_memchr _ft_memchr
# define ft_strchr _ft_strchr
# define ft_memcmp _ft_memcmp
#endif
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#define buf 80

extern size_t ft_strlen(char *);
extern void ft_bzero(void*, size_t);
extern int ft_isalpha(int);
extern int ft_isdigit(int);
extern int ft_isalnum(int);
extern int ft_isascii(int);
extern int ft_isprint(int);
extern void *ft_memcpy(void *, void *, size_t);
extern void *ft_memset(void *, int, size_t);
#ifdef __MACH__
extern char *ft_strdup(const char *);
extern int ft_puts(const char *);
extern void ft_cat(int fd);
extern void *ft_memchr(void *, int, size_t);
extern char *ft_strchr(char *, int);
extern int ft_memcmp(void *, void *, size_t);
extern int ft_strcmp(char *, char *);
#endif

int		main(int ac, char **av)
{
	char b[buf];
	char t[buf];
	int c;

	ft_memset(b, 'c', buf);
	for (int i = 0; i < buf; i++)
		printf("%-3.2hhx", b[i]);
	printf("\n");
	ft_bzero(b, buf);
	for (int i = 0; i < buf; i++)
		printf("%-3.2hhx", b[i]);
	printf("\nstrlen %lu %lu\n", ft_strlen(av[1]), strlen(av[1]));
	c = av[1][0];
	printf("isalpha %d\n", ft_isalpha(c));
	printf("isdigit %d\n", ft_isdigit(c));
	printf("isalnum %d\n", ft_isalnum(c));
	printf("isascii %d %d\n", ft_isascii(c), c);
	printf("isprint %d\n", ft_isprint(c));
	int fd = open("/dev/urandom", O_RDONLY);
	read(fd, b, buf);
	for (int i = 0; i < buf; i++)
		printf("%-3.2hhx", b[i]);
	printf("\n");
	read(fd, &c, sizeof(int));
	c &= 0x7fffffff;
	int ca = ((c >> 16) % buf);
	int cb = ((c >> 8) % buf);
	c %= buf;
	printf("%d %d %d\n", ca, cb, c);
	printf("memchr me %p him %p\n", ft_memchr(b, cb[b], ca), memchr(b, cb[b], ca));
	ft_memcpy(t, b, buf);
	for (int i = 0; i < buf; i++)
		printf("%-3.2hhx", t[i]);
	b[buf - 1] = 0;
	printf("\nstrchr me %p him %p\n", ft_strchr(b, b[c]), strchr(b, b[c]));
	printf("memcpy dif %d\n", memcmp(t, b, buf));
	printf("memcmp  %d %d, should no dif\n", ft_memcmp(t, b, buf), memcmp(t, b, buf));
	read(fd, t, buf);
	printf("memcmp dif %d %d\n", ft_memcmp(t, b, buf), memcmp(t, b, buf));
	t[buf - 1] = 0;
	read(fd, b, buf);
	b[buf - 1] = 0;
	printf("strcmp dif %d %d\n", ft_strcmp(t, b), strcmp(t, b));
	read(fd, &c, 1);
	ft_memset(b, c, buf);
	printf("expected %hhx\n", c);
	for (int i = 0; i < buf; i++)
		printf("%-3.2hhx", b[i]);
	printf("\n");
#ifdef __MACH__
	void *p = ft_strdup(av[1]);
	printf("strdup %s\n", p);
	free(p);
	dprintf(1, "puts ");
	c = ft_puts(av[1]);
	printf("\nputs ret %d\n", c);
# ifdef CAT
	int fd2 = open("./main.c", O_RDONLY);
	ft_cat(fd2);
# endif /* endif CAT*/
#endif /* endif __MACH__ */
}
