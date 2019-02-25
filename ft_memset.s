	global _ft_memset
	default rel
	section .text
_ft_memset:
	mov al, sil
	mov rsi, rdi
	mov rcx, rdx
	rep stosb
	mov rax, rdi
	ret
