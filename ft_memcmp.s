	extern _ft_memcmp
	default rel
	section .text
_ft_memcmp:
	push rbp
	lea rbp, [rsp]
	xor rax, rax
L1:
	test rdx, rdx
	jz END
	mov cl, [rdi]
	cmp cl, [rsi]
	jne F1
	inc rdi
	inc rsi
	dec rdx
	jmp L1
F1:
	movzx eax, cl
	movzx ecx, byte [rsi]
	sub eax, ecx
END:
	pop rbp
	ret
