	extern _ft_memchr
	default rel
	section .text
_ft_memchr:
	xor rax, rax
L1:
	cmp rdx, 0
	jz END
	cmp sil, [rdi]
	je F1
	inc rdi
	dec rdx
	jmp L1
F1:
	lea rax, [rdi]
END:
	ret
