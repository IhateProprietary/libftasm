	global _ft_puts
	extern _ft_strlen
	default rel
	section .text
_ft_puts:
	call _ft_strlen
	mov rsi, rdi
	mov rdx, rax
	mov rdi, 1
	mov rax, 0x2000004
	syscall
	ret
