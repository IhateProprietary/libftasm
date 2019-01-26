	global _ft_memcpy
	default rel
	section .text
_ft_memcpy:
	lea rax, [rdi]
	mov rcx, rdx
	rep movsb
	ret
