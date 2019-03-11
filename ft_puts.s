	global _ft_puts
	extern _ft_strlen
	default rel
	section .text
_ft_puts:
	push rbp
	lea rbp, [rsp]
	push rdi
	call _ft_strlen
	mov rsi, [rsp]
	mov rdx, rax
	mov rdi, 1
	mov rax, 0x2000004
	syscall
	jnc END
	mov rax, -1
END:
	add rsp, 8
	pop rbp
	ret
