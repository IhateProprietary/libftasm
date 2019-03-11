	global _ft_bzero
	default rel
	section .text
_ft_bzero:
	push rbp
	lea rbp, [rsp]
	xor rax, rax
	test rsi, rsi
	jz L2
L1:
	mov [rdi], al
	inc rdi
	dec rsi
	jnz L1
L2:
	pop rbp
	ret
