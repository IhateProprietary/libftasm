	global _ft_strlen
	default rel
	section .text
_ft_strlen:
	xor rax, rax
	xor rcx, rcx
	cld
	not rcx
	repne scasb
	mov rax, rcx
	not rax
	dec rax
	ret
