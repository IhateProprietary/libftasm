	global _ft_memset
	default rel
	section .text
_ft_memset:
	push rbp
	lea rbp, [rsp]
	mov al, sil
	mov rsi, rdi
	mov rcx, rdx
	rep stosb
	mov rax, rdi
	pop rbp
	ret
