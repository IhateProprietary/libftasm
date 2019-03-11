	global _ft_memcpy
	default rel
	section .text
_ft_memcpy:
	push rbp
	lea rbp, [rsp]
	lea rax, [rdi]
	mov rcx, rdx
	rep movsb
	pop rbp
	ret
