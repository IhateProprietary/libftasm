	global _ft_strlen
	default rel
	section .text
_ft_strlen:
	lea rax, [rdi]
L1:
	cmp byte [rax], 0
	jz L2
	inc rax
	jnz L1
L2:	
	sub rax, rdi
	ret
