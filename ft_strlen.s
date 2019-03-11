	global _ft_strlen
	default rel
	section .text
_ft_strlen:
	push rbp
	lea rbp, [rsp]
	xor rax, rax
	xor rcx, rcx
	cld
	not rcx
	mov rsi, rdi
	repne scasb
	mov rax, rdi
	sub rax, rsi
	dec rax
	pop rbp
	ret
