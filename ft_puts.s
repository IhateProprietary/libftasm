	global _ft_puts
	extern _ft_strlen
	default rel
	section .text
_ft_puts:
	push rdi
	call _ft_strlen
	mov rsi, [rsp]
	mov rdx, rax
	mov rdi, 1
	mov rax, 0x2000004
	syscall
	add rsp, 8
	ret
