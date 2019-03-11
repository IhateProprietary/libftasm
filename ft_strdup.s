	extern _malloc
	extern _ft_strlen
	global _ft_strdup
	default rel
	section .text
_ft_strdup:
	push rbp
	lea rbp, [rsp]
	push rdi 					;rdi const char*
	call _ft_strlen
	add rax, 1					;rdi == rax + 1
	mov rdi, rax
	push rax					;save size
	mov rdi, [rsp]				;get size from stack
	call _malloc
	test rax, rax				;malloc == NULL?
	jz END						;if NULL return NULL
	mov rdi, rax				;put malloc ret in rdi
	mov rsi, [rsp + 8]
	mov rcx, [rsp]
	rep movsb
END:
	add rsp, 16
	pop rbp
	ret
