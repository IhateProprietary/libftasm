	extern _ft_strcmp
	default rel
	section .text
_ft_strcmp:
L1:
	mov cl, [rdi]
	cmp cl, 0
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
	ret
