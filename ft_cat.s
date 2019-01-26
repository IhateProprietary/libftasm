	global _ft_cat
	default rel
	section .bss
BUFFER:	resb 4096
	section .text
_ft_cat:
	push rdi
L1:	
	mov rax, 0x2000003
	lea rsi, [BUFFER]
	mov rdx, 4096
	mov rdi, [rsp]
	syscall
	cmp rax, 0
	jle END
	lea rsi, [BUFFER]
	mov rdx, rax
	mov rdi, 1
	mov rax, 0x2000004
	syscall
	jmp L1
END:
	add rsp, 8
	ret
