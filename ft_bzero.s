	global _ft_bzero
	default rel
	section .text
_ft_bzero:
	xor rax, rax
	cmp rsi, 0
	jz L2
L1:
	mov [rdi], al
	inc rdi
	dec rsi
	jnz L1
L2:	
	ret
