	extern _ft_strcmp
	default rel
	section .text
_ft_strcmp:
	push rbp
	lea rbp, [rsp]
L1:
	mov cl, [rdi]
	test cl, cl
	jz F1
	cmp cl, [rsi]
	jne F1
	inc rdi
	inc rsi
	jmp L1
F1:
	movzx eax, cl
	movzx ecx, byte [rsi]
	sub eax, ecx
END:
	pop rbp
	ret
