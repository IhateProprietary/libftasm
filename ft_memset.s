	global _ft_memset
	default rel
	section .text
_ft_memset:
	mov rax, rdi
	mov [rdi], sil
	inc rdi
	dec rcx
	jnz _ft_memset
	ret
