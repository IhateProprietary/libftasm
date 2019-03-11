	extern _ft_memchr
	default rel
	section .text
_ft_memchr:
	push rbp
	lea rbp, [rsp]
	xor rax, rax
L1:
	test rdx, rdx
	jz END
	cmp sil, [rdi]
	je F1
	inc rdi
	dec rdx
	jmp L1
F1:
	lea rax, [rdi]
END:
	pop rbp
	ret
