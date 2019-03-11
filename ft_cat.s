	global _ft_cat
	default rel
	section .bss
BUFFER:	resb 4096
	section .text
_ft_cat:
	push rbp
	lea rbp, [rsp]
	push rdi
L1:	
	mov rax, 0x2000003
	lea rsi, [BUFFER]
	mov rdx, 4096
	mov rdi, [rsp]
	syscall
	jc END
	lea rsi, [BUFFER]
	mov rdx, rax
	mov rdi, 1
	mov rax, 0x2000004
	syscall
	jc END
	jmp L1
END:
	add rsp, 8
	pop rbp
	ret
