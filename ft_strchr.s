	extern _ft_strchr
	default rel
	section .text
_ft_strchr:
	push rbp
	lea rbp, [rsp]
	xor rax, rax
L1:
	cmp sil, [rdi]
	je F1
	cmp byte [rdi], 0
	jz END
	inc rdi
	jmp L1
F1:
	lea rax, [rdi]
END:
	pop rbp
	ret
