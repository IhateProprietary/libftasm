	extern _malloc
	extern _ft_strlen
	global _ft_strdup
	default rel
	section .text
_ft_strdup:
	push rdi 					;rdi const char*
	call _ft_strlen
	add rax, 1					;rdi == rax + 1
	mov rdi, rax
	push rax					;save size
	mov rdi, [rsp]				;get size from stack
	sub rsp, 8					;align
	call _malloc
	cmp rax, 0					;malloc == NULL?
	jz END						;if NULL return NULL
	mov rdi, rax				;put malloc ret in rdi
	mov rsi, [rsp + 16]
	mov rcx, [rsp + 8]
	rep movsb
END:
	add rsp, 24
	ret
